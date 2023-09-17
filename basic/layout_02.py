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

# レイアウトの列数と割合を設定
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)
# レイアウトの行数と割合を設定
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

# Frame の生成
frame_l1 = tk.Frame(root, relief='raised', bd=3, bg='#fce4d6')
frame_l2 = tk.Frame(root, relief='raised', bd=3, bg='#e2efda')
frame_r1 = tk.Frame(root, relief='raised', bd=3, bg='#ddebf7')
# Frame の配置
frame_l1.grid(column=0, row=0, rowspan=1, padx=5, pady=5, sticky=tk.NSEW)
frame_l2.grid(column=0, row=1, rowspan=1, padx=5, pady=5, sticky=tk.NSEW)
frame_r1.grid(column=1, row=0, rowspan=2, padx=5, pady=5, sticky=tk.NSEW)

# イベントループ
root.mainloop()