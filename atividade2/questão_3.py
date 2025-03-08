numeros = []

while True:
    entrada = input("Digite um numero de 0 a 100 ou 'sair' para finalizar: ")

    if entrada.lower() == "sair":
        break
    
    if entrada.isdigit():
        number = float(entrada)
        if 0 <= number <= 100:
            numeros.append(float(number))
        else:
            print("Digite um número válido")
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
    print(f"Maior = {maior:.2f}\nMenor = {menor:.2f}\nTotal = {total:.2f}")
else:
    print("Nenhum número foi adicionado")