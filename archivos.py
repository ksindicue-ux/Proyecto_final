RUTA_PARTICIPANTES = 'participantes.txt'
RUTA_CAMPEONES = 'campeones.txt'


def leer_participantes(ruta_archivo=RUTA_PARTICIPANTES):
    lista = []
    try:
        archivo = open(ruta_archivo, 'r')
        for linea in archivo:
            nombre = linea.strip()
            if nombre != '':
                lista.append(nombre)
        archivo.close()
    except FileNotFoundError:
        print("No existe el archivo participantes.txt")
    return lista



def guardar_campeon(nombre_campeon, ruta_archivo=RUTA_CAMPEONES):
    archivo = open(ruta_archivo, 'a')
    archivo.write(nombre_campeon + '\n')

    archivo.close()



def leer_historial(ruta_archivo=RUTA_CAMPEONES):
    lista = []
    try:
        archivo = open(ruta_archivo, 'r')
        for linea in archivo:
            linea = linea.strip()
            if linea != '':
                lista.append(linea)
        archivo.close()
    except FileNotFoundError:
        pass

    return lista