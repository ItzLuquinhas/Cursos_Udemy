numeros=[]
def maior_num_dig(lista):
    maior = lista[0]
    for i in lista:
        if i>maior:
            maior = i
    print(f"O maior núemro digitado foi: {maior}")
while True:
    try:
        num_usuário = int(input("Digite um número ente 0 e 10: "))
        numeros.append(num_usuário)
    except ValueError:
        print("Digite apenas números inteiros.")
        continue
    if num_usuário == 0:
        print("Acertou!")
        maior_num_dig(numeros)
        break
    else:
        print("Opa... Você errou, tente novamente!")