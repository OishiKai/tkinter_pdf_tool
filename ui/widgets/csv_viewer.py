import tkinter as tk
from tkinter import ttk
import config.fonts as fonts
import customtkinter as ctk


class CSVViewer(ctk.CTkFrame):
    def __init__(self, master, result):
        super().__init__(master, fg_color="transparent", corner_radius=0)
        self.pack(fill="both", expand=True, pady=20)
        self.result = result
        font = fonts.get_fonts()

        top_frame = ctk.CTkFrame(self, fg_color="transparent", corner_radius=0)
        top_frame.pack(fill="x", padx=10)

        self.load_button = ctk.CTkButton(
            top_frame, text="郵送対象者を表示", command=self.setup_csv
        )
        self.load_button.pack(side="left", padx=10, pady=5)

        # ttk のスタイルを設定（フォントサイズを統一）
        style = ttk.Style()
        style.configure("Treeview", font=("Meiryo UI", 10))  # 本体のフォント
        style.configure(
            "Treeview.Heading", font=("Meiryo UI", 12, "bold")
        )  # ヘッダーのフォント

        # Treeviewウィジェットを追加（テーブル表示用）
        self.tree = ttk.Treeview(self, show="headings")  # ヘッダーを表示
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        # 横スクロールバーを追加
        self.x_scrollbar = ttk.Scrollbar(
            self, orient="horizontal", command=self.tree.xview
        )
        self.tree.configure(xscrollcommand=self.x_scrollbar.set)
        self.x_scrollbar.pack(fill="x", side="bottom")

        self.after(100, self.setup_csv)

    def setup_csv(self):
        headers = self.result["header"]
        no_matches = self.result["no_match"]

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
        for row_data in no_matches:
            self.tree.insert("", "end", values=list(row_data.values()))  # 行を追加
