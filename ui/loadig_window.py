import customtkinter as ctk
import config.fonts as fonts


class LoadingWindow(ctk.CTkToplevel):
    """「読み込み中」ウィンドウ"""

    def __init__(self, parent, message="マッチング処理中..."):
        super().__init__(parent)
        font = fonts.get_fonts()
        self.title("Loading")
        self.geometry("200x200")
        self.resizable(False, False)
        self.grab_set()  # メインウィンドウの操作をブロック

        # 親ウィンドウの中央に配置する
        self.center_window(parent)

        # 閉じるボタン（×）を無効化
        self.protocol("WM_DELETE_WINDOW", self.disable_close)

        self.label = ctk.CTkLabel(self, text=message, font=font["title"])
        self.label.pack(expand=True, padx=10, pady=20)

    def center_window(self, parent):
        """親ウィンドウの中央に配置"""
        self.update_idletasks()  # ウィンドウサイズの正確な計算のために更新
        parent_x = parent.winfo_x()
        parent_y = parent.winfo_y()
        parent_width = parent.winfo_width()
        parent_height = parent.winfo_height()

        window_width = 200
        window_height = 100

        pos_x = parent_x + (parent_width - window_width) // 2
        pos_y = parent_y + (parent_height - window_height) // 2

        self.geometry(f"{window_width}x{window_height}+{pos_x}+{pos_y}")

    def disable_close(self):
        """閉じるボタンを無効化（何もしない）"""
        pass

    def close(self):
        if self.winfo_exists():
            self.withdraw()  # ウィンドウを非表示にする
            self.grab_release()  # メインウィンドウの操作を再開
            self.destroy()  # ウィンドウを破棄
