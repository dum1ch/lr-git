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