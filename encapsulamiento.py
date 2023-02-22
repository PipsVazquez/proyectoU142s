class Vehiculos:
    #Atributos
    #marca, modelo, año, color, numeroSerie
    def __init__(self, marca, modelo, anio, color, numeroSerie, tipoMotor):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.color = color
        self.__numeroSerie = numeroSerie #Encapsular
        self.__tipoMotor = tipoMotor

    def avanzar(self):
        print("Estoy Avanzando")
    def frenando(self):
        print("Estoy frenando")
    def semaforo(self):
        print("Estoy en un semaforo")
    def presentar(self):
        print(f"El carro {self.modelo} de la marca {self.marca} y año {self.anio} es {self.color}, con numero de serie {self.__numeroSerie} y tipo de motor es {self.__tipoMotor}")
    def getNumeroSerie(self):
        print(self.__numeroSerie)
    
    def __verificarTenencia(self):
        if self.anio >= 2010:
            return True
        else:
            return False

    def costoTenencia(self):
        if self.__verificarTenencia():
           return 1000*1.5 
        else:
            return "No paga tenencia"

carroPips = Vehiculos("Toyota", "Corolla", 2021, "Blanco", "X0001", "Gasolina")
carroPips.presentar()
print('-------------------------')
#print(carroPips.numeroSerie)
#print(carroPips.verificarTenencia())
print("El costo de la tenencia del carro es: ",carroPips.costoTenencia())


