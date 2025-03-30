import customtkinter as ctk
from ui.csv_matching_window import CsvMatchingPage
from ui.matching_result_window import MatchingResultPage


class SlepPdfApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("SLEP PDF作成ツール")
        self.geometry("1000x800")

        # 画面管理用の辞書
        self.frames = {}
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # 画面を作成（PageOneは後で `result` を渡すので、ここでは作成しない）
        start_page = CsvMatchingPage(parent=self)
        self.frames["CsvCsvMatchingPage"] = start_page
        start_page.grid(row=0, column=0, sticky="nsew")

        self.show_frame("CsvCsvMatchingPage")

    def show_frame(self, page_name, result=None):
        """指定したページを表示する（必要なら result を渡す）"""
        if page_name == "MatchingResultPage":
            if "MatchingResultPage" in self.frames:
                self.frames[page_name].destroy()  # 既存のFrameを破棄
            frame = MatchingResultPage(
                parent=self,
                result=result,
            )  # `result` を渡して新しく作成
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        frame = self.frames[page_name]
        frame.tkraise()

    # フォーカスを解除するメソッド
    def remove_focus(self, event):
        self.focus_set()


if __name__ == "__main__":
    app = SlepPdfApp()
    app.mainloop()
