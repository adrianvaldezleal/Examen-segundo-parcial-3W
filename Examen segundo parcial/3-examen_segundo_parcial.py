#3-Examen segundo parcial
print("Valdez Leal Angel Adrian-1350-3W")
print(" ")

#aqui se hara un programa donde se almacenen las asignaturas de un curso
asignaturas = ["Matematicas", "Ingles", "Programacion", "Ecosistemas", "Lenguaje"]

#aqui se almacenaran las notas de las asignaturas
notas = {}

#aqui se le preguntara al alumno pr las notas de las asignaturas
for asignaturas in asignaturas:
    try:
        nota = float(input(f"Introduce la nota de {asignaturas}: "))
        notas[asignaturas] = nota
    except ValueError:
        print("introduce una nota válida")
#aqui se mostrara las notas obtenidas de las asignaturas
print(" ")
for asignatura, nota in notas.items():
    print(f"En {asignatura} has sacado {nota}")

