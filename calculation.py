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

# --3 -й ряд--
# Мощность 2
second_power = Button(tk_calc, button_params, text='x\u00B2',
                      command=lambda: button_click('**2')).grid(row=3, column=0, sticky="nsew")
# Мощность 3
third_power = Button(tk_calc, button_params, text='x\u00B3',
                     command=lambda: button_click('**3')).grid(row=3, column=1, sticky="nsew")
# Мощность n
nth_power = Button(tk_calc, button_params, text='x^n',
                   command=lambda: button_click('**')).grid(row=3, column=2, sticky="nsew")
# Обратное число
inv_power = Button(tk_calc, button_params, text='x\u207b\xb9',
                   command=lambda: button_click('**(-1)')).grid(row=3, column=3, sticky="nsew")
# Степени 10
tens_powers = Button(tk_calc, button_params, text='10^x', font=('sans-serif', 15, 'bold'),
                     command=lambda: button_click('10**')).grid(row=3, column=4, sticky="nsew")

# --4 - й ряд--
# Квадратный корень из числа
square_root = Button(tk_calc, button_params, text='\u00B2\u221A',
                     command=square_root).grid(row=4, column=0, sticky="nsew")
# Третий корень из числа
third_root = Button(tk_calc, button_params, text='\u00B3\u221A',
                    command=third_root).grid(row=4, column=1, sticky="nsew")
# n-й корень числа
nth_root = Button(tk_calc, button_params, text='\u221A',
                  command=lambda: button_click('**(1/')).grid(row=4, column=2, sticky="nsew")
# Логарифм числа с основанием 10
log_base10 = Button(tk_calc, button_params, text='log\u2081\u2080', font=('sans-serif', 16, 'bold'),
                    command=lambda: button_click('log(')).grid(row=4, column=3, sticky="nsew")
# Логарифм числа с основанием e (ln)
log_basee = Button(tk_calc, button_params, text='ln',
                   command=lambda: button_click('ln(')).grid(row=4, column=4, sticky="nsew")

# --5 -й ряд--
# Добавить левую скобку
left_par = Button(tk_calc, button_params, text='(',
                  command=lambda: button_click('(')).grid(row=5, column=0, sticky="nsew")
# Добавить правую круглую скобку
right_par = Button(tk_calc, button_params, text=')',
                   command=lambda: button_click(')')).grid(row=5, column=1, sticky="nsew")
# Изменить знак числа
signs = Button(tk_calc, button_params, text='\u00B1',
               command=sign_change).grid(row=5, column=2, sticky="nsew")
# Преобразовать число в процент
percentage = Button(tk_calc, button_params, text='%',
                    command=percent).grid(row=5, column=3, sticky="nsew")
# Вычислить функцию e^x
ex = Button(tk_calc, button_params, text='e^x',
            command=lambda: button_click('e(')).grid(row=5, column=4, sticky="nsew")

# --6-й ряд--
button_7 = Button(tk_calc, button_params_main, text='7',
                  command=lambda: button_click('7')).grid(row=6, column=0, sticky="nsew")
button_8 = Button(tk_calc, button_params_main, text='8',
                  command=lambda: button_click('8')).grid(row=6, column=1, sticky="nsew")
button_9 = Button(tk_calc, button_params_main, text='9',
                  command=lambda: button_click('9')).grid(row=6, column=2, sticky="nsew")
delete_one = Button(tk_calc, bd=5, fg='#000', font=('sans-serif', 20, 'bold'),
                    text='DEL', command=button_delete, bg='#db701f').grid(row=6, column=3, sticky="nsew")
delete_all = Button(tk_calc, bd=5, fg='#000', font=('sans-serif', 20, 'bold'),
                    text='AC', command=button_clear_all, bg='#db701f').grid(row=6, column=4, sticky="nsew")

# --7-я строка--
button_4 = Button(tk_calc, button_params_main, text='4',
                  command=lambda: button_click('4')).grid(row=7, column=0, sticky="nsew")
button_5 = Button(tk_calc, button_params_main, text='5',
                  command=lambda: button_click('5')).grid(row=7, column=1, sticky="nsew")
button_6 = Button(tk_calc, button_params_main, text='6',
                  command=lambda: button_click('6')).grid(row=7, column=2, sticky="nsew")
mul = Button(tk_calc, button_params_main, text='*',
             command=lambda: button_click('*')).grid(row=7, column=3, sticky="nsew")
div = Button(tk_calc, button_params_main, text='/',
             command=lambda: button_click('/')).grid(row=7, column=4, sticky="nsew")
