class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
        
    # Getter para acceder a un atributo privado
    def get_nombre(self):
        return self._nombre    
    
    # Setter para definir un valor privado
    
    def set_nombre(self, new_nombre):
        self._nombre = new_nombre    
        
dalto = Persona("Lucas",21)

nombre = dalto.get_nombre()
print(nombre)

dalto.set_nombre("Pedro")
nombre = dalto.get_nombre()

print(nombre)