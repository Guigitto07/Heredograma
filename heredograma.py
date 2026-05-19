homen = ["□","■"]
mulher = ["○","•"]
FGeraçoes = []
Formatos = []
CopyFormatos = Formatos.copy
def desenhar(s,c):
    if s == "Masculino":
        if c == "Sim":
            CopyFormatos.append(homen[1])
            
        else:
            CopyFormatos.append(homen[0])
    else:
        if c == "Sim":
            CopyFormatos.append(mulher[1])
        else:
            CopyFormatos.append(mulher[0])

AlelosH = ""
AlelosF = ""
geracoes = []
QGeracoes = int(input("Quantidade de geraçoes :"))
for i in range(1,QGeracoes + 1):
    atual = {}
    quantidadeDePessoasNaGeracao = int(input(f"Quantas pessoas tem na geração {i}?"))
    for o in range(1 , quantidadeDePessoasNaGeracao + 1):
        HorM = input("Homen ou Mulher?:")
        if HorM == "Homen":
            AlelosH = input("Alelos:")
            Infectado = input("Esta Infectado:")
            Homen = {"sexo": "Masculino", "Alelos": AlelosH,"Infectado": Infectado}
            atual[o] = Homen
            desenhar(Homen["sexo"],Homen["Infectado"])
        else:
            AlelosF = input("Alelos:")
            Infectado = input("Esta Infectado:")
            Mulher = {"sexo": "Feminino", "Alelos": AlelosF,"Infectado": Infectado}
            atual[o] = Mulher
            desenhar(Mulher["sexo"],Mulher["Infectado"])
    geracoes.append(atual)
    Formatos = CopyFormatos
    FGeraçoes.append(Formatos)
    CopyFormatos.pop(0)
    CopyFormatos.pop(0)
for i in range(0,QGeracoes):
    print(FGeraçoes[i])


def primeiraLeideMendel(x,y):
    Contador = 0
    #mae/////////////////////////////////////
    genotipoMae = x
    a = 0
    b = 0
    for i in genotipoMae:
        Contador = Contador + 1
        if i == "A":
            if Contador == 1:
                a = 1 
            elif Contador == 2:
                b = 1
    #Pai////////////////////////////////////////
    genotipoPai = y
    c = 0
    d = 0
    for z in genotipoPai:
        Contador = Contador + 1
        if z == "A":
            if Contador == 3:
                c = 1 
            elif Contador == 4:
                d = 1
    # mendel 
    soma = a + b + c + d
    print()
    if soma == 2:
        if ((c == 0) and (d == 0)) or ((a == 0) and (b==0)):
            print("100% hterozigoto")
        else:
            print("50% Heterozigoto\n25% Homozigoto dominante\n25% Homozigoto recessivo")
    elif soma == 3:
        print("50% hterozigoto\n50% Homozigoto dominante")
    elif soma == 4:
        print("100% Homozigoto dominante")
    elif soma == 1:
        print("50% hterozigoto\n50% Homozigoto recessivo")
    elif soma == 0:
        print("100% Homozigoto recessivo")



