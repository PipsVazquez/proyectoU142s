#HAcer una funcion que sume y calcule el promedio 
def calculoPromedio(calificacionesAlumnos):
    return sum(calificacionesAlumnos)/len(calificacionesAlumnos)

respuesta = "si"
calificacionesAlumnos = []

print(''' 
    Bienvenidos a todos
       _                     _       _           _             
   __ _ _ __| |_    __ _ _ __   __| |   __| | ___  ___(_) __ _ _ __  
  / _` | '__| __|  / _` | '_ \ / _` |  / _` |/ _ \/ __| |/ _` | '_ \ 
 | (_| | |  | |_  | (_| | | | | (_| | | (_| |  __/\__ \ | (_| | | | |
  \__,_|_|   \__|  \__,_|_| |_|\__,_|  \__,_|\___||___/_|\__, |_| |_|
                                                         |___/       


''')

while respuesta == "si":
    calificacionesAlumnos.append(int(input("Escribe la calificación del siguiente alumno: ")))

    respuesta = input("Escribe si para seguir añadiendo números: ")

print(calificacionesAlumnos)
promedio = calculoPromedio(calificacionesAlumnos)
print(promedio)



