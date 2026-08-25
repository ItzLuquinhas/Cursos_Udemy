while True:
    print("Valor da hora: R$2,00")
    try:
        min_usados = int(input("Quantos minutos o usuário usou o pc? "))
    except ValueError:
        print("Digite apenas números.")
    min_calc = min_usados/60
    valor_pagar = min_calc*2
    print(f"O cliente deve pagar R${valor_pagar:.2f} por {min_usados} minutos usados.\n")