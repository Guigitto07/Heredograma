def desenhar(s,c,i):
    homen = ["□","■"]
    mulher = ["○","•"]
    if s == "H":
        if c == "S":
            i.append(homen[1])
            
        else:
            i.append(homen[0])
    else:
        if c == "S":
            i.append(mulher[1])
        else:
            i.append(mulher[0])
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
