''' 
Задача 101: 
Вычислить число π c заданной точностью d

Пример: 
    при d = 0.001, π = 3.141    0.1 ≤ d ≤ 0.00000000001
'''
"""
import math
from re import I

while True:
    try:
        d = input("Введите точность d для числа Пи в формате 0.1 ≤ d ≤ 0.00000000001: ")
        if (d[-1] == '1') and (0 < float(d) < 1) and (d == '0.1' or float(d[1:-1]) == 0):
            st = len(str(d))
            result = float(str(math.pi)[:st])
            print(result)
            break
        else:
            print("Неправильно задан формат, попробуйте еще раз")
    except:
        print("Некорректный ввод. Попробуйте еще раз")
"""
'''

Задача 102: 
Задайте натуральное число N. Напишите программу, которая 
составит список простых множителей числа N.

'''
import os
os.system('cls')

# while True:
    # try:
        # N = int(input("Введите N:"))
        # if N <= 0:
            # print("Некорректный ввод. Попробуйте еще раз")
        # else:
            # mnoz = [1]
            # num = N
            # i=2
            # while i <= num:
                # print(i)        
                # if i % 2 != 0 or i == 2:   
                    # if num % i == 0:                #проверяем делитель
                        # num = num// i 
                        # while num%i==0:             #проверяем повторение делителя
                            # num = num// i 
                        # mnoz.append(i)
                # if i > num/2: 
                    # mnoz.append(num)
                    # break
                # i += 1
            # if len(mnoz) >2:
                # print ("Простые множители числа - ",*mnoz)
            # else:    
                # print(f"число {N} - простое, т.е. делится только на себя и 1")
            # break
    # except:
        # print("Некорректный ввод. Попробуйте еще раз")
        # 
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
# import random
# 
# k = int(input("Введите степень многочлена: "))
# koef = []
# for i in range(k+1):
    # koef.append(int(random.randint(0,101)))
# x = "*x"
# st = ''
# for i in range(k+1):
    # st = st + str(koef[i])+x*(k-i) + " + "
# final = st.rstrip()[:-1] + " = 0" 
# with open ("file2.txt", "w") as f:
    # f.write(final)
# print(final)
# 
"""
 Задача 104. Даны два файла file1.txt и file2.txt, в каждом из которых находится 
 запись многочлена (полученные в результате работы программы из задачи 103). 
 Необходимо сформировать файл file_sum.txt, содержащий сумму многочленов.
    
"""

with open ("file1.txt", "r") as f:
    str1 = f.read()

with open ("file2.txt", "r") as f:
    str2 = f.read()

print (str1+"\n"+str2)


