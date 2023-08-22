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
                        
                        
class Artista:
    def __init__(self,habilidad):
        self.habilidad = habilidad
        
        
        def mostrar_habilidad(self):
            print(f"mi habilidad es: {self.habilidad}")                       
            
# Esta es una class que hereda de 2 clases, es una herencia multiple.
class EmpleadoArtista(Persona,Artista):
    def __init__(self,nombre,edad,nacionalidad,habilidad,salario,empresa):
        Persona.__init__(self,nombre,edad,nacionalidad)
        Artista.__init__(self,habilidad)
        self.salario = salario
        self.empresa = empresa
        
        def presentar(self):
            return (f'{self.mostrar_habilidad()}')
 