import customtkinter as ctk
from config import colors
from config.fonts import get_fonts
from ui.widgets.file_save_form import FileSaveForm
from ui.widgets.set_replace_words import SetReplaceWords
from ui.widgets.select_original_book import SelectOriginalBookFrame


class CreateDigitalPdfPage(ctk.CTkFrame):
    def __init__(self, parent, result):
        super().__init__(parent)
        fonts = get_fonts()

        # ヘッダー
        header_frame = ctk.CTkFrame(self, fg_color=colors.theme_color, corner_radius=0)
        header_frame.pack(fill="x")

        ctk.CTkLabel(
            header_frame,
            text="デジタル通知PDF作成",
            font=fonts["title"],
            text_color="white",
        ).pack(side="left", padx=20, pady=4)

        # デジタル通知PDF作成説明
        intro_frame = ctk.CTkFrame(self, fg_color="transparent", corner_radius=0)
        intro_frame.pack(fill="x")

        # Csvマッチングに戻る
        ctk.CTkButton(
            intro_frame,
            text="← 通知物分別結果に戻る",
            text_color="white",
            fg_color=colors.theme_color,
            hover_color=colors.theme_color,
            font=fonts["title"],
            command=lambda: parent.back_frame("MatchingResultPage"),
        ).pack(side="top", anchor="nw", padx=10, pady=10)

        ctk.CTkLabel(
            intro_frame,
            text="デジタル通知用の通知物を作成します。",
            font=fonts["description"],
        ).pack(side="top", anchor="nw", padx=10)

        # 通知物名入力・保存先選択
        self.file_save_form = FileSaveForm(self)

        # 置換文字設定
        self.replace_words = SetReplaceWords(self, result)

        # 原本ブック選択
        self.original_book_frame = SelectOriginalBookFrame(self)
