#contagem crescente
def cont_cresc(num):
    for i in range(0,num+1):
        print(i)
def cont_regressiva(num):
    for i in range(num,0,-1):
        print(f"Começando em {i}")
try:
    num_usuário = int(input("Digite um número para ver suas contagens: "))
except ValueError:
    print("Digite apenas números inteiros.")
cont_cresc(num_usuário)
print()
cont_regressiva(num_usuário)