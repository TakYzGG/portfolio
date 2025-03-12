# Ahorcado en python

from random import randint
from os import system

def mostrar_persona(fase):
    if fase == 1:
        print(" ", r"_" * 12)
        print(r" |", " " * 10, r"|")
        print(r" |", " " * 10, r"|")
        print(r" |")
        print(r" |")
        print(r" |")
        print(r" |")
        print(r" |")
        print(r" |")
        print("---")

    if fase == 2:
        print(" ", r"_" * 12)
        print(r" |", " " * 10, r"|")
        print(r" |", " " * 10, r"|")
        print(r" |", " " * 10, "O")
        print(r" |")
        print(r" |")
        print(r" |")
        print(r" |")
        print(r" |")
        print("---")

    if fase == 3:
        print(" ", r"_" * 12)
        print(r" |", " " * 10, r"|")
        print(r" |", " " * 10, r"|")
        print(r" |", " " * 10, "O")
        print(r" |", " " * 10, "|")
        print(r" |")
        print(r" |")
        print(r" |")
        print(r" |")
        print("---")

    if fase == 4:
        print(" ", r"_" * 12)
        print(r" |", " " * 10, r"|")
        print(r" |", " " * 10, r"|")
        print(r" |", " " * 10, "O")
        print(r" |", " " * 9, "/|")
        print(r" |")
        print(r" |")
        print(r" |")
        print(r" |")
        print("---")

    if fase == 5:
        print(" ", r"_" * 12)
        print(r" |", " " * 10, r"|")
        print(r" |", " " * 10, r"|")
        print(r" |", " " * 10, "O")
        print(r" |", " " * 9, "/|\\")
        print(r" |")
        print(r" |")
        print(r" |")
        print(r" |")
        print("---")

    if fase == 6:
        print(" ", r"_" * 12)
        print(r" |", " " * 10, r"|")
        print(r" |", " " * 10, r"|")
        print(r" |", " " * 10, "O")
        print(r" |", " " * 9, "/|\\")
        print(r" |", " " * 9, "/")
        print(r" |")
        print(r" |")
        print(r" |")
        print("---")

    if fase == 7:
        print(" ", r"_" * 12)
        print(r" |", " " * 10, r"|")
        print(r" |", " " * 10, r"|")
        print(r" |", " " * 10, "O")
        print(r" |", " " * 9, "/|\\")
        print(r" |", " " * 9, "/ \\")
        print(r" |")
        print(r" |")
        print(r" |")
        print("---")

def elegir_dificultad():
    system("clear")
    print("Elige la dificultad")
    print("[1] Facil (4-6 letras)")
    print("[2] Intermedio (6-8 letras)")
    print("[3] Dificil (+8 letreas)")
    print("[4] Sigma (solo para sigmas)")
    dificultad = int(input("Dificultad: "))

    if dificultad == 1: lista = dificultad_facil
    elif dificultad == 2: lista = dificultad_intermedia
    elif dificultad == 3: lista = dificultad_dificil
    elif dificultad == 4: lista = dificultad_sigma
    else: print("No es una opcion valida")

    return lista

def elegir_palabra(lista_palabras):
    x = randint(0, len(lista_palabras) -1)
    palabra = lista_palabras[x]
    return palabra

def mostrar_palabra(palabra):
    palabra_oculta = "-" * len(palabra)
    return palabra_oculta

def actualizar_palabra(palabra, palabra_oculta, letra):
    nuevo_estado = ""

    for i in range(len(palabra)):
        if palabra[i] == letra:
            # Si la letra adivinada está en la palabra, la mostramos
            nuevo_estado += letra
        else:
            # Si no, dejamos lo que ya estaba (guion o letra descubierta antes)
            nuevo_estado += palabra_oculta[i]

    return nuevo_estado

def pedir_letra():
    letra = input("Letra: ")
    return letra

# listas con las palabras segun su dificultad
dificultad_facil = [
    "gato",
    "perro",
    "sol",
    "luz",
    "flor",
    "casa",
    "pan",
    "lago",
    "sal",
    "vino",
    "fuego",
    "raton",
    "arbol",
    "llave",
    "plaza"
]

dificultad_intermedia = [
    "montaña",
    "caballo",
    "ventana",
    "librero",
    "murcielago",
    "pintura",
    "cuchillo",
    "espejo",
    "relojero",
    "cultura",
    "paraguas",
    "palmera",
    "frutilla",
    "cueva",
    "semilla"
]

dificultad_dificil = [
    "astronauta",
    "electricidad",
    "constitucion",
    "murcielago",
    "anticonstitucional",
    "biblioteca",
    "programador",
    "hipopotamo",
    "travesia",
    "melancolia",
    "subterraneo",
    "ornitorrinco",
    "psicologia",
    "desarrollador",
    "hidraulico"
]

dificultad_sigma = [
    "sigma",
    "mewing",
    "skibidi",
    "toilet",
    "hentai",
    "cepecito",
    "tetas",
    "culos",
    "pornhub",
    "xvideos"
]

verificacion = False

# bucle principal
while True:
    system("clear")
    print("<< Menu principal >>")
    print("[1] Elegir dificultad")
    print("[2] Jugar")
    print("[3] Salir")
    opcion = int(input("Opcion: "))

    if opcion == 1:
        dificultad_lista = elegir_dificultad()
        verificacion = True

    elif opcion == 2 and verificacion:
        
        fase = 1
        letras_usadas = []

        palabra = elegir_palabra(dificultad_lista)
        palabra_oculta = mostrar_palabra(palabra)

        while True:
            system("clear")
            mostrar_persona(fase)
            print()
            print(palabra_oculta)
            print(f"Letras usadas: {letras_usadas}")
            print()

            letra = pedir_letra()

            if len(letra) > 1:
                print("No puedes poner más de una letra down de mierda")
                input("Presiona ENTER para continuar")
                continue  # Vuelve a pedir una letra

            if letra in letras_usadas:
                print("Ya usaste esa letra. Intenta otra.")
                input("Presiona ENTER para continuar")
                continue  # Vuelve a pedir una letra

            # Si la letra no ha sido usada, la agregamos a la lista
            letras_usadas.append(letra)

            # Si la letra está en la palabra
            if letra in palabra:
                nueva_palabra_oculta = actualizar_palabra(palabra, palabra_oculta, letra)

                # Si no cambió, es porque ya estaba descubierta
                if nueva_palabra_oculta == palabra_oculta:
                    print(f"La letra '{letra}' ya estaba descubierta.")
                else:
                    palabra_oculta = nueva_palabra_oculta
                    print(f"¡Bien! La letra '{letra}' está en la palabra.")
            else:
                print(f"La letra '{letra}' no está en la palabra.")
                fase += 1

            input("Presiona ENTER para continuar")

            # Ganaste
            if palabra_oculta == palabra:
                print("\n¡Felicidades! Adivinaste la palabra:", palabra)
                input("Presiona ENTER para continuar")
                break

            # Perdiste
            if fase >= 7:
                system("clear")
                mostrar_persona(fase)
                print("\n¡Perdiste! La palabra era:", palabra)
                input("Presiona ENTER para continuar")
                break
        
    elif opcion == 3:
        print("Saliste del programa")
        break

    else:
        print("Opcion invalida")
        input("Presiona ENTER para continuar")
