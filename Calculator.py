from tkinter import *
root = Tk()

def enternumber(x):
    if  entry1.get() == '0':
        if x != '.':
            entry1.delete(0,'end')
            entry1.insert(0,x)
        else:
            length = len(entry1.get())
            entry1.insert(length, x)
    else:
        length = len(entry1.get())
        entry1.insert(length,x)

def enter_operator(x):
    if entry1.get() != '0':
        length = len(entry1.get())
        entry1.insert(length, operators[x]['text'])

def clear():
    entry1.delete(0,END)
    entry1.insert(0,'0')

history = []
def equal():
    content = entry1.get()
    result = eval(content)
    entry1.delete(0,'end')
    entry1.insert(0,result)
    history.append(content)
    history.reverse()
    status.configure(text = "History: "+'|'.join(history[:4]), font  = 'verdana 10 bold')


def delete():
    length = len(entry1.get())
    entry1.delete(length-1,'end')
    if length == 1:
        entry1.insert(0,'0')


entry1 = Entry(root, font = 'verdana 18 bold' ,width = 19 , border  = 6,justify = RIGHT)
entry1.insert(0,'0')
entry1.place(x=38,y=20)

buttons = []
for i in range(10):
    buttons.append(Button(root,width = 7,text = str(i), border = 6, command = lambda x = i: enternumber(x) ))

button_text = 1
for i in range (3):
    for j in range(3):
        buttons[button_text].place(x =38+j*90, y = 70 + i*70)
        button_text+=1

button_zero = Button(width = 7, text= '0',border = 6, command = lambda x = 0: enternumber(x))
button_zero.place(x = 38 ,y= 280)

button_dot = Button(width = 7, text= '.',border = 6, command = lambda x = '.': enternumber(x))
button_dot.place(x = 230 ,y= 280)

button_equal = Button(width = 7, text= '=',border = 6, command = equal)
button_equal.place(x = 38 ,y= 350)

button_clear = Button(width = 7 , text = 'C', border = 6 , command = clear)
button_clear.place(x = 140 , y = 280)

button_del = Button(width = 7 , text = 'Del', border = 6 , command = delete)
button_del.place(x = 140 , y = 350)

status = Label(root, text = 'History', relief = SUNKEN , height = 2 , anchor = W , font = 'verdana 10 bold')
status.pack(side = BOTTOM,fill = X)

operators = []
for i in range (4):
    operators.append(Button(root,width = 7, border = 6,command =lambda x = i : enter_operator(x)))

operators[0]['text'] = '+'
operators[1]['text'] = '-'
operators[2]['text'] = '*'
operators[3]['text'] = '/'

for i in range(4):
    operators[i].place(x = 320, y = 70+i*70)

root.title('Calculator')
root.geometry('400x450')
root.resizable(False,False)
root.mainloop()