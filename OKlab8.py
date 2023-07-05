string1 = input()
string2 = input()

while string2 == string1:
    string2 = input()

acentos_a = ["á", "à", "â", "ã"]
acentos_e = ["é", "ê"]
acentos_i = ["í"]
acentos_o = ["ó"]

string1_lista = []
string2_lista = []

for item in string1:
    if item in acentos_a:
        for item in string1:
            string1_lista.append(item)
            for i in string1_lista:
                if i in acentos_a:
                    localizacao = string1_lista.index(i)
                    string1_lista.remove(i)
                    string1_lista.insert(localizacao, "a")
        string1 = "".join(string1_lista)
    if item in acentos_e:
        for item in string1:
            string1_lista.append(item)
            for i in string1_lista:
                if i in acentos_e:
                    localizacao = string1_lista.index(i)
                    string1_lista.remove(i)
                    string1_lista.insert(localizacao, "e")
        string1 = "".join(string1_lista)
    if item in acentos_i:
        for item in string1:
            string1_lista.append(item)
            for i in string1_lista:
                if i in acentos_i:
                    localizacao = string1_lista.index(i)
                    string1_lista.remove(i)
                    string1_lista.insert(localizacao, "i")
        string1 = "".join(string1_lista)
    if item in acentos_o:
        for item in string1:
            string1_lista.append(item)
            for i in string1_lista:
                if i in acentos_o:
                    localizacao = string1_lista.index(i)
                    string1_lista.remove(i)
                    string1_lista.insert(localizacao, "o")
        string1 = "".join(string1_lista)

for item in string2:
    if item in acentos_a:
        for item in string2:
            string2_lista.append(item)
            for i in string2_lista:
                if i in acentos_a:
                    localizacao = string2_lista.index(i)
                    string2_lista.remove(i)
                    string2_lista.insert(localizacao, "a")
        string2 = "".join(string2_lista)
    if item in acentos_e:
        for item in string2:
            string2_lista.append(item)
            for i in string2_lista:
                if i in acentos_e:
                    localizacao = string2_lista.index(i)
                    string2_lista.remove(i)
                    string2_lista.insert(localizacao, "e")
        string2 = "".join(string2_lista)
    if item in acentos_i:
        for item in string2:
            string2_lista.append(item)
            for i in string2_lista:
                if i in acentos_i:
                    localizacao = string2_lista.index(i)
                    string2_lista.remove(i)
                    string2_lista.insert(localizacao, "i")
        string2 = "".join(string2_lista)
    if item in acentos_o:
        for item in string2:
            string2_lista.append(item)
            for i in string2_lista:
                if i in acentos_o:
                    localizacao = string2_lista.index(i)
                    string2_lista.remove(i)
                    string2_lista.insert(localizacao, "o")
        string2 = "".join(string2_lista)
       
anagrama = False        
n = 0

if len(string1) == len(string2):
    for item in string1:
        if item in string2:
            n += 1
            if n == (len(string1) -1):
                anagrama = True
            continue
        else: print(f"{string2} não é um anagrama de {string1}")
else: print(f"{string2} não é um anagrama de {string1}")

if anagrama == True:
    print(f"{string2} é um anagrama de {string1}")
