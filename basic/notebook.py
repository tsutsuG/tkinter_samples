import tkinter as tk
import tkinter.ttk as ttk
from tkinter import font

#---------- 定数設定 ----------
WINDOW_SIZE = '300x150'     # ウィンドウサイズ
WINDOW_POS  = '100+100'     # ウィンドウ位置
WINDOW_TITLE = 'Window'     # ウィンドウ名

# トップレベルウィジェットの生成
root = tk.Tk()
font_bold = font.Font(size=10, weight="bold")

# ウィンドウサイズと位置の設定
root.geometry(WINDOW_SIZE + '+' + WINDOW_POS)
# ウィンドウタイトルの設定
root.title(WINDOW_TITLE)

# スタイルの生成
style = ttk.Style()
style.theme_use('classic')

# ノートブックのスタイルの設定
style.configure(
    'nob_main.TNotebook',
    tabposition='wn',
    background='#eeeeee'
)

# タブのスタイルの設定
style.configure(
    'nob_main.TNotebook.Tab',
    foreground='#000000',
    background='#aaaaaa'
)
style.map(
    'nob_main.TNotebook.Tab',
    foreground=[
        ('active'  , '#ffffff'),
        ('disabled', '#aaaaaa' ),
        ('selected', '#2222ff' )
    ],
    background=[
        ('active'  , '#2222ff'),
        ('disabled', '#000000' ),
        ('selected', '#a6ccee' )
    ]
)

# Notebook ウィジェットの生成
nob_main = ttk.Notebook(
    root,
    style="nob_main.TNotebook"
)

nob_main.pack(padx=2, pady=2, fill=tk.BOTH, expand=True)

frames = []
for i in range(4):
    widget = ttk.Frame(
        root,
        name="frame_" + str(i),
    )
    frames.append(widget)
    nob_main.add(
        widget,
        text="TAB " + str(i)
    )

# メインループ
nob_main.focus()
root.mainloop()