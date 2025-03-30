import customtkinter as ctk
import config.colors as colors
from config.fonts import get_fonts
from logic.file_handler import open_csv
import logic.file_handler as file_handler


# 利用登録者、全送付者リストCSV読み込み
class SelectCsvFile(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=0, fg_color="transparent")
        self.pack(fill="x")
        fonts = get_fonts()

        first_discription = ctk.CTkLabel(
            self,
            text="1. 下記の手順に従い、CSVファイルを読み込みます。",
            font=fonts["description"],
        )
        first_discription.pack(side="top", anchor="nw", padx=8)

        # 利用登録者一覧CSV読み込みFrame
        user_list_csv_frame = ctk.CTkFrame(
            self,
            corner_radius=0,
            fg_color="transparent",
        )

        user_list_csv_frame.pack(fill="x", padx=20)

        # 利用登録者一覧CSV読み込み説明
        user_list_csv_discription = ctk.CTkLabel(
            user_list_csv_frame,
            text="①Speed Letter Plus管理Webからダウンロードした利用者一覧CSVを選択してください。",
            font=fonts["description"],
        )
        user_list_csv_discription.pack(side="top", anchor="nw")

        # 利用登録者一覧CSV読み込みボタン
        button_open = ctk.CTkButton(
            user_list_csv_frame,
            fg_color=colors.theme_color,
            hover_color=colors.theme_color,
            text="利用者一覧CSV読み込み",
            text_color="white",
            font=fonts["title"],
            command=self.select_user_list_csv,
            width=180,
        )
        button_open.pack(side="left")

        # 余白
        margin = ctk.CTkFrame(
            user_list_csv_frame,
            corner_radius=0,
            fg_color="transparent",
            height=10,
            width=10,
        )
        margin.pack(side="left")

        # 利用登録者一覧CSVパス
        self.user_list_csv_path = ctk.CTkEntry(
            user_list_csv_frame,
            text_color=colors.link_color,
        )
        self.user_list_csv_path.pack(side="left", fill="x", expand=True)

        # 全送付者リストCSV読み込みFrame
        address_list_csv_frame = ctk.CTkFrame(
            self,
            corner_radius=0,
            fg_color="transparent",
        )
        address_list_csv_frame.pack(fill="x", padx=20, pady=10)

        # 全送付者リストCSV読み込み説明
        address_list_csv_discription = ctk.CTkLabel(
            address_list_csv_frame,
            text="②自治体基幹システム等からダウンロードした全送付者リストCSVを選択してください。",
            font=fonts["description"],
        )
        address_list_csv_discription.pack(side="top", anchor="nw")

        # 全送付者リストCSV読み込みボタン
        button_open = ctk.CTkButton(
            address_list_csv_frame,
            fg_color=colors.theme_color,
            hover_color=colors.theme_color,
            text="全送付者リストCSV読み込み",
            text_color="white",
            font=fonts["title"],
            command=self.select_address_list_csv,
            width=180,
        )
        button_open.pack(side="left")

        # 余白
        margin = ctk.CTkFrame(
            address_list_csv_frame,
            corner_radius=0,
            fg_color="transparent",
            height=10,
            width=10,
        )
        margin.pack(side="left")

        # 全送付者リストCSVパス
        self.address_list_csv_path = ctk.CTkEntry(
            address_list_csv_frame,
            text_color=colors.link_color,
        )
        self.address_list_csv_path.pack(side="left", fill="x", expand=True)

        # 過去のマッチング設定を読み込む
        previous_matching_config = file_handler.load_matching_config_from_json()
        if previous_matching_config:
            # 過去のマッチング設定が存在する場合、CSVパスをセット
            self.user_list_csv_path.insert(
                0, previous_matching_config["user_list_csv_path"]
            )
            self.address_list_csv_path.insert(
                0, previous_matching_config["address_list_csv_path"]
            )

    # 利用登録者一覧CSVファイル選択
    def select_user_list_csv(self):
        file_path = open_csv()

        if not file_path:
            return

        self.user_list_csv_path.delete(0, "end")
        self.user_list_csv_path.insert(0, file_path)
        self.focus_set()

    # 全送付者リストCSVファイル選択
    def select_address_list_csv(self):
        file_path = open_csv()

        if not file_path:
            return

        self.address_list_csv_path.delete(0, "end")
        self.address_list_csv_path.insert(0, file_path)
        self.focus_set()
