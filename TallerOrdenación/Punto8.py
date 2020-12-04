def mezcla(lista):
    if len(lista)==1:
        return lista
    izq, der = dividir(lista)
    print("Pasada: ", lista)
    return mezclar(mezcla(izq), mezcla(der))

def dividir(lista):
    mid = len(lista)//2
    return lista[:mid], lista[mid:]

def mezclar(izquierda, derecha):
    listaMezclada=[]
    i=0
    j=0
    while i<len(izquierda) and j<len(derecha):
        if izquierda[i]<derecha[j]:
            listaMezclada.append(izquierda[i])
            i+=1
        else:
            listaMezclada.append(derecha[j])
            j+=1
    listaMezclada.extend(izquierda[i:])
    listaMezclada.extend(derecha[j:])
    return listaMezclada

lista = [21, 1, 26, 45, 29, 28, 2, 9, 16, 49, 39, 27, 43, 34, 46, 40] 
print("Resultado: ", mezcla(lista))