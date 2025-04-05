import  tkinter  as tk


class App(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.pack()

        self.chose_text = ["鲜花", "鼓掌", "鸡蛋"]
        self.chose_Var = tk.StringVar()
        self.chose_Var = tk.StringVar(value="请选择")  # 设置初始值
        self.chose_label = tk.Label(self, text="请选择", textvariable=self.chose_Var, width=30)
        self.chose_label.grid(row=0, column=0, columnspan=3)

        # 复选按钮
        self.A_Checkbutton = tk.Checkbutton(self,text="C语言",state="disabled")
        self.A_Checkbutton.select()
        self.A_Checkbutton.grid(row=1,column=0,sticky = tk.N)

        self.B_Checkbutton = tk.Checkbutton(self,text="Java")
        self.B_Checkbutton.deselect()
        self.B_Checkbutton.grid(row=1,column=1,sticky = tk.N)

        self.C_Checkbutton = tk.Checkbutton(self,text="Python")
        self.C_Checkbutton.select()
        self.C_Checkbutton.grid(row=1,column=2,sticky = tk.N)


        # 单选按钮
        self.radVar = tk.IntVar()
        self.radiobuttons = []
        for i in range(3):
            radiobutton = tk.Radiobutton(self, text=self.chose_text[i], variable=self.radVar, value=i, command=self.radCall)
            radiobutton.grid(row=2, column=i, sticky=tk.N)
            self.radiobuttons.append(radiobutton)


    def radCall(self):
        self.chose_Var.set(self.chose_text[self.radVar.get()])


def main():
    root = tk.Tk()
    root.title("单选和复选")
    root.geometry("300x150+200+20")
    app=App(master=root)
    app.mainloop()


if __name__ == '__main__':
    main()