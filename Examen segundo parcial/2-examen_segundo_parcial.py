#2-Examen segundo parcial
print("Valdez Leal Angel Adrian-1350-3W")
print(" ")

#aqui se creara un diccionario con asignaturas y sus creditos
asignaturas_creditos = {
    'Matematicas': 7,
    'programacion': 5,
    'Español': 6
}

#total de creditos
total_creditos = 0

#aqui se mostraran los creditos de las asignaturas
for asignatura, creditos in asignaturas_creditos.items():
    print(f"{asignatura} tiene {creditos} creditos")
    total_creditos += creditos  #se sumaran los créditos

#aqui se mostrara el total de créditos del curso
print(f"Numero total de creditos del curso es: {total_creditos}")
