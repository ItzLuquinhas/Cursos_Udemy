#armazenar todos os números pares de 0 a 100 em uma lista usando for

lista_pares = []
for i in range(101):
    if i %2==0:
        lista_pares.append(i)
print(lista_pares)