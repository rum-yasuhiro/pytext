from tkinter import *
from tkinter import filedialog

root=Tk("Text Editor")
text = Text(root)
text.grid()

def save_as():
    global text
    
    t = text.get("1.0", "end-1c")

    save_location = filedialog.asksaveasfilename()
    
    file1 = open(save_location, "w+")
    file1.write(t)
    file1.close()
    
button = Button(root, text="Save", command=save_as)
button.grid()

def FontHelvetica():
    global text
    text.config(font="Helvetica")
    
def FontCourier():
    global text
    text.config(font="Courier")
    
font =Menubutton(root, text="Font")
font.grid()

font.menu=Menu(font, tearoff=0)
font["menu"]=font.menu

helvetica=IntVar()
courier=IntVar()

font.menu.add_checkbutton(label="Courier", variable=courier, command=FontCourier)
font.menu.add_checkbutton(label="Helvetica", variable=helvetica, command=FontHelvetica)

root.mainloop()