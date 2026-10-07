print("\033c")

class Coches:
    def _init_(self, marca, color, modelo, velocidad, caballaje, plazas):
        self._marca = marca
        self._color = color
        self._modelo = modelo
        self._velocidad = velocidad
        self._caballaje = caballaje
        self._plazas = plazas

    def acelerar(self):
        self.__velocidad += 1   

    def frenar(self):
        self.__velocidad -= 1

#Crear los metodos setters y getters .- estos metodos son importantes y necesarios en todos clases para que el programador interactue con los valores de los atributos a traves de estos metodos ... digamos que es la manera mas adecuada y recomendada para solicitar un valor (get) y/o para ingresar o cambiar un valor (set) a un atributo en particular de la clase a traves de un objeto. 
# En teoria se deberia de crear un metodo Getters y Setters por   cada atributo que contenga la clase
#   Los metodos get siempre regresan valor es decir el valor de la propiedad a traves del return
#Por otro lado el metodo set siempre recibe parametros para cambiar o modificar el valor del atributo o propiedad en cuestion

    def getVelocidad(self):
        return self._velocidad 

    def setVelocidad(self,velocidad):
        self._velocidad=velocidad

    def getMarca(self):
        return self._marca 

    def setMarca(self,marca):
        self._marca=marca

    def getColor(self):
        return self._color 

    def setColor(self,color):
        self._color=color

    def getModelo(self):
        return self._modelo 

    def setModelo(self,modelo):
        self._modelo=modelo

    def getCaballaje(self):
        return self._caballaje 

    def setCaballaje(self,caballaje):
        self._caballaje=caballaje

    def getPlazas(self):
        return self._plazas 

    def setPlazas(self,plazas):
        self._plazas=plazas

coche1=Coches("VW", "Blanco", "2022", 220, 150, 5)
coche2=Coches("Nissan", "Azul", "2020", 180, 150, 6)

coche1.acelerar()
coche1.acelerar()

#print(coche1.__velocidad)

#coche1.__velocidad=400
#print(coche1.__velocidad)

print(coche1.getVelocidad())
coche1.setVelocidad(400)
print(coche1.getVelocidad())

class Camiones(Coches):
    def __init__(self,marca,color,modelo,velocidad,potencia,asientos,eje,capacidadCarga):
        super().__init__(marca,color,modelo,velocidad,potencia,asientos)
        self.__eje=eje
        self.__capacidadCarga=capacidadCarga




    def cargar(self,tipo_carga):
        print(f"El tipo de carga es: {tipo_carga}")

    def acelerar(self):
            self.__velocidad += 1   
            print(f"Estoy acelerando como un camion")
    
    def frenar(self):
            self.__velocidad -= 1
            print(f"Estoy frenando como un camion")

    def gateje(self):
        return self.__eje

    def seteje(self,eje):
        self.__eje=eje

    def getCapacidadCarga(self):
        return self.__capacidadCarga

    def setCapacidadCarga(self,capacidadCarga):
        self.__capacidadCarga=capacidadCarga

class Camionetas(Coches):
    def __init__(self,marca,color,modelo,velocidad,potencia,asientos,traccion,cerrada):
        super().__init__(marca,color,modelo,velocidad,potencia,asientos,)
        self.__traccion=traccion
        self.__cerrada=cerrada

    def transporte(self,num_pasajero):
        print(f"El numero de pasajeros en la camioneta es: {num_pasajero}")

    def acelerar(self):
                    self.__velocidad += 1   
                    print(f"Estoy acelerando como un camioneta")
            
    def frenar(self):
                    self.__velocidad -= 1
                    print(f"Estoy frenando como un camioneta")

    def setTraccion(self,traccion):
         self.__traccion=traccion

    def getTraccion(self):
         return self.__traccion
    
    def setCerrada(self,cerrada):
         self.__cerrada=cerrada

    def getCerrada(self):
         return self.__cerrada


