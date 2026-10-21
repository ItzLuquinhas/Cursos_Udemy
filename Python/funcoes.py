#Uma função
def minhaPrimeiraFuncao():
    print("Essa é a minha primeira função criada com Python")

minhaPrimeiraFuncao()

#-----------------------------------

def funcaoTexto(nome):
    print(nome, "Lucas")

funcaoTexto("Victor")
funcaoTexto("Luiz")
funcaoTexto("Marco")

#-----------------------------------

print("\n\n")

def funcaoSaudacao(saudacao, nome):
    print(saudacao, nome)

funcaoSaudacao("Boa noite", "Victor")
funcaoSaudacao("Bom dia", "Luiz")
funcaoSaudacao("Boa tarde", "Marco")

#-----------------------------------

print("\n\n")

#Funcao com 2 argumentos
def funcaoComArgumentos(nome, sobrenome):
    print("Nome completo:", nome,sobrenome)

nomeInput = input("Digite o seu nome: ")
sobrenomeInput = input("Digite o seu sobrenome: ")

funcaoComArgumentos(nomeInput, sobrenomeInput)

#-----------------------------------

def funcaoDivisao(numero1, numero2):
    return numero1 / numero2

resultado = funcaoDivisao(10, 2)
print(resultado)

#-----------------------------------

def funcaoMedia(nota1, nota2, nota3, nota4):
    return (nota1 + nota2 + nota3 + nota4) / 4

media = funcaoMedia(10, 6, 8, 10)

print(media)
print("\n")
#-----------------------------------

#Função com argumentos arbitrários, *args
#o args possibilita selecionar um item específico na lista
def frutaPreferida(*fruta):
    print("Eu gosto de ", fruta[0])
    print("Eu gosto de ", fruta[1])
    print("Eu gosto de ", fruta[2])
    print("Eu gosto de ", fruta[3])

frutaPreferida("Banana", "Goiaba", "Laranja", "Kiwi")

#-----------------------------------

print("\n")

def unirListas(*listas):
    print(listas)

lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]

unirListas(*lista1, *lista2)

#-----------------------------------

print("\n")

#Se o número de argumentos da palavra chave for
#desconhecido adicionamos ** antes do nome do parâmetro
def funcaoKwargs(**parametro):
    print("Eu moro em", parametro["cidade1"])
    print("Eu moro em", parametro["cidade2"])

funcaoKwargs(cidade1 = "SP", cidade2 = "RJ")

#-----------------------------------

#Argumentos com chaves
def provaAluno(nota1, nota2, nota3):
    print("O aluno tirou", nota2)

provaAluno(nota1=9, nota2=7, nota3=10)

#-------------------------------

print("\n\n")
#Função com um parametro padrão

def funcaoNome(nome = "Python"):
    print("Meu nome é", nome)

funcaoNome("Lucas")
funcaoNome("Victor")
funcaoNome()
funcaoNome("Luiz")

#----------------------------------

print("\n\n")

#Passando uma lista como um argumento
def funcaoListaNumeros(numero):
    print(numero)
    for item in numero:
        print(item)


listaNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

funcaoListaNumeros(listaNumeros)

#-----------------------------------------

print("\n\n")

def multiplicacaoDoisNumeros(numeroRecebido):
    return 10 * numeroRecebido

print(multiplicacaoDoisNumeros(5))
print(10, "x", 10, "=", multiplicacaoDoisNumeros(10))
print(10, "x", 8, "=", multiplicacaoDoisNumeros(8))

#-----------------------------------------

