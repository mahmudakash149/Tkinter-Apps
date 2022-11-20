from tkinter import *
from tkinter import colorchooser
from tkinter import ttk
import tkinter as tk
from turtle import color

root = Tk()
root.title('Black Board')
root.geometry('1000x600+150+150')
root.configure(bg= 'white')
root.resizable(False, False)

current_x = 0
current_y = 0
color = 'white'

def locate_xy(work):

    global current_x ,current_y

    current_x = work.x
    current_y = work.y

def addLine(work):

    global current_x, current_y

    board.create_line((current_x,current_y,work.x,work.y), width =get_current_value() , fill = color,capstyle = ROUND , smooth = TRUE)
    current_x , current_y = work.x , work.y

def show_color(new_color):

    global color

    color = new_color

def new_canvas():
    board.delete('all')
    colours()
#icon
icon = PhotoImage(file="E:\\Programming\\Tkinter\\Black Board\\blackboard.png")
root.iconphoto(False,icon)

colour_box = PhotoImage(file="E:\\Programming\\Tkinter\\Black Board\\1x\\Asset 1.png")
Label(root, image = colour_box ).place(x=10,y = 5)

colors = Canvas(root, width = 90, height = 350, bg = '#57544d')
colors.place(x= 30, y = 40)

eraser = PhotoImage(file = "E:\\Programming\\Tkinter\\Black Board\\rsz_1erase.png")
Button1 = Button(root, image = eraser , command = new_canvas )
Button1.place(x= 30 , y = 400)

def colours():

    draw = colors.create_rectangle((10,10,40,40),fill = 'black')
    colors.tag_bind(draw, '<Button-1>',lambda x: show_color('black'))

    draw = colors.create_rectangle((10, 50, 40, 80), fill='#9e0000')
    colors.tag_bind(draw, '<Button-1>', lambda x: show_color('#9e0000'))

    draw = colors.create_rectangle((10, 90, 40, 120), fill='#02c27c')
    colors.tag_bind(draw, '<Button-1>', lambda x: show_color('#02c27c'))

    draw = colors.create_rectangle((10, 130, 40, 160), fill='#02a5c2')
    colors.tag_bind(draw, '<Button-1>', lambda x: show_color('#02a5c2'))

    draw = colors.create_rectangle((10, 170, 40, 200), fill='purple')
    colors.tag_bind(draw, '<Button-1>', lambda x: show_color('purple'))

    draw = colors.create_rectangle((50, 10, 80, 40), fill='white')
    colors.tag_bind(draw, '<Button-1>', lambda x: show_color('white'))

    draw = colors.create_rectangle((50, 50, 80, 80), fill='#c26f02')
    colors.tag_bind(draw, '<Button-1>', lambda x: show_color('#c26f02'))

    draw = colors.create_rectangle((50, 90, 80, 120), fill='#bfc202')
    colors.tag_bind(draw, '<Button-1>', lambda x: show_color('#bfc202'))

    draw = colors.create_rectangle((50, 130, 80, 160), fill='#c4021c')
    colors.tag_bind(draw, '<Button-1>', lambda x: show_color('#c4021c'))

colours()

board = Canvas(root, width = 845 , height = 570, cursor = "circle", bg = 'black')
board.place(x = 140 , y = 10)



board.bind('<Button-1>', locate_xy)
board.bind("<B1-Motion>",addLine)

#Sldier

current_value = tk.DoubleVar()

def get_current_value():

    return'{: .2f}'.format(current_value.get())

def slider_changed(event):

    value_label.configure(text = get_current_value())

slider = ttk.Scale(root, from_=0, to =100, orient = 'horizontal', command = slider_changed, variable = current_value)
slider.place(x=20,y=530)

value_label = ttk.Label(root, text = get_current_value())
value_label.place(x=24,y=550)

root.mainloop()