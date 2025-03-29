from tkinter import filedialog
import json


def open_csv():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    return file_path


def save_matching_config_to_json(matching_config):

    with open("./.previous_matching_config.json", "w", encoding="utf-8") as f:
        json.dump(matching_config, f, ensure_ascii=False, indent=4)


def load_matching_config_from_json():
    try:
        with open("./.previous_matching_config.json", "r", encoding="utf-8") as f:
            matching_config = json.load(f)
        return matching_config
    except FileNotFoundError:
        return None
