def burbuja(lista):
    for numPasada in range(len(lista)-1,0,-1):        
        for i in range (numPasada):
            print("Burbuja: ",lista)
            if lista[i]>lista[i+1]:
                aux = lista[i]
                lista[i]=lista[i+1]
                lista[i+1] = aux
    return lista
lista = [47,3,21,32,56,92]
print(burbuja(lista))

def insercion (lista):
    for i in range(1,len(lista)):
        print("insercion:", lista)
        valor_a_ordenar=lista[i]
        while lista[i-1]>valor_a_ordenar and i>0:
            lista[i],lista[i-1] = lista[i-1],lista[i]
            i = i-1
    return lista
lista = [47,3,21,32,56,92]
print(insercion(lista))

#def seleccion(lista):
   #for i in range(len(Lista)-1,0,-1):
       #mayor=0
       #for j in range(1,i+1):
           #if lista[j]>lista[mayor]:
               #mayor = j
        #aux = lista[i]
        #lista[i] = lista[mayor]
        #lista[mayor] = aux
#lista = [47,3,21,32,56,92]
#print(seleccion(lista))
