
class Celular:
    # Metodo Constructor
    def __init__(self, marca,modelo,camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    
    # Un metodo corresponde a una "Función dentro de la clase"    
    def llamar(self):
        print(f"Estas llamando desde un : {self.modelo}")
    
    def cortar(self):
        print(f"Estas cortando desde un : {self.modelo}")

    
    
celular1 = Celular("Samsung", "S23", "48MP")
celular2 = Celular("Apple", "xd", "96MP")

celular1.llamar()
print(celular2.marca)
