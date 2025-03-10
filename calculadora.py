# calculadora simple en python

def pedir_numeros():
    x = float(input("X: "))
    y = float(input("Y: "))
    return x,y

suma = lambda x,y: x + y
resta = lambda x,y: x - y
multi = lambda x,y: x * y
div = lambda x,y: x / y

while True:

    print("[1] suma")
    print("[2] resta")
    print("[3] multiplicacion")
    print("[4] divicion")
    print("[5] salir")
    opcion = int(input("Opcion: "))

    x,y = pedir_numeros()

    if opcion == 1: print(suma(x,y))

    elif opcion == 2: print(resta(x,y))

    elif opcion == 3: print(multi(x,y))

    elif opcion == 4: print(div(x,y))

    elif opcion == 5: break

    else: print("Error")
