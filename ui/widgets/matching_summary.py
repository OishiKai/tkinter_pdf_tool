import customtkinter as ctk
import config.colors as colors
from config.fonts import get_fonts


# CSVマッチング概要表示
class MatchingSummary(ctk.CTkFrame):
    def __init__(self, master, result):
        super().__init__(master, corner_radius=0, fg_color="transparent")
        self.pack(fill="x")
        fonts = get_fonts()

        # 結果概要説明
        summary_description = ctk.CTkLabel(
            self,
            text="通知方法の分別に成功しました。分別結果を確認してください。",
            font=fonts["description"],
        )
        summary_description.pack(side="top", anchor="nw", padx=12)

        # 結果概要Frame
        summary_frame = ctk.CTkFrame(
            self,
            corner_radius=0,
            fg_color="transparent",
        )
        summary_frame.pack(fill="x", padx=20)

        ctk.CTkLabel(
            summary_frame,
            text="結果概要",
            font=fonts["default"],
        ).pack(side="top", anchor="nw")

        all_summary_frame = ctk.CTkFrame(
            self,
            corner_radius=0,
            fg_color="transparent",
        )
        all_summary_frame.pack(side="top", anchor="nw", padx=20)

        summary = "OK"
        if len(result["multiple_match"]) > 0:
            summary = "NG"

        # 結果概要のテーブル
        ctk.CTkLabel(
            all_summary_frame,
            text="全体結果",
            width=100,
            font=fonts["default"],
            text_color="white",
            fg_color="gray",
        ).grid(row=0, column=0)
        self.all_summary = ctk.CTkLabel(
            all_summary_frame,
            text=summary,
            width=100,
            font=fonts["default"],
            fg_color="lightgray",
        ).grid(row=0, column=1)
        ctk.CTkLabel(
            all_summary_frame,
            text="OK : すべてのデータを分別完了, NG : 分別不可のデータあり",
            font=fonts["description"],
            fg_color="transparent",
        ).grid(row=0, column=2, padx=10)

        # 2行目はマージン
        ctk.CTkFrame(
            all_summary_frame,
            fg_color="transparent",
            corner_radius=0,
            width=100,
            height=10,
        ).grid(row=1, column=0)
        ctk.CTkFrame(
            all_summary_frame,
            fg_color="transparent",
            corner_radius=0,
            width=100,
            height=10,
        ).grid(row=1, column=1)

        # 3行目 デジタル通知
        ctk.CTkLabel(
            all_summary_frame,
            text="デジタル通知",
            width=100,
            font=fonts["default"],
            text_color="white",
            fg_color=colors.link_color,
        ).grid(row=2, column=0)
        ctk.CTkLabel(
            all_summary_frame,
            text=len(result["one_match"]),
            width=100,
            font=fonts["default"],
            fg_color="lightgray",
        ).grid(row=2, column=1)

        # 4行目 郵送通知
        ctk.CTkLabel(
            all_summary_frame,
            text="郵送通知",
            width=100,
            font=fonts["default"],
            text_color="white",
            fg_color=colors.accent_color,
        ).grid(row=3, column=0)
        ctk.CTkLabel(
            all_summary_frame,
            text=len(result["no_match"]),
            width=100,
            font=fonts["default"],
            fg_color="lightgray",
        ).grid(row=3, column=1)

        # 5行目 分別不可
        ctk.CTkLabel(
            all_summary_frame,
            text="分別不可",
            width=100,
            font=fonts["default"],
            text_color="white",
            fg_color=colors.error_color,
        ).grid(row=4, column=0)
        ctk.CTkLabel(
            all_summary_frame,
            text=len(result["multiple_match"]),
            width=100,
            font=fonts["default"],
            fg_color="lightgray",
        ).grid(row=4, column=1)
