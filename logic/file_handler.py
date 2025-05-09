from tkinter import filedialog
import json
import pandas as pd


# CSVファイルを選択するダイアログを表示
def open_csv():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    return file_path


# 選択されたマッチング設定をJSON形式で保存
def save_matching_config_to_json(matching_config):

    with open("./.previous_matching_config.json", "w", encoding="utf-8") as f:
        json.dump(matching_config, f, ensure_ascii=False, indent=4)


# 保存済みのマッチング設定をJSON形式で読み込み
def load_matching_config_from_json():
    try:
        with open("./.previous_matching_config.json", "r", encoding="utf-8") as f:
            matching_config = json.load(f)
        return matching_config
    except FileNotFoundError:
        return None


# 保存先のディレクトリを選択するダイアログを表示
def open_directory():
    directory_path = filedialog.askdirectory()
    return directory_path


# Excelファイルを選択するダイアログを表示 .xlsx .xlsm
def open_excel():
    file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx *.xlsm")])
    return file_path


# Excelファイルからシート一覧を取得
def get_excel_sheets(file_path):
    try:
        # Excelファイルを読み込む
        excel_file = pd.ExcelFile(file_path)
        # シート名の一覧を取得
        sheet_names = excel_file.sheet_names
        return sheet_names
    except Exception as e:
        print(f"Excelファイルの読み込みエラー: {e}")
        return []
