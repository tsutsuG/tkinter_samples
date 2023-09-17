import tkinter as tk

#---------- 定数設定 ----------
WINDOW_SIZE = '300x150'     # ウィンドウサイズ
WINDOW_POS  = '100+100'     # ウィンドウ位置
WINDOW_TITLE = 'Window'     # ウィンドウ名

# grid の引数指定
# (column, columnspan, row, rowspan)
GRID_ARGS = ({'column':0, 'columnspan':1, 'row':0, 'rowspan':1},
             {'column':1, 'columnspan':1, 'row':0, 'rowspan':1},
             {'column':0, 'columnspan':1, 'row':1, 'rowspan':1},
             {'column':1, 'columnspan':1, 'row':1, 'rowspan':1},
             {'column':0, 'columnspan':2, 'row':2, 'rowspan':1})
# grid の個数
GRID_NUMS = len(GRID_ARGS)

#--------- メイン処理 ----------
# トップレベルウィジェットの生成
root = tk.Tk()

# ウィンドウサイズと位置の設定
root.geometry(WINDOW_SIZE + '+' + WINDOW_POS)
# ウィンドウタイトルの設定
root.title(WINDOW_TITLE)

# レイアウトの列数と割合を設定
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
# レイアウトの行数と割合を設定
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)

# Label ウィジェットの生成
lbl_texts = [tk.Label(root, text='No.'+str(num), relief=tk.SOLID) for num in range(5)]
# Label ウィジェットの配置
for i in range(GRID_NUMS):
    lbl_texts[i].grid(cnf=GRID_ARGS[i])

# イベントループ
root.mainloop()