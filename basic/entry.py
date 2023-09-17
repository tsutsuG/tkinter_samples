import tkinter as tk

#---------- 定数設定 ----------
WINDOW_SIZE = '300x150'     # ウィンドウサイズ
WINDOW_POS  = '100+100'     # ウィンドウ位置
WINDOW_TITLE = 'Window'     # ウィンドウ名

#---------- 関数定義 ----------
def print_txt(event:tk.Event):
    print(event.char)

#--------- メイン処理 ----------
# トップレベルウィジェットの生成
root = tk.Tk()
# ウィンドウサイズと位置の設定
root.geometry(WINDOW_SIZE + '+' + WINDOW_POS)
# ウィンドウタイトルの設定
root.title(WINDOW_TITLE)

# Entry ウィジェットの生成+配置
ent_test = tk.Entry(root, width=20, state='normal')
ent_test.pack(pady=50)
# イベントハンドラの設定
ent_test.bind('<KeyPress>', print_txt)

# イベントループ
root.mainloop()