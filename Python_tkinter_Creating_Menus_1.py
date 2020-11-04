from tkinter import *


def do_nothing():
    print("ok ok I won't...")


root = Tk()

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(Label="File", menu=subMenu)
subMenu.add_command(Label="New Project...", command=do_nothing)
subMenu.add_command(Label="New...", command=do_nothing)
subMenu.add_separator()
subMenu.add_command(Label="Exit", command=do_nothing)

editMenu = Menu(menu)
menu.add_cascade(Label="Edit", menu=editMenu)
editMenu.add_command(Label="Redo", command=do_nothing)


root.mainloop()
