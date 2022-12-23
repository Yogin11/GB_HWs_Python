"""
Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.


"""

import os
os.system('cls')


def recur(A, B):
    if A <= B:
        if A == 0:
            return B
        else:
            return recur(A-1,B+1)
    else:
        return recur(B,A)

while True:
    try:
        A = int(input("Введите неотрицательное число A: "))
        B = int(input("Введите неотрицательное число B: "))
        if B < 0 or A < 0:
            print("Некорректный ввод. Попробуйте еще раз")
            break
        else:
            print(f" Сумма равна {recur(A,B)} ")
            break
    except:
        print("Некорректный ввод. Попробуйте еще раз")
