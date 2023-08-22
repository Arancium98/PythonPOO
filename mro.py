class A:
    def hablar(self):
     print("hola desde A")
     
class B(A):
    def hablar(self):
     print("hola desde B")
     
class C(A):
    def hablar(self):
     print("hola desde C")   
     
     
class D(B,C):
    def hablar(self):
     print("hola desde D")   
     

d = D()

# Asi utilizo el metodo del B
B.hablar(d)