# juego de piedra papel o tijeras

rondas = 1
ganadas_maximas = 3
ganadas_jugador1 = 0
ganadas_jugador2 = 0

while True:
    
    print("[1] piedra")
    print("[2] papel")
    print("[3] tijeras")

    jugador1 = int(input("Elige una opcion (jugador 1): "))
    jugador2 = int(input("Elige una opcion (jugador 2): "))

    # situaciones de victoria
    if jugador1 == 1 and jugador2 == 3:
        print("Gano el jugador 1")
        ganadas_jugador1 += 1

    elif jugador2 == 1 and jugador1 == 3:
        print("Gano el jugador 2")
        ganadas_jugador1 += 1

    elif jugador1 == 2 and jugador2 == 1:
        print("Gano el jugador 1")
        ganadas_jugador1 += 1

    elif jugador2 == 2 and jugador1 == 1:
        print("Gano el jugador 2")
        ganadas_jugador2 += 1

    elif jugador1 == 3 and jugador2 == 2:
        print("Gano el jugador 1")
        ganadas_jugador1 += 1

    elif jugador2 == 3 and jugador1 == 2:
        print("Gano el jugador 2")
        ganadas_jugador2 += 1

    # empates
    elif jugador1 == 1 and jugador2 == 1:
        print("Empate")

    elif jugador1 == 2 and jugador2 == 2:
        print("Empate")

    elif jugador1 == 3 and jugador2 == 3:
        print("Empate")

    rondas += 1

    if ganadas_maximas == ganadas_jugador1:
        print("Ganador: jugador 1")
        break

    if ganadas_maximas == ganadas_jugador2:
        print("Ganador: jugador 2")
        break

print(f"rondas jugadas: {rondas}")
