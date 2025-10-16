from tkinter import *
from tkinter import ttk



def calculate(*args):
    try:
        value = feet.get()  # используем геттер для объекта StringVal
        meters.set(float(eval(value)))  # используем сеттер для объекта StringVal

    except ValueError:
        pass
    except ZeroDivisionError:
        pass


root = Tk()
root.title("calculator")


mainframe = ttk.Frame(root, padding="3 3 12 12") #виджет для содержания других виджетов
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=1)
mainframe.columnconfigure(3, weight=1)
mainframe.rowconfigure(1, weight=1)
mainframe.rowconfigure(2, weight=1)
mainframe.rowconfigure(3, weight=1)

feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet) ## поле ввода Feet 1 -аргу - виджет родитель
feet_entry.grid(column=2, row=1, sticky=(W, S, E))


meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))


ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=1, row=3, sticky=W)

ttk.Label(mainframe, text="выражение").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="результат равен").grid(column=1, row=2, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5) #создание отступов для виджетов

feet_entry.focus() ## курсор сразу в поле ввода

root.bind("<Return>", calculate)
root.geometry("300x100")
root.resizable(False, False)
root.mainloop()