"""  
 Programación Orinetada a Objetos POO o OOP

CLASES .- es como un molde a traves del cual se puede instanciar un objeto dentro de las clases se definen los atributos (propiedades / caracteristicas) y los métodos (funciones o acciones)

OBJETOS O INSTANCIAS .- son parte de una clase los objetos o instacias pertenecen a una clase, es decir para interacturar con la clase o clases y hacer uso de los atributos y metodos es necesario crear un objeto o objetos.
"""

#Ejemplo 1 Crear una clase (un molde para crear mas objetos)llamada Coches y apartir de la clase crear objetos o instancias (coche) con caracteristicas similares


print("\033c")
class Coches:
    marca=""
    color=" Blanco"
    modelo=""
    velocidad=100
    potencia=0
    asientos=0 

    def acelerar(self):
        self.velocidad+=1
        print(f"Ahora la velocidad final es :{self.velocidad}")
        
    def frenar(self):
        self.velocidad-=1
        print(f"Ahora la velocidad final es :{self.velocidad}")
#multiples objetos
coche1=Coches()
coche2=Coches()

print(f"el color del coche es{coche1.color}")
print(f"el color del coche es{coche2.color}")    

for i in range(1,11):
    coche1.acelerar()