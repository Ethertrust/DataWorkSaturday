from tkinter import ttk
from tkinter import *
from tkinter import Tk, Frame, Menu
import tkinter as tk
import sys

#https://sky.pro/wiki/python/ustanovka-i-ispolzovanie-tkinter-bez-instalyatsii-v-python/
######Function
# def test():
# sub.mainloop()

# ---------------------------------------
def test():
    sub.deiconify()  # показать окно


# ---------------------------------------

def qu1():
    a = ent_1.get()
    x = (float(a))
    y = str(x)
    if float(x) == 1:
        sublabel2["text"] = ("Ваш вес идеален")
    elif float(x) == 2:
        sublabel2["text"] = ("Вам нужно набрать" + y + " кг")
    elif float(x) == 3:
        sublabel2["text"] = ("Вам нужно сбросить" + y + " кг")


def quit():
    sys.exit()

    ###################


def theoryfile1():
    text_box.delete(1.0, END)
    for word in numbers:
        text_box.insert(END, word)


def theoryfile2():
    text_box.delete(1.0, END)
    for word in numbers2:
        text_box.insert(END, word)


def theoryfile3():
    text_box.delete(1.0, END)
    for word in numbers3:
        text_box.insert(END, word)


def practicfile1():
    text_box.delete(1.0, END)
    for word in numbers4:
        text_box.insert(END, word)


def practicfile2():
    text_box.delete(1.0, END)
    for word in numbers5:
        text_box.insert(END, word)


def practicfile3():
    text_box.delete(1.0, END)
    for word in numbers6:
        text_box.insert(END, word)


def practic():
    label.config(text="Практическая часть", font=("Arial Black", 14))
    label2.config(text="ПР 1 Составление линейных алгоритмов", font=("Arial", 12))
    label3.config(text="ПР 2 Составление разветвляющихся алгоритмов", font=("Arial", 12))
    label4.config(text="ПР 3 Составление цикла со схемой ПОКА", font=("Arial", 12))
    btn2.config(text=" + ", width=4, command=pluspractic)
    btn3.config(command=practicfile1)
    btn4.config(command=practicfile2)
    btn5.config(command=practicfile3)


def theory():
    label.config(text="Теоретическая часть", font=("Arial Black", 14))
    label2.config(text="1.1. Основные алгоритмические конструкции", font=("Arial", 12))
    label3.config(text="1.1.1. Понятие алгоритма и его свойства", font=("Arial", 12))
    label4.config(text="1.1.2. Основные алгоритмические конструкции", font=("Arial", 12))
    btn2.config(command=plusteory)
    btn3.config(command=theoryfile1)
    btn4.config(command=theoryfile2)
    btn5.config(command=theoryfile3)


def minus():
    label2.config(text="")
    label3.config(text="")
    label4.config(text="")
    btn2.config(text=" + ", width=4, state=NORMAL)
    btn3.config(state=DISABLED)
    btn4.config(state=DISABLED)
    btn5.config(state=DISABLED)


def plusteory():
    label2.config(text="1.1. Основные алгоритмические конструкции", font=("Arial", 12))
    label3.config(text="1.1.1. Понятие алгоритма и его свойства", font=("Arial", 12))
    label4.config(text="1.1.2. Основные алгоритмические конструкции", font=("Arial", 12))
    btn3.config(state=NORMAL)
    btn4.config(state=NORMAL)
    btn5.config(state=NORMAL)


def pluspractic():
    label2.config(text="ПР 1 Составление линейных алгоритмов", font=("Arial", 12))
    label3.config(text="ПР 2 Составление разветвляющихся алгоритмов", font=("Arial", 12))
    label4.config(text="ПР 3 Составление цикла со схемой ПОКА", font=("Arial", 12))
    btn3.config(state=NORMAL)
    btn4.config(state=NORMAL)
    btn5.config(state=NORMAL)


######Window


root = Tk()
root.title("Электронный учебник")
root.geometry("800x400")

with open("111.htm", 'r') as file:
    contents = file.readlines()
    numbers = list(contents)

with open("112.htm",'r') as file:
    contents = file.readlines()
    numbers2 = list(contents)

with open("113.htm", 'r') as file:
    contents = file.readlines()
    numbers3 = list(contents)

with open("1.htm ", 'r') as file:
    contents = file.readlines()
    numbers4 = list(contents)

with open("2.htm ", 'r') as file:
    contents = file.readlines()
    numbers5 = list(contents)

with open("3.htm ", 'r') as file:
    contents = file.readlines()
    numbers6 = list(contents)

main_menu = Menu()
main_menu.add_command(label="Теория", command=theory)
main_menu.add_command(label="Практика", command=practic)
main_menu.add_command(label="Начать тест", command=test)
main_menu.add_command(label="Выход", command=quit)

label = Label(text="Теоретическая часть", font=("Arial Black", 14))
label.place(x=1, y=1)

label2 = Label(text="1.1. Основные алгоритмические конструкции", font=("Arial", 12))
label2.place(x=1, y=40)

label3 = Label(text="1.1.1. Понятие алгоритма и его свойства", font=("Arial", 12))
label3.place(x=1, y=80)

label4 = Label(text="1.1.2. Основные алгоритмические конструкции", font=("Arial", 12))
label4.place(x=1, y=120)

btn = Button(text=" - ", width=4, command=minus)
btn.place(x=300, y=1)

btn2 = Button(text=" + ", width=4, command=plusteory, state=DISABLED)
btn2.place(x=250, y=1)

btn3 = Button(text="+", command=theoryfile1)
btn3.place(x=370, y=40)

btn4 = Button(text="+", command=theoryfile2)
btn4.place(x=370, y=80)

btn5 = Button(text="+", command=theoryfile3)
btn5.place(x=370, y=120)

text_box = tk.Text(height=22, width=45)

text_box.place(x=400, y=1)

root.config(menu=main_menu)

sub = tk.Toplevel(root)
sub.transient(root)
sub.title('Ебаный тест')
sub.geometry("300x400")

sublabel = Label(sub, text="Cколько будет 1+1", font=("Arial", 10))
sublabel.place(x=1, y=1)

sublabel2 = Label(sub, text="", font=("Arial", 10))
sublabel2.place(x=1, y=60)

ent_1 = Entry(sub, width=10)
ent_1.place(x=1, y=20)
subbtn = Button(sub, text=" Назад ", width=4, command=quit)
subbtn.place(x=250, y=200)

subbtn2 = Button(sub, text=" ОК ", width=4, command=qu1)
subbtn2.place(x=150, y=200)

subbtn3 = Button(sub, text=" Далее ", width=4, command=quit)
subbtn3.place(x=1, y=200)

# ---------------------------------------
sub.withdraw()  # скрыть окно


# заменить закрытие  окна на скрытие окна:
def hide_sub():
    sub.withdraw()


sub.protocol("WM_DELETE_WINDOW", hide_sub)  # переназначаем кнопку закрытия  окна на скрытие окна

# ---------------------------------------

root.mainloop()