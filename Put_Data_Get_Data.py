from tkinter import *

def get_data(event=None):
    print("String value ",strVar.get())
    print("Integer value ", intVar.get())
    print("Double value ", dblVar.get())
    print("Boolean value ", boolVar.get())

def bool_button(event=None):
    if boolVar.get():
        button.unbind('<Button-1>')
    else:
        button.bind('<Button-1>',get_data)

root = Tk()

strVar = StringVar()
intVar = IntVar()
dblVar = DoubleVar()
boolVar = BooleanVar()

strVar.set("Enter string")
intVar.set("Enter integer")
dblVar.set("Enter double")
boolVar.set(True)

strEntry=Entry(root,textvariable=strVar)
strEntry.pack(side=LEFT)
intEntry=Entry(root,textvariable=intVar)
intEntry.pack(side=LEFT)
dblEntry=Entry(root,textvariable=dblVar)
dblEntry.pack(side=LEFT)

checker = Checkbutton(root,text='Switch',variable=boolVar)
checker.bind('<Button-1>',bool_button)
checker.pack(side=LEFT)

button = Button(root,text='Get Data')
button.bind('<Button-1>',get_data)
button.pack(side=LEFT)

root.mainloop()