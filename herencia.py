class Cazador: #Clase Padre
    #Atributos / propiedades
    def __init__(self, nombre, rango, espada):
        self.nombre = nombre
        self.rango = rango
        self.espada = espada

    #Métodos
    def presentar(self):
        print(f'Mi nombre es {self.nombre}, tengo el rango de {self.rango} y mi espada es {self.espada}')

class Pilar(Cazador): #Clase Hijo
    def __init__(self,nombre, rango, espada, respiracion, posturas):
        super().__init__(nombre, rango, espada) #Traer los atributos de la superclase
        self.respiracion = respiracion
        self.posturas = posturas

rangoBajo = Cazador("Tanjiro", "Mizunoto", "Negra")#Instanciar
rangoBajo.presentar()
print("-----------------------------")
himejima  = Pilar("Himejima", "Pilar", "Bola de picos y Hacha", "Respiracion de la Roca", 5)
himejima.presentar()
print(f'La respiración es {himejima.respiracion} y su número son {himejima.posturas}')
