import random

numeros_jogador1 = []
numeros_jogador2 = []
numeros_computador = []

pontosjogador1 = 0
pontosjogador2 = 0
pontos1 = []
pontos2 = []
a = 1

while a != 0:
    for i in range (0,5):
        numero1 = int(input())
        if numero1 > 0 and numero1 < 21:
            numeros_jogador1.append(numero1)
        else:
            numero1 = int(input())
    for j in range (0,5):
        numero2 = int(input())
        if numero2 > 0 and numero2 < 21:
            numeros_jogador2.append(numero2)
        else:
            numero2 = int(input())
            
    for k in range(0,5):
        random.seed(None)
        rnd = random.randint(1, 20)
        numeros_computador.append(rnd)
        if numeros_jogador1.count(rnd) >= 1:
            pontosjogador1 += 10
        if numeros_jogador2.count(rnd) >= 1:
            pontosjogador2 += 10
            
    pontos1.append(pontosjogador1)
    pontos2.append(pontosjogador2)

    a = int(input())

b = len(pontos1)

for l in range(0, b):
    print(f"JOGADOR 1 = {pontos1} JOGADOR 2 = {pontos2}")

soma1 = 0
soma2 = 0

for m in range(0, b):
    soma1 += pontos1[m]
    soma2 += pontos2[m]

if soma1 > soma2:
    print("JOGADOR 1 VENCEU!")
elif soma1 < soma2:
    print("JOGADOR 2 VENCEU!")
else:
    print("EMPATE!")
