"""
Задача 14
Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
"""

def ranks(n):
    k = s = 1
    while s <= n:
        print(s, end=" ")
        s = 2**k
        k += 1


while True:
    try:
        n = float(input("Введите положительное число: "))
        if n < 0:
            print("Некорректный ввод. Попробуйте еще раз")
        else:
            ranks(float(n))
            break
    except:
        print("Некорректный ввод. Попробуйте еще раз")