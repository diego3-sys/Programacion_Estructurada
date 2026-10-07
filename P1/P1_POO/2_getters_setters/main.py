#Programa principal desde la que se manda llamar los objetos de la clase de coches

from coches import Coches

coche1 = Coches("VW", "Blanco", "2022", 220, 150, 5)
coche2 = Coches("Nissan", "Azul", "2020", 180, 150, 6)

coche1.acelerar()
coche1.acelerar()

#print(coche1._velocidad)
print(coche1.getVelocidad())

#coche1.__velocidad=400
#print._(coche1._velocidad)
print(coche1.getVelocidad)