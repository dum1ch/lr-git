#======================#
#  Tkinter Calculator  #
#----------------------#
#  Konstantinos Thanos #
#   Mathematician, MSc #
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