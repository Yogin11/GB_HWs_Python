''' 
Задача 101: 
Вычислить число π c заданной точностью d

Пример: 
    при d = 0.001, π = 3.141    0.1 ≤ d ≤ 0.00000000001
'''

import math

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

