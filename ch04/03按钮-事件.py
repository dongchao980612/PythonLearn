import tkinter as tk


win = tk.Tk()
win.title("第一个窗体")
win.geometry("250x120+100+100")

def on_clicked():
    print("click...")

btn = tk.Button(win,text = "点我",command=on_clicked)
btn.pack()

win.mainloop()