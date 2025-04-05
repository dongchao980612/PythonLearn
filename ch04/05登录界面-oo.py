import  tkinter  as tk

class AfterLoginApp():
    def __init__(self,master,text):
        tk.Label(master, text=text).pack()


class LoginApp(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.textChange = None
        self.pack()
        self.frm1 = tk.Frame(master)
        self.frm1.pack()
        self.frm2 = tk.Frame(master)
        self.frm2.pack()
        self.frm3 = tk.Frame(master)
        self.frm3.pack()

        self.name_label = tk.Label(self.frm1, text="账号")
        self.name_label.pack(side=tk.LEFT)
        self.name_entry = tk.Entry(self.frm1, textvariable=tk.StringVar())
        self.name_entry.pack(side=tk.LEFT)


        self.passwd_label = tk.Label(self.frm2, text="密码")
        self.passwd_label.pack(side=tk.LEFT)
        self.passwd_entry = tk.Entry(self.frm2,show="*", textvariable=tk.StringVar())
        self.passwd_entry.pack(side=tk.LEFT)

        self.login_button = tk.Button(self.frm3, text="登录", command=self.handlerLogin)
        self.login_button.pack(side=tk.RIGHT)

    def handlerLogin(self,):

        # 获取用户和密码
        name = self.name_entry.get()
        passwd =self.passwd_entry.get()

        print(name, passwd)
        if name.strip() == "admin" and passwd.strip() == "root":
            self.textChange = "欢迎进入本系统"
        else  :
            self.textChange="对不起，不能进入本系统"
        self.frm1.destroy()
        self.frm2.destroy()
        self.frm3.destroy()

        AfterLoginApp(self,self.textChange)



def loginMain():
    win = tk.Tk()
    win.title("用户登陆界面示例")
    win.geometry("300x80+200+20")
    lgApp=LoginApp(master=win)
    lgApp.pack()
    lgApp.mainloop()


if __name__ == '__main__':
    loginMain()