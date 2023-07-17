texto = input().lower
#tirar virgulas e pontuações

dict_letras = {}

lista_palavras = texto.split()

for item in lista_palavras:
    a = list(item)

print("Letra\tOcorrência\tFrequência")
