class Estudiante:
    def __init__(self, nombre,edad,grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
    def estudiar(self):
        print(f"El estudiante  {self.nombre} está estudiando")
 
# Solicitud de datos 
nombre = input("Digame su nombre")
edad = input("Digame su edad")
grado = input("Digame su grado")       


Estudiante1 = Estudiante(nombre, edad, grado)


Estudiante1.estudiar()     