from tkinter import *
from tkinter import ttk


def AddToDo():
    global lastAction, oldTask
    if taskName.get().strip() != "":
        label.insert(END, taskName.get())
        oldTask = taskName.get()
        taskName.delete(0, END)
        lastAction = "add"


def DeleteToDo():
    global lastAction, itemDeleted, deletedLocation
    delete = label.curselection()
    if delete != ():
        for i in label.curselection():
            deletedLocation = delete
            itemDeleted = label.get(i)
        label.delete(delete)
        lastAction = "delete"


def Undo():
    global lastAction, index
    if lastAction == "delete":
        label.insert(deletedLocation, itemDeleted)
        lastAction = None
    elif lastAction == "add":
        index = label.get(0, END).index(oldTask)
        label.delete(index)
        lastAction = None


window = Tk()
x = int(window.winfo_screenwidth() / 2 - 250)
y = int(window.winfo_screenheight() / 2 - 250)
window.title("ToDo")
window.geometry(f"500x500+{x}+{y}")
label = Listbox(window, height=9, width=11, font="calibri 40 bold")
label.place(x=200, y=20)
lastAction = None
itemDeleted = ""
oldTask = ""
deletedLocation = 0
index = 0
taskName = ttk.Entry(window, width=20)
add = Button(text="Add An Item", command=AddToDo)
delete = Button(text="Delete An Item", command=DeleteToDo)
undo = Button(text="Undo An Action", command=Undo)
taskName.place(relx=0.2, rely=0.39, anchor=CENTER)
add.place(relx=0.2, rely=0.45, anchor=CENTER)
delete.place(relx=0.2, rely=0.51, anchor=CENTER)
undo.place(relx=0.2, rely=0.57, anchor=CENTER)
mainloop()
