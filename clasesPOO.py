
class TortugasNinja:
    #Atributos/Propiedades
    poderAtaque = 100
    poderDefensa = 90
    agilidad = 100
    puntosVida = 200
    vidas = 3
    velocidad = 300
    arma = " "
    #Métodos
    def ataque(self):
        print("Ataque")
    def  defensa(self):
        print("Defiendo")

#Objeto
donatello = TortugasNinja()
donatello.arma = "Bo"
print(f'El poder de ataque de Donatello es {donatello.poderAtaque} y su arma es {donatello.arma}')

miguelAngel = TortugasNinja()
miguelAngel.arma = "Nunchakus"
print(f'El poder de ataque de Miguel Angel es {miguelAngel.poderAtaque} y su arma es {miguelAngel.arma}')

enemigoCerca = input("¿Está Destructor cerca? ")


if enemigoCerca == "si":

    donatello.defensa()
    miguelAngel.ataque()


