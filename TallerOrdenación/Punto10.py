def encontrar(matriz,n):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if n in matriz[j]:
                return "Si"
    return "no"


matriz = [[1,2,2,2,3,4],[1,2,3,3,4,5],[3,4,4,4,4,6],[4,5,6,7,8,9]]
print(encontrar(matriz,8))