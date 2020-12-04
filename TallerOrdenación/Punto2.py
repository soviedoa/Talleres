def elimDupOrd(lista):
    nuevaLista = []
    for i in range(len(lista)):
        if lista[i] not in nuevaLista:
            nuevaLista.append(lista[i])
    return nuevaLista
lista = [3,4,4,5,5,7,7,9,11,11]
print(elimDupOrd(lista))