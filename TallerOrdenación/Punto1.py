def elimDup(lista):
    nuevaLista = []
    for i in range(len(lista)):
        if lista[i] not in nuevaLista:
            nuevaLista.append(lista[i])
    return nuevaLista

lista=[4,7,11,4,9,5,11,7,3,5]
lista.sort()
print(elimDup(lista))