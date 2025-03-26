import customtkinter as ctk
from ui.sub_window import SubWindow
from logic.file_handler import open_csv

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("メインウィンドウ")
        self.geometry("500x300")

        self.button_open = ctk.CTkButton(self, text="CSVを開く", command=self.open_file)
        self.button_open.pack(pady=20)

        self.button_sub = ctk.CTkButton(self, text="サブウィンドウを開く", command=self.open_sub_window)
        self.button_sub.pack(pady=20)

    def open_file(self):
        file_path = open_csv()
        print(f"選択したファイル: {file_path}")

    def open_sub_window(self):
        self.sub_win = SubWindow(self)
        self.sub_win.grab_set()
