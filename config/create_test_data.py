import csv


# fmt: off
def create_test_csv():
    # 利用登録者CSV (user_list.csv)
    user_data = [
        ["お問い合わせ番号", "ユーザーID", "管理コード", "シリアル番号", "登録日時", "氏名", "フリガナ", "生年月日", "性別", "住所", "電話番号", "メールアドレス"],
        ["1001", "U001", "A123", "SN1001", "2024-03-29 12:00:00", "田中 太郎", "タナカ タロウ", "1990/01/15", "男性", "東京都新宿区1-2-3", "090-1234-5678", "tanaka@example.com"],
        ["1002", "U002", "B456", "SN1002", "2024-03-28 14:30:00", "鈴木 花子", "スズキ ハナコ", "1985/07/22", "女性", "大阪府大阪市4-5-6", "080-9876-5432", "suzuki@example.com"],
        ["1003", "U003", "C789", "SN1003", "2024-03-27 09:15:00", "佐藤 健", "サトウ ケン", "1978/04/03", "男性", "北海道札幌市7-8-9", "070-5555-6666", "sato@example.com"],
        ["1004", "U004", "D012", "SN1004", "", "高橋 美咲", "タカハシ ミサキ", "2000/12/30", "女性", "福岡県福岡市10-11-12", "090-2222-3333", "takahashi@example.com"],
        ["1005", "U005", "E345", "SN1005", "2024-03-25 16:10:00", "木本 一郎", "キモト イチロウ", "1975/08/20", "男性", "愛知県名古屋市13-14-15", "080-3333-4444", "yamamoto@example.com"],
        ["1006", "U006", "F678", "SN1006", "2024-03-24 18:50:00", "中村 美穂", "ナカムラ ミホ", "1981/02/15", "女性", "京都府京都市16-17-18", "070-7777-8888", "nakamura@example.com"],
        ["1007", "U007", "G901", "SN1007", "2024-03-23 11:05:00", "井上 直樹", "イノウエ ナオキ", "1995/12/10", "男性", "広島県広島市19-20-21", "090-9999-0000", "inoue@example.com"],
        ["1008", "U008", "H234", "SN1008", "", "松本 由美", "マツモト ユミ", "1963/04/25", "女性", "宮城県仙台市22-23-24", "080-5555-6666", "matsumoto@example.com"],
        ["1009", "U009", "I567", "SN1009", "2024-03-21 13:40:00", "小林 翔", "コバヤシ ショウ", "2002/09/05", "男性", "長野県長野市25-26-27", "070-1111-2222", "kobayashi@example.com"],
        ["1010", "U010", "J890", "SN1010", "2024-03-20 15:20:00", "藤田 さくら", "フジタ サクラ", "1999/04/07", "女性", "神奈川県横浜市28-29-30", "090-4444-5555", "fujita@example.com"],
        ["1011", "U011", "K123", "SN1011", "2024-03-19 14:25:00", "中島 健太", "ナカジマ ケンタ", "1994/06/11", "男性", "静岡県静岡市31-32-33", "080-1234-5678", "nakajima@example.com"],
        ["1012", "U012", "L456", "SN1012", "2024-03-18 10:30:00", "斉藤 秀子", "サイトウ ヒデコ", "1987/03/30", "女性", "北海道旭川市34-35-36", "070-2222-3333", "saito@example.com"],
        ["1013", "U013", "M789", "SN1013", "2024-03-17 16:45:00", "石井 弘樹", "イシイ ヒロキ", "1991/08/01", "男性", "岩手県盛岡市37-38-39", "090-3333-4444", "ishii@example.com"],
        ["1014", "U014", "N012", "SN1014", "2024-03-16 17:05:00", "渡辺 優子", "ワタナベ ユウコ", "1996/10/10", "女性", "福島県郡山市40-41-42", "080-4444-5555", "watanabe@example.com"],
        ["1015", "U015", "O345", "SN1015", "2024-03-15 19:20:00", "山田 大輔", "ヤマダ ダイスケ", "1990/01/12", "男性", "青森県青森市43-44-45", "070-5555-6666", "yamada@example.com"],
        ["1016", "U016", "P678", "SN1016", "2024-03-14 15:10:00", "村本 佳子", "ムラモト ケイコ", "1984/05/21", "女性", "和歌山県和歌山市46-47-48", "090-6666-7777", "murakami@example.com"],
        ["1017", "U017", "Q901", "SN1017", "2024-03-13 13:30:00", "高田 俊", "タカダ シュン", "1992/02/28", "男性", "茨城県水戸市49-50-51", "080-7777-8888", "takada@example.com"],
        ["1018", "U018", "R234", "SN1018", "", "山口 幸子", "ヤマグチ サチコ", "1980/11/13", "女性", "群馬県前橋市52-53-54", "070-8888-9999", "yamaguchi@example.com"],
        ["1019", "U019", "S567", "SN1019", "2024-03-12 10:50:00", "黒田 清", "クロダ セイ", "2003/01/19", "男性", "福井県福井市55-56-57", "090-9999-0000", "kuroda@example.com"],
        ["1020", "U020", "T890", "SN1020", "2024-03-11 11:45:00", "藤井 美和", "フジイ ミワ", "1997/09/23", "女性", "栃木県宇都宮市58-59-60", "080-1111-2222", "fujii@example.com"],
        ["1001", "U001", "A123", "SN1001", "2024-03-29 12:00:00", "田中 太郎", "タナカ タロウ", "1990/01/15", "男性", "東京都新宿区1-2-3", "090-1234-5678", "tanaka@example.com"],
    ]

    # 全送付者CSV (address_list.csv)
    address_data = [
        ["氏名", "生年月日", "シリアル番号", "管理番号", "住所", "任意項目1", "任意項目2", "任意項目3141444", "任意項目4", "任意項目5"],
        ["田中 太郎", "19900115", "SN1001", "A123", "東京都新宿区1-2-3", "任意値1", "任意値2", "任意値3", "任意値4", "任意値5"],
        ["鈴木 花子", "19850722", "SN1002", "B456", "大阪府大阪市4-5-6", "任意値1", "任意値2", "任意値3", "任意値4", "任意値5"],
        ["佐藤 健", "19780403", "SN1003", "C789", "北海道札幌市7-8-9", "任意値1", "任意値2", "任意値3", "任意値4", "任意値5"],
        ["高橋 美咲", "20001230", "SN1004", "D012", "福岡県福岡市10-11-12", "任意値1", "任意値2", "任意値3", "任意値4", "任意値5"],
        ["山本 一郎", "19750820", "SN1005", "E345", "愛知県名古屋市13-14-15", "任意値1", "任意値2", "任意値3", "任意値4", "任意値5"],
        ["中村 美穂", "19810215", "SN1006", "F678", "京都府京都市16-17-18", "任意値1", "任意値2", "任意値3", "任意値4", "任意値5"],
        ["井上 直樹", "19951210", "SN1007", "G901", "広島県広島市19-20-21", "任意値1", "任意値2", "任意値3", "任意値4", "任意値5"],
        ["松本 由美", "19630425", "SN1008", "H234", "宮城県仙台市22-23-24", "任意値1", "任意値2", "任意値3", "任意値4", "任意値5"],
        ["小林 俊介", "20020905", "SN1009", "I567", "長野県長野市25-26-27", "", "", "", "", ""],
        ["藤田 さくら", "19990407", "SN1010", "J890", "神奈川県横浜市28-29-30", "任意値1", "任意値2", "任意値3", "任意値4", "任意値5"],
        ["中島 健太", "19940611", "SN1011", "K123", "静岡県静岡市31-32-33", "任意値1", "任意値2", "任意値3", "任意値4", "任意値5"],
        ["斉藤 智子", "19870330", "SN1012", "L456", "北海道旭川市34-35-36", "任意値1", "任意値2", "任意値3", "任意値4", "任意値5"],
        ["石井 弘樹", "19910801", "SN1013", "M789", "岩手県盛岡市37-38-39", "任意値1", "任意値2", "任意値3", "任意値4", "任意値5"],
        ["渡辺 優子", "19961010", "SN1014", "N012", "福島県郡山市40-41-42", "任意値1", "任意値2", "任意値3", "任意値4", "任意値5"],
        ["山田 大輔", "19900112", "SN1015", "O345", "青森県青森市43-44-45", "任意値1", "任意値2", "任意値3", "任意値4", "任意値5"],
        ["村上 佳子", "19840521", "SN1016", "P678", "和歌山県和歌山市46-47-48", "任意値1", "任意値2", "任意値3", "任意値4", "任意値5"],
        ["高田 俊", "19920228", "SN1017", "Q901", "茨城県水戸市49-50-51", "任意値1", "任意値2", "任意値3", "任意値4", "任意値5"],
        ["山口 幸子", "19801113", "SN1018", "R234", "群馬県前橋市52-53-54", "任意値1", "任意値2", "任意値3", "任意値4", "任意値5"],
        ["黒田 清", "20030119", "SN1019", "S567", "福井県福井市55-56-57", "任意値1", "任意値2", "任意値3", "任意値4", "任意値5"],
        ["藤井 美和", "19970923", "SN1020", "T890", "栃木県宇都宮市58-59-60", "任意値1", "任意値2", "任意値3", "任意値4", "任意値5"],
        ["田中 二郎", "19900115", "SN2001", "A123", "東京都新宿区1-2-3", "任意値1", "任意値2", "任意値3", "任意値4", "任意値5"],
        ["鈴木 三郎", "19850722", "SN2002", "B456", "大阪府大阪市4-5-6", "任意値1", "任意値2", "任意値3", "任意値4", "任意値5"],
        ["佐藤 四郎", "19780403", "SN2003", "C789", "北海道札幌市7-8-9", "任意値1", "任意値2", "任意値3", "任意値4", "任意値5"],
        ["高橋 五郎", "20001230", "SN2004", "D012", "福岡県福岡市10-11-12", "任意値1", "任意値2", "任意値3", "任意値4", "任意値5"],
        ["山本 六郎", "19750820", "SN2005", "E345", "愛知県名古屋市13-14-15", "任意値1", "任意値2", "任意値3", "任意値4", "任意値5"],
        ["中村 七郎", "19810215", "SN2006", "F678", "京都府京都市16-17-18", "任意値1", "任意値2", "任意値3", "任意値4", "任意値5"],
        ["井上 八郎", "19951210", "SN2007", "G901", "広島県広島市19-20-21", "任意値1", "任意値2", "任意値3", "任意値4", "任意値5"],
        ["松本 九郎", "19630425", "SN2008", "H234", "宮城県仙台市22-23-24", "", "", "", "", ""],
        ["小林 十郎", "20020905", "SN2009", "I567", "長野県長野市25-26-27", "任意値1", "任意値2", "任意値3", "任意値4", "任意値5"],
        ["藤田 十一郎", "19990407", "SN2010", "J890", "神奈川県横浜市28-29-30", "任意値1", "任意値2", "任意値3", "任意値4", "任意値5"],
        ["中島 十二郎", "19940611", "SN2011", "K123", "静岡県静岡市31-32-33", "任意値1", "任意値2", "任意値3", "任意値4", "任意値5"],
        ["斉藤 十三郎", "19870330", "SN2012", "L456", "北海道旭川市34-35-36", "任意値1", "任意値2", "任意値3", "任意値4", "任意値5"],
        ["石井 十四郎", "19910801", "SN2013", "M789", "岩手県盛岡市37-38-39", "任意値1", "任意値2", "任意値3", "任意値4", "任意値5"],
        ["渡辺 十五郎", "19961010", "SN2014", "N012", "福島県郡山市40-41-42", "", "", "", "", ""],
        ["山田 十六郎", "19900112", "SN2015", "O345", "青森県青森市43-44-45", "", "", "", "", ""],
        ["村上 十七郎", "19840521", "SN2016", "P678", "和歌山県和歌山市46-47-48", "", "", "", "", ""],
        ["高田 十八郎", "19920228", "SN2017", "Q901", "茨城県水戸市49-50-51", "", "", "", "", ""],
        ["山口 十九郎", "19801113", "SN2018", "R234", "群馬県前橋市52-53-54", "", "", "", "", ""],
        ["黒田 二十郎", "20030119", "SN2019", "S567", "福井県福井市55-56-57"],
        ["藤井 二十一郎", "19970923", "SN2020", "T890", "栃木県宇都宮市58-59-60", "", "", "", "", ""],
        ["田中 二十二郎", "19900115", "SN2021", "A123", "東京都新宿区1-2-3", "", "", "", "", ""],
        ["鈴木 二十三郎", "19850722", "SN2022", "B456", "大阪府大阪市4-5-6", "", "", "", "", ""],
        ["佐藤 二十四郎", "19780403", "SN2023", "C789", "北海道札幌市7-8-9", "", "", "", "", ""],
        ["高橋 二十五郎", "20001230", "SN2024", "D012", "福岡県福岡市10-11-12", "", "", "", "", ""],
        ["山本 二十六郎", "19750820", "SN2025", "E345", "愛知県名古屋市13-14-15", "", "", "", "", ""],
        ["中村 二十七郎", "19810215", "SN2026", "F678", "京都府京都市16-17-18", "", "", "", "", ""],
        ["井上 二十八郎", "19951210", "SN2027", "G901", "広島県広島市19-20-21", "", "", "", "", ""],
        ["松本 二十九郎", "19630425", "SN2028", "H234", "宮城県仙台市22-23-24", "", "", "", "", ""],
        ["小林 三十郎", "20020905", "SN2029", "I567", "長野県長野市25-26-27", "", "", "", "", ""],
        ["藤田 三十一郎", "19990407", "SN2030", "J890", "神奈川県横浜市28-29-30", "", "", "", "", ""],
        ["中島 三十二郎", "19940611", "SN2031", "K123", "静岡県静岡市31-32-33", "", "", "", "", ""],
        ["斉藤 三十三郎", "19870330", "SN2032", "L456", "北海道旭川市34-35-36", "", "", "", "", ""],
        ["石井 三十四郎", "19910801", "SN2033", "M789", "岩手県盛岡市37-38-39", "", "", "", "", ""],
        ["渡辺 三十五郎", "19961010", "SN2034", "N012", "福島県郡山市40-41-42", "", "", "", "", ""],
        ["山田 三十六郎", "19900112", "SN2035", "O345", "青森県青森市43-44-45", "任意値1", "任意値2", "任意値3", "任意値4", "任意値5"],
        ["村上 三十七郎", "19840521", "SN2036", "P678", "和歌山県和歌山市46-47-48", "任意値1", "任意値2", "任意値3", "任意値4", "任意値5"],
        ["高田 三十八郎", "19920228", "SN2037", "Q901", "茨城県水戸市49-50-51", "任意値1", "任意値2", "任意値3", "任意値4", "任意値5"],
        ["山口 三十九郎", "19801113", "SN2038", "R234", "群馬県前橋市52-53-54", "任意値1", "任意値2", "任意値3", "任意値4", "任意値5"],
        ["黒田 四十郎", "20030119", "SN2039", "S567", "福井県福井市55-56-57", "任意値1", "任意値2", "任意値3", "任意値4", "任意値5"],
        ["藤井 四十一郎", "19970923", "SN2040", "T890", "栃木県宇都宮市58-59-60", "任意値1", "任意値2", "任意値3", "任意値4", "任意値5"],
        ["田中 四十二郎", "19900115", "SN2041", "A123", "東京都新宿区1-2-3", "任意値1", "任意値2", "任意値3", "任意値4", "任意値5"],
        ["鈴木 四十三郎", "19850722", "SN2042", "B456", "大阪府大阪市4-5-6", "任意値1", "任意値2", "任意値3", "任意値4", "任意値5"],
        ["佐藤 四十四郎", "19780403", "SN2043", "C789", "北海道札幌市7-8-9", "任意値1", "任意値2", "任意値3", "任意値4", "任意値5"],
        ["高橋 四十五郎", "20001230", "SN2044", "D012", "福岡県福岡市10-11-12", "任意値1", "任意値2", "任意値3", "任意値4", "任意値5"],
        ["山本 四十六郎", "19750820", "SN2045", "E345", "愛知県名古屋市13-14-15", "任意値1", "任意値2", "任意値3", "任意値4", "任意値5"],
        ["中村 四十七郎", "19810215", "SN2046", "F678", "京都府京都市16-17-18", "任意値1", "任意値2", "任意値3", "任意値4", "任意値5"],
        ["井上 四十八郎", "19951210", "SN2047", "G901", "広島県広島市19-20-21", "任意値1", "任意値2", "任意値3", "任意値4", "任意値5"],
        ["松本 四十九郎", "19630425", "SN2048", "H234", "宮城県仙台市22-23-24", "任意値1", "任意値2", "任意値3", "任意値4", "任意値5"],
        ["小林 五十郎", "20020905", "SN2049", "I567", "長野県長野市25-26-27", "任意値1", "任意値2", "任意値3", "任意値4", "任意値5"],
    ]

    # CSVファイルを作成
    with open(
        "./assets/test_csv/利用登録者リスト.csv", "w", newline="", encoding="utf-8"
    ) as f:
        writer = csv.writer(f)
        writer.writerows(user_data)

    with open(
        "./assets/test_csv/全送付者リスト.csv", "w", newline="", encoding="utf-8"
    ) as f:
        writer = csv.writer(f)
        writer.writerows(address_data)

    print("テストデータを作成しました！")


# 実行
create_test_csv()
