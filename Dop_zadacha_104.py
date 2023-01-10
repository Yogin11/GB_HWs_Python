"""
 Задача 104. Даны два файла file1.txt и file2.txt, в каждом из которых находится 
 запись многочлена (полученные в результате работы программы из задачи 103). 
 Необходимо сформировать файл file_sum.txt, содержащий сумму многочленов.
    
"""
import os
from Dop_z_103_104_modules import *
os.system('cls')

def components (str):               # помещаем коэффициенты и степени членов в словарь
    dic = {}
    for i in str.split("+"):
        if "=" in i:
            i=i.replace("=","")
        stepen=i.count("x")
        if i.startswith(" x") or i.startswith("x"):
            koef = " 1 "
        else:
            koef = i[:i.find("*")]
        dic[stepen] = int(koef.strip())
    return dic

print ("Полученные из файлов многочлены:") 
pattern ={}
for i in range(2):
    loadstr = ioFile ("r",i+1) 
    print (loadstr)
    urav = components(loadstr)
    maximstep = max(urav.keys())                # максимальная степень загруженного многочлена
    for j in range(maximstep+1,-1,-1):
        if j in urav:
            pattern[j] = pattern.get(j,0) + urav[j]
    
result = createMnogochlen (pattern)
ioFile ("w",'_sum',result)
print (f"Итоговый многочлен их суммы, записанный в файл: {result} ")
