"""
Задача 26:  
Напишите программу, которая на вход принимает два числа A и B, 
и возводит число А в целую степень B с помощью рекурсии.
"""

import os
os.system('cls')


def recur(A, B):
    if B > 0:                           # Если степень положительная 
        if B == 1:
            return A
        elif B % 2 == 0:
            return recur(A*A, B//2)
        else:
            return A*recur(A*A, B//2)
    else:                               # Если степень отрицательная
        if B == -1:
            return 1/A
        elif B % 2 == 0:
            return recur(A*A, B//2)
        else:
            return 1/A*recur(A*A, B//2+1)
    

while True:
    try:
        A = float(input("Введите A: "))
        B = int(input("Введите B: "))
        if B == 0:
            print(f" {A} в степени {B} равно: {1} ")
            break
        else:
            print(f" {A} в степени {B} равно: {recur(A,B)} ")
            break
    except:
        print("Некорректный ввод. Попробуйте еще раз")
