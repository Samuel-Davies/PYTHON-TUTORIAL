from tkinter import N


def TopTen():
    n = 1
    while n <= 10:
        sq = n * n
        yield sq
        n += 1


values = TopTen()



for i in values: 
    print(i)
