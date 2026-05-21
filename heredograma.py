
Alelos = []
Formatos = []
geracoes = []
Casais = 0
def verificacao(a,b,c):
    while True:
        if a == b or a == c:
            break
        else:
            a = input(f"Comando Invalido DIgite novamente  {b}/{c} :")   
def desenhar(s,c):
    homen = ["□","■"]
    mulher = ["○","•"]
    if s == "Masculino":
        if c == "S":
            Formatos.append(homen[1])
            
        else:
            Formatos.append(homen[0])
    else:
        if c == "S":
            Formatos.append(mulher[1])
        else:
            Formatos.append(mulher[0])
QGeracoes = int(input("Quantidade de geraçoes :"))
for i in range(1,QGeracoes + 1):
    atual = {} #Variavel de passagem
    quantidadeDePessoasNaGeracao = int(input(f"Quantas pessoas tem na geração {i}?"))
    for o in range(1 , quantidadeDePessoasNaGeracao + 1):
        HorM = input("Homen ou Mulher?:")
        verificacao(HorM,"H","M")
        if o >= 2 :
            casalSN = ("Os dois anteriores são um casal? :")
            verificacao(casalSN,"S","N")
            if casalSN == "S":
                Casais = Casais + 1
            else:
                if HorM == "H":
                    if Casais >= 1:
                        Filho = "Ele é filho de alguem? se sim de quem?:"
                    AlelosH = input("Alelos:")
                    Alelos.append(AlelosH)
                    Infectado = input("Esta Infectado:")
                    verificacao(Infectado,"S","N")
                    Homen = {"sexo": "Masculino", "Alelos": AlelosH,"Infectado": Infectado,"Filho":Filho}
                    atual[o] = Homen
                    desenhar(Homen["sexo"],Homen["Infectado"])
                else:
                    if Casais >= 1:
                        Filho = "Ele é filho de alguem? se sim de quem?:"
                    AlelosF = input("Alelos:")
                    Alelos.append(AlelosF)
                    Infectado = input("Esta Infectado:")
                    verificacao(Infectado,"S","N")
                    Mulher = {"sexo": "Feminino", "Alelos": AlelosF,"Infectado": Infectado,"Filho":Filho}
                    atual[o] = Mulher
                    desenhar(Mulher["sexo"],Mulher["Infectado"])
    geracoes.append(atual)
    Formatos.append("//")
    Alelos.append("//")
for i in range(0,len(Formatos)):
    if (Formatos[i] == "//") or (Formatos[i] == "//"):
        if i == len(Formatos) - 1:
            print("")
        else:
            print("")
            print("  |")
    else:
        if i == len(Formatos) - 2:
            print(Formatos[i],"(",Alelos[i],")")
        else:
            print(Formatos[i],"(",Alelos[i],")",end=" -- ")
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



