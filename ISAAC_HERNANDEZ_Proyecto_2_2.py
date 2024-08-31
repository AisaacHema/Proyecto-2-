def identificar_cuadrante(x, y):
    """Función para identificar el cuadrante en el que se encuentra el punto (x, y)."""
    if x == 0 or y == 0:
        return "Las coordenadas no deben ser cero."
    elif x > 0 and y > 0:
        return "El punto está en el primer cuadrante."
    elif x < 0 and y > 0:
        return "El punto está en el segundo cuadrante."
    elif x < 0 and y < 0:
        return "El punto está en el tercer cuadrante."
    elif x > 0 and y < 0:
        return "El punto está en el cuarto cuadrante."

def dibujar_plano_cartesiano(x, y):
    """Función para dibujar una representación simple del plano cartesiano con el punto."""
    # Crear una cuadrícula básica de 21x21
    grid_size = 21
    grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]
    
    # Ejes
    for i in range(grid_size):
        grid[grid_size // 2][i] = '-'
        grid[i][grid_size // 2] = '|'
    
    # Centro
    grid[grid_size // 2][grid_size // 2] = '+'
    
    # Coordenadas (ajustar a la cuadrícula)
    cx = grid_size // 2 + int(x)
    cy = grid_size // 2 - int(y)
    
    if 0 <= cx < grid_size and 0 <= cy < grid_size:
        grid[cy][cx] = 'X'
    
    # Mostrar la cuadrícula
    for row in grid:
        print(''.join(row))

def main():
    try:
        # Solicitar al usuario que ingrese las coordenadas
        x = float(input("Ingresa la coordenada x: "))
        y = float(input("Ingresa la coordenada y: "))

        # Identificar el cuadrante
        resultado = identificar_cuadrante(x, y)
        print(resultado)
        
        if "Las coordenadas no deben ser cero." not in resultado:
            # Dibujar el plano cartesiano y el punto
            dibujar_plano_cartesiano(x, y)

    except ValueError:
        print("Por favor, ingresa valores numéricos válidos.")

# Llamar a la función principal
main()
