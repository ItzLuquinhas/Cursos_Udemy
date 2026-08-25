def esc_apartamento(apt):
    if apt==1: print("Andar 1: R$200,000")
    if apt in [2,3,4]: print("Andar 2, 3, 4: R$220,000")
    if apt in [5,6,7]: print("Andar 5, 6, 7: R$250,000")
    if apt in [8,9,10]: print("Andar 8, 9, 10: R$300,000")
    if apt in [11,12,13,14,15,16,17,18]: print("Andar 11, 12, 13, 14, 15, 16, 17, 18: R$500,000")
try:
    apt = int(input("Andares disponíveis do 1 ao 18.\nSelecione o andar que deseja comprar o seu apartamento: "))
except ValueError:
    print("Digite apenas números para selecionar o apartamento.")
esc_apartamento(apt)