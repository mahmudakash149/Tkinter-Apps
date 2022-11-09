from tkinter import *
import wikipedia
root = Tk()

def information():
    entry_value = entry1.get()
    textbox.delete(1.0,END)
    try:
        textbox_value = wikipedia.summary(entry_value)
        textbox.insert(INSERT, textbox_value)
    except:
        textbox.insert(INSERT,'Please check your input or internet connection')

topframe = Frame(root)

entry1 = Entry(topframe,width = 40)
entry1.pack()

button1 = Button(topframe,text = "Search", command = information)
button1.pack()

topframe.pack(side = TOP)

bottom_frame = Frame(root)

scroll = Scrollbar(bottom_frame)
scroll.pack(side=RIGHT, fill=Y)

textbox = Text(bottom_frame, width = 40 , height = 20,yscrollcommand = scroll.set, wrap = WORD)
scroll.config(command=textbox.yview)
textbox.pack()
bottom_frame.pack()


root.geometry("400x400+400+200")
root.mainloop()