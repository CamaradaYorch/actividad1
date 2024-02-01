# Algoritmo Actividad 1
def suma_pares_impares():
    lista_de_variables = []
    suma_pares = 0
    suma_impares = 0

    try:
        # Leer lista_de_variables
        input_str = input("Ingrese la lista de digitos (separados por espacio): ")
        lista_de_variables = list(map(int, input_str.split()))

        # Leer cada numero y sumar
        for digito in lista_de_variables:
            if digito % 2 == 0:
                suma_pares += digito
            else:
                suma_impares += digito

        # Mostrar resultados
        print('Suma de pares:', suma_pares)
        print('Suma de impares:', suma_impares)

    except ValueError:
        print("Error: Ingrese solo números.")

# Llamar a la función principal
suma_pares_impares()

