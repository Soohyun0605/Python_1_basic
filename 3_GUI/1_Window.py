# (Graphic User Interface)//cf) LUI (Line User Interface)
from tkinter import *

window = Tk()
window.title('Soohyun GUI')
window.geometry('640x480')
window.resizable(True, True)

frame_btn=Frame(window, relief="solid",bd=1)
frame_btn.pack(fill="x")

def change():
    change_txt=txt.get('1.0',END)
    label. config(text=change_txt)
    txt.delete('1.0',END)

def delete():
    txt.delete('1.0',END)
    label.config(text="")
# Button Section
btn1 = Button(frame_btn, text="change", command=change)
btn1.pack(side='left')

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

window.mainloop()

