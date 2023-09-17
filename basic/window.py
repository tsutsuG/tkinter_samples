import tkinter as tk

#---------- 定数設定 ----------
WINDOW_SIZE = '300x150'     # ウィンドウサイズ
WINDOW_POS  = '100+100'     # ウィンドウ位置
WINDOW_TITLE = 'Window'     # ウィンドウ名

#--------- メイン処理 ----------
# トップレベルウィジェットの生成
root = tk.Tk()

# ウィンドウサイズと位置の設定
root.geometry(WINDOW_SIZE + '+' + WINDOW_POS)
# ウィンドウタイトルの設定
root.title(WINDOW_TITLE)

# イベントループ
root.mainloop()