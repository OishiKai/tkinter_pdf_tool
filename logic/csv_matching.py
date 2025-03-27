import csv


# CSVマッチング処理
def csv_matching(
    user_list_csv_path,  # 利用登録者一覧CSVパス
    address_list_csv_path,  # 全送付者リストCSVパス
    matching_terget,  # マッチング対象項目
    matching_entry_map,  # マッチング項目値 {マッチング項目: Entry}
):

    # matching_tergetの「(」以降を削除 (※1)や(※2)を削除
    matching_terget = matching_terget.split("(")[0]

    # matching_tergetの「・」で分割
    matching_terget_list = matching_terget.split("・")

    # matching_entry_mapのうち、keyがmaching_terget_listに含まれるものを取得
    matching_entry_map = {
        key: value
        for key, value in matching_entry_map.items()
        if key in matching_terget_list
    }

    # matching_entry_mapを{マッチング項目: "Entryの値"}に変換
    matching_value_map = {key: value.get() for key, value in matching_entry_map.items()}
    print(matching_value_map)

    try:
        # CSVファイル(shif-jis)を開く
        user_list_csv_file = open(user_list_csv_path, "r", encoding="cp932")
        address_list_csv_file = open(address_list_csv_path, "r", encoding="cp932")

        # CSVファイルを読み込む
        user_list_csv = csv.reader(user_list_csv_file)
        address_list_csv = csv.reader(address_list_csv_file)

        # 利用登録者CSV : マッチング対象のヘッダーのインデックスを取得
        user_list_csv_header = next(user_list_csv)
        user_list_csv_index = [
            user_list_csv_header.index(item) for item in matching_terget_list
        ]

        # 利用登録者CSV : マッチング対象の値を取得
        user_list_csv_target_values = []
        for row in user_list_csv:
            user_list_csv_target_values.append(
                [row[index] for index in user_list_csv_index]
            )

        # for value in user_list_csv_target_values:
        #     print(value)

        # 全送付者リストCSV : matching_value_mapのvalueと一致するヘッダーのインデックスを取得
        address_list_csv_header = next(address_list_csv)
        address_list_csv_index = []

        if any(matching_value_map):
            # matching_value_mapが空でない場合、valueと一致するヘッダーのインデックスを取得
            address_list_csv_index = [
                address_list_csv_header.index(key)
                for key in matching_value_map.values()
            ]
        else:
            # matching_value_mapが空の場合、比較対象のヘッダー名が利用登録者CSVと全送付者リストCSVで一致するものを取得
            address_list_csv_index = [
                address_list_csv_header.index(item) for item in matching_terget_list
            ]

        # 全送付者リストCSV : matching_value_mapのvalueと一致する値を取得
        address_list_csv_target_values = []
        for row in address_list_csv:
            address_list_csv_target_values.append(
                [row[index] for index in address_list_csv_index]
            )

        for value in address_list_csv_target_values:
            print(value)

    except FileNotFoundError as e:
        return "CSVファイルが見つかりません"

    # except csv.Error as e:
    #     return "CSVファイルが不正です"

    # except ValueError as e:
    #     print(e)
    #     return "マッチングに失敗しました"

    # except UnicodeDecodeError as e:
    #     return "CSVファイルの文字コードが不正です"
