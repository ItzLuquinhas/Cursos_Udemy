def fatoracao(num):
    lista=[]
    a=1
    for i in range(1,num+1):
        lista.append(i)
    for j in lista:
        a*=j
    return a
try:
    num_usuario = int(input("Digite um número aleatório para ver a soma da sua fatoração: "))
except ValueError:
    print("Digite apenas núemros inteiros.")
print(f"Resultado da fatoração: {fatoracao(num_usuario)}")