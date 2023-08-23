
class MiClase:
    def __init__(self):
        # Con el _ previo se definie como privado,
        # Si se utiliza 2 _ quedará "Muy privado"
        self.__atributo_privado = "Valor"
    
    #Metodo privado    
    def _hablar(self):
            print("hola")
        
        
objeto = MiClase()
print(objeto._atributo_privado) 

## Mejora la legibilidad del cogigo, como por ejemplo definir como que no se pueda ingresar al atributo de esa forma
