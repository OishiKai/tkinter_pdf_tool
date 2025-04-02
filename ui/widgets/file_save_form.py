import customtkinter as ctk
from config import colors
from config.fonts import get_fonts
import logic.file_handler as file_handler


# PDF作成時のファイル名入力・保存先選択フォーム
class FileSaveForm(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=0, fg_color="transparent")
        self.pack(fill="x")
        fonts = get_fonts()

        # ファイル保存先選択
        description_frame = ctk.CTkFrame(
            self,
            corner_radius=0,
            fg_color="transparent",
        )
        description_frame.pack(fill="x", padx=10)

        ctk.CTkLabel(
            description_frame,
            text="1. 保存する通知物名を入力し、作成するPDFの保存先を選択してください。",
            font=fonts["description"],
            height=0,
        ).pack(side="top", anchor="nw")

        ctk.CTkLabel(
            description_frame,
            text="※ 通知物名に使用できる文字は「ひらがな」「カタカナ」「漢字(第1水準漢字及び第2水準漢字)」「英字」「数字」「全角記号(・？！々ー)」のみです。",
            font=fonts["description"],
            height=0,
        ).pack(side="top", anchor="nw")

        file_save_form_frame = ctk.CTkFrame(
            self,
            corner_radius=0,
            fg_color="transparent",
        )
        file_save_form_frame.pack(fill="x", padx=20, pady=15)

        ctk.CTkLabel(
            file_save_form_frame,
            text="通知物名",
            font=fonts["default"],
            text_color="white",
            width=100,
            fg_color="gray",
            bg_color="gray",
        ).grid(row=0, column=0)

        # 通知物名入力
        self.file_name_entry = ctk.CTkEntry(
            file_save_form_frame,
            font=fonts["default"],
            width=200,
            fg_color=colors.input_color,
            bg_color=colors.input_color,
            border_width=0,
        )
        self.file_name_entry.grid(row=0, column=1, sticky="w")

        # 保存先選択
        ctk.CTkButton(
            file_save_form_frame,
            text="保存先選択",
            font=fonts["title"],
            fg_color=colors.theme_color,
            hover_color=colors.theme_color,
            text_color="white",
            command=self.select_save_directory,
            width=100,
        ).grid(row=1, column=0, pady=10, padx=10, sticky="ew")

        file_save_form_frame.columnconfigure(1, weight=1)

        # 保存先ディレクトリパス
        self.save_directory_path = ctk.CTkEntry(
            file_save_form_frame,
            text_color=colors.link_color,
            fg_color="white",
            bg_color="transparent",
            font=fonts["default"],
            corner_radius=5,
            state="readonly",
        )
        self.save_directory_path.grid(row=1, column=1, sticky="ew")

        # 初期表示時、フォーム内の色が変わるのを防ぐ
        self.save_directory_path.focus_set()

    def select_save_directory(self):
        # 保存先ディレクトリ選択
        directory_path = file_handler.open_directory()
        if directory_path:
            self.save_directory_path.configure(state="normal")
            self.save_directory_path.delete(0, ctk.END)
            self.save_directory_path.insert(0, directory_path)
            self.save_directory_path.configure(state="readonly")

        self.focus_set()  # フォーカス戻す
