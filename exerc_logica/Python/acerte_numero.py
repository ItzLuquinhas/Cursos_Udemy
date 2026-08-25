from random import randint
numeros = []
num_sistema = randint(1,20)
tentativas = 0
def soma_lista(lista):
    if len(lista) == 1:
        a = lista[0]
        return a
    else:
        a = 0
        for i in lista:
            a+=i
        return a
while True:
    try:
        print(num_sistema)
        num_usuario = int(input("Digite um número aleatório de 1 a 20: "))
        numeros.append(num_usuario)
        tentativas+=1
    except ValueError:
        print("Digite apenas números inteiros.")
        continue
    if num_usuario != num_sistema:
        print("Opa... Você errou o número, tente novamente!")
        continue
    else:
        print(f"Parabéns, você acertou o número!\nNúmero escolhido pelo sistema: {num_sistema}\nTentativas: {tentativas}\nSoma dos números que você digitou: {soma_lista(numeros)}")
        break