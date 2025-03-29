import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog
import csv
from ui.widgets.scrollable_frame import ScrollableFrame


class CSVViewer(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=0)
        self.pack(fill="both", expand=True, pady=20)

        top_frame = ctk.CTkFrame(self)
        top_frame.pack(fill="x", padx=10)

        self.load_button = ctk.CTkButton(
            top_frame, text="CSVを開く", command=self.load_csv
        )
        self.load_button.pack(side="left", padx=10, pady=5)

        self.scrollable_frame = ScrollableFrame(self)
        self.scrollable_frame.pack(fill="both", expand=True, padx=10, pady=10)

    def load_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if not file_path:
            return

        # 既存のウィジェットをクリア
        for widget in self.scrollable_frame.scrollable_frame.winfo_children():
            widget.destroy()

        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            data = list(reader)

        # ヘッダー行を作成
        for col, header in enumerate(data[0]):
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
        for row, row_data in enumerate(data[1:], start=1):
            for col, cell in enumerate(row_data):
                frame = ctk.CTkFrame(
                    self.scrollable_frame.scrollable_frame,
                    corner_radius=0,
                )
                frame.grid(row=row, column=col, padx=1, pady=1, sticky="nsew")

                label = ctk.CTkLabel(frame, text=cell)
                label.pack(fill="both", expand=True, padx=5)
                label.bind("<MouseWheel>", self.scrollable_frame.mouse_y_scroll)

        # カラム幅を自動調整
        for col in range(len(data[0])):
            self.scrollable_frame.scrollable_frame.grid_columnconfigure(col, weight=1)

        self.scrollable_frame.update_scroll_region()
