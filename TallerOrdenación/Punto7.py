import time
def negativos(lista):
    nuevaLista = []
    for i in range(len(lista)):
        if lista[i]<0:
            nuevaLista.append(lista[i])
            i+=1
    return nuevaLista
lista = [-6,5,2,-3,1,-10,-9,9,7,-4,12]
print(negativos(lista))
peorCaso = [5,2,1,9,7,12,-6,-3,-10,-9,-4]
start_time = time.time()
print(negativos(peorCaso))
print("--- %s seconds ---" % (time.time() - start_time))