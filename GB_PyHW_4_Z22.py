"""
Задача 22:
Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа.
n - кол-во элементов первого набора.
m - кол-во элементов второго набора.
Значения генерируются случайным образом.

Input: 11 6
(значения сгенерированы случайным образом
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18)
Output: 11 6
6 12

"""

import os
import random
os.system('cls')

def fillArr(N):
    arr = []
    for i in range(N):
        arr.append(random.randint(1,N))
    return arr

while True:
    try: 
        st = input("Введите количество элементов первого и второго набора через пробел': ").split()
        if int(st[0]) <= 0 or int(st[1]) <=0:
            print ("Некорректный ввод. Попробуйте еще раз")
        else:
            arr1=fillArr(int(st[0]))
            arr2=fillArr(int(st[1]))
            print ("Первый набор:",*arr1)
            print("Второй набор:",*arr2)
            d=list(set(arr1) & set(arr2))
            d.sort() 
            print("Числа из обоих наборов:",*d)
            break
    except:
        print ("Некорректный ввод. Попробуйте еще раз")