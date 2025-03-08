numero = int(input("digite um número inteiro: "))

divisores = []

for i in range(1,numero + 1):
    if numero % i == 0:
        divisores.append(i)

quantidade = len(divisores)

if quantidade == 2:
    print("é um número primo")
else:
    print("não é um numero primo")