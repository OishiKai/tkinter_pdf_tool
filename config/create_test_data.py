import csv


def create_test_csv():
    # 利用登録者CSV (user_list.csv)
    user_data = [
        ["生年月日", "住所", "電話番号", "シリアル番号", "管理コード", "氏名"],
        ["1990/01/01", "東京都千代田区", "090-1234-5678", "1234", "A123", "田中 太郎"],
        ["1985/05/23", "大阪府大阪市", "080-9876-5432", "5678", "B456", "鈴木 花子"],
        ["2000/12/31", "福岡県福岡市", "070-5555-1111", "9101", "C789", "山田 一郎"],
    ]

    # 全送付者CSV (address_list.csv)
    address_data = [
        ["name", "生年月日", "prefecture", "contact", "シリアル番号", "管理コード"],
        ["田中 太郎", "19900101", "東京都千代田区", "090-1234-5678", "8901", "A126"],
        ["鈴木 花子", "19850523", "大阪府大阪市", "080-9876-5432", "8902", "B987"],
        ["山田 一郎", "20001231", "福岡県福岡市", "070-5555-1111", "8903", "C112"],
        ["佐藤 次郎", "19950315", "北海道札幌市", "060-1234-5678", "8905", "D114"],
    ]

    # CSVファイルを Shift-JIS (cp932) で保存
    with open("user_list.csv", "w", newline="", encoding="cp932") as f:
        writer = csv.writer(f)
        writer.writerows(user_data)

    with open("address_list.csv", "w", newline="", encoding="cp932") as f:
        writer = csv.writer(f)
        writer.writerows(address_data)

    print("テストデータを作成しました！")


# 実行
create_test_csv()
