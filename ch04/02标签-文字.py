import tkinter as  tk

win = tk.Tk()
win.title("第一个窗体")
win.geometry("300x400+100+100")


text_label = tk.Label(win,text="你好,世界",font="楷体")
text_label.pack()

win.mainloop()




