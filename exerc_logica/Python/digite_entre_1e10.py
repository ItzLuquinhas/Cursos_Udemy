while True:
    try:
        num_usuario = int(input("Digite um número entre 1 e 10: "))
    except ValueError:
        print("Digite apenas números inteiros.")
        continue
    if num_usuario <=10:
        print(f"Você digitou {num_usuario}")
        break
    else:
        print("Digite apenas números entre 1 e 10.")
        continue