import tkinter as tk
from tkinter import messagebox

#---------- 定数設定 ----------
WINDOW_SIZE  = '300x150'    # ウィンドウサイズ
WINDOW_POS   = '100+100'    # ウィンドウ位置
WINDOW_TITLE = 'Window'     # ウィンドウ名

#---------- 関数定義 ----------
def show_msgbox():
    messagebox.showinfo('msgbox', 'Button pressed.')

#--------- メイン処理 ----------
# トップレベルウィジェットの生成
root = tk.Tk()
# ウィンドウサイズと位置の設定
root.geometry(WINDOW_SIZE + '+' + WINDOW_POS)
# ウィンドウタイトルの設定
root.title(WINDOW_TITLE)

# Button ウィジェットの生成+配置
btn_test = tk.Button(root, text='test', command=show_msgbox)
btn_test.pack()

# イベントループ
root.mainloop()