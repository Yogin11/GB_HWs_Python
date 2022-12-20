"""
   Задача 18:
Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
Заполните массив случайными натуральными числами от 1 до N/2.
Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший.

Ввод: 5
Ввод: 6
1 2 0 4 7
Вывод: 7

"""
import os
os.system('cls')
import random
def fillArr(N):
    arr = []
    if N == 1:
        arr.append(random.randint(1,100//2))
    else:
        for i in range(N):
            arr.append(random.randint(1,N//2))
    return arr

def findClosest (arr,X):
    lis = [arr[0]]
    delta = abs(X - arr[0])
    for i in range(1,len(arr)):
        if delta > abs(X-arr[i]):
            delta = abs(X-arr[i])
            lis.clear() 
            lis.append(arr[i])
        elif delta == abs(X-arr[i]):
            lis.append(arr[i])
    return min(lis)

while True:
    try: 
        N = int(input("Введите число элементов массива: "))
        if N <=0: 
            print ("Ошибка ввода, попробуйте еще раз")
        elif N ==1:
            print (f"Ближайшее число равно случайному числу {str(fillArr(N))[1:-1]}, т.к. нет других вариантов для сравнения")
            break
        else:
            arr = fillArr(N)
            print (arr)
            X = int(input("Введите число, которое нужно проверить: "))
            print (f"ближайшее к {X} число = {findClosest(arr,X)} ")
            break
    except:
        print ("Ошибка ввода, попробуйте еще раз")
    

