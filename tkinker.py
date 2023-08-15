from tkinter import *

from PIL import ImageTk,Image

var = Tk()

var.title('Discord')

var.iconbitmap("discord.ico")

var.geometry('1920x1080')

var.configure(background='#36393e')

img = Image.open('dsbg.png')

resized_img = img.resize((1920, 1080))

img_tk = ImageTk.PhotoImage(resized_img)

img_label = Label(var, image=img_tk)

img_label.place(x=-2, y=-2)

img_2 = Image.open('dark.png')

resized_img_2 = img_2.resize((800, 400))

img_tk_2 = ImageTk.PhotoImage(resized_img_2)

img_label_2 = Label(var, image=img_tk_2)

img_label_2.place(x=400, y=210)

text_label = Label(var, text='Welcome back!', fg='white', bg='#36393e')

text_label.place(relx=0.5, rely=0.5, anchor=CENTER)

text_label.config(font=('Uni Sans', 20))

var.mainloop()