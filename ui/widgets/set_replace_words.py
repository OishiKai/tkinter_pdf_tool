import customtkinter as ctk
import config.matching_targets as matching_targets
from config.fonts import get_fonts
from config import colors
from ui.widgets.scrollable_frame import ScrollableFrame


class SetReplaceWords(ctk.CTkFrame):
    def __init__(self, master, result):
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
            text="2. 通知物名に置換する文字を入力してください。",
            font=fonts["description"],
            height=0,
        ).pack(side="top", anchor="nw")

        # 横スクロール可能なフォーム
        form_frame = ctk.CTkFrame(
            self,
            corner_radius=0,
            fg_color="transparent",
            height=81,  # フォームの高さを固定
        )
        form_frame.pack(fill="x", padx=10, pady=5)
        form_frame.pack_propagate(False)  # 高さを固定

        # ScrollableFrameの作成
        scrollable_frame = ScrollableFrame(form_frame)
        scrollable_frame.pack(fill="x", expand=True)

        # ヘッダー行の作成
        header_frame = ctk.CTkFrame(
            scrollable_frame.scrollable_frame, fg_color="transparent"
        )
        header_frame.pack(fill="x")

        # 列幅の計算
        column_widths = []
        for header in result["header"]:
            # 文字数に応じて幅を計算（1文字あたり約10ピクセル）
            width = max(100, len(header) * 10 + 20)  # 最小幅100、余白20
            column_widths.append(width)

        for col, header in enumerate(result["header"]):
            label = ctk.CTkLabel(
                header_frame,
                text=header,
                font=fonts["default"],
                width=column_widths[col],
                height=30,
                fg_color="lightgray",
            )
            label.grid(row=0, column=col)

        # 入力フィールド行の作成
        entry_frame = ctk.CTkFrame(
            scrollable_frame.scrollable_frame, fg_color="transparent"
        )
        entry_frame.pack(fill="x")

        self.entries = []
        for col, header in enumerate(result["header"]):
            entry = ctk.CTkEntry(
                entry_frame,
                font=fonts["default"],
                border_width=1,
                corner_radius=0,
                fg_color=colors.input_color,
                width=column_widths[col],
                height=30,
                justify="center",  # 文字を中央寄せ
            )
            entry.insert(0, f"$${header}$$")  # 初期値を設定
            entry.grid(row=0, column=col)
            self.entries.append(entry)
