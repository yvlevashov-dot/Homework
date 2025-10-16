import pandas as pd
from tkinter import *
from tkinter import ttk
from random import randint
from tkinter import messagebox

def Find_film(*args):
        gen=genre.get()
        if gen not in genres_set:
            messagebox.showinfo("Error", "Фильмов такого жанра нет в списке")
        else:
            cond=[]
            for i in range(250):
                if gen in films.iloc[i]["Genre"].split(" | "):
                    cond.append(films.iloc[i]["Title"])
            k = randint(0, len(cond)-1)
            f=cond[k]
            film.set(f)
films = pd.read_csv('imdb_top_250.csv')
film_genres_list = list(films['Genre'])
# попробуйте посмотреть промежуточный результат в film_list
# print(film_list)

complex_genres = []  # будем хранить составные жанры, чтобы потом их удалить
for film_genre in film_genres_list:
    genres = film_genre.split(' | ')  # разберем каждый составной жанр на составляющие
    if len(genres) > 1:  # если попался составной жанр
        for genre in genres:  # то пройдемся по всем элементарным жанрам фильма
            film_genres_list.append(genre)  # и добавим их
        complex_genres.append(film_genre)
    # обратите внимание, что мы не можем в процессе итерации через for удалять элементы, поскольку это собьет итератор. Можете посмотреть, к чему это приведет, написав вместо complex_genres.append(film_genre) сразу film_genres_list.remove(film_genre)

for genre in complex_genres:
    film_genres_list.remove(genre)  # удалим все составные жанры из списка жанров

genres_set = set(film_genres_list) # чтобы сделать из этого set! теперь здесь лежат все уникальные элементарные жанры

root = Tk()
root.title("Поиск фильма")
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

genre=StringVar()
ttk.Label(mainframe, text="жанр").grid(column=1, row=1, sticky=W)
genre_entry = ttk.Entry(mainframe, width=7, textvariable=genre) ## поле ввода Feet 1 -аргу - виджет родитель
genre_entry.grid(column=2, row=1, sticky=(W, S, E))
ttk.Label(mainframe, text="Фильм").grid(column=1, row=2, sticky=W)

ttk.Button(mainframe, text="Найти", command=Find_film).grid(column=1, row=3, sticky=W)

film=StringVar()
ttk.Label(mainframe, textvariable=film).grid(column=2, row=2, sticky=(W, E))

root.geometry("300x100")
root.mainloop()