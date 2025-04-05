import tkinter as tk


win = tk.Tk()
win.title("第一个窗体")
win.geometry("250x120+100+100")

btn = tk.Button(win,text = "点我")
btn.pack()

win.mainloop()