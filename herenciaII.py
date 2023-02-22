class Persona: #Clase Padre
    #Atributos
    def __init__(self, nombre, apellido): #Constructor
        self.nombre = nombre
        self.apellido = apellido
    #Métodos
    def saludar(self):
        return f'Soy {self.nombre} {self.apellido}'

class Profesor(Persona):
    def __init__(self,nombre, apellido, edad, carrera):
        super().__init__(nombre, apellido)
        self.edad = edad
        self.carrera = carrera
    
    #Método
    def saludarProfe(self):
        return f'Soy el profesor {self.nombre} {self.apellido} tengo {self.edad} años y soy de la carrera de{self.carrera}'


class Estudiante(Profesor):
    def __init__(self,nombre, apellido, edad, carrera, sexo, matricula, turno):
        super().__init__(nombre, apellido, edad, carrera,)
        self.sexo = sexo
        self.matricula = matricula
        self.turno = turno
    def saludarEstudiante(self):
        return f'Soy el estudiante {self.nombre} {self.apellido} tengo {self.edad} años y soy de la carrera de {self.carrera}, {self.sexo}, {self.matricula}, {self.turno}'


pipsVazquez = Persona("Pips", "Vazquez")
print(pipsVazquez.saludar())

print("------------------------------------")
profePips = Profesor("Pips", "Vazquez", 15, "Electronica")
print(profePips.saludarProfe())

print("------------------------------------")
profePips = Estudiante("Pips", "Vazquez", 15, "Electronica", "Masculino", "A01064269", "Mixto")
print(profePips.saludarEstudiante())
