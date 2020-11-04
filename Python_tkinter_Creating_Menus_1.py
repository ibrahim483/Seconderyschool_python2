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
subMenu.add_command(label="Exit", command=do_nothing)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=do_nothing)


root.mainloop()
