"""
Задача 103:
Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
(значения от 0 до 100) многочлена и записать в файл file1.txt многочлен степени k.

Пример:  k=2 

Возможные варианты многочленов:
2*x*x + 4*x + 5 = 0 
x*x + 5 = 0 
10*x*x = 0
""" 
import os
from Dop_z_103_104_modules import *
os.system('cls')
   
randlimit = 101
while True:
    try:
        k = int(input(f"Введите степень многочлена больше 1:  "))
        if k <=1:
            print("ошибка ввода, попробуйте еще раз")
        else:
            final = createMnogochlen(koefistepenSlov(k,randlimit))
            print (f"Вид записанного в файл многочлена: {final} ")    
            ioFile("w",1,final)
            break
    except:
        print("Некорректный ввод. Попробуйте еще раз")


