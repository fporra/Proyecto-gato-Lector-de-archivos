import random  # movimiento aleatorio de la IA

# imprimir el tablero del juego
def print_tablero(tablero):
    linea1 = '| {} | {} | {} |'.format(tablero[0], tablero[1], tablero[2])
    linea2 = '| {} | {} | {} |'.format(tablero[3], tablero[4], tablero[5])
    linea3 = '| {} | {} | {} |'.format(tablero[6], tablero[7], tablero[8])

    print()
    print(linea1)
    print(linea2)
    print(linea3)
    print()

# movimiento del jugador
def movimiento_jugador(icon, tablero):
    if icon == 'X':
        number = 1
    elif icon == 'O':
        number = 2

    print("Turno del jugador {}".format(number))

    while True:
        try:
            eleccion = int(input("Coloca la coordenada de movimiento (1-9): ").strip())  # Jugador selecciona movimiento
            if 1 <= eleccion <= 9 and tablero[eleccion - 1] == ' ': 
                break
            else:
                print("Por favor, selecciona una casilla válida.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

    tablero[eleccion - 1] = icon

# movimiento de la IA
def movimiento_IA(tablero):
    return random.choice([i for i, c in enumerate(tablero) if c == ' ']) + 1  # recorre el tablero asta que encuentre un espacio vacio y se le suma una para que empiese en la casilla n1 

# verificar si hay victoria
def es_victoria(icon, tablero):
    return (
        (tablero[0] == icon and tablero[1] == icon and tablero[2] == icon) or
        (tablero[3] == icon and tablero[4] == icon and tablero[5] == icon) or
        (tablero[6] == icon and tablero[7] == icon and tablero[8] == icon) or
        (tablero[0] == icon and tablero[3] == icon and tablero[6] == icon) or
        (tablero[1] == icon and tablero[4] == icon and tablero[7] == icon) or
        (tablero[2] == icon and tablero[5] == icon and tablero[8] == icon) or
        (tablero[0] == icon and tablero[4] == icon and tablero[8] == icon) or
        (tablero[2] == icon and tablero[4] == icon and tablero[6] == icon)
    )

# Menú principal del juego
while True:
    print("Menu de Gato:")
    print("1. Player vs IA")
    print("2. Player vs Player")
    print("3. Salir")

    opc = input("Seleccione una opción (1-3): ")

    if opc == "1":  # Jugador contra IA
        tablero = [' ' for _ in range(9)]  # Crea un tablero vacio
        while True:
            print_tablero(tablero)  # Imprime el tablero actual
            movimiento_jugador('X', tablero)  # Movimiento del jugador humano
            print_tablero(tablero)
            if es_victoria('X', tablero):  # Verifica si el jugador humano ha ganado
                print("¡Jugador gana! ¡Felicidades!")
                break
            elif ' ' not in tablero:  # Verifica si hay un empate
                print("¡Es un empate!")
                break
            movimiento = movimiento_IA(tablero)  # Movimiento de la IA
            tablero[movimiento - 1] = 'O'
            if es_victoria('O', tablero):  # Verifica si la IA ha ganado
                print_tablero(tablero)
                print("¡La IA gana! ¡Felicidades!")
                break

    elif opc == "2":  # Jugador contra Jugador
        tablero = [' ' for _ in range(9)]  # Crea un tablero vacio
        while True:
            print_tablero(tablero)  # Imprime el tablero actual
            movimiento_jugador('X', tablero)  # Movimiento del jugador 1
            print_tablero(tablero)
            if es_victoria('X', tablero):  # Verifica si el jugador 1 ha ganado
                print("¡Jugador 1 gana! ¡Felicidades!")
                break
            elif ' ' not in tablero:  # Verifica si hay un empate
                print("¡Es un empate!")
                break
            movimiento_jugador('O', tablero)  # Movimiento del jugador 2
            print_tablero(tablero)
            if es_victoria('O', tablero):  # Verifica si el jugador 2 ha ganado
                print("¡Jugador 2 gana! ¡Felicidades!")
                break

    elif opc == "3":  # Salir del programa
        print("Saliendo del programa...")
        break

    else:  # Opcion invalida
        print("Opción inválida. Por favor, seleccione una opción válida.")
