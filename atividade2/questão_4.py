while True:
    nome = input("Digite seu nome (maior que 3 caracteres): ")
    caracteres = len(nome)
    if caracteres > 3:
        break
    else:
        print("Nome inválido, poucos caracteres!")

while True:
    idade = int(input("Digite sua idade: "))
    if 0 < idade < 150:
        break
    else:
        print("Idade inválida!")

while True:
    salario = float(input("Digite seu salário: "))
    if salario > 0:
        break
    else:
        print("Salário não pode ser menor ou igual a zero!")

while True:
    sexo = input("Digite seu sexo ('F' ou 'M'): ")
    sexo2 = sexo.upper()
    if sexo2 == "F" or sexo2 == "M":
        break
    else:
        print("sexo inválido!")

while True:
    estado_civil = input("Digite seu estado civil ('S', 'C', 'V', 'D'): ")
    estado_civil2 = estado_civil.upper()
    if estado_civil2 == "S" or estado_civil2 == "C" or estado_civil2 == "V" or estado_civil2 == "D":
        break
    else:
        print("Estado civil inválido!")

print(f"Nome: {nome}\nIdade: {idade} anos\nSalário: R$ {salario:.2f}\nSexo: {sexo2}\nEstado civil: {estado_civil2}")