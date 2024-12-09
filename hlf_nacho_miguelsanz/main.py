from utils import *

'''
El gameplay consta de un sistema de turnos, en el que tras dar la bienvenida se crean los tableros.
Una vez se crean los tableros se colocan los barcos de ambos jugadores, Player 1 tendrá la opción de seleccionar la posición manualmente,
pero para ajustarnos al tiempo de presentación, se crearán de forma aleatoria como para la CPU.

Se dará a P1 la opción de elegir cara o cruz, y se sorte el incio del juego.

En su turno, cada jugador disparará a una coordenada, mientras acierte podrá seguir disparando, pero en el momento que falle pasará su turno.

El juego acabará cuando uno de los jugadores destruya todos los barcos ("⚓") del tablero rival.
'''
import time
print("¡Hola Grumete! Prepara la artillería, que empieza el juego...")

print("Puede que los nervios te traicionen, pero respira hondo mientras se crean las zonas de combate")
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print("Tablero Jugador 1")
tablero_p1 = crear_tablero(10)
print("Tablero CPU")
tablero_oculto = crear_tablero(10) # El tablero sobre el que ataque P1, sirve de control para el avance del juego.
tablero_cpu_show = crear_tablero(10, show=False) # El tablero de ayuda de P1, no muestra posiciones pero si se da agua o barcos acertados.
barcos_partida = (2,2,2,3,3,4)

ask1_p1 = input("Lo primero que debemos hacer es preparar la estrategia, ¿quieres encargarte de ello o delegar en el Almirante Random? ").lower()
if "deleg" in ask1_p1:
    print("De acuerdo el Almirante Random colocará tus barcos")
    posiciones_p1 = []
    coor_ut = []
    for eslora in barcos_partida:
        posiciones_p1.append(crear_barcos(eslora))
    for posicion in posiciones_p1:
        colocar_barco(posicion, tablero_p1, show=False)
    print("Tablero Jugador 1")
    for fila in tablero_p1:    
        print(" ".join(fila))
else: # esto podría hacerse con un bucle while, mientras barcos a crear != 0 pedir al usuario meter coordenadas para ese barco
    print("De acuerdo Grumete, confía en tu formación y crea una lista de n tuplas con la posición de cada barco. \nRecuerda, n es igual al tamaño de eslora de cada barco,teniendo que crear 3 barcos de tamaño 2, 2 barcos de 3 posiciones y un barco de tamaño 4.\n Las coordenadas van de -0,0 a 9,9-")
    time.sleep(1)
    print("Empecemos por los barcos pequeños, recuerda que necesitamos 3")
    barco2_1_x = int(input("Dime la primera posición X para el primer barco de eslora = 2:"))
    barco2_1_y = int(input("Dime la primera posición y para el primer barco de eslora = 2:"))
    barco2_1_x2 = int(input("Dime la segunda posición X para el primer barco de eslora = 2:"))
    barco2_1_y2 = int(input("Dime la segunda posición y para el primer barco de eslora = 2:"))
    barco2_p1_1 = [(barco2_1_x, barco2_1_y),(barco2_1_x2, barco2_1_y2)]
    barco2_2_x = int(input("Dime la primera posición X para el segundo barco de eslora = 2:"))
    barco2_2_y = int(input("Dime la primera posición y para el segundo barco de eslora = 2:"))
    barco2_2_x2 = int(input("Dime la segunda posición X para el segundo barco de eslora = 2:"))
    barco2_2_y2 = int(input("Dime la segunda posición y para el segundo barco de eslora = 2:"))
    barco2_p1_2 = [(barco2_2_x, barco2_2_y),(barco2_2_x2, barco2_2_y2)]
    barco2_3_x = int(input("Dime la primera posición X para el tercer barco de eslora = 2:"))
    barco2_3_y = int(input("Dime la primera posición y para el tercer barco de eslora = 2:"))
    barco2_3_x2 = int(input("Dime la segunda posición X para el tercer barco de eslora = 2:"))
    barco2_3_y2 = int(input("Dime la segunda posición y para el tercer barco de eslora = 2:"))   
    barco2_p1_3 = [(barco2_3_x, barco2_3_y),(barco2_3_x2, barco2_3_y2)]
    barcos2_p1 = [barco2_p1_1, barco2_p1_2, barco2_p1_3]
    print("Vamos a colocar los Barcos de tamaño 2...")
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print("Colocando")
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    for posicion in barcos2_p1:
        colocar_barco(posicion, tablero_p1, show=False)
    print("Tablero Jugador 1")
    for fila in tablero_p1:    
        print(" ".join(fila))
    
    print("Sigamos por los barcos medianos, recuerda que necesitamos 2")
    barco3_1_x = int(input("Dime la primera posición X para el primer barco de eslora = 3:"))
    barco3_1_y = int(input("Dime la primera posición y para el primer barco de eslora = 3:"))
    barco3_1_x2 = int(input("Dime la segunda posición X para el primer barco de eslora = 3:"))
    barco3_1_y2 = int(input("Dime la segunda posición y para el primer barco de eslora = 3:"))
    barco3_1_x3 = int(input("Dime la tercera posición X para el primer barco de eslora = 3:"))
    barco3_1_y3 = int(input("Dime la tercera posición y para el primer barco de eslora = 3:"))
    barco3_p1_1 = [(barco3_1_x, barco3_1_y),(barco3_1_x2, barco3_1_y2), (barco3_1_x3, barco3_1_y3)]
    barco3_2_x = int(input("Dime la primera posición X para el segundo barco de eslora = 3:"))
    barco3_2_y = int(input("Dime la primera posición y para el segundo barco de eslora = 3:"))
    barco3_2_x2 = int(input("Dime la segunda posición X para el segundo barco de eslora = 3:"))
    barco3_2_y2 = int(input("Dime la segunda posición y para el segundo barco de eslora = 3:"))
    barco3_2_x3 = int(input("Dime la tercera posición X para el primer barco de eslora = 3:"))
    barco3_2_y3 = int(input("Dime la tercera posición y para el primer barco de eslora = 3:"))
    barco3_p1_2 = [(barco3_2_x, barco3_2_y),(barco3_2_x2, barco3_2_y2), (barco3_2_x3, barco3_2_y3)]
    barcos3_p1 = [barco3_p1_1,barco3_p1_2]

    print("Vamos a colocar los Barcos de tamaño 3...")
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print("Colocando")
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    for posicion in barcos3_p1:
        colocar_barco(posicion, tablero_p1, show=False)
    print("Tablero Jugador 1")
    for fila in tablero_p1:    
        print(" ".join(fila))

    print("Solo nos queda el barco de tamaño 4, vamos con él")
    barco4_1_x = int(input("Dime la primera posición X para el barco de eslora = 4:"))
    barco4_1_y = int(input("Dime la primera posición y para el barco de eslora = 4:"))
    barco4_1_x2 = int(input("Dime la segunda posición X para el barco de eslora = 4:"))
    barco4_1_y2 = int(input("Dime la segunda posición y para el barco de eslora = 4:"))
    barco4_1_x3 = int(input("Dime la tercera posición X para el barco de eslora = 4:"))
    barco4_1_y3 = int(input("Dime la tercera posición y para el barco de eslora = 4:"))
    barco4_1_x4 = int(input("Dime la cuarta posición X para el barco de eslora = 4:"))
    barco4_1_y4 = int(input("Dime la cuarta posición y para el barco de eslora = 4:"))
    barco4_p1_1 = [(barco4_1_x, barco4_1_y),(barco4_1_x2, barco4_1_y2), (barco4_1_x3, barco4_1_y3), (barco4_1_x4, barco4_1_y4)]
    barcos4_p1 = [barco4_p1_1]

    print("coloquemos el último barco...")
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print("Colocando")
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    for posicion in barcos4_p1:
        colocar_barco(posicion, tablero_p1, show=False)
    print("Tablero Jugador 1")
    for fila in tablero_p1:    
        print(" ".join(fila))

print("Espera mientras el rival, posicina sus naves. Aprovecha para repasar la estrategia y arengar a la tripulación")
print(".")
time.sleep(0.5)
print(".")
time.sleep(0.5)
print(".")
time.sleep(0.5)
print("Colocando")
print(".")
time.sleep(0.5)
print(".")
time.sleep(0.5)
print(".")
time.sleep(0.5)
# Creamos los barcos y los posicionamos
barcos_partida_cpu = (2,2,2,3,3,4)
posiciones_cpu = []
coor_ut = []
for eslora in barcos_partida_cpu:
    posiciones_cpu.append(crear_barcos_cpu(eslora))
#posiciones_cpu = [item for item in posiciones_cpu if item is not None]
for posicion in posiciones_cpu:
    colocar_barco(posicion, tablero_oculto, show=False, pos=True)
for posicion in posiciones_cpu:
    colocar_barco(posicion, tablero_cpu_show, show=False, pos=False)
print("Tablero CPU")
for fila in tablero_cpu_show:    
    print(" ".join(fila))
print("Tablero CPU chuleta")
for fila in tablero_oculto:    
    print(" ".join(fila))
'''
# El incio de la partida se sortea, se da la oportunidad al P1 de elegir lado de la moneda, si acierta empezará
print("Vamos a sortear el inicio, por favor elige...")
moneda = [0,1]
moneda_p1 = input("¿Cara o Cruz?").lower()
if input("¿Cara o Cruz?").lower() == "cara":
    "y"
else:
    "n"
if moneda_p1 == random.choice(moneda):
    incia_p1 = "y"
else:
    inicia_p1 = "n"
'''
# Ponemos el contador a 0 para ir sumando según uno de los jugadores aciertan
contador = 0
contador_pc = 0
disparos_jugador = set()
disparos_realizados = set()

turno_jugador(tablero_cpu_show, tablero_oculto, contador, disparos_jugador)
turno_cpu(tablero_p1,disparos_realizados,contador_pc)
play(tablero_p1,tablero_cpu_show, tablero_oculto,contador,contador_pc, disparos_realizados, disparos_jugador)