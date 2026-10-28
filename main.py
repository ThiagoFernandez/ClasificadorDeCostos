
datos = {
    "a": {
        "Es una inversion": "CapEx",
        "se paga mes a mes": "OpEx"
    },
    "b": {
        "Es compartido con otros proyectos": "Indirecto",
        "Es unico del proyecto": "Directo"
    },
    "c":{
        "Cambia con el volumen de produccion": "Variable",
        "No cambia con el volumen de produccion": "Fijo"
    }
}

respuestas = []

for categoria, opciones in datos.items():
    opciones_lista = list(opciones.items())
    print(f"\nCategoría {categoria}:")

    for indice, (pregunta, _) in enumerate(opciones_lista, start=1):
        print(f"{indice} - {pregunta}?")

    while True:
        try:
            seleccion = int(input("Selecciona una opcion: "))
            if 1 <= seleccion <= len(opciones_lista):
                respuestas.append(opciones_lista[seleccion - 1][1])
                break
            print("Opcion fuera de rango.")
        except ValueError:
            print("Introduce el número de una opcion.")

print("\nClasificacion:", ", ".join(respuestas))

    