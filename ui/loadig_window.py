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
        self.label = ctk.CTkLabel(self, text=message, font=font["title"])
        self.label.pack(expand=True, padx=10, pady=20)

    def close(self):
        if self.winfo_exists():  # ウィンドウが存在する場合のみ破棄
            self.destroy()
