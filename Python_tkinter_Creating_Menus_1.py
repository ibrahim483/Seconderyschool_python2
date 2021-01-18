from tkinter import *


def do_nothing():
    print("ok ok I won't...")


root = Tk()

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New Project...", command=do_nothing)
subMenu.add_command(label="New...", command=do_nothing)
subMenu.add_separator()


def do_something():
    print("what do you want to redo!!")


editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=do_something)


def exit1():
    print(" Think you for using our porogram")
subMenu.add_command(label="Exit", fg="red", command=exit)





root.mainloop()
