def par_ou_impar(num):
    if num %2==0:
        print(f"O número {num} é par.")
    else:
        print(f"O número {num} é ímpar.")
try:
    num = int(input("Insira um número para verificar se ele é par ou ímpar: "))
except ValueError:
    print("Insira apenas números inteiros.")
par_ou_impar(num)