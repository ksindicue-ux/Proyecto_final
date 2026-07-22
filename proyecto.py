import random
def cargar_participantes():

    participantes = []

    try:
        with open("participantes.txt", "r") as archivo:

            for linea in archivo:

                nombre = linea.strip()

                if nombre != "":
                    participantes.append(nombre)

        print("\nParticipantes cargados correctamente.\n")

    except FileNotFoundError:

        print("\nNo existe el archivo participantes.txt\n")

    return participantes

def mostrar_participantes(participantes):

    if len(participantes) == 0:

        print("\nNo hay participantes cargados.\n")
        return

    print("\n===== PARTICIPANTES =====")

    for i, participante in enumerate(participantes, start=1):

        print(f"{i}. {participante}")

    print()


def generar_enfrentamientos(participantes):

    jugadores = participantes.copy()

    random.shuffle(jugadores)

    enfrentamientos = []

    for i in range(0, len(jugadores), 2):

        enfrentamientos.append([jugadores[i], jugadores[i + 1]])

    return enfrentamientos

def guardar_historial(campeon):

    with open("historial.txt", "a") as archivo:

        archivo.write(f"Campeón: {campeon}\n")

def es_potencia_de_dos(n):

    if n <= 0:
        return False

    while n % 2 == 0:
        n = n // 2

    return n == 1

def simular_torneo(participantes):

    if len(participantes) == 1:

        print("\n================================")
        print("CAMPEÓN DEL TORNEO")
        print(participantes[0])
        print("================================\n")

        guardar_historial(participantes[0])

        return participantes[0]

    enfrentamientos = generar_enfrentamientos(participantes)

    ganadores = []

    print("\n===== ENFRENTAMIENTOS =====")

    for duelo in enfrentamientos:

        print(duelo[0], "VS", duelo[1])

    print("\n===== RESULTADOS =====")

    for duelo in enfrentamientos:

        ganador = random.choice(duelo)

        print(duelo[0], "VS", duelo[1], "-> Gana", ganador)

        ganadores.append(ganador)

    if len(participantes) % 2 != 0:

        ultimo = participantes[-1]

        print("\n", ultimo, "pasa automáticamente a la siguiente ronda.\n")

        ganadores.append(ultimo)

    return simular_torneo(ganadores)

participantes = []
while True:

    print("===================================")
    print("     SIMULADOR DE TORNEOS")
    print("===================================")
    print("1. Cargar participantes")
    print("2. Mostrar participantes")
    print("3. Simular torneo")
    print("4. Ver historial")
    print("5. Salir")

    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":

        participantes = cargar_participantes()

    elif opcion == "2":

        mostrar_participantes(participantes)

    elif opcion == "3":

        if len(participantes) == 0:

            print("\nPrimero cargue los participantes.\n")
        elif not es_potencia_de_dos(len(participantes)):
            print("\nEl número de participantes no es una potencia de 2.\n")
        else:
            simular_torneo(participantes)

    elif opcion == "4":

        try:

            archivo = open("historial.txt", "r")

            print("\n===== HISTORIAL DE CAMPEONES =====\n")

            contenido = archivo.readlines()

            if len(contenido) == 0:

                print("Todavía no hay campeones registrados.")

            else:

                contador = 1

                for linea in contenido:

                    print(contador, "-", linea.strip())

                    contador += 1

            archivo.close()

            print()

        except FileNotFoundError:

            print("\nTodavía no existe el historial.\n")

    elif opcion == "5":

        print("\nGracias por utilizar el programa.")

        break

    else:

        print("\nOpción inválida.\n")

