import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog
import csv


class ScrollableFrame(ctk.CTkFrame):
    """スクロール可能なフレーム"""

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.canvas = tk.Canvas(self, highlightthickness=0)
        self.scrollbar_x = ctk.CTkScrollbar(
            self, orientation="horizontal", command=self.canvas.xview
        )

        self.scrollable_frame = ctk.CTkFrame(self.canvas, fg_color="transparent")
        self.frame_id = self.canvas.create_window(
            (0, 0), window=self.scrollable_frame, anchor="nw"
        )

        self.canvas.configure(xscrollcommand=self.scrollbar_x.set)

        # スクロールバーをキャンバスの横に配置
        self.scrollbar_x.pack(side="bottom", fill="x")
        self.canvas.pack(side="top", fill="both", expand=True)

        self.scrollable_frame.bind("<Configure>", self.update_scroll_region)
        self.bind_all_scroll_events()

    def update_scroll_region(self, event=None):
        """スクロール領域を更新"""
        self.canvas.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def bind_all_scroll_events(self):
        """マウスホイール・トラックパッドでスクロールできるようにする"""
        self.scrollable_frame.bind("<MouseWheel>", self.mouse_scroll)
        self.scrollable_frame.bind("<Shift-MouseWheel>", self.mouse_scroll)
        self.canvas.bind("<MouseWheel>", self.mouse_scroll)
        self.canvas.bind("<Shift-MouseWheel>", self.mouse_scroll)

    def mouse_scroll(self, event):
        """スクロール（マウスホイール・トラックパッド対応）"""
        if event.state == 0 or event.state == 8:  # 縦スクロール
            direction = -1 if event.delta > 0 else 1
            self.canvas.xview_scroll(direction, "units")
        elif event.state == 1 or event.state == 9:  # 横スクロール
            direction = -1 if event.delta > 0 else 1
            self.canvas.xview_scroll(direction, "units")
