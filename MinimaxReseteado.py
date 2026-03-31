import random,os,time    #se importan librerias para random y para limpiar la consola

tablero=[]          #se crea la lista quue va a guardar el tablero donde se desarrolla la partida
xtablero=random.randint(5,20)       #se define la cantidad de filas aleatoriamenten
ytablero=random.randint(5,20)       #se define la cantidad de columnas aleatoriamente
coord_raton=[0,0]                   #se define la coordenada inicial del raton
coord_gato=[xtablero-1,ytablero-1]  #se define la coordenada inicial del gato en el final del tablero
coord_queso=[xtablero//2,ytablero//2]   #se define la coordenada del queso aproximadamente a mitad del tablero
coord_salida=[0,ytablero-1]         #se define la salida del tablero en la esquina superior derecha del tablero
turno=0                             # se inicializa el contador de turnos
TURNO_MAX = 200                     # se define la constante de maxima cantidad de turnos

def generar_tablero(xtablero,ytablero,tablero,obstaculos,coord_raton,coord_gato,coord_queso,coord_salida):#funcion que crea la matriz en la lista tablero
    for i in range(xtablero):       #desde 0 a x nro de filas
        fila=[]                     # crea la lista vacia: fila
        for j in range(ytablero):   #desde 0 a y nro de columnas
            if coord_raton!=[i,j] and coord_gato!=[i,j] and coord_queso!=[i,j] and coord_salida!=[i,j]:     #si las cordenadas del raton, el gato, el queso y la salida son distintas de la coordenada actual 
                if obstaculos==True:#si los obstaculos estan activados
                    aleatorio =random.randint(1,3) #guarda en aleatorio un valor al azar entre 1 y 3
                    if aleatorio==1:    #si el valor al azar es 1
                        #fila.append("|####|")
                        fila.append("|⬛|")  #añade un obstaculo a la lista fila
                    else:       #sino
                        #fila.append("|____|")
                        fila.append("|__|") #añade un espacio vacio a la lista fila
                else:       #si no estan activados los obstaculos
                    #fila.append("|____|")
                    fila.append("|__|")     #añade un espacio vacio a la lista fila
            elif coord_raton==[i,j]:        #si la cordenada igual a la del raton
                #fila.append("|ᘛ⁐̤ᕐᐷ|")
                fila.append("|🐭|")
            elif coord_gato==[i,j]:
                #fila.append("|ᓚᘏᗢ |")
                fila.append("|🐱|")
            elif coord_queso==[i,j]:
                #fila.append("|⪩. .|")
                fila.append("|🧀|")
            elif coord_salida==[i,j]:
                #fila.append("|exit|")
                fila.append("|🚪|")
        tablero.append(fila)

def mostrar_tablero(xtablero,ytablero,tablero):
    os.system('cls')
    cadena=""
    for x in range(xtablero):
        for y in range(ytablero):
            cadena=cadena + tablero[x][y]
        print(cadena)
        cadena=""
        
def validar_movimiento(x, y, tablero):
    #return 0 <= x < len(tablero) and 0 <= y < len(tablero[0]) and tablero[x][y] != "|####|"
    return 0 <= x < len(tablero) and 0 <= y < len(tablero[0]) and tablero[x][y] != "|⬛|"

def obtener_movimientos_validos(x, y, tablero):
    movimientos=[]
    direcciones=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for i in range(len(direcciones)):
        nueva_x=x+direcciones[i][0]
        nueva_y=y+direcciones[i][1]
        if validar_movimiento(nueva_x,nueva_y,tablero):
            movimientos.append([nueva_x,nueva_y])
    return movimientos

def distancia_chebyshev(punto_a,punto_b):
    distancia=max(abs(punto_a[0]-punto_b[0]),abs(punto_a[1]-punto_b[1]))
    return distancia

def movimiento_random(animal,coord,tablero):
    if obtener_movimientos_validos(coord[0],coord[1],tablero)!= None:
        tablero[coord[0]][coord[1]]="|__|"
        dirs=obtener_movimientos_validos(coord[0],coord[1],tablero)
        rand=random.randint(0,(len(dirs)-1))
        tablero[dirs[rand][0]][dirs[rand][1]]=animal
        return [dirs[rand]]
    else:
        print("sin movimientos disponibles")

def evaluar_raton(coord_raton,coord_queso, coord_gato, coord_salida):
    distancia_gato= distancia_chebyshev(coord_gato,coord_raton)
    distancia_queso=distancia_chebyshev(coord_queso,coord_raton)
    distancia_salida=distancia_chebyshev(coord_salida,coord_raton)
    puntaje=(distancia_gato*10)-(distancia_queso*3)-(distancia_salida*5)
    return puntaje

def evaluar_gato(coord_gato, coord_raton):
    distancia_raton=distancia_chebyshev(coord_raton,coord_gato)
    puntaje=-distancia_raton
    return puntaje

def juego_terminado(coord_raton, coord_gato, coord_salida):
    if coord_gato==coord_raton:
        return True
    if coord_raton== coord_salida:
        return True
    return False

# def minimax(tablero, coord_raton, coord_gato, coord_queso, coord_salida,profundidad, turno_raton):
#     if profundidad==0 or juego_terminado(coord_raton,coord_gato,coord_salida):
#         if turno_raton:
#             return evaluar_raton(coord_raton,coord_queso,coord_gato,coord_salida), None
#         else:
#             return evaluar_gato(coord_gato,coord_raton), None
        
#     mejor_movimiento = None

#     if turno_raton:
#         mejor_puntaje=float('-inf')
#         for movi in obtener_movimientos_validos(coord_raton[0],coord_raton[1],tablero):
#             posicion = [coord_raton[0]+movi[0],coord_raton[1]+movi[1]]
#             puntaje, _=minimax(tablero,posicion,coord_gato,coord_queso,coord_salida,profundidad-1,False)
#             if puntaje>mejor_puntaje:
#                 mejor_puntaje=puntaje
#                 mejor_movimiento=movi
#         return mejor_puntaje,mejor_movimiento
#     else:
#         mejor_puntaje=float('inf')
#         for movi in obtener_movimientos_validos(coord_gato[0],coord_gato[1],tablero):
#             posicion=[coord_gato[0]+movi[0],coord_gato[1]+movi[1]]
#             puntaje,_=minimax(tablero,coord_raton,posicion,coord_queso,coord_salida,profundidad-1,True)
#             if puntaje<mejor_puntaje:
#                 mejor_puntaje=puntaje
#                 mejor_movimiento=movi
#         return mejor_puntaje,mejor_movimiento

def minimax(tablero, coord_raton, coord_gato, coord_queso, coord_salida, profundidad, es_turno_raton):
    
    # Condición de parada
    if profundidad == 0 or juego_terminado(coord_raton, coord_gato, coord_salida):
        if es_turno_raton:
            return evaluar_raton(coord_raton, coord_queso, coord_gato, coord_salida), None
        else:
            return evaluar_gato(coord_gato, coord_raton), None

    # Obtenemos los movimientos válidos del jugador actual
    if es_turno_raton:
        pos_actual = coord_raton
        es_maximizando = True
    else:
        pos_actual = coord_gato
        es_maximizando = False

    movimientos = obtener_movimientos_validos(pos_actual[0], pos_actual[1], tablero)
    
    if not movimientos:
        return 0, None   # Sin movimientos posibles

    mejor_movimiento = None
    mejor_puntaje = float('-inf') if es_maximizando else float('inf')

    for movi in movimientos:
        # Calculamos nueva posición
        nueva_x = pos_actual[0] + movi[0]
        nueva_y = pos_actual[1] + movi[1]
        nueva_pos = [nueva_x, nueva_y]

        # Llamada recursiva
        if es_turno_raton:
            puntaje, _ = minimax(tablero, nueva_pos, coord_gato, coord_queso, coord_salida, profundidad-1, False)
        else:
            puntaje, _ = minimax(tablero, coord_raton, nueva_pos, coord_queso, coord_salida, profundidad-1, True)

        # Actualizamos el mejor
        if es_maximizando:
            if puntaje > mejor_puntaje:
                mejor_puntaje = puntaje
                mejor_movimiento = movi
        else:
            if puntaje < mejor_puntaje:
                mejor_puntaje = puntaje
                mejor_movimiento = movi

    return mejor_puntaje, mejor_movimiento

#loop del juego
# ====================== BUCLE PRINCIPAL CON DEBUG ======================
generar_tablero(xtablero, ytablero, tablero, True, coord_raton, coord_gato, coord_queso, coord_salida)
mostrar_tablero(xtablero, ytablero, tablero)

profundidad = 4   # Bajamos a 4 para que sea más rápido y estable

while turno < TURNO_MAX:
    time.sleep(0.7)

    print(f"\n--- Turno {turno + 1} ---")

    # Turno del Ratón
    puntaje_r, mejor_mov_raton = minimax(tablero, coord_raton, coord_gato, coord_queso, coord_salida, profundidad, True)
    print(f"Ratón - Puntaje: {puntaje_r} | Movimiento: {mejor_mov_raton}")

    if mejor_mov_raton:
        nx = coord_raton[0] + mejor_mov_raton[0]
        ny = coord_raton[1] + mejor_mov_raton[1]
        tablero[coord_raton[0]][coord_raton[1]] = "|__|"
        tablero[nx][ny] = "|🐭|"
        coord_raton = [nx, ny]
        print(f"   Ratón se movió a {coord_raton}")
    else:
        print("   Ratón: NO se pudo mover (None)")

    # Turno del Gato
    puntaje_g, mejor_mov_gato = minimax(tablero, coord_raton, coord_gato, coord_queso, coord_salida, profundidad, False)
    print(f"Gato  - Puntaje: {puntaje_g} | Movimiento: {mejor_mov_gato}")

    if mejor_mov_gato:
        nx = coord_gato[0] + mejor_mov_gato[0]
        ny = coord_gato[1] + mejor_mov_gato[1]
        tablero[coord_gato[0]][coord_gato[1]] = "|__|"
        tablero[nx][ny] = "|🐱|"
        coord_gato = [nx, ny]
        print(f"   Gato se movió a {coord_gato}")
    else:
        print("   Gato: NO se pudo mover (None) ← ESTE ES EL PROBLEMA")

    mostrar_tablero(xtablero, ytablero, tablero)
    turno += 1

    if juego_terminado(coord_raton, coord_gato, coord_salida):
        if coord_gato == coord_raton:
            print("¡El gato atrapó al ratón!")
        else:
            print("¡El ratón escapó por la salida!")
        break