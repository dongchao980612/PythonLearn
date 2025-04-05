import tkinter
import tkinter as  tk
from PIL import Image, ImageTk


win = tk.Tk()
win.title("第一个窗体")
win.geometry("300x400+500+500")


text_label = tk.Label(win,text="你好,世界",font="楷体")
text_label.pack()


bg_image = ImageTk.PhotoImage(file = "pic.png")
image_label = tk.Label(win,image=bg_image)
image_label.pack()


win.mainloop()

