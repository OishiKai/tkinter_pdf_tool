import customtkinter as ctk
from config.fonts import get_fonts


class ConfigureMatchingName(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=0, fg_color="transparent")
        self.pack(fill="x", pady=8)
        fonts = get_fonts()

        first_discription = ctk.CTkLabel(
            self,
            text="3. 全送付者リストCSVのマッチング項目(※)を設定します。②全送付者リスト内で使用されている項目名を水色の枠内に入力してください。",
            font=fonts["description"],
        )
        first_discription.pack(side="top", anchor="nw", padx=8)

        matching_name_discription = ctk.CTkLabel(
            self,
            text="※全送付者リストCSVのマッチング項目とは、マッチング対象の「氏名」「生年月日」「シリアル番号」「管理コード」の4項目に該当する②CSVの項目名を確認するためのものです。",
            font=fonts["description"],
            height=0,
        )
        matching_name_discription.pack(side="top", anchor="nw", padx=12)

        expample_description = ctk.CTkLabel(
            self,
            text="例 : ②CSVで氏名にあたる項目名が「name」の場合、水色の枠内に「name」と入力してください。",
            font=fonts["description"],
            height=0,
        )
        expample_description.pack(side="top", anchor="nw", padx=12)

        # マッチング項目名称入力Frame
        matching_name_frame = ctk.CTkFrame(
            self,
            corner_radius=0,
            fg_color="transparent",
        )
        matching_name_frame.pack(fill="x", padx=20)

        matching_name_discription = ctk.CTkLabel(
            matching_name_frame,
            text="マッチング項目名称入力",
            font=fonts["description"],
        )
        matching_name_discription.pack(side="top", anchor="nw")

        # マッチング項目名のテーブル
        matching_item_frame = ctk.CTkFrame(
            self,
            corner_radius=0,
            fg_color="transparent",
        )
        matching_item_frame.pack(fill="x", padx=20, pady=0)

        # マッチング項目名のテーブル
        ctk.CTkLabel(
            matching_item_frame,
            text="項目名",
            font=fonts["default"],
            width=150,
            height=20,
            bg_color="lightgray",
        ).grid(row=0, column=0)
        ctk.CTkLabel(
            matching_item_frame,
            text="氏名",
            font=fonts["default"],
            width=150,
            height=20,
            bg_color="lightgray",
        ).grid(row=0, column=1)
        ctk.CTkLabel(
            matching_item_frame,
            text="生年月日",
            font=fonts["default"],
            width=150,
            height=20,
            bg_color="lightgray",
        ).grid(row=0, column=2)
        ctk.CTkLabel(
            matching_item_frame,
            text="シリアル番号",
            font=fonts["default"],
            width=150,
            height=20,
            bg_color="lightgray",
        ).grid(row=0, column=3)
        ctk.CTkLabel(
            matching_item_frame,
            text="管理コード",
            font=fonts["default"],
            width=150,
            height=20,
            bg_color="lightgray",
        ).grid(row=0, column=4)
        ctk.CTkLabel(
            matching_item_frame,
            text="項目値",
            font=fonts["default"],
            width=150,
            height=40,
            bg_color="lightgray",
        ).grid(row=1, column=0)

        # マッチング項目名入力

        # 氏名
        self.matching_name = ctk.CTkEntry(
            matching_item_frame,
            corner_radius=0,
            border_width=1,
            font=fonts["default"],
            width=150,
            height=40,
            justify="center",
            fg_color="#ddebf7",
            border_color="gray",
        )
        self.matching_name.grid(row=1, column=1)

        # 生年月日
        self.matching_birthday = ctk.CTkEntry(
            matching_item_frame,
            corner_radius=0,
            border_width=1,
            font=fonts["default"],
            width=150,
            height=40,
            justify="center",
            fg_color="#ddebf7",
            border_color="gray",
        )
        self.matching_birthday.grid(row=1, column=2)

        # シリアル番号
        self.matching_serial_number = ctk.CTkEntry(
            matching_item_frame,
            corner_radius=0,
            border_width=1,
            font=fonts["default"],
            width=150,
            height=40,
            justify="center",
            fg_color="#ddebf7",
            border_color="gray",
        )
        self.matching_serial_number.grid(row=1, column=3)

        # 管理コード
        self.matching_code = ctk.CTkEntry(
            matching_item_frame,
            corner_radius=0,
            border_width=1,
            font=fonts["default"],
            width=150,
            height=40,
            justify="center",
            fg_color="#ddebf7",
            border_color="gray",
        )
        self.matching_code.grid(row=1, column=4)
