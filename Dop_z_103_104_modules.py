def koefistepenSlov(k,limit):                       # формируем коэффициенты и степени членов в словаре
            import random
            slovar = {}
            endit = random.randint(0,1)*(-1)
            for i in range(k,endit,-1):  
                slovar[i] = random.randint(0,limit)
                if i == 0:
                    slovar[0] = random.randint(1,limit)
            return slovar    



def createMnogochlen (pattern):              # формируем новый многочлен на базе словаря
    x = "*x"
    mnoz = []
    for i in pattern:
        if pattern[i]==0:
            continue
        if pattern[i] == 1:
            mnoz.append((x*(i))[1:])
        else:
            mnoz.append(str(pattern[i])+x*(i))
    d = " + ".join(mnoz)
    return d + " = 0" 



def ioFile (mode, filenum='', result=''):                   # чтение или запись в файл
    with open ("file"+str(filenum)+".txt", mode) as f:
        if mode == "r":
            st = f.read()
            return st
        if mode == "w":
            f.write(result)
