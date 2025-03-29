import csv
from dateutil import parser
import logic.date as date_logic


# CSVマッチング処理
def csv_matching(
    user_list_csv_path,  # 利用登録者一覧CSVパス
    address_list_csv_path,  # 全送付者リストCSVパス
    matching_terget,  # マッチング対象項目
    matching_entry_map,  # マッチング項目値 {マッチング項目: Entry}
):

    # (※1)や(※2)など、マッチング対象名の「(」以降を削除
    matching_terget = matching_terget.split("(")[0]

    # 「・」で分割
    matching_terget_list = matching_terget.split("・")

    # matching_entry_map から、matching_terget_list に含まれるキーのみ取得
    matching_entry_map = {
        key: value
        for key, value in matching_entry_map.items()
        if key in matching_terget_list
    }

    # matching_entry_map を {マッチング項目: Entryの値} に変換
    matching_value_map = {
        key: value.get() if value else "" for key, value in matching_entry_map.items()
    }
    print(f"matching_value_map: {matching_value_map}")

    try:
        # CSVファイルを開く
        with open(user_list_csv_path, "r", encoding="utf-8") as user_file, open(
            address_list_csv_path, "r", encoding="utf-8"
        ) as address_file:

            # CSVファイルを読み込む
            user_list_csv = csv.reader(user_file)
            address_list_csv = csv.reader(address_file)

            # ヘッダーを取得
            user_list_csv_header = next(user_list_csv)
            address_list_csv_header = next(address_list_csv)

            # matching_tergetに対応するカラムのインデックスを取得
            user_list_csv_index = [
                user_list_csv_header.index(item) for item in matching_terget_list
            ]

            # matching_value_mapに基づいて全送付者リストCSVのインデックスを取得
            address_list_csv_index = []
            for key, mapped_col in matching_value_map.items():
                if mapped_col == "":
                    # 空文字の場合は、利用登録者CSVと全送付者リストCSVでカラム名が一致していると判断
                    if key in address_list_csv_header:
                        address_list_csv_index.append(
                            address_list_csv_header.index(key)
                        )
                    else:
                        raise ValueError(f"{key} カラムが全送付者リストに存在しません")
                else:
                    # 空文字でない場合、指定されたカラム名を使ってインデックスを取得
                    if mapped_col in address_list_csv_header:
                        address_list_csv_index.append(
                            address_list_csv_header.index(mapped_col)
                        )
                    else:
                        raise ValueError(
                            f"{mapped_col} カラムが全送付者リストに存在しません"
                        )

            # 利用登録者CSVと全送付者リストCSVのターゲット値を取得
            user_list_csv_target_values = [
                [row[index] for index in user_list_csv_index] for row in user_list_csv
            ]
            address_list_csv_target_values = [
                [row[index] for index in address_list_csv_index]
                for row in address_list_csv
            ]

            # 後で戻すため、全送付者リストCSVの日付フォーマットを保持しておく
            address_csv_date_format = ""

            # 「生年月日」が比較対象の場合、日付のフォーマットを統一
            if "生年月日" in matching_terget_list and address_list_csv_target_values:
                first_row = address_list_csv_target_values[0]
                for value in first_row:
                    try:
                        parser.parse(value, dayfirst=False, yearfirst=True)
                        # 日付フォーマットを取得
                        address_csv_date_format = date_logic.get_date_format(value)
                    except ValueError:
                        pass

                # 利用登録者CSVの生年月日をフォーマット
                user_list_csv_target_values = [
                    [
                        (
                            date_logic.normalize_date(value)
                            if "生年月日" in matching_terget_list
                            else value
                        )
                        for value in row
                    ]
                    for row in user_list_csv_target_values
                ]

                # 全送付者リストCSVの生年月日をフォーマット
                address_list_csv_target_values = [
                    [
                        (
                            date_logic.normalize_date(value)
                            if "生年月日" in matching_terget_list
                            else value
                        )
                        for value in row
                    ]
                    for row in address_list_csv_target_values
                ]

            # 一致しなかったレコード、1件一致したレコード、2件以上一致したレコードに分ける
            no_match = []
            one_match = []
            multiple_matches = []

            # 各レコードの比較
            for addr_row in address_list_csv_target_values:
                # user_row を全送付者リストの値と比較
                matches = [
                    user_row
                    for user_row in user_list_csv_target_values
                    if user_row == addr_row  # 値が一致する場合
                ]

                if len(matches) == 0:
                    no_match.append(addr_row)  # 一致しなかった場合
                elif len(matches) == 1:
                    one_match.append(matches[0])  # 1件一致した場合
                else:
                    multiple_matches.append(matches[0])  # 2件以上一致した場合

            # 全送付者リスト検索のため、日付のフォーマットを元に戻す
            no_match_keys = date_logic.dete_format_rows(
                no_match, address_csv_date_format
            )
            one_match_keys = date_logic.dete_format_rows(
                one_match, address_csv_date_format
            )
            multiple_matches_keys = date_logic.dete_format_rows(
                multiple_matches, address_csv_date_format
            )

            # 全送付者検索用のカラム名を準備
            address_list_csv_primary_key = []
            for key, value in matching_value_map.items():
                if value == "":
                    # 空文字の場合は、利用登録者CSVと全送付者リストCSVでカラム名が一致していると判断
                    address_list_csv_primary_key.append(key)
                else:
                    # 空文字でない場合、指定されたカラム名を使ってインデックスを取得
                    address_list_csv_primary_key.append(value)

            no_match_records = []
            for row in no_match_keys:
                # 各レコードの値を辞書形式に変換
                row_dict = {
                    key: value for key, value in zip(address_list_csv_primary_key, row)
                }
                # 条件を指定してCSVファイルを検索
                search_result = search_csv(
                    address_list_csv_path,
                    {key: value for key, value in row_dict.items()},
                )
                if isinstance(search_result, list):
                    no_match_records.append(search_result[0])

            one_match_records = []
            for row in one_match_keys:
                # 各レコードの値を辞書形式に変換
                row_dict = {
                    key: value for key, value in zip(address_list_csv_primary_key, row)
                }
                # 条件を指定してCSVファイルを検索
                search_result = search_csv(
                    address_list_csv_path,
                    {key: value for key, value in row_dict.items()},
                )
                if isinstance(search_result, list):
                    one_match_records.append(search_result[0])

            multiple_matches_records = []
            for row in multiple_matches_keys:
                # 各レコードの値を辞書形式に変換
                row_dict = {
                    key: value for key, value in zip(address_list_csv_primary_key, row)
                }
                # 条件を指定してCSVファイルを検索
                search_result = search_csv(
                    address_list_csv_path,
                    {key: value for key, value in row_dict.items()},
                )
                if isinstance(search_result, list):
                    multiple_matches_records.append(search_result[0])
            # 結果をまとめる
            result = {
                "no_match": no_match_records,
                "one_match": one_match_records,
                "multiple_matches": multiple_matches_records,
            }
            print(f"一致しなかったレコード: {no_match_records}")
            print(f"1件一致したレコード: {one_match_records}")
            print(f"2件以上一致したレコード: {multiple_matches_records}")

    # 結果を返す

    except FileNotFoundError:
        return "CSVファイルが見つかりません"
    except csv.Error:
        return "CSVファイルが不正です"
    except ValueError as e:
        print(e)
        return f"エラー: {str(e)}"
    except UnicodeDecodeError:
        return "CSVファイルの文字コードが不正です"


def search_csv(csv_file, conditions):
    result = []

    # CSVファイルを開いて読み込む
    with open(csv_file, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        # 各レコードを確認して条件をすべて満たすものを検索
        for row in reader:
            # 条件がすべて一致するかを確認
            if all(row[key] == value for key, value in conditions.items()):
                result.append(row)

    # 該当するレコードが見つからなかった場合
    if not result:
        return f"No record found with conditions: {conditions}"

    return result
