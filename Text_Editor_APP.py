from tkinter import *
from tkinter import filedialog

class text_editor:
    current_open_file = 'No Text'
    def openfile(self):
        open_return = filedialog.askopenfile(initialdir ='/', title = 'Select file to open')
        if(open_return != None):
            self.text_area.delete(1.0,END)
            for line in open_return:
                self.text_area.insert(END,line)
            self.current_open_file = open_return.name
            open_return.close()

    def saveas_file(self):
        save_as_file = filedialog.asksaveasfile(mode = 'w', defaultextension = '.txt')
        if save_as_file is None:
            return
        text2save = self.text_area.get(1.0,END)
        self.current_open_file = save_as_file.name
        save_as_file.write(text2save)
        save_as_file.close()

    def save_file(self):
        if self.current_open_file == 'No Text':
            self.saveas_file()
        else:
            f = open(self.current_open_file,'w')
            f.write(self.text_area.get(1.0,END))
            f.close()
    def new_file(self):
        self.text_area.delete(1.0,END)
        self.current_open_file == 'No Text'

    def copy (self):
        self.text_area.clipboard_clear()
        self.text_area.clipboard_append(self.text_area.selection_get())

    def cut(self):
        self.copy()
        self.text_area.delete('sel.first','sel.last')

    def paste(self):
        self.text_area.insert(INSERT, self.text_area.clipboard_get())



    def __init__(self,master):
        self.master = master
        master.title("Text Editor")
        self.text_area = Text(self.master, undo = True)
        self.text_area.pack(fill = BOTH , expand = 1)
        self.Main_menu = Menu()
        self.master.config(menu = self.Main_menu)

        self.filemenu = Menu(self.Main_menu, tearoff = False)
        self.Main_menu.add_cascade(label = 'File', menu = self.filemenu)

        self.filemenu.add_command(label = 'New File ', command=self.new_file)
        self.filemenu.add_command(label = 'Open', command = self.openfile)
        self.filemenu.add_separator()
        self.filemenu.add_command(label = 'Save As', command = self.saveas_file)
        self.filemenu.add_command(label = 'Save', command=self.save_file)
        self.filemenu.add_separator()
        self.filemenu.add_command(label = 'Exit ', command = master.quit)

        self.editmenu = Menu(self.Main_menu, tearoff = False)
        self.Main_menu.add_cascade(label = 'Edit', menu=self.editmenu)
        self.editmenu.add_command(label = 'Copy', command=self.copy)
        self.editmenu.add_command(label = 'Cut ', command=self.cut)
        self.editmenu.add_command(label = 'Paste ', command=self.paste)
        self.editmenu.add_separator()
        self.editmenu.add_command(label = 'Redo ', command=self.text_area.edit_redo)
        self.editmenu.add_command(label = 'Undo ', command=self.text_area.edit_undo)


root = Tk()
text = text_editor(root)
root.mainloop()
