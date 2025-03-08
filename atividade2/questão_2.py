numeros = []

while True:
    entrada = input("Digite um numero ou 'sair' para finalizar: ")

    if entrada.lower() == "sair":
        break
    
    if entrada.isdigit():
        numeros.append(int(entrada))
    else:
        print("Digite um número válido")

if numeros:
    maior = numeros[0]
    menor = numeros[0]

    for numero in numeros:
        if numero > maior:
            maior = numero
        
        if numero < menor:
            menor = numero
    
    total = maior + menor
    print(f"maior = {maior} menor = {menor} total = {total}")
else:
    print("nenhum número foi adicionado")