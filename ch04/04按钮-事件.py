import tkinter

def  click_fun1():
    lable1 = tkinter.Label(win,text="点击才出现")
    lable1.pack()
win = tkinter.Tk()
win.geometry("250x120+100+100")

btn = tkinter.Button(win,text = "点我",command=click_fun1)

btn.pack()
win.mainloop()