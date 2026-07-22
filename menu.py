def mostrar_menu():
    print("")
    print("========================================")
    print(" SIMULADOR DE TORNEO POR ELIMINACION")
    print("       ¿Quién ganará esta vez?")
    print("========================================")
    print("1. Ver participantes")
    print("2. Iniciar torneo")
    print("3. Ver historial de campeones")
    print("4. Salir")

    opcion = input("Elige una opcion: ")
    while opcion != "3" and opcion != "2" and opcion != "1" and opcion != "4":
        print("opcion invalida, intenta de nuevo")
        opcion = input("Elige una opcion: ")

    return int(opcion)


def pausar():
    input("\npresiona enter para continuar...")
