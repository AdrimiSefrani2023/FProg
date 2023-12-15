import random

def imprimir_tablero(tablero):
    for fila in tablero:
        print(" | ".join(fila))
        print("-" * 5)

def verificar_ganador(tablero):
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != ' ':
            return tablero[i][0]
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != ' ':
            return tablero[0][i]

    if tablero[0][0] == tablero[1][1] == tablero[2][2] != ' ':
        return tablero[0][0]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != ' ':
        return tablero[0][2]

    return None

def jugar_michi():
    tablero = [[' ' for _ in range(3)] for _ in range(3)]
    
    jugador1 = input("Ingrese el nombre del Jugador 1 (X): ")
    jugador2 = input("Ingrese el nombre del Jugador 2 (O): ")
    
    jugadores = {'X': jugador1, 'O': jugador2}
    jugador_actual = random.choice(['X', 'O'])

    while True:
        imprimir_tablero(tablero)

        fila = int(input(f"{jugadores[jugador_actual]}, elige la fila (0, 1, 2): "))
        columna = int(input(f"{jugadores[jugador_actual]}, elige la columna (0, 1, 2): "))

        if tablero[fila][columna] == ' ':
            tablero[fila][columna] = jugador_actual
        else:
            print("¡Esa casilla ya está ocupada! Intenta de nuevo.")
            continue

        ganador = verificar_ganador(tablero)

        if ganador:
            imprimir_tablero(tablero)
            print(f"¡{jugadores[ganador]} ha ganado!")
            break

        if all(tablero[i][j] != ' ' for i in range(3) for j in range(3)):
            imprimir_tablero(tablero)
            print("¡Empate!")
            break

        jugador_actual = 'O' if jugador_actual == 'X' else 'X'

if __name__ == "__main__":
    jugar_michi()
