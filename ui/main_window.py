import customtkinter as ctk
from config.fonts import get_fonts
from ui.sub_window import SubWindow
from ui.widgets.select_csv_file import SelectCsvFile
from ui.widgets.select_matching_item import SelectMatchingItem
from ui.widgets.configure_matching_name import ConfigureMatchingName
from logic.file_handler import open_csv


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("SLEP PDF作成ツール")
        self.geometry("1000x800")
        fonts = get_fonts()

        # ヘッダー
        intro_frame = ctk.CTkFrame(self, fg_color="#766b6b", corner_radius=0)
        intro_frame.pack(fill="x")

        intro_label = ctk.CTkLabel(
            intro_frame,
            text="Speed Letter Plus 通知方法判別ツール",
            font=fonts["title"],
            text_color="white",
        )
        intro_label.pack(side="left", padx=20, pady=4)

        # 1. 二種CSV読み込み
        self.select_csv_file = SelectCsvFile(self)

        # # 2. マッチング対象選択
        self.slect_matching_item = SelectMatchingItem(self)

        # # 3. マッチング項目値入力
        self.configure_matching_name = ConfigureMatchingName(self)

        # 4. マッチング実行
        matching_button_frame = ctk.CTkFrame(
            self,
            corner_radius=0,
            fg_color="transparent",
        )
        matching_button_frame.pack(fill="x", padx=10, pady=10)

        # マッチング実行説明
        ctk.CTkLabel(
            matching_button_frame,
            text="4. 「分別開始」ボタンを押すと通知方法が分別されます。",
            font=fonts["description"],
        ).pack(side="top", anchor="nw")

        # マッチング実行ボタン
        matching_button = ctk.CTkButton(
            matching_button_frame,
            text="分別開始",
            font=fonts["title"],
            fg_color="#2fb22b",
            hover_color="#2fb22b",
            text_color="white",
            command=self.execute_matching,
            width=300,
        )
        matching_button.pack(side="top", anchor="nw", padx=20, pady=10)

        # クリック時にフォーカスを解除
        self.bind_all("<Return>", self.remove_focus)

    # フォーカスを解除するメソッド
    def remove_focus(self, event):
        self.focus_set()

    # マッチング実行
    def execute_matching(self):
        print("マッチング実行")

        # csvファイルパス取得
        user_list_csv_path = self.select_csv_file.user_list_csv_path.get()
        address_list_csv_path = self.select_csv_file.address_list_csv_path.get()
        print(user_list_csv_path)
        print(address_list_csv_path)
        if not user_list_csv_path or not address_list_csv_path:
            print("ファイルが選択されていません")
            return

        # マッチング項目取得
        matching_target = self.slect_matching_item.matching_target.get()

        # マッチング項目値取得
        matching_name = self.configure_matching_name.matching_name.get()
        matching_birthday = self.configure_matching_name.matching_birthday.get()
        matching_serial = self.configure_matching_name.matching_serial_number.get()
        matching_code = self.configure_matching_name.matching_code.get()
