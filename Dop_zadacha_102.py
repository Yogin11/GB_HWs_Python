'''

Задача 102: 
Задайте натуральное число N. Напишите программу, которая 
составит список простых множителей числа N.

'''

import os
os.system('cls')


while True:
    try:
        num = int(input("Введите N:"))
        if num <= 0:
            print("Некорректный ввод. Попробуйте еще раз")
        else:
            g={1}
            i=2
            while i <= num:
                if i % 2 != 0 or i == 2:   
                    while num%i==0:
                        num = num// i
                        g.add(i)
                if i > num/2: 
                    g.add(num)
                    break
                i += 1
            mnoz = list(g)
            mnoz.sort()
            print ("Простые множители числа: ",*mnoz)
            break
    except:
        print("Некорректный ввод. Попробуйте еще раз")



