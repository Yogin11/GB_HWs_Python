"""
   Задача 16:
Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
Заполните массив случайными натуральными числами от 1 до N/2.
Выведите, сколько раз X встречается в массиве.

Ввод: 5
Ввод: 3

1 2 3 4 5
Вывод: 1

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


def search (arr,X):
    a=arr.count(X)
    return a

while True:
    try: 
        N = int(input("Введите число элементов массива: "))
        if N <=0: 
            print ("Ошибка ввода, попробуйте еще раз")
        else:
            arr = fillArr(N)
            print (arr)
            X = int(input("Введите число, которое нужно проверить: "))
            print (f"Число {X} встречается {search(arr,X)} раз(а)")
            break
    except:
        print ("Ошибка ввода, попробуйте еще раз")
    

