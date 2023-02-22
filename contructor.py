'''
#Atributos/Propiedades
    poderAtaque = 100
    poderDefensa = 90
    agilidad = 100
    puntosVida = 200
    vidas = 3
    velocidad = 300
    arma = " "

'''

#Pilar Abstracción

class TortugasNinja:
    #Atributos / Propiedades
    #Constructor
    #Init nos permite inicializar los valores o propiedades
    def __init__(self, nombre, ataque, defensa, arma, puntosVida, vidas):
        self.nombre = nombre
        self.ataque = ataque
        self.defensa = defensa
        self.arma = arma
        self.puntosVida = puntosVida
        self.vidas = vidas

    #Métodos
    def ataque(self):
        print("Ataque")
    def  defensa(self):
        print("Defiendo")


donatello = TortugasNinja("Donatello", 100, 120, "Bo", 200, 3) #Instanciar 
print(f'{donatello.nombre} tiene {donatello.ataque} puntos de ataque y su arma es: {donatello.arma}')


tortugaMala = TortugasNinja("DonatelloMalo", 120, 100, "Metralladora", 300, 1)
print(f'{tortugaMala.nombre} tiene {tortugaMala.ataque} puntos de ataque y su arma es: {tortugaMala.arma}')


if donatello.ataque > tortugaMala.ataque:
    print("Gana Donatello")

else: 
    #donatello.vidas = donatello.vidas - 1
    donatello.vidas -= 1
    print(donatello.vidas)
