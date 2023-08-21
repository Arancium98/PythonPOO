class Persona:
    
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

# Clase heredada
class Empleado(Persona):
    def __init__(self, nombre,edad,nacionalidad,trabajo, salario):
        #Esta herado de la clase padre
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario

class Estudiante(Persona):
    def __init__(self, nombre,edad,nacionalidad,notas, universidad):
        #Esta herado de la clase padre
        super().__init__(nombre, edad, nacionalidad)
        self.notas = notas
        self.universidad = universidad
                        