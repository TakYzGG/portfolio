# juego de adivinar el numero

from random import randint

MIN = 1
MAX = 10
intentos = 1

num = randint(MIN, MAX)

while True:
    user_num = int(input("Intenta adivinar el numero: "))

    if user_num < MIN or user_num > MAX:
        print(f"El numero no puede ser menor a {MIN} o mayor a {MAX}")
        continue

    elif user_num < num:
        print(f"El numero es mayor a {user_num}")

    elif user_num > num:
        print(f"El numero es menor a {user_num}")

    elif user_num == num:
        print("Ganaste!!!")
        break

    print()
    intentos += 1

print(f"Numero de intentos: {intentos}")
