#examen segundo parcial
print("Valdez Leal Angel Adrian-1350-3W")
print(" ")

#Lista de las materias correspondidas
materias = ["Matemáticas", "Ecosistemas", "Ingles", "programacion", "Lenguaje"]

#Crear una lista para las materias que el usuario tiene que repetir
materias_repetir = []

#aqui se le preguntara al alumno pr las calificaiones de las materias
for materias in materias:
    try:
        nota = float(input(f"Introduce la nota de {materias}: "))
        if nota < 6:
            materias_repetir.append(materias)
    except ValueError: #se debera poner una calificacion valida para evitar error
        print("introduce una nota válida") #en caso de que salga error se debera introducir otra calificacion

#aqui se mostraran las materias que se tienen que repetir
if materias_repetir:
    print("materias que tienes que repetir:")
    for materias in materias_repetir:
        print(materias)

![image](https://github.com/user-attachments/assets/d19bdb8a-8e28-4033-a0d2-48041180cb22)
![image](https://github.com/user-attachments/assets/330e181d-618f-4538-9cf8-9f40fd0da7c9)
