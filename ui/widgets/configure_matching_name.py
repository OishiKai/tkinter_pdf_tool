import customtkinter as ctk
import config.colors as colors
import config.matching_targets as matching_targets
import logic.file_handler as file_handler
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
            width=600 / len(matching_targets.matching_items),
            height=20,
            bg_color="lightgray",
        ).grid(row=0, column=0)

        # マッチング項目名分ループしてテーブルのヘッダーを作成
        for item in matching_targets.matching_items:
            ctk.CTkLabel(
                matching_item_frame,
                text=item,
                font=fonts["default"],
                width=600 / len(matching_targets.matching_items),
                height=20,
                bg_color="lightgray",
            ).grid(row=0, column=matching_targets.matching_items.index(item) + 1)

        ctk.CTkLabel(
            matching_item_frame,
            text="項目値",
            font=fonts["default"],
            width=600 / len(matching_targets.matching_items),
            height=40,
            bg_color="lightgray",
        ).grid(row=1, column=0)

        # マッチング項目値入力フォーム
        self.matching_entry_map = {}  # {"項目名": entry} の形式で入力された値を保持

        # マッチング項目名分ループしてテーブルのボディーを作成
        for item in matching_targets.matching_items:
            entry = ctk.CTkEntry(
                matching_item_frame,
                corner_radius=0,
                border_width=1,
                font=fonts["default"],
                width=600 / len(matching_targets.matching_items),
                height=40,
                justify="center",
                fg_color=colors.input_color,
                border_color="gray",
            )
            entry.grid(row=1, column=matching_targets.matching_items.index(item) + 1)
            self.matching_entry_map[item] = entry

        # 過去のマッチング設定を読み込む
        previous_matching_config = file_handler.load_matching_config_from_json()
        if previous_matching_config:
            # 過去のマッチング設定を読み込む
            previous_map = previous_matching_config["matching_value_map"]
            for item, entry in self.matching_entry_map.items():
                if item in previous_map:
                    entry.insert(0, previous_map[item])
