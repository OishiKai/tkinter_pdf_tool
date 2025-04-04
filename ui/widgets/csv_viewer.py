import tkinter as tk
from tkinter import ttk
import config.fonts as fonts
import customtkinter as ctk
import config.colors as colors


class CSVViewer(ctk.CTkFrame):
    def __init__(self, master, result):
        super().__init__(master, fg_color="transparent", corner_radius=0)
        self.pack(fill="both", expand=True)
        self.result = result
        font = fonts.get_fonts()

        top_frame = ctk.CTkFrame(self, fg_color="transparent", corner_radius=0)
        top_frame.pack(fill="x", padx=10)

        self.load_digital_button = ctk.CTkButton(
            top_frame,
            text="デジタル通知対象を表示",
            text_color="white",
            fg_color=colors.link_color,
            hover_color=colors.link_color,
            command=self.show_digital_target,
            font=font["title"],
        )
        self.load_digital_button.pack(side="left", padx=10, pady=10)

        self.load_postal_button = ctk.CTkButton(
            top_frame,
            text="郵送通知対象を表示",
            text_color="white",
            fg_color=colors.accent_color,
            hover_color=colors.accent_color,
            command=self.show_postal_target,
            font=font["title"],
        )
        self.load_postal_button.pack(side="left", padx=10, pady=10)

        if len(self.result["multiple_match"]) > 0:
            self.load_multiple_button = ctk.CTkButton(
                top_frame,
                text="分別不可データを表示",
                text_color="white",
                fg_color=colors.error_color,
                hover_color=colors.error_color,
                command=self.show_multiple_target,
                font=font["title"],
            )
            self.load_multiple_button.pack(side="left", padx=10, pady=5)

        # ttk のスタイルを設定（フォントサイズを統一）
        style = ttk.Style()
        style.configure("Treeview", font=("Meiryo UI", 10))  # 本体のフォント
        style.configure(
            "Treeview.Heading", font=("Meiryo UI", 12, "bold")
        )  # ヘッダーのフォント

        # csv表示用Frame
        csv_frame = ctk.CTkFrame(self, fg_color="transparent", corner_radius=0)
        csv_frame.pack(fill="both", expand=True, padx=10)
        csv_frame.grid_rowconfigure(0, weight=1)  # 行の重みを設定
        csv_frame.grid_columnconfigure(0, weight=1)

        # Treeviewウィジェットを追加（テーブル表示用）
        self.tree = ttk.Treeview(csv_frame, show="headings")  # ヘッダーを表示
        self.tree.grid(row=0, column=0, sticky="nsew")

        # 縦スクロールバーを追加
        self.y_scrollbar = ttk.Scrollbar(
            csv_frame, orient="vertical", command=self.tree.yview
        )
        self.tree.configure(yscrollcommand=self.y_scrollbar.set)
        self.y_scrollbar.grid(row=0, column=1, sticky="ns")

        # 横スクロールバーを追加
        self.x_scrollbar = ttk.Scrollbar(
            csv_frame, orient="horizontal", command=self.tree.xview
        )
        self.tree.configure(xscrollcommand=self.x_scrollbar.set)
        self.x_scrollbar.grid(row=1, column=0, sticky="ew")

        self.show_digital_target()  # 初期表示はデジタル通知対象者

    # テーブル要素構築
    def setup_csv(self, csv_data):
        headers = self.result["header"]

        # ヘッダーの設定
        self.tree["columns"] = headers
        fixed_column_width = 120  # 列の幅を固定

        for header in headers:
            self.tree.heading(header, text=header)  # ヘッダー名を設定
            self.tree.column(
                header,
                width=fixed_column_width,
                anchor="center",
                stretch=tk.NO,
            )  # 列幅固定

        # データを挿入（古いデータは削除）
        self.tree.delete(*self.tree.get_children())  # 既存データをクリア
        for index, row_data in enumerate(csv_data):
            tag = "evenrow" if index % 2 == 0 else "oddrow"
            self.tree.insert("", "end", values=list(row_data.values()), tags=(tag,))

        self.tree.tag_configure("evenrow", background="#e8e8e8")  # 偶数行
        self.tree.tag_configure("oddrow", background="white")

    # デジタル通知対象者を表示
    def show_digital_target(self):
        self.setup_csv(self.result["one_match"])

    # 郵送対象者を表示
    def show_postal_target(self):
        self.setup_csv(self.result["no_match"])

    # 分別不可データを表示
    def show_multiple_target(self):
        self.setup_csv(self.result["multiple_match"])
