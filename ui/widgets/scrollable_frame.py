import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog
import csv


class ScrollableFrame(ctk.CTkFrame):
    """スクロール可能なフレーム"""

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.canvas = tk.Canvas(self, bg="white", highlightthickness=0)
        self.scrollbar_y = ctk.CTkScrollbar(
            self, orientation="vertical", command=self.canvas.yview
        )
        self.scrollbar_x = ctk.CTkScrollbar(
            self, orientation="horizontal", command=self.canvas.xview
        )

        self.scrollable_frame = ctk.CTkFrame(self.canvas)
        self.frame_id = self.canvas.create_window(
            (0, 10000), window=self.scrollable_frame, anchor="nw"
        )

        self.canvas.configure(
            yscrollcommand=self.scrollbar_y.set, xscrollcommand=self.scrollbar_x.set
        )

        # スクロールバーをキャンバスの横・縦に配置
        self.scrollbar_y.pack(side="right", fill="y")
        self.scrollbar_x.pack(side="bottom", fill="x")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.scrollable_frame.bind("<Configure>", self.update_scroll_region)
        self.bind_all_scroll_events()

    def update_scroll_region(self, event=None):
        """スクロール領域を更新"""
        self.canvas.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def bind_all_scroll_events(self):
        """マウスホイール・トラックパッドでスクロールできるようにする"""
        self.scrollable_frame.bind("<MouseWheel>", self.mouse_y_scroll)
        self.scrollable_frame.bind("<Shift-MouseWheel>", self.mouse_x_scroll)
        self.scrollable_frame.bind(
            "<Button-4>", self.on_linux_scroll_up
        )  # Linux上スクロール
        self.scrollable_frame.bind(
            "<Button-5>", self.on_linux_scroll_down
        )  # Linux下スクロール

    def mouse_y_scroll(self, event):
        """縦スクロール（トラックパッド対応）"""
        if event.state == 0 or event.state == 8:  # 縦スクロール
            direction = -1 if event.delta > 0 else 1
            self.canvas.yview_scroll(direction, "units")
        elif event.state == 1 or event.state == 9:  # 横スクロール
            direction = -1 if event.delta > 0 else 1
            self.canvas.xview_scroll(direction, "units")

    def mouse_x_scroll(self, event):
        """横スクロール（Shift + マウスホイール対応）"""
        direction = -1 if event.delta > 0 else 1
        self.canvas.xview_scroll(direction, "units")

    def on_linux_scroll_up(self, event):
        """Linuxのスクロール（上）"""
        self.canvas.yview_scroll(-1, "units")

    def on_linux_scroll_down(self, event):
        """Linuxのスクロール（下）"""
        self.canvas.yview_scroll(1, "units")
