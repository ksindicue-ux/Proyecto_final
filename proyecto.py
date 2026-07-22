import random


def guardar_participantes(participantes):
    with open(participantes.txt, "r") as archivo:
        for participante in participantes:
            archivo.write(participante + "\n")

def registrar_participantes():

    participantes = []

    cantidad = int(input("Cantidad de participantes: "))

    for i in range(cantidad):
        nombre = input(f"Participante {i + 1}: ")
        participantes.append(nombre)




def mostrar_participantes(participantes):

    if len(participantes) == 0:
        print("\nNo hay participantes registrados.\n")
        return

    print("\n Participantes :")

    for i, participante in enumerate(participantes, start=1):
        print(f"{i}. {participante}")

    print()


#Se generan enfrentamientos de forma aleatoria

def generar_enfrentamientos(participantes):

    random.shuffle(participantes)

    enfrentamientos = []

    for i in range(0, len(participantes), 2):
        enfrentamientos.append(
            [participantes[i], participantes[i + 1]]
        )

    return enfrentamientos


def mostrar_llaves(enfrentamientos):

    print("\n Enfrentamientos")

    for i, duelo in enumerate(enfrentamientos, start=1):
        print(f"Partido {i}: {duelo[0]} VS {duelo[1]}")

    print()

# Se simula aletoriamente
def simular_ronda(enfrentamientos):

    ganadores = []

    print("\n Resultados")

    for duelo in enfrentamientos:

        ganador = random.choice(duelo)

        print(f"{duelo[0]} VS {duelo[1]} -> Gana: {ganador}")

        ganadores.append(ganador)

    print()

    return ganadores