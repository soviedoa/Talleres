class pila: 
    def __init__(self):
        self.pila = []
    def __str__(self):
        return str(self.pila)
    def vacia(self): 
        return len(self.pila) == 0
    def apilar(self, data):
        self.pila.append(data)
    def desapilar(self):
        assert not self.vacia()
        return self.pila.pop()
    def invertir(self):
        inversa = pila()
        for i in range(1, len(self.pila)):
            inversa.apilar(self.pila[-i])
        inversa.apilar(self.pila[0])
        for i in range(len(self.pila)):
            self.desapilar()
        return inversa
    def promedio(self):
        suma= self.pila[0]
        for i in range (len(self.pila)-1):
            suma = suma+self.pila[i+1]
            prom = suma/len(self.pila)
            return prom

pila1 = pila()
for i in range(10):
    pila1.apilar(i)
print("Pila: ", pila1)
aux = pila1.promedio()
print("Promedio: ", aux)