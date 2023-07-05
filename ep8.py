string1 = input()
string2 = input()

acentos_a = ["á", "à", "â", "ã"]
acentps_e = ["é"]
acentos_i = ["í"]
acentos_o = ["ó"]

string1_lista = []

for item in string1:
    if item in acentos_a:
        for item in string1:
             string1_lista.append(item)
        
        
while string2 == string1:
    string2 = input()

anagrama = False
n = 0

if len(string1) == len(string2):
    for item in string1:
        if item in string2:
            n += 1
            if n == (len(string1) -1):
                anagrama = True
            continue
        else: print(f"{string2} não é um anagrama de {string2}")
else: print(f"{string2} não é um anagrama de {string2}")
