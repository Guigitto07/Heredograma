import Funcao as f
def verificacao(a,b,c):
    while True:
        if a == b or a == c:
            break
        else:
            a = input(f"Comando Invalido DIgite novamente  {b}/{c} :")   
while True:
    heredograma = []
    informacoes = [
        [], #Alelos
        [], #Formatos
        [], #Geracoes
    ]

    Casais = 0

    quantidadeDeGeracao = int(input("Quantidade de geraçoes :")) # Arrumar a verificação de numero


    for i in range(1,quantidadeDeGeracao + 1):

        atual = {} #Variavel de passagem

        quantidadeDePessoasNaGeracao = int(input(f"Quantas pessoas tem na geração {i}?")) # Arrumar a verificação de numero

        for o in range(1 , quantidadeDePessoasNaGeracao + 1):
            sexo = input("Homen ou Mulher?:") # Arrumar o caps lock

            verificacao(sexo,"H","M") 

            if Casais >= 1:
                Filho = "Ele é filho de alguem? se sim de quem?:"

            Alelos = input("Alelos:")

            informacoes[0].append(Alelos)

            Infectado = input("Esta Infectado:")

            verificacao(Infectado,"S","N")

            pessoa = {"sexo": sexo, "Alelos": Alelos,"Infectado": Infectado}

            atual[o] = pessoa

            f.desenhar(pessoa["sexo"],pessoa["Infectado"],informacoes[1])

        informacoes[2].append(atual)

        informacoes[2].append("//")

        informacoes[0].append("//")

    for i in range(0,len(informacoes[1])):
        heredograma.append([])
    for l in range(len(informacoes[1])):
        print(heredograma[l])


