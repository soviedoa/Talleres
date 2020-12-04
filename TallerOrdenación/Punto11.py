def quickSort(lista):
    izquierda = []
    derecha = []
    mid = []
    if len(lista)>1:
        piv = lista[len(lista)-1]
        for i in lista:
            if i<piv:
                izquierda.append(i)
            elif i  == piv:
                mid.append(i)
            else:
                derecha.append(i)
        return quickSort(izquierda)+mid+quickSort(derecha)
    else:
        return lista

listaA= [1, 19, 5, 26, 31, 33, 26, 6, 4, 36, 13, 43, 40, 49, 5, 25, 5, 5, 19, 10, 19, 38, 45, 4, 31, 8, 8, 25, 32, 3, 43, 25, 22, 15, 47, 6, 45, 26, 7, 44, 19, 27, 49, 22, 40, 6, 23, 47, 49, 7, 24, 44, 41, 10, 37, 38, 18, 46, 37, 42, 37, 11, 44, 44, 45, 34, 42, 50, 21, 38, 12, 43, 13, 23, 14, 9, 19, 13, 5, 3, 29, 14, 50, 8, 38, 6, 24, 11, 12, 29, 0, 16, 33, 39, 42, 34, 34, 5, 27, 36]

listaB = [30, 26, 7, 4, 25, 18, 12, 1, 28, 1, 15, 6, 29, 4, 48, 43, 2, 41, 19, 45, 37, 48, 47, 33, 1, 3, 16, 18, 41, 50, 47, 38, 18, 16, 34, 23, 42, 16, 45, 0, 10, 11, 36, 40, 23, 37, 3, 14, 30, 36, 32, 38, 41, 29, 13, 34, 34, 17, 15, 18]

print("Lista A ordenada: ",quickSort(listaA))
print("Lista B ordenada: ",quickSort(listaA))

listaC = listaA + listaB
print("lista C ordenada: ", quickSort(listaC))