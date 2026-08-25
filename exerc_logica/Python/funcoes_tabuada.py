def somar(a,b):
    resultado = a+b
    print(f"A soma de {a}+{b} é {resultado}")
def subtrair(a,b):
    resultado = a-b
    print(f"A subtração de {a}-{b} é {resultado}")
def multiplicacao(a,b):
    resultado = a*b
    print(f"A multiplicação de {a}*{b} é {resultado}")
def divisao(a,b):
    resultado = a/b
    print(f"A divisão de {a}/{b} é {resultado:.2f}")
while True:
    print("""Bem-vindo, selecione a operação que deseja fazer.
    [1] - Somar
    [2] - Subtrair
    [3] - Multiplicação
    [4] - Divisão""")
    try:
        operacao = int(input("Selecione uma operação: "))
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
    except ValueError:
        print("Digite apenas números de 1 a 4.")
    if operacao==1:
        somar(num1,num2)
        break
    elif operacao==2:
        subtrair(num1,num2)
        break
    elif operacao==3:
        multiplicacao(num1,num2)
        break
    elif operacao==4:
        divisao(num1,num2)
        break
    else:
        print("Selecione uma operação válida.")
        continue