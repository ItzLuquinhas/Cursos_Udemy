def tabuada(num):
    print(f"Tabuada do número {num}:")
    for i in range(1,11):
        print(f"{num}x{i}={num*i}")
try:
    num_usuário = int(input("Digite um número para ver a sua respectiva tabuada: "))
except ValueError:
    print("Digite apenas números inteiros.")
tabuada(num_usuário)