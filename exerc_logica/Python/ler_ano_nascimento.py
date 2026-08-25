import time
ano_atual = time.localtime().tm_year
def calc_ano(ano_usuario,ano_atual):
    ano_final = ano_atual-ano_usuario
    return ano_final
while True:
    try:
        ano_usuario = int(input("Insira o seu ano de nascimento: "))
    except ValueError:
        print("Insira apenas o ano em números.")
        continue
    ano_final = calc_ano(ano_usuario,ano_atual)
    if ano_final<16:
        print(f"Você possui {ano_final} anos.\nVocê não pode votar e não pode tirar a carteira de motorista.")
        break
    elif ano_final>=16 and ano_final<18:
        print(f"Você possui {ano_final} anos.\nVocê pode votar, mas não pode tirar a carteira de motorista.")
        break
    else:
        print(f"Você possui {ano_final} anos.\nVocê pode votar e tirar a carteira de motorista.")
        break