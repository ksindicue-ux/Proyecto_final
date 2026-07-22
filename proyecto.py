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

def simular_torneo(participantes):

    if len(participantes) == 1:

        print("\n==============================")
        print("CAMPEÓN DEL TORNEO")
        print(participantes[0])
        print("==============================\n")

        guardar_historial(participantes[0])

        return participantes[0]

    enfrentamientos = generar_enfrentamientos(participantes)

    print("\n===== ENFRENTAMIENTOS =====")

    for i, duelo in enumerate(enfrentamientos, start=1):

        print(f"Partido {i}: {duelo[0]} VS {duelo[1]}")

    print()

    ganadores = []

    print("===== RESULTADOS =====")

    for duelo in enfrentamientos:

        ganador = random.choice(duelo)

        print(f"{duelo[0]} VS {duelo[1]} -> Gana {ganador}")

        ganadores.append(ganador)

    print()

    return simular_torneo(ganadores)

participantes = []

