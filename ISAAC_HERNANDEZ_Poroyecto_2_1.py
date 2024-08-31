# Función principal para validar la longitud de la palabra
def verificar_longitud():
    while True:
        # Solicitar al usuario que ingrese una palabra
        palabra = input("Ingresa una palabra: ")

        # Calcular la longitud de la palabra
        longitud = len(palabra)

        # Verificar la longitud de la palabra y mostrar el mensaje adecuado
        if 4 <= longitud <= 8:
            print("La palabra es correcta.")
            break  # Salir del bucle si la palabra es correcta
        elif longitud < 4:
            print(f"Hacen falta letras. Solo tiene {longitud} letras.")
        else:
            print(f"Sobran letras. Tiene {longitud} letras.")

# Llamar a la función principal
verificar_longitud()
