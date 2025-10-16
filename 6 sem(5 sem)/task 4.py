from tkinter import *
from tkinter import ttk



def calculate(*args):
    c = color.get()
    if 255 - int(c[1:3], 16) == 0:
        c1_r = str(hex(255 - int(c[1:3], 16)))[2:] + str(hex(255 - int(c[1:3], 16)))[2:]
    else:
        c1_r = str(hex(255 - int(c[1:3], 16)))[2:]
    if 255 - int(c[3:5], 16) == 0:
        c2_r = str(hex(255 - int(c[3:5], 16)))[2:] + str(hex(255 - int(c[3:5], 16)))[2:]
    else:
        c2_r = str(hex(255 - int(c[3:5], 16)))[2:]
    if 255 - int(c[5:7], 16) == 0:
        c3_r = str(hex(255 - int(c[5:7], 16)))[2:] + str(hex(255 - int(c[5:7], 16)))[2:]
    else:
        c3_r = str(hex(255 - int(c[5:7], 16)))[2:]
    c_r="#"+c1_r+c2_r+c3_r
    comp_color.set(c_r)


root = Tk()
root.title("Калькулятор комплементарного цвета")


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

color = StringVar()
color_entry = ttk.Entry(mainframe, width=7, textvariable=color) ## поле ввода Feet 1 -аргу - виджет родитель
color_entry.grid(column=2, row=1, sticky=(W, S, E))


comp_color = StringVar()
ttk.Label(mainframe, textvariable=comp_color).grid(column=2, row=2, sticky=(W, E))


ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=1, row=3, sticky=W)

ttk.Label(mainframe, text="выражение").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="результат равен").grid(column=1, row=2, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5) #создание отступов для виджетов

root.geometry("300x100")
root.resizable(False, False)



root.mainloop()