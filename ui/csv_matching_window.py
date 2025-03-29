import customtkinter as ctk
import config.colors as colors
from config.fonts import get_fonts
from ui.matching_result_window import MatchingResultWindow
from ui.widgets.select_csv_file import SelectCsvFile
from ui.widgets.select_matching_item import SelectMatchingItem
from ui.widgets.configure_matching_name import ConfigureMatchingName
from logic.file_handler import open_csv
from logic.csv_matching import csv_matching


class CsvMatchingWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("SLEP PDF作成ツール")
        self.geometry("1000x800")
        fonts = get_fonts()

        # ヘッダー
        intro_frame = ctk.CTkFrame(self, fg_color=colors.theme_color, corner_radius=0)
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
            fg_color=colors.accent_color,
            hover_color=colors.accent_color,
            text_color="white",
            command=self.execute_matching,
            width=300,
        )
        matching_button.pack(side="top", anchor="nw", padx=20)

        # エラーメッセージFrame
        self.error_message_frame = ctk.CTkFrame(
            self,
            fg_color=colors.error_color,
            corner_radius=5,
            height=30,
        )
        self.error_message_frame.pack_forget()  # 初期状態は非表示

        # エラーメッセージ
        self.error_message = ctk.CTkLabel(
            self.error_message_frame,
            font=fonts["title"],
            text_color="white",
        )
        self.error_message.pack(side="top", anchor="nw", padx=20)

        # Enterでフォーカスを解除
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

        if not user_list_csv_path or not address_list_csv_path:
            self.error_message.configure(text="CSVファイルを選択してください")
            self.error_message_frame.pack(side="top", anchor="nw", padx=30)
            return

        self.error_message_frame.pack_forget()

        # マッチング項目取得
        matching_target = self.slect_matching_item.matching_target.get()

        # マッチング項目値取得
        matching_entry_map = self.configure_matching_name.matching_entry_map

        # マッチング実行
        result = csv_matching(
            user_list_csv_path=user_list_csv_path,
            address_list_csv_path=address_list_csv_path,
            matching_terget=matching_target,
            matching_entry_map=matching_entry_map,
        )

        if isinstance(result, str):
            self.error_message.configure(text=result)
            self.error_message_frame.pack(side="top", anchor="nw", padx=30)
            return

        # マッチング結果を表示するサブウィンドウを開く
        sub_window = MatchingResultWindow(self, result)
        sub_window.grab_set()
        sub_window.focus_set()
