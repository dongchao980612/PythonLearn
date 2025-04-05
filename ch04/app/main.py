import  tkinter  as tk
import tkinter as tk
from tkinter import filedialog, font
from tkinter.colorchooser import askcolor
from tkinter.messagebox import showerror, askyesnocancel


class App(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.master = master
        self.text_font = font.Font(family="Arial", size=15)  # 初始化字体
        self.current_file_path = None  # 当前打开的文件路径
        self.is_modified = False  # 跟踪文本是否被修改
        self.create_widgets()
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)  # 绑定关闭窗口事件

    def create_widgets(self):
        # 创建文本框
        self.text = tk.Text(self, font=self.text_font)
        self.text.pack(expand=True, fill="both")
        self.text.bind("<KeyRelease>", self.mark_modified)  # 绑定事件，标记文本被修改

        # 创建菜单栏
        menubar = tk.Menu(self.master)
        self.master.config(menu=menubar)

        # 文件菜单
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="打开", command=self.open_file)
        file_menu.add_command(label="保存", command=self.save_file)
        file_menu.add_command(label="另存为", command=self.save_file_as)
        file_menu.add_separator()
        file_menu.add_command(label="退出", command=self.quit_app)
        menubar.add_cascade(label="文件", menu=file_menu)
        # 修改菜单
        change_menu = tk.Menu(menubar, tearoff=0)
        change_menu.add_command(label="字体变大", command=self.increase_font)
        change_menu.add_command(label="字体变小", command=self.decrease_font)
        change_menu.add_separator()
        change_menu.add_command(label="选择字体颜色", command=self.change_text_color)
        change_menu.add_command(label="选择背景颜色", command=self.change_background_color)
        menubar.add_cascade(label="修改", menu=change_menu)


        # 编辑菜单
        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="复制", command=self.copy_text, accelerator="Ctrl+C")
        edit_menu.add_command(label="粘贴", command=self.paste_text, accelerator="Ctrl+V")
        menubar.add_cascade(label="编辑", menu=edit_menu)



        # 绑定快捷键
        self.master.bind("<Control-o>", lambda event: self.open_file())
        self.master.bind("<Control-s>", lambda event: self.save_file())
        self.master.bind("<Control-c>", lambda event: self.copy_text())
        self.master.bind("<Control-v>", lambda event: self.paste_text())



    def mark_modified(self, event=None):
        self.is_modified = True  # 标记文本被修改

    def open_file(self, event=None):
        if self.is_modified:  # 如果文本被修改且未保存，提示保存
            self.save_file()
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            self.current_file_path = file_path  # 更新当前文件路径
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                self.text.delete("1.0", tk.END)
                self.text.insert(tk.END, content)
            self.is_modified = False  # 重置修改标志志
        else:
            showerror("错误","未选择任何文件")

    def save_file(self, event=None):
        if self.current_file_path:  # 如果已经打开过文件
            with open(self.current_file_path, "w", encoding="utf-8") as file:
                content = self.text.get("1.0", tk.END)
                file.write(content)
            self.is_modified = False  # 重置修改标志
        else:  # 如果没有打开过文件，调用另存为
            self.save_file_as()

    def save_file_as(self, event=None):
        file_path = filedialog.asksaveasfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            self.current_file_path = file_path  # 更新当前文件路径
            with open(file_path, "w", encoding="utf-8") as file:
                content = self.text.get("1.0", tk.END)
                file.write(content)
            self.is_modified = False  # 重置修改标志

    def quit_app(self, event=None):
        if self.is_modified:  # 如果文本被修改且未保存，提示保存
            response = askyesnocancel("保存", "您有未保存的更改，是否保存？")
            if response is True:  # 用户选择“是”
                self.save_file()
            elif response is None:  # 用户选择“取消”
                return  # 不退出程序
        self.master.quit()  # 退出程序

    def on_closing(self):
        if self.is_modified:  # 如果文本被修改且未保存，提示保存
            response = askyesnocancel("保存", "您有未保存的更改，是否保存？")
            if response is True:  # 用户选择“是”
                self.save_file()
            elif response is None:  # 用户选择“取消”
                return  # 不退出程序
        self.master.destroy()  # 关闭窗口

    def increase_font(self):
        current_size = self.text_font.cget("size")
        self.text_font.configure(size=current_size + 1)

    def decrease_font(self):
        current_size = self.text_font.cget("size")
        if current_size > 1:  # 防止字体大小小于1
            self.text_font.configure(size=current_size - 1)

    def copy_text(self, event=None):
        self.text.event_generate("<<Copy>>")  # 调用系统复制功能

    def paste_text(self, event=None):
        self.text.event_generate("<<Paste>>")  # 调用系统粘贴功能

    def change_text_color(self):
        color = askcolor(title="选择字体颜色")
        if color[1]:  # 如果用户选择了颜色
            self.text.config(fg=color[1])  # 设置文本颜色

    def change_background_color(self):
        color =askcolor(title="选择背景颜色")
        if color[1]:  # 如果用户选择了颜色
            self.text.config(bg=color[1])  # 设置背景颜色


def main():
    root = tk.Tk()
    root.title("文本编辑器")
    root.geometry("500x800+200+20")
    app=App(master=root)
    app.pack(expand=True, fill="both")

    app.mainloop()


if __name__ == '__main__':
    main()