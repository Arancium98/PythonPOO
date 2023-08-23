"""
Una función que decora otra. 
Toma una función como entrada, le agrega una funcionalidad extra 
y devuelve como salia la función modificada

"""

# def decorador(funcion):
#     def funcion_modificada():
#         print("Antes de llamar a la función")
#         funcion()
#         print("Despues de llamar a la funcion")
#     return funcion_modificada
# def saludo():
#     print("Hola")

# saludo_modificado = decorador(saludo)
# saludo_modificado()

def decorador(funcion):
    def funcion_modificada():
        print("Antes de llamar a la función")
        funcion()
    return funcion_modificada

@decorador

def saludo():
    print("Hola")
    
    
saludo()