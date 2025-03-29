import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog
import csv
from ui.widgets.scrollable_frame import ScrollableFrame


class CSVViewer(ctk.CTkFrame):
    def __init__(self, master, result):
        super().__init__(master, fg_color="transparent", corner_radius=0)
        self.pack(fill="both", expand=True, pady=20)
        self.result = result

        top_frame = ctk.CTkFrame(self, fg_color="transparent", corner_radius=0)
        top_frame.pack(fill="x", padx=10)

        self.load_button = ctk.CTkButton(
            top_frame, text="郵送対象者を表示", command=self.setup_csv
        )
        self.load_button.pack(side="left", padx=10, pady=5)

        self.scrollable_frame = ScrollableFrame(self)
        self.scrollable_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.after(10, self.setup_csv)

    def setup_csv(self):
        # 既存のウィジェットをクリア
        for widget in self.scrollable_frame.scrollable_frame.winfo_children():
            widget.destroy()

        headers = self.result["header"]
        no_matches = self.result["no_match"]
        one_matches = self.result["one_match"]
        multiple_matches = self.result["multiple_matches"]

        # ヘッダー行を作成
        for col, header in enumerate(headers):
            frame = ctk.CTkFrame(
                self.scrollable_frame.scrollable_frame,
                fg_color="gray",
                corner_radius=0,
            )
            frame.grid(row=0, column=col, padx=1, pady=1, sticky="nsew")

            label = ctk.CTkLabel(
                frame,
                text=header,
                text_color="white",
                fg_color="gray",
            )
            label.pack(fill="both", expand=True, padx=5)
            label.bind("<MouseWheel>", self.scrollable_frame.mouse_y_scroll)

        # データ行を作成
        for row, row_data in enumerate(no_matches, start=1):
            for col, cell in enumerate(row_data.values()):
                frame = ctk.CTkFrame(
                    self.scrollable_frame.scrollable_frame,
                    corner_radius=0,
                )
                frame.grid(row=row, column=col, padx=1, pady=1, sticky="nsew")

                label = ctk.CTkLabel(frame, text=cell)
                label.pack(fill="both", expand=True, padx=5)
                label.bind("<MouseWheel>", self.scrollable_frame.mouse_y_scroll)

        # カラム幅を自動調整
        for col in range(len(headers)):
            self.scrollable_frame.scrollable_frame.grid_columnconfigure(col, weight=1)

        self.scrollable_frame.update_scroll_region()
