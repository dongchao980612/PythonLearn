import tkinter as tk
from tkinter import ttk


def changeGUI(textChange):
    frm1.destroy()
    frm2.destroy()
    frm3.destroy()

    tk.Label(win, text=textChange).pack()



def  handlerLogin():

    # 获取用户和密码
    name = name_entry.get()
    passwd = passwd_entry.get()

    print(name,passwd)
    if name.strip()=="admin" and passwd.strip()=="root":
        changeGUI("欢迎进入本系统")
    else:
        changeGUI("对不起，不能进入本系统")
win = tk.Tk()
win.title("用户登录界面")  # #窗口标题
win.geometry("300x80+200+20")  # #窗口位置500后面是字母x

frm1=tk.Frame(win)
frm1.pack()
name_label = tk.Label(frm1,text = "账号")
name_label.pack(side = tk.LEFT)
name_entry = tk.Entry(frm1,textvariable=tk.StringVar())
name_entry.pack(side = tk.LEFT)

frm2=tk.Frame(win)
frm2.pack()
passwd_label = tk.Label(frm2,text = "密码")
passwd_label.pack(side = tk.LEFT)
passwd_entry = tk.Entry(frm2,show="*",textvariable=tk.StringVar())
passwd_entry.pack(side = tk.LEFT)


frm3=tk.Frame(win)
frm3.pack()
login_button = tk.Button(frm3,text="登录",command=handlerLogin)
login_button.pack(side = tk.RIGHT)


win.mainloop()  # #窗口持久化