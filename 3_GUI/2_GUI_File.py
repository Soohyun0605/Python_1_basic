# (Graphic User Interface)//cf) LUI (Line User Interface)
from tkinter import *
import os
from tkinter import filedialog
from pathlib import Path

window = Tk()
window.title('Soohyun GUI')
window.geometry('640x480')
window.resizable(True, True)

change_txt=''
filename=""
def open_file():
    global filename
    filename=filedialog.askopenfilename(title='select open file',
                                        filetypes=(("text file", "*.txt"),("all files","*.*")),
                                        initialdir='C:\\Users\\visioncoding1\\Desktop\\Soohyun Song\\3_GUI\\2_GUI_File.py')
    if os.path.isfile(filename):
        file =open(filename,"r")
        txt.delete("1.0",END)
        txt.insert(END, file.read())    

def browse_dest_path():
    filesave=filedialog.asksaveasfilename(title="Save",
                                          defaultextension=".txt",
                                          filetypes=(("text file", "*.txt"),("all files","*.*")),
                                        initialdir='C:\\Users\\visioncoding1\\Desktop\\Soohyun Song\\3_GUI\\2_GUI_File.py')
    if filesave=="":
        return
    return filesave


def save_file():
    global filename
    global change_txt
    file_pass=browse_dest_path()
    with open(file_path,"w")as file:
        file.write(change_txt)


menu=Menu(window)
menu_file=Menu(menu, tearoff=0)


menu_file.add_command(label="Open",command=open_file)
menu_file.add_command(label="Save",command=save_file)
menu_file.add_separator()
menu_file.add_command(label="Exit",command=window.quit)
menu.add_cascade(label="File", menu=menu_file)


frame_btn=Frame(window, relief="solid",bd=1)
frame_btn.pack(fill="x")

def change():
    global change_txt
    change_txt=txt.get('1.0',END)
    label. config(text=change_txt)
    txt.delete('1.0',END)

def delete():
    txt.delete('1.0',END)
    label.config(text="")
# Button Section
btn1 = Button(frame_btn, text="change", command=change)
btn1.pack(side='left')

def save():
    global change_txt
    txt_file =open('save.txt','w',newline='')
    txt_file.write(change_txt)
    txt_file.close()
    

btn_save = Button(frame_btn, text="save", command=save)
btn_save.pack()

btn2 = Button(frame_btn, fg='red', bg='yellow',  text="delete", command=delete)
btn2.pack(side='right')

#btn1 = Button(window, padx=5, pady=10, text="Hello")
#btn1.pack(side='right')

#frame section
frame_txt=Frame(window, relief="solid",bd=1)
frame_txt.pack(fill="both")

scr= Scrollbar(frame_txt)
scr.pack(side='right', fill='y')

#text section
txt=Text(frame_txt,yscrollcommand=scr.set)
txt.pack(fill='both')
scr.config(command=txt.yview)


# label section
label=Label(window, text='hello')
label.pack()


window.config(menu=menu)
window.mainloop()

