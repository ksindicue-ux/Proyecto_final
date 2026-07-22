def cargar_participantes():
    participantes = []

    with open("participantes.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            participantes.append(linea.strip())

    return participantes
def mostrar_torneo(participantes, llaves):

    print("\nParticipantes")

    for jugador in participantes:
        print(jugador)

    print("\nEnfrentamientos")

    for pareja in llaves:
        print(f"{pareja[0]} vs {pareja[1]}")
