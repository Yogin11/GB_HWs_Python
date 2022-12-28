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
# from ast import pattern
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
import random

def createMnogochlen (pattern):              # формируем новый многочлен на базе словаря
    x = "*x"
    mnoz = []
    for i in pattern:
        if pattern[i]==0:
            continue
        if pattern[i] == 1:
            mnoz.append((x*(i))[1:])
        else:
            mnoz.append(str(pattern[i])+x*(i))
    d = " + ".join(mnoz)
    return d + " = 0" 

def ioFile (mode, filenum='', result=''):                   # чтение или запись в файл
    with open ("file"+str(filenum)+".txt", mode) as f:
        if mode == "r":
            st = f.read()
            return st
        if mode == "w":
            f.write(result)
   


for l in range(1,3): 
    k = int(input("Введите степень многочлена: "))
    slovar = {}
    for i in range(k,random.randint(0,1)*(-1),-1):  # формируем коэффициенты и степени членов в словаре
        slovar[i] = random.randint(0,101)
        
    final = createMnogochlen(slovar)    
    ioFile("w",l,final)

"""
 Задача 104. Даны два файла file1.txt и file2.txt, в каждом из которых находится 
 запись многочлена (полученные в результате работы программы из задачи 103). 
 Необходимо сформировать файл file_sum.txt, содержащий сумму многочленов.
    
"""


str1= ioFile ("r",1)
str2= ioFile ("r",2)


print (str1+"\n"+str2)
 
def components (str):               # помещаем коэффициенты и степени членов в словарь
    dic = {}
    for i in str.split("+"):
        if "=" in i:
            i=i.replace("=","")
        stepen=i.count('x')
        koef = i[:i.find("*")]
        dic[stepen] = int(koef.strip())
    return dic

urav1 = components(str1)
urav2 = components(str2)
pattern ={}
maxstep = max(max(urav1.keys()),max(urav2.keys()))  # максимальная степень многочленов 

for i in range(maxstep+1,-1,-1):
    pattern[i] = 0
    if i in urav1:
        pattern[i] += urav1[i]
    if i in urav2:
        pattern[i] += urav2[i]
    
result = createMnogochlen (pattern)

ioFile ("w",'_sum',result)

print (result)
       


