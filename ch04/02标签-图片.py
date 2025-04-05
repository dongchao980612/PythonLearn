import tkinter
import tkinter as  tk
from PIL import Image, ImageTk


win = tk.Tk()
win.title("第一个窗体")
win.geometry("300x400+100+100")


text_label = tk.Label(win,text="你好,世界",font="楷体")


bg_image= None
image_label = tk.Label(win,image=bg_image)

text_label.pack()
image_label.pack()

win.mainloop()




# bg_image = ImageTk.PhotoImage(file = "pic.png")