from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Image Viewer')
root.iconbitmap('py\image.ico')
root.geometry("1920x1080")

frm = LabelFrame(root, text='Vedansh', font=('Century Gothic',50,'bold'), padx=10, pady=10)
frm.pack(padx=10,pady=10)


my_img1 = ImageTk.PhotoImage(Image.open('py//images/image1.jpg'))
my_img2 = ImageTk.PhotoImage(Image.open('py/images/image2.jpg'))
my_img3 = ImageTk.PhotoImage(Image.open('py/images/image3.jpg'))
my_img4 = ImageTk.PhotoImage(Image.open('py/images/image4.jpg'))
my_img5 = ImageTk.PhotoImage(Image.open('py/images/image5.jpg'))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

status = Label(frm, text='Image 1 of ' + str(len(image_list)),font=('Consolas',10,'bold'), bd=1, relief=SUNKEN, anchor=E)

my_label = Label(frm, image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_num):
    global my_label
    global button_back
    global button_forward

    my_label.grid_forget()
    my_label = Label(frm, image=image_list[image_num-1])

    button_forward = Button(frm, text='>>', font=('Consolas',10,'bold'), command=lambda: forward(image_num+1))
    button_back = Button(frm, text='<<',font=('Consolas',10,'bold'), command=lambda: back(image_num-1))

    if image_num==5:
        button_forward = Button(frm, text='>>', state=DISABLED)

    my_label.grid(row=0,column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)

    status = Label(frm, text='Image ' + str(image_num) + ' of ' + str(len(image_list)),font=('Consolas',10,'bold'), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

def back(image_num):
    global my_label
    global button_back
    global button_forward

    my_label.grid_forget()
    my_label = Label(frm, image=image_list[image_num-1])

    button_forward = Button(frm, text='>>',font=('Consolas',10,'bold'), command=lambda: forward(image_num+1))
    button_back = Button(frm, text='<<',font=('Consolas',10,'bold'), command=lambda: back(image_num-1))

    if image_num == 1:
        button_back = Button(frm, text='<<',font=('Consolas',10,'bold'), state=DISABLED)

    my_label.grid(row=0,column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)

    status = Label(frm, text='Image '+ str(image_num) +' of ' + str(len(image_list)),font=('Consolas',10,'bold'), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


button_back = Button(frm, text='<<',font=('Consolas',10,'bold'), state=DISABLED).grid(row=1, column=0)
button_forward = Button(frm, text='>>',font=('Consolas',10,'bold'), command=lambda: forward(2)).grid(row=1, column=2)
button_quit = Button(frm, text="Exit Image Viewer",font=('Consolas',10,'bold'), command=root.quit)
button_quit.grid(row=1,column=1, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)
root.mainloop()
