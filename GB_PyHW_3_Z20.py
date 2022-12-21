"""
Задача 20:
В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
В случае с английским алфавитом очки распределяются так:
A, E, I, O, U, L, N, S, T, R – 1 очко;
D, G – 2 очка;
B, C, M, P – 3 очка;
F, H, V, W, Y – 4 очка;
K – 5 очков;
J, X – 8 очков;
Q, Z – 10 очков.

А русские буквы оцениваются так:
А, В, Е, И, Н, О, Р, С, Т – 1 очко;
Д, К, Л, М, П, У – 2 очка;
Б, Г, Ё, Ь, Я – 3 очка;
Й, Ы – 4 очка;
Ж, З, Х, Ц, Ч – 5 очков;
Ш, Э, Ю – 8 очков;
Ф, Щ, Ъ – 10 очков.

Напишите программу, которая вычисляет стоимость введенного пользователем слова.
Будем считать, что на вход подается только одно слово, которое содержит либо только английские, 
либо только русские буквы.

Ввод: ноутбук
Вывод: 12

"""

import os
import string
os.system('cls')

def loaddict(path):                     # чтение данных о стоимости букв из файлов
    data = open(path, 'r',encoding="utf8")
    dictionary = {} 
    for line in data: 
        sep = line.split(',',1)
        sep[1]=sep[1][:-1].replace(',','')
        dictionary[int(sep[0])] = sep[1]
    data.close()
    return dictionary

engl=set(string.ascii_letters)          # множество латинских букв
rus=''
for i in range(ord('А'), ord('Я')+1): 
    rus+=chr(i)                         # строка прописных букв кириллицы
rus+= chr(ord('Ё'))                     # добавляем в строку букву Ё
    
while True:
    word = input('Введите слово(без дефиса)/Please enter the word(without hyphen): ').upper()
    if set(word).issubset(engl):
        path = 'englalphabet.txt'
        break
    elif set(word).issubset(rus):
        path = 'rusalphabet.txt'
        break
    else:
        print ("\tВ слове содержатся символы отличные от букв. Попробуйте еще раз.")
        print ("\tThe word contains non-alphabetical characters. Please try again.")
        
evaluations = loaddict(path)
sum = 0  
for i in word:                  # Подсчет стоимости букв и слова
    for j in evaluations:
        if i in evaluations[j]:
            sum+=j
            break
print(f"Стоимость слова/The word's value = {sum}")

