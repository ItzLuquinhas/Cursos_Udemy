notas = []
media = 0
aluno = str(input("Qual o nome do aluno? "))
while True:
    try:
        notas_entrada = float(input("Insira as notas do aluno: "))
        notas.append(notas_entrada)
    except ValueError:
        print("Digite apenas números.")
        continue
    if len(notas) == 4:
        for i in notas:
            media+=i
            divisor=len(notas)
            media_final=media/divisor
        print(f"A média do aluno {aluno} é: {media_final}")
        if media_final >= 7:
            print("Aluno aprovado.")
            break
        else:
            print("O aluno está de recuperação.")
            try:
                nota_recuperacao = float(input("Insira a nota de recuperação: "))
            except ValueError:
                print("Digite apenas números.")
            resultado_recuperacao = media_final+nota_recuperacao
            resultado_recuperacao = resultado_recuperacao/2
            if resultado_recuperacao >= 7:
                print(f"Aluno aprovado. Média de {resultado_recuperacao}")
                break
            else:
                print(f"Aluno reprovado. Média de {resultado_recuperacao}")
                break
    else:
        breakpoint