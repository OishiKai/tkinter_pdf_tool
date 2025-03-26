import customtkinter as ctk
from ui.sub_window import SubWindow
from ui.widgets.select_csv_file import SelectCsvFile
from ui.widgets.select_matching_item import SelectMatchingItem
from logic.file_handler import open_csv


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("SLEP PDF作成ツール")
        self.geometry("1000x800")

        # ヘッダー
        intro_frame = ctk.CTkFrame(self, fg_color="#766b6b", corner_radius=0)
        intro_frame.pack(fill="x")

        intro_label = ctk.CTkLabel(
            intro_frame,
            text="Speed Letter Plus 通知方法判別ツール",
            font=("Helvetica Bold", 12),
            text_color="white",
        )
        intro_label.pack(side="left", padx=20, pady=4)

        # 1. 二種CSV読み込み
        select_csv_file = SelectCsvFile(self)

        # 2. マッチング対象選択
        slect_matching_item = SelectMatchingItem(self)

    def open_sub_window(self):
        self.sub_win = SubWindow(self)
        self.sub_win.grab_set()
