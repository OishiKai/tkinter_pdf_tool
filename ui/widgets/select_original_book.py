import customtkinter as ctk
from config.fonts import get_fonts
from config import colors
import logic.file_handler as file_handler


class SelectOriginalBookFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=0, fg_color="transparent")
        self.pack(fill="x")
        fonts = get_fonts()

        # 説明
        description_frame = ctk.CTkFrame(
            self,
            corner_radius=0,
            fg_color="transparent",
        )
        description_frame.pack(fill="x", padx=10)

        ctk.CTkLabel(
            description_frame,
            text="3. 原本ブックを選択してください。",
            font=fonts["description"],
            height=0,
        ).pack(side="top", anchor="nw")

        # 原本ブック選択ボタン
        button_frame = ctk.CTkFrame(
            self,
            corner_radius=0,
            fg_color="transparent",
        )
        button_frame.pack(fill="x", padx=10, pady=5)

        self.select_button = ctk.CTkButton(
            button_frame,
            text="原本ブック選択",
            font=fonts["title"],
            fg_color=colors.theme_color,
            hover_color=colors.theme_color,
            text_color="white",
            command=self.select_original_book,
        )
        self.select_button.pack(side="left", padx=(10, 0))

        # 原本ブックパス
        self.file_path = ctk.CTkEntry(
            button_frame,
            text_color=colors.link_color,
        )
        self.file_path.pack(side="left", fill="x", expand=True, padx=10)

    def select_original_book(self):
        file_path = file_handler.open_excel()
        if file_path:
            self.file_path.delete(0, ctk.END)
            self.file_path.insert(0, file_path)
            self.file_path.configure(text_color=colors.link_color)

            # シート一覧を取得してコンソールに表示
            sheet_names = file_handler.get_excel_sheets(file_path)
            print("\n=== シート一覧 ===")
            if sheet_names:
                for i, sheet_name in enumerate(sheet_names):
                    print(f"{i+1}. {sheet_name}")
            else:
                print("シートが見つかりませんでした。")
            print("===============\n")
