import customtkinter as ctk


class ConfigureMatching(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=0, fg_color="transparent")
        self.pack(fill="x")

        # 共通フォント
        default_font = ctk.CTkFont(family="Helvetica", size=10)

        first_discription = ctk.CTkLabel(
            self,
            text="2. マッチング対象を選択し、項目値を設定します。",
            font=default_font,
        )
        first_discription.pack(side="top", anchor="nw", padx=8)

        # マッチング対象選択
        matching_target_frame = ctk.CTkFrame(
            self,
            corner_radius=0,
            fg_color="transparent",
        )

        matching_target_frame.pack(fill="x", padx=20)

        matching_target_discription = ctk.CTkLabel(
            matching_target_frame,
            text="②マッチング対象を選択してください。",
            font=("Helvetica", 10),
        )
        matching_target_discription.pack(side="top", anchor="nw")

        self.matching_target = ctk.CTkComboBox(
            matching_target_frame,
            font=("Helvetica", 10),
            width=30,
        )
        self.matching_target.pack(side="left")

        # 項目値設定
        item_value_frame = ctk.CTkFrame(
            self,
            corner_radius=0,
            fg_color="transparent",
        )

        item_value_frame.pack(fill="x", padx=20)

        item_value_discription = ctk.CTkLabel(
            item_value_frame,
            text="③項目値を設定してください。",
            font=("Helvetica", 10),
        )
        item_value_discription.pack(side="top", anchor="nw")

        self.item_value = ctk.CTkComboBox(
            item_value_frame,
            font=("Helvetica", 10),
            width=30,
        )
        self.item_value.pack(side="left")
