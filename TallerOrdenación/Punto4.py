def shell(lista):
    contSublista = len(lista)//2
    while contSublista > 0:
        for psiInicial in range(contSublista):
            print(lista)
            brecha(lista,psiInicial,contSublista)
        contSublista = contSublista//2
    return lista
    
def brecha(lista, inicio, brecha):
    for i in range(inicio + brecha,len(lista), brecha):
        valorActual = lista[i]
        posicion = i
        while posicion >= brecha and lista[posicion-brecha] > valorActual:
            lista[posicion] = lista[posicion-brecha]
            posicion = posicion-brecha
        lista[posicion]=valorActual

lista = [8,43,17,6,40,16,18,97,11,7]
print(shell(lista))