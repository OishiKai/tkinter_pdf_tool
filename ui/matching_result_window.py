import customtkinter as ctk
from config import colors
from config.fonts import get_fonts
from ui.widgets.matching_summary import MatchingSummary


class MatchingResultWindow(ctk.CTkToplevel):
    def __init__(self, master, result):
        super().__init__(master)
        self.title("SLEP PDF作成ツール")
        self.geometry("1000x800")
        fonts = get_fonts()

        # ヘッダー
        header_frame = ctk.CTkFrame(self, fg_color=colors.theme_color, corner_radius=0)
        header_frame.pack(fill="x")

        ctk.CTkLabel(
            header_frame,
            text="CSVマッチング結果",
            font=fonts["title"],
            text_color="white",
        ).pack(side="left", padx=20, pady=4)

        intro_frame = ctk.CTkFrame(self, fg_color="transparent", corner_radius=0)
        intro_frame.pack(fill="x")

        # Csvマッチングに戻る
        ctk.CTkButton(
            intro_frame,
            text="← マッチングに戻る",
            text_color="white",
            fg_color=colors.theme_color,
            hover_color=colors.theme_color,
            font=fonts["title"],
            command=self.backWindow,
        ).pack(side="top", anchor="nw", padx=10, pady=10)

        # 結果概要
        self.summary_frame = MatchingSummary(self)

    def backWindow(self):
        self.destroy()
        self.master.deiconify()
