import time
import random

def crear_tablero(tamano: int, show=True):
    ''' 
    Función para crear un tablero de tamaño tamano x tamano
    y mostrarlo en la consola.
    '''
    # Inicializar el tablero vacío
    tablero = []

    '''
    Procedemos a rellenar el tablero con - indicando agua por explorar.
    Para ello nos servimos de un bucle for anidado, con el cual,
    sirviéndonos del tamano definido en un range, recorremos n filas
    y columnas con el icono de agua.
    '''
    for i in range(tamano):
        fila = []
        for j in range(tamano):
            fila.append("🟦")
        tablero.append(fila)

    # Imprimir el tablero
    if show == True:
        for fila in tablero:    
            print(" ".join(fila))

    return tablero
# Crear e imprimir el tablero de 10x10
#crear_tablero(10)

def colocar_barco(barco, tablero, show=True, pos=True):
    '''
    Función para colocar un barco en el tablero.
    barco: lista de tuplas que representan las coordenadas del barco
    tablero: la matriz del tablero
    print: dependiendo de la iteración, nos devuelve el tablero o no,
    esto se implementa en el caso de utilizar esta función en un bucle.
    '''
    if pos == True:
        for coordenada in barco:
            x, y = coordenada
            tablero[x][y] = "⚓"
    if show == True:
        for fila in tablero:
            print(" ".join(fila))

    return

def disparar(casilla:tuple, tablero:list, show=True):
    for x,y in casilla:
        if tablero[x][y] == "⚓":
            tablero[x][y] = "💥"
            acierto = True
        else:
            tablero[x][y] = "🌊"
            acierto = False
    
    if show == True:
        for fila in tablero:
            print(" ".join(fila))
    
    return acierto

coor_ut = []  # Coordenadas utilizadas

def crear_barcos(n):

    '''
    Para crear barcos de n posiciones en el tablero (eslora), 
    generaremos un set de coordenadas para evitar duplicidades,
    también definiremos los posibles movimientos en el tablero
    (vertical->arriba y abajo-, horizontal->izquierda y derecha.)
    y generaremos un contador de intentos limitado a 100 para evitar
    que el bucle while que crea barcos pueda entrar en una ejecución
    infinita.
    '''
    coor_ut = []  # Coordenadas utilizadas
    direc = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Direcciones: derecha, abajo, izquierda, arriba
    max_intentos = 100  # Máximo número de intentos para colocar un barco
    intentos = 0  # Contador de intentos

    while intentos < max_intentos:
        x, y = random.randint(0, 9), random.randint(0, 9)  # Coordenada de inicio aleatoria
        new_direc = random.choice(direc)  # Dirección aleatoria

        coor = set()  # Conjunto de coordenadas del barco
        coor.add((x, y))  # Añadimos la coordenada inicial
        
        # Intentamos construir el barco en una dirección
        for _ in range(n - 1):
            x, y = x + new_direc[0], y + new_direc[1]
            # Verificamos si la nueva coordenada es válida (en el tablero y no ocupada)
            if not (0 <= x < 10 and 0 <= y < 10 and (x, y) not in coor and (x, y) not in coor_ut):
                break  # Si no es válida, rompemos el bucle
            coor.add((x, y))  # Si es válida, la añadimos al conjunto de coordenadas

        # Si hemos añadido n coordenadas, tenemos un barco válido
        if len(coor) == n:
            # Añadimos las coordenadas a las coordenadas utilizadas
            if not any(abs(x1 - x2) < 2 and abs(y1 - y2) < 2 for (x1, y1) in coor for (x2, y2) in coor_ut):
                ''' 
                Este condiconal se asegura de que se cumple al menos una (any) de las cláusulas que le presentamos 
                en cada bucle for anidado, en el que comprueba si en cada movimiento horizontal o vertical guarda
                margen con el barco anterior, y si lo guarda que no esté dentro de las coordenadas utilizadas.
                '''
                coor_ut.extend(list(coor))
                return list(coor)

        # Si no se pudo generar un barco válido, incrementamos el contador de intentos
        intentos += 1

        # Intentamos con una dirección diferente si la actual no fue exitosa
        # Primero probamos con una dirección aleatoria que sea distinta de la actual
        direc_restante = [d for d in direc if d != new_direc]
        if direc_restante:
            new_direc = random.choice(direc_restante)
   
    # Si no se pudo generar el barco después de los intentos, devolvemos None
    #coor_ut = [] # Al finalizar la iteración limpiamos la lista para el siguiente jugador. (Importante cuando integramos en un bucle for)
    return None

def turno_jugador(tablero_rival, tablero_oculto, contador, disparos_jugador):
    while True:
        print("Introduce las coordenadas y dispara")
        x = int(input("Introduce coordenada y (vertical): "))
        y = int(input("y ahora coordenada x (horizontal): "))
        if (x, y) in disparos_jugador:
            print("Esas coordenadas ya las has dicho, prueba otras")
        else:
            print("¡FUEGO!")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            disparo = (x, y)
            disparos_jugador.add(disparo)
            acierto = disparar([disparo], tablero_oculto, show=False)
            if acierto:
                print('¡Tocado!')
                tablero_rival[x][y] = '💥'
                contador += 5
                print(contador)
                for fila in tablero_rival:
                    print(" ".join(fila))
                if contador >= 80:
                    print(""" **************************** ¡ENHORABUENA!¡FLOTA HUNDIDA! **************************** """)
                    return tablero_rival, contador, True  # El jugador gana si llega a 80
            else:
                tablero_rival[x][y] = '🌊'
                print('¡Agua!')
                print(contador)
                break  # Si falla, se sale del bucle y cambia el turno
                
    for fila in tablero_rival:
       print(" ".join(fila))  
    
    return tablero_rival, contador, False  # Si falló, se cambia el turno

def turno_cpu(tablero_rival, disparos_realizados, contador_pc):
    while True:
        x, y = random.randint(0, len(tablero_rival)-1), random.randint(0, len(tablero_rival[0])-1)
        if (x, y) in disparos_realizados:
            continue
        print(f"CPU dispara a {x}, {y}")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        disparo_cpu = (x, y)
        disparos_realizados.add(disparo_cpu)
        acierto = disparar([disparo_cpu], tablero_rival)
        if acierto:
            print('CPU ha acertado!')
            contador_pc += 5
            print(contador_pc)
            if contador_pc >= 80:
                print(""" **************************** ¡UY!¡TU FLOTA SE HA HUNDIDO! **************************** """)
                return contador_pc, True  # La CPU gana si llega a 80
        else:
            print('CPU ha fallado!')
            print(contador_pc)
            break  # Si falla, se sale del bucle y cambia el turno

    return contador_pc, False  # Si falló, se cambia el turno

def play(tablero, tablero_pc, tablero_oculto, contador, contador_pc, disparos_realizados_jugador, disparos_realizados_cpu):
    # Turno del jugador
    tablero_pc, contador, juego_terminado = turno_jugador(tablero_pc, tablero_oculto, contador, disparos_realizados_jugador)
    if juego_terminado:
        return  # Detener el juego si el jugador ha ganado

    # Turno de la CPU
    contador_pc, juego_terminado = turno_cpu(tablero, disparos_realizados_cpu, contador_pc)
    if juego_terminado:
        return  # Detener el juego si la CPU ha ganado

    # Llamada recursiva para el siguiente turno si no se ha ganado
    play(tablero, tablero_pc, tablero_oculto, contador, contador_pc, disparos_realizados_jugador, disparos_realizados_cpu)