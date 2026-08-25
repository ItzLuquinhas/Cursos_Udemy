def dia_semana(num):
    if num == 1: print("Hoje é domingo.")
    if num == 2: print("Hoje é segunda.")
    if num == 3: print("Hoje é terça.")
    if num == 4: print("Hoje é quarta.")
    if num == 5: print("Hoje é quinta.")
    if num == 6: print("Hoje é sexta.")
    if num == 7: print("Hoje é sábado.")
try:
    num = int(input("Digite um número de 1 a 7: "))
except ValueError:
    print("Digite apenas números e de 1 a 7.")
dia_semana(num)