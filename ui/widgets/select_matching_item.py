import customtkinter as ctk
from config.fonts import get_fonts
import config.matching_targets as matching_targets
import logic.file_handler as file_handler


# マッチング項目選択
class SelectMatchingItem(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=0, fg_color="transparent")
        self.pack(fill="x", pady=8)
        fonts = get_fonts()

        first_discription = ctk.CTkLabel(
            self,
            text="2. 1で読み込んだ①と②のCSVをマッチングして郵送者リストとデジタル送付者リストを作成するために、マッチング項目をプルダウンから選択します。",
            font=fonts["description"],
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
            text="マッチング対象を選択",
            font=fonts["description"],
        )
        matching_target_discription.pack(side="top", anchor="nw")

        # マッチング対象選択プルダウン
        self.matching_target = ctk.CTkComboBox(
            matching_target_frame,
            values=matching_targets.matching_targets,
            font=fonts["title"],
            width=200,
            state="readonly",
        )
        self.matching_target.set(matching_targets.matching_targets[0])
        self.matching_target.pack(side="left")
        self.matching_target.bind("<<ComboboxSelected>>", self.focus_set())

        # 注釈Frame
        matching_target_discription_frame = ctk.CTkFrame(
            self,
            corner_radius=0,
            fg_color="transparent",
        )
        matching_target_discription_frame.pack(fill="x", padx=30, pady=10)

        # シリアル番号注釈
        matching_target_discription1 = ctk.CTkLabel(
            matching_target_discription_frame,
            text="※1: シリアル番号でのマッチングは利用登録Webの本人確認アプリオプションのみご利用可能です。",
            font=fonts["description"],
            height=0,
        )
        matching_target_discription1.pack(side="top", anchor="nw")

        # 管理コード注釈
        matching_target_discription2 = ctk.CTkLabel(
            matching_target_discription_frame,
            text="※2: 管理コードでのマッチングは導入時に管理コード項目を選択した場合のみご利用可能です。",
            font=fonts["description"],
            height=0,
        )
        matching_target_discription2.pack(side="top", anchor="nw")

        previous_matching_config = file_handler.load_matching_config_from_json()
        if previous_matching_config:
            # 過去のマッチング設定を読み込む
            matching_target = previous_matching_config["matching_terget"]
            if matching_target in matching_targets.matching_targets:
                self.matching_target.set(matching_target)
            else:
                self.matching_target.set(matching_targets.matching_targets[0])
