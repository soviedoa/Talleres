class Alumno:
    def __init__(self, nombre, edad, carrera, pasatiempo):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.pasatiempo = pasatiempo
    def __str__(self):
       return self.nombre+' - '+str(self.edad)+' años, '+'carrera: '+str(self.carrera)+', pasatiempo: '+str(self.pasatiempo)

class Nodo:
    def __init__(self, datos):
        self.datos = datos
        self.next = None

primero = None
Alumnos = [Alumno('Daniel Garcia', 18, "ingenieria de sistemas", "videojuegos"), Alumno('Daniel Gonzales', 29, "ingenieria de sistemas", "videojuegos"),Alumno('Diego Velasquez', 17, "ingenieria matematica", "musica"),
Alumno('Harold Gonzales', 17, "ingenieria matematica", "musica"),Alumno('Jayder Ochoa', 17, "ingenieria de sistemas", "anime"),Alumno('Juan Felipe Agudelo', 17, "ingenieria matematica", "musica"),
Alumno('Juan Felipe Martines', 20, "ingenieria mecanica e Ingenieria de sistemas", "leer"),Alumno('Juan Manuel Muñoz', 17, "ingenieria de sistemas", "vodeojuegos"),Alumno('Donovan Castrillon', 18, "ingenieria de sistemas", "videojuegos"),
Alumno('Jose Miguel Blanco', 18, "sistemas", "videojuegos"),Alumno('Jose Manuel Ramirez', 17, "ingenieria matematica", "videojuegos"),Alumno('Mylle', 17, "ingenieria matematica", "bailar"),
Alumno('Daniel Andres Hernandez', 17, "ingenieria de sistemas", "futbol"),Alumno('Julian Mazo', 17, "ingenieria de sistemas", "videojuegos"),Alumno('Santiago Parra', 16, "ingenieria matematica", "Peliculas"),
Alumno('Salomon Velez', 17, "ingenieria de sistemas", "videojuegos"),Alumno('Simon Gomez', 17, "ingenieria sistemas", 'anime')]
for alumno in Alumnos:
    nodo = Nodo(alumno)
    nodo.next = primero
    primero = nodo
    print(nodo.datos)
