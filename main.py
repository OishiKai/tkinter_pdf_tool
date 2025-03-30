import customtkinter as ctk
from ui.csv_matching_window import CsvMatchingPage
from ui.matching_result_window import MatchingResultPage


# メインアプリクラス
class SlepPdfApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("SLEP PDF作成ツール")
        self.geometry("1000x800")

        # 表示する画面の管理
        self.frames = {}

        # 縦横いっぱいに表示
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # 初期表示画面作成
        start_page = CsvMatchingPage(parent=self)
        self.frames["CsvCsvMatchingPage"] = start_page
        start_page.grid(row=0, column=0, sticky="nsew")

        # 初期画面を表示
        self.show_frame("CsvCsvMatchingPage")

    # 画面遷移メソッド
    def show_frame(
        self,
        page_name,  # 遷移先ページ名
        result=None,  # MatchingResultPage用の引数
    ):

        # MatchingResultPageへの遷移時
        if page_name == "MatchingResultPage":
            if "MatchingResultPage" in self.frames:
                self.frames[page_name].destroy()  # 既存のFrameを破棄
            frame = MatchingResultPage(
                parent=self,
                result=result,
            )  # `result` を渡して新しく作成
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # それ以外のページへの遷移
        frame = self.frames[page_name]
        frame.tkraise()

    # 前の画面に戻る
    def back_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    # フォーカスを解除するメソッド
    def remove_focus(self, event):
        self.focus_set()


if __name__ == "__main__":
    app = SlepPdfApp()
    app.mainloop()
