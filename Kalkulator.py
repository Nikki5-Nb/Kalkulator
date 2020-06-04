from math import sqrt
from tkinter import *

root = Tk()
root.title("Kalkulator")

e = Entry(root, width=60, borderwidth=10)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


# przyciski (liczby)
def button_go(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


# dodawanie // addition
def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "add"
    f_num = int(first_number)
    e.delete(0, END)


# odejmowanie // substraction
def button_sub():
    first_number = e.get()
    global f_num
    global math
    math = "sub"
    f_num = int(first_number)
    e.delete(0, END)


# mnozenie // multiplication
def button_mult():
    first_number = e.get()
    global f_num
    global math
    math = "mult"
    f_num = int(first_number)
    e.delete(0, END)


# dzielenie // division
def button_div():
    first_number = e.get()
    global f_num
    global math
    math = "div"
    f_num = int(first_number)
    e.delete(0, END)


# potegowanie // the power of
def button_pow():
    first_number = e.get()
    global f_num
    global math
    math = "pow"
    f_num = int(first_number)
    e.insert(0, pow(f_num, 2))
    e.delete(0, END)


# pierwiastkowanie // square root
def button_squ():
    first_number = e.get()
    global f_num
    global math
    math = "squ"
    f_num = int(first_number)
    e.insert(0, sqrt(f_num))
    e.delete(0, END)


# wynik  // equal
def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "add":
        e.insert(0, f_num + int(second_number))
    if math == "sub":
        e.insert(0, f_num - int(second_number))
    if math == "mult":
        e.insert(0, f_num * int(second_number))
    if math == "div":
        try:
            e.insert(0, f_num / int(second_number))
        except SyntaxError:
            e.delete(0, END)
            e.insert(0, str("Syntax Error"))
        except ZeroDivisionError:
            e.delete(0, END)
            e.insert(0, str("Nie można dzielić przez zero!"))

    if math == "pow":
        e.insert(0, pow(f_num, 2))
    if math == "squ":
        e.insert(0, sqrt(f_num))
    if math == str:
        print("Podaj poprawną licznę!")


# usuwanie // clear
def button_clear():
    e.delete(0, END)


button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_go(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_go(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_go(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_go(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_go(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_go(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_go(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_go(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_go(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_go(0))

button_add = Button(root, text="+", padx=37, pady=20, command=button_add)
button_sub = Button(root, text="-", padx=39, pady=20, command=button_sub)
button_mult = Button(root, text="*", padx=39, pady=20, command=button_mult)
button_div = Button(root, text="/", padx=39, pady=20, command=button_div)
button_pow = Button(root, text="x²", padx=38, pady=20, command=button_pow)
button_squ = Button(root, text="√x", padx=36, pady=20, command=button_squ)
button_equal = Button(root, text="=", padx=88, pady=20, command=button_equal)
button_clear = Button(root, text="C", padx=90, pady=20, command=button_clear)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)

button_add.grid(row=1, column=3)
button_sub.grid(row=2, column=3)
button_mult.grid(row=3, column=3)
button_div.grid(row=4, column=3)
button_pow.grid(row=4, column=1)
button_squ.grid(row=4, column=2)

button_equal.grid(row=5, column=2, columnspan=2)
button_clear.grid(row=5, column=0, columnspan=2)

root.mainloop()
