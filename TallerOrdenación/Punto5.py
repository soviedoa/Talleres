def elecciones(lista):
    votosCand1=0
    votosCand2=0
    for i in range(len(lista)):
        if lista[i]==1:
            votosCand1+=1
        elif lista[i]==0:
            votosCand2+=1
        else:
            pass
    if votosCand1>votosCand2:
        print("Ganó el candidato 1")
    else:
        print("Ganó el candidato 2")
    
    return votosCand1,votosCand2

lista = [1,0,1,1,0,1,1,0,0,1,1,0,1,1,0,1,1,0,0,1,0,1,0,1,0,0,1,1,0,0,1,1,1,1,1,0,1,0,1,0,1,0,0,0,0,1,1,0,1,1,0,1,0,1,0,0,0,1,0,1,1,1,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,1,1,0,0,0,1,1]
print(elecciones(lista))