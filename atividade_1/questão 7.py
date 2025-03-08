pontos = 0

pergunta_1 = int(input("telefonou para a vítima? 1. Sim  2. Não:"))
if pergunta_1 == 1:
    pontos += 1

pergunta_2 = int(input("esteve no local do crime?1. Sim 2. Não:"))
if pergunta_2 == 1:
    pontos += 1

pergunta_3 = int(input("mora perto da vítima? 1. Sim 2. Não:"))
if pergunta_3 == 1:
    pontos += 1

pergunta_4 = int(input("Devia para a vítima? 1. Sim 2. Não:"))
if pergunta_4 == 1:
    pontos += 1

pergunta_5 = int(input("Já trabalhou com a vítima? 1. Sim 2. Não:"))
if pergunta_5 == 1:
    pontos += 1

if pontos == 2:
    print("você é supeito")
elif pontos == 3 or pontos == 4:
    print("você é o cúmplice")
elif pontos == 5:
    print("você é o assassino")
else:
    print("você é inocente")
