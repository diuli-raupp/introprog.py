try:
    num1 = int(input())
    num2 = int(input())
except:
    print("Entrada inválida")

num2 += 1
soma = 0

for item in range (num2, num1):
    soma = soma + item

if soma % 2 == 0:
    num2 -= 1
    metade = (num1 + num2) / 2
    print(f"Início do intervalo: {num1}\nFim do intervalo: {num2}\nSomatório do intervalo: {soma}\nMetade do intervalo: {metade}")
else:
    num2 -= 1
    metade1 = (num1 + num2 + 1) / 2
    metade2 = (num1 + num2 - 1) / 2
    print(f"Início do intervalo: {num1}\nFim do intervalo: {num2}\nSomatório do intervalo: {soma}\nMetade do intervalo: {metade1} {metade2}")
