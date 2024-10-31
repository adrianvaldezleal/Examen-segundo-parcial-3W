#4-Examen segundo parcial
print("Valdez Leal Angel Adrian-1350-3W")
print(" ")

#aqui se creara un diccionario donde se almacenen los datos del alumno
alumno = {}

#aqui se le preguntara al alumno su informacion personal
alumno['nombre'] = input("Ingresa tu nombre: ") #nombre
alumno['edad'] = input("Ingresa tu edad: ") #edad
alumno['direccion'] = input("ingresa tu direccion: ") #direccion
alumno['telefono'] = input("Igresa tu numero de telefono: ") #numero de telefono

#aqui se va a imprimir las informacion ingresada por el alumno
print(f"{alumno['nombre']} tiene {alumno['edad']} años vive en {alumno['direccion']} y su numero de telefono es {alumno['telefono']}")
