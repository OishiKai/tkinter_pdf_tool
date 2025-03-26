import customtkinter as ctk
from logic.file_handler import open_csv


class SelectCsvFile(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=0, fg_color="transparent")
        self.pack(fill="x")

        # 共通フォント
        default_font = ctk.CTkFont(family="Helvetica", size=10)

        first_discription = ctk.CTkLabel(
            self,
            text="1. 下記の手順に従い、CSVファイルを読み込みます。",
            font=default_font,
        )
        first_discription.pack(side="top", anchor="nw", padx=8)

        # 利用登録者一覧CSV読み込み
        user_list_csv_frame = ctk.CTkFrame(
            self,
            corner_radius=0,
            fg_color="transparent",
        )

        user_list_csv_frame.pack(fill="x", padx=20)

        user_list_csv_discription = ctk.CTkLabel(
            user_list_csv_frame,
            text="①Speed Letter Plus管理Webからダウンロードした利用者一覧CSVを選択してください。",
            font=("Helvetica", 10),
        )
        user_list_csv_discription.pack(side="top", anchor="nw")

        button_open = ctk.CTkButton(
            user_list_csv_frame,
            fg_color="#766b6b",
            hover_color="#766b6b",
            text="利用者一覧CSV読み込み",
            text_color="white",
            font=("Helvetica Bold", 12),
            command=self.select_user_list_csv,
            width=180,
        )
        button_open.pack(side="left")

        margin = ctk.CTkFrame(
            user_list_csv_frame,
            corner_radius=0,
            fg_color="transparent",
            height=10,
            width=10,
        )
        margin.pack(side="left")

        self.user_list_csv_path = ctk.CTkEntry(
            user_list_csv_frame,
            text_color="#6495ed",
        )
        self.user_list_csv_path.pack(side="left", fill="x", expand=True)

        # 全送付者リストCSV読み込み

        address_list_csv_frame = ctk.CTkFrame(
            self,
            corner_radius=0,
            fg_color="transparent",
        )

        address_list_csv_frame.pack(fill="x", padx=20, pady=10)

        address_list_csv_discription = ctk.CTkLabel(
            address_list_csv_frame,
            text="②自治体基幹システム等からダウンロードした全送付者リストCSVを選択してください。",
            font=("Helvetica", 10),
        )

        address_list_csv_discription.pack(side="top", anchor="nw")

        button_open = ctk.CTkButton(
            address_list_csv_frame,
            fg_color="#766b6b",
            hover_color="#766b6b",
            text="全送付者リストCSV読み込み",
            text_color="white",
            font=("Helvetica Bold", 12),
            command=self.select_address_list_csv,
            width=180,
        )
        button_open.pack(side="left")

        margin = ctk.CTkFrame(
            address_list_csv_frame,
            corner_radius=0,
            fg_color="transparent",
            height=10,
            width=10,
        )
        margin.pack(side="left")

        self.address_list_csv_path = ctk.CTkEntry(
            address_list_csv_frame,
            text_color="#6495ed",
        )
        self.address_list_csv_path.pack(side="left", fill="x", expand=True)

    def select_user_list_csv(self):
        file_path = open_csv()
        self.user_list_csv_path.delete(0, "end")
        self.user_list_csv_path.insert(0, file_path)

    def select_address_list_csv(self):
        file_path = open_csv()
        self.address_list_csv_path.delete(0, "end")
        self.address_list_csv_path.insert(0, file_path)
