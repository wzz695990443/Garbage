import tkinter as tk
import pywinstyles


if __name__ == '__main__':
    import tkinter as tk

    # 创建窗口
    window = tk.Tk()
    window.title('Mywindow')  # 窗口的标题
    window.geometry('200x100')  # 窗口的大小
    # 定义一个lable
    l = tk.Label(window,
                 text='Hi! this is TK!',  # 标签的文字
                 bg='green',  # 标签背景颜色
                 font=('Arial', 12),  # 字体和字体大小
                 width=15, height=2  # 标签长宽（以字符长度计算）
                 )
    l.pack()  # 固定窗口位置

    window.mainloop()
