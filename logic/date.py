from dateutil import parser
import re


# 日付のフォーマットをYYYY-MM-DD形式に修正
def normalize_date(date_str, date_format="%Y-%m-%d"):
    try:
        parsed_date = parser.parse(date_str, dayfirst=False, yearfirst=True)
        return parsed_date.strftime(date_format)
    except ValueError:
        return date_str  # 変換できない場合は元の文字列を返す


# 引数の文字列が表す日付形式を判別してフォーマットを返す関数
def get_date_format(date_str):
    # 日付形式にマッチする正規表現パターン
    patterns = {
        r"\d{4}-\d{2}-\d{2}": "%Y-%m-%d",  # 例: 2025-03-29
        r"\d{8}": "%Y%m%d",  # 例: 20201011
        r"\d{2}/\d{2}/\d{4}": "%m/%d/%Y",  # 例: 03/29/2025
        r"\d{4}/\d{2}/\d{2}": "%Y/%m/%d",  # 例: 2025/03/29
    }

    # 正規表現を使ってパターンをチェック
    for pattern, format_str in patterns.items():
        if re.fullmatch(pattern, date_str):
            return format_str

    # どのパターンにもマッチしなかった場合
    return None


def dete_format_rows(rows, date_format):
    """
    指定された日付フォーマットに従って、各行の値を変換します。
    :param rows: 変換する行のリスト
    :param date_format: 日付フォーマット
    :return: 変換された行のリスト
    """
    formatted_rows = []
    for row in rows:
        formatted_row = []
        for value in row:
            if len(value) > 4:
                # 日付を正規化
                normalized_date = normalize_date(value, date_format)
                formatted_row.append(normalized_date)
            else:
                formatted_row.append(value)
        formatted_rows.append(formatted_row)
    return formatted_rows


# テスト
# sample_dates = [
#     "2025/03/29",
#     "29-03-2025",
#     "March 29, 2025",
#     "2025.03.29",
#     "03-29-2025",
#     "29 March 2025",
#     "20250329",
#     "19990101",
#     "2020/1/1",
# ]

# normalized_dates = [normalize_date(date) for date in sample_dates]
# print(normalized_dates)
