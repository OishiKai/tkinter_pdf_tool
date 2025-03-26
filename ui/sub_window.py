import customtkinter as ctk

class SubWindow(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("サブウィンドウ")
        self.geometry("300x200")

        label = ctk.CTkLabel(self, text="サブウィンドウ")
        label.pack(pady=20)
