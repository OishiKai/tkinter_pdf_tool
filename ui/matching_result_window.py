import customtkinter as ctk
from config import colors
from config.fonts import get_fonts
from ui.widgets.matching_summary import MatchingSummary
from ui.widgets.csv_viewer import CSVViewer


class MatchingResultPage(ctk.CTkFrame):
    def __init__(self, parent, result):
        super().__init__(parent)
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
            command=lambda: parent.back_frame("CsvCsvMatchingPage"),
        ).pack(side="top", anchor="nw", padx=10, pady=10)

        # 分別結果概要
        self.summary_frame = MatchingSummary(self, result)

        # 分別結果CSV表示
        self.view = CSVViewer(self, result)

        next_frame = ctk.CTkFrame(self, fg_color="transparent", corner_radius=0)
        next_frame.pack(fill="x")

        # 郵送通知PDF作成
        if len(result["no_match"]) > 0:
            ctk.CTkButton(
                next_frame,
                text="郵送通知PDF作成",
                text_color="white",
                fg_color=colors.accent_color,
                hover_color=colors.accent_color,
                command=lambda: print("郵送通知PDF作成"),
                font=fonts["title"],
            ).pack(side="right", padx=10, pady=10)

        # デジタル通知PDF作成
        if len(result["one_match"]) > 0:
            ctk.CTkButton(
                next_frame,
                text="デジタル通知PDF作成",
                text_color="white",
                fg_color=colors.link_color,
                hover_color=colors.link_color,
                command=lambda: print("デジタル通知PDF作成"),
                font=fonts["title"],
            ).pack(side="right", padx=10, pady=10)

    def backWindow(self):
        if self.winfo_exists():
            self.withdraw()  # ウィンドウを非表示にする
            self.grab_release()  # メインウィンドウの操作を再開
            self.destroy()  # ウィンドウを破棄
            print("マッチングウィンドウに戻ります")
