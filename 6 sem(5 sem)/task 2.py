from tkinter import *
from tkinter import ttk
def calculate(*args):
    try:
        mass_int=int(mass.get())
        height_int=int(height.get())
        imt= round((mass_int)/(height_int**2)*(100**2),2)
        imt_r.set(imt)
        if imt<=16:
            advise.set("Выраженный дефицит массы тела")
        if 16<imt<=18.5:
            advise.set("Недостаточная (дефицит) масса тела")
        if 18.5<imt<=25:
            advise.set("Норма")
        if 25<imt<=30:
            advise.set("Избыточная масса тела (предожирение)")
        if 30<imt<=35:
            advise.set("Ожирение 1 степени")
        if 35<imt<=40:
            advise.set("Ожирение 2 степени")
        if 40<imt:
            advise.set("Ожирение 3 степени")


    except ValueError:
        pass
    except ZeroDivisionError:
        pass

root = Tk()
root.title("ИМТ")
root.geometry("300x300")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=1)
mainframe.columnconfigure(3, weight=1)
mainframe.columnconfigure(4, weight=1)
mainframe.rowconfigure(1, weight=1)
mainframe.rowconfigure(2, weight=1)
mainframe.rowconfigure(3, weight=1)
mainframe.rowconfigure(4, weight=1)


mass = StringVar()
mass_entry = ttk.Entry(mainframe, width=7, textvariable=mass)
mass_entry.grid(column=2, row=1, sticky=(W, E))
label_mass = ttk.Label(mainframe, text="Масса тела:").grid(column=1, row=1, sticky=(W, E))

height = StringVar()
height_entry = ttk.Entry(mainframe, width=7, textvariable=height)
height_entry.grid(column=2, row=2, sticky=(W, E))
label_height = ttk.Label(mainframe, text="Ваш рост:").grid(column=1, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Подсчет ИМТ", command=calculate).grid(column=1, row=5, sticky=W)
label_res = ttk.Label(mainframe, text="Результат").grid(column=1, row=3, sticky=(W, E))

imt_r = StringVar()
ttk.Label(mainframe, textvariable=imt_r).grid(column=2, row=3, sticky=(W, E))
advise = StringVar()
ttk.Label(mainframe, textvariable=advise).grid(column=1, row=4, sticky=(W, E))



for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5) #создание отступов для виджетов

root.mainloop()