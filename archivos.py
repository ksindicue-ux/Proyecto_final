RUTA_PARTICIPANTES = 'participantes.txt'
RUTA_CAMPEONES = 'campeones.txt'


def leer_participantes(ruta_archivo=RUTA_PARTICIPANTES):
    lista=[]

    archivo =open(ruta_archivo, 'r')

    for linea in archivo:
        linea= linea.strip()
        if linea== '':
            continue

        datos = linea.split(',')
        nombre = datos[0].strip()

        if nombre == 'Nombre':
            continue
        lista.append(nombre)

    archivo.close()
    return lista


