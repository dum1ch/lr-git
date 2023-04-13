#======================#
#  Tkinter Calculator  #
#======================#

# Импорт пакетов
from tkinter import *
import math
import numpy as np

'''
Functions
'''
# Функция для добавления в ввод текстового отображения
def button_click(char):
    global calc_operator
    calc_operator += str(char)
    text_input.set(calc_operator)

# Функция для очистки всей записи от отображения текста
def button_clear_all():
    global calc_operator
    calc_operator = ""
    text_input.set("")

# Функция для удаления одного за другим из последнего в записи текстового отображения
def button_delete():
    global calc_operator
    text = calc_operator[:-1]
    calc_operator = text
    text_input.set(text)

# Функция для вычисления факториала числа
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

def fact_func():
    global calc_operator
    result = str(factorial(int(calc_operator)))
    calc_operator = result
    text_input.set(result)

# Функция для вычисления тригонометрических чисел угла
def trig_sin():
    global calc_operator
    result = str(math.sin(math.radians(int(calc_operator))))
    calc_operator = result
    text_input.set(result)

def trig_cos():
    global calc_operator
    result = str(math.cos(math.radians(int(calc_operator))))
    calc_operator = result
    text_input.set(result)

def trig_tan():
    global calc_operator
    result = str(math.tan(math.radians(int(calc_operator))))
    calc_operator = result
    text_input.set(result)

def trig_cot():
    global calc_operator
    result = str(1/math.tan(math.radians(int(calc_operator))))
    calc_operator = result
    text_input.set(result)

# Функция для нахождения квадратного корня из числа
def square_root():
    global calc_operator
    if int(calc_operator)>=0:
        temp = str(eval(calc_operator+'**(1/2)'))
        calc_operator = temp
    else:
        temp = "ERROR"
    text_input.set(temp)

# Функция для нахождения третьего корня числа
def third_root():
    global calc_operator
    if int(calc_operator)>=0:
        temp = str(eval(calc_operator+'**(1/3)'))
        calc_operator = temp
    else:
        temp = "ERROR"
    text_input.set(temp)

# Функция для изменения знака числа
def sign_change():
    global calc_operator
    if calc_operator[0]=='-':
        temp = calc_operator[1:]
    else:
        temp = '-'+calc_operator
    calc_operator = temp
    text_input.set(temp)

# Функция для вычисления процента от числа
def percent():
    global calc_operator
    temp = str(eval(calc_operator+'/100'))
    calc_operator = temp
    text_input.set(temp)

# Функция для нахождения результата операции
def button_equal():
    global calc_operator
    temp_op = str(eval(calc_operator))
    text_input.set(temp_op)
    calc_operator = temp_op   

'''
Variables
'''
sin, cos, tan = math.sin, math.cos, math.tan
log, ln = math.log10, math.log
e = math.exp
p = math.pi
E = '*10**'
# Здесь мы определяем некоторые математические функции (синус, косинус, тангенс, логарифм, 
# экспонента и число пи) из модуля math, чтобы использовать их в дальнейшем коде. Также 
# определяются значения "E" и "p", которые будут использоваться в калькуляторе.

tk_calc = Tk()
# Здесь мы создаем объект главного окна нашей программы, используя класс "Tk" из библиотеки tkinter.

tk_calc.configure(bg="#293C4A", bd=10)
tk_calc.title("Scientific Calculator")
# Здесь мы настраиваем окно калькулятора, задавая его цвет фона (bg), размер рамки (bd) и заголовок окна (title).

calc_operator = ""
text_input = StringVar()

text_display = Entry(tk_calc, font=('sans-serif', 20, 'bold'), textvariable=text_input,
                     bd=5, insertwidth=5, bg='#BBB', justify='right').grid(columnspan=5, padx=10, pady=15)
# Здесь мы создаем виджет Entry (поле для ввода текста) с помощью класса Entry из tkinter 
# и привязываем его к нашему главному окну. Также мы определяем различные параметры виджета,
# такие как шрифт, цвет фона, размер рамки и положение относительно других элементов в окне.

button_params = {'bd': 5, 'fg': '#BBB',
                 'bg': '#3C3636', 'font': ('sans-serif', 20, 'bold')}
button_params_main = {'bd': 5, 'fg': '#000',
                      'bg': '#BBB', 'font': ('sans-serif', 20, 'bold')}
# Здесь мы создаем словари параметров для кнопок на калькуляторе. Каждый словарь содержит 
# значения для параметров кнопок, таких как цвет фона, шрифт, размер рамки и т.д.

'''
Buttons
'''

# --1 - й ряд--
# Абсолютное значение числа
abs_value = Button(tk_calc, button_params, text='abs',
                   command=lambda: button_click('abs(')).grid(row=1, column=0, sticky="nsew")

# Здесь мы создаем кнопку для вычисления абсолютного значения числа с помощью класса 
# Button из библиотеки tkinter. Мы задаем параметры для кнопки, такие как текст, цвет 
# фона, шрифт и функцию, которая будет вызываться при нажатии. Мы также устанавливаем 
# позицию кнопки на первой строке (row=1) и первом столбце (column=0) нашего окна калькулятора.

# Остаток от деления
modulo = Button(tk_calc, button_params, text='mod',
                command=lambda: button_click('%')).grid(row=1, column=1, sticky="nsew")

# Здесь мы создаем кнопку для вычисления остатка от деления двух чисел. 
# Мы также устанавливаем позицию кнопки на первой строке (row=1) и втором столбце 
# (column=1) нашего окна калькулятора.

# Коэффициент целочисленного деления
int_div = Button(tk_calc, button_params, text='div',
                 command=lambda: button_click('//')).grid(row=1, column=2, sticky="nsew")

# Здесь мы создаем кнопку для вычисления целочисленного деления двух чисел. 
# Мы также устанавливаем позицию кнопки на первой строке (row=1) и третьем столбце 
# (column=2) нашего окна калькулятора.

# Факториал числа
factorial_button = Button(tk_calc, button_params, text='x!',
                          command=fact_func).grid(row=1, column=3, sticky="nsew")

# Здесь мы создаем кнопку для вычисления факториала числа. Мы также устанавливаем 
# позицию кнопки на первой строке (row=1) и четвертом столбце (column=3) нашего окна калькулятора.

# Число Эйлера e
eulers_num = Button(tk_calc, button_params, text='e',
                    command=lambda: button_click(str(math.exp(1)))).grid(row=1, column=4, sticky="nsew")

# Здесь мы создаем кнопку для вычисления числа e (euler's number). Мы также устанавливаем 
# позицию кнопки на первой строке (row=1) и пятом столбце (column=4)

# --2 - й ряд--
# Синус угла в градусах
sine = Button(tk_calc, button_params, text='sin',
              command=trig_sin).grid(row=2, column=0, sticky="nsew")
# Косинус угла в градусах
cosine = Button(tk_calc, button_params, text='cos',
                command=trig_cos).grid(row=2, column=1, sticky="nsew")
# Тангенс угла в градусах
tangent = Button(tk_calc, button_params, text='tan',
                 command=trig_tan).grid(row=2, column=2, sticky="nsew")
# Котангенс угла в градусах
cotangent = Button(tk_calc, button_params, text='cot',
                   command=trig_cot).grid(row=2, column=3, sticky="nsew")
# Pi(3,14...) число
pi_num = Button(tk_calc, button_params, text='π',
                command=lambda: button_click(str(math.pi))).grid(row=2, column=4, sticky="nsew")
