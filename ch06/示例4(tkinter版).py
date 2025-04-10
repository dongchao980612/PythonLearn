import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

class CopyDirectoryApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # 创建三个 Frame
        self.frm1 = tk.Frame(self)
        self.frm1.pack(fill=tk.X, padx=10, pady=5)
        self.frm2 = tk.Frame(self)
        self.frm2.pack(fill=tk.X, padx=10, pady=5)
        self.frm3 = tk.Frame(self)
        self.frm3.pack(fill=tk.X, padx=10, pady=5)

        # 源路径输入框和按钮
        self.old_path_label = tk.Label(self.frm1, text="源路径:")
        self.old_path_label.pack(side=tk.LEFT, padx=5)
        self.old_path_entry = tk.Entry(self.frm1, width=40)
        self.old_path_entry.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        self.old_path_button = tk.Button(self.frm1, text="选择路径", command=self.handler_old_path_choice)
        self.old_path_button.pack(side=tk.RIGHT, padx=5)

        # 目标路径输入框和按钮
        self.new_path_label = tk.Label(self.frm2, text="目标路径:")
        self.new_path_label.pack(side=tk.LEFT, padx=5)
        self.new_path_entry = tk.Entry(self.frm2, width=40)
        self.new_path_entry.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        self.new_path_button = tk.Button(self.frm2, text="选择路径", command=self.handler_new_path_choice)
        self.new_path_button.pack(side=tk.RIGHT, padx=5)

        # 复制按钮
        self.copy_button = tk.Button(self.frm3, text="复制", command=self.handlerCopy)
        self.copy_button.pack(side=tk.RIGHT, padx=5)

    def handler_old_path_choice(self):
        # 打开文件夹选择对话框，选择源文件夹
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.old_path_entry.delete(0, tk.END)
            self.old_path_entry.insert(0, folder_path)

    def handler_new_path_choice(self):
        # 打开文件夹选择对话框，选择目标文件夹
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.new_path_entry.delete(0, tk.END)
            self.new_path_entry.insert(0, folder_path)

    def handlerCopy(self):
        # 获取输入框中的路径
        old_path = self.old_path_entry.get().strip()
        new_path = self.new_path_entry.get().strip()

        isExits = os.path.exists(new_path)
        if isExits:
            shutil.rmtree(new_path)

        isExits = os.path.exists(old_path)
        if isExits:
            shutil.copytree(old_path, new_path)
            print("文件夹 " + old_path + " 复制到 " + new_path + " 成功")
        else:
            print(old_path + "目录不存在")

# 创建主窗口并运行应用
if __name__ == "__main__":
    root = tk.Tk()
    root.title("文件夹复制工具")
    root.geometry("500x200")
    app = CopyDirectoryApp(master=root)
    app.mainloop()