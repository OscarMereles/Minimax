import random,os,time    #se importan librerias para random, os para limpiar la consola y time para generar tiempos de espera
tablero=[]          #se crea la lista quue va a guardar el tablero donde se desarrolla la partida
x_de_tablero=random.randint(5,20)       #se define la cantidad de filas aleatoriamenten
y_de_tablero=random.randint(5,20)       #se define la cantidad de columnas aleatoriamente
coord_raton=[0,0]                   #se define la coordenada inicial del raton
coord_gato=[x_de_tablero-1,y_de_tablero-1]  #se define la coordenada inicial del gato en el final del tablero
coord_queso=[x_de_tablero//2,y_de_tablero//2]   #se define la coordenada del queso aproximadamente a mitad del tablero
coord_salida=[0,y_de_tablero-1]         #se define la salida del tablero en la esquina superior derecha del tablero
turno=0                             # se inicializa el contador de turnos
TURNO_MAX = 200                     # se define la constante de maxima cantidad de turnos

def generar_tablero(x_de_tablero,y_de_tablero,tablero,obstaculos,coord_raton,coord_gato,coord_queso,coord_salida):#funcion que crea la matriz en la lista tablero
    for i in range(x_de_tablero):       #desde 0 a x nro de filas -1
        fila=[]                     # crea la lista vacia: fila
        for j in range(y_de_tablero):   #desde 0 a y nro de columnas -1
            if coord_raton!=[i,j] and coord_gato!=[i,j] and coord_queso!=[i,j] and coord_salida!=[i,j]:     #si las cordenadas del raton, el gato, el queso y la salida son distintas de la coordenada actual 
                if obstaculos==True:#si los obstaculos estan activados
                    aleatorio =random.randint(1,4) #guarda en aleatorio un valor al azar entre 1 y 3
                    if aleatorio==1:    #si el valor al azar es 1
                        #fila.append("|####|")
                        fila.append("|⬛|")  #añade un obstaculo a la lista fila
                    else:       #sino
                        #fila.append("|____|")
                        fila.append("|__|") #añade un espacio vacio a la lista fila
                else:       #si no estan activados los obstaculos
                    #fila.append("|____|")
                    fila.append("|__|")     #añade un espacio vacio a la lista fila
            elif coord_raton==[i,j]:        #si la cordenada es igual a la del raton
                #fila.append("|ᘛ⁐̤ᕐᐷ|")
                fila.append("|🐭|")         #añade un espacio con el raton a la lista fila
            elif coord_gato==[i,j]:         #si la coordenada es igual a la del gato
                #fila.append("|ᓚᘏᗢ |")
                fila.append("|🐱|")         #añade un espacio con el gato a la lista fila
            elif coord_queso==[i,j]:        #si la coordenada es igual a la del queso
                #fila.append("|⪩. .|")
                fila.append("|🧀|")         #añade un espacio con el queso a la lista fila
            elif coord_salida==[i,j]:       #si la coordenada es igual a la de la salida
                #fila.append("|exit|")
                fila.append("|🚪|")         #añade un espacio con la salida a la lista fila
        tablero.append(fila)            #al terminar los condicionales añade la lista fila a la lista tablero

def mostrar_tablero(x_de_tablero,y_de_tablero,tablero): #funcion que muestra el tablero
    os.system('cls')    #limpia la consola
    cadena=""   #crea un variabler cadena vacia
    for x in range(x_de_tablero):   #desde 0 hasta la cantidad de filas-1
        for y in range(y_de_tablero):   #desde 0 hasta la cantidad de columnas-1
            cadena=cadena + tablero[x][y]   #se concatena con la cadena el elemento del tablero en el indice actual
        print(cadena)   #al finalizar la fila se imprime la fila completa
        cadena=""   #se vuelve a limpiar la cadena para la proxima fila
        
def validar_movimiento(x, y, tablero):      #funcion de validacion de movimientos, recibe coordenadas en x y en y, ademas del tablero con el que trabaja
    #return 0 <= x < len(tablero) and 0 <= y < len(tablero[0]) and tablero[x][y] != "|####|"
    return 0 <= x < len(tablero) and 0 <= y < len(tablero[0]) and tablero[x][y] != "|⬛|"    #si se da que las coordenadas estan dentro del tablero y la coordenada no tiene un obstaculo es verdadero el retorno

def obtener_movimientos_validos(x, y, tablero):     #funcion que obtiene movimientos validos desde una coordenada, recibe coordenadas en x y en y, ademas del tablero con el que trabaja
    movimientos=[]      #se crea la lista vacia de las coordenadas de los movimientos validos 
    direcciones=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]     #se define una lista de tuplas de los movimientos posibles en 8 direcciones
    for i in range(len(direcciones)):       #desde 0 a la cantidad de direcciones (8) -1
        nueva_x=x+direcciones[i][0]         #se suma la coordenada x de las variaciones del movimiento a la coordenada actual obteniendo una nueva coordenada x
        nueva_y=y+direcciones[i][1]         #se suma la coordenada y de las variaciones del movimiento a la coordenada actual obteniendo una nueva coordenada y
        if validar_movimiento(nueva_x,nueva_y,tablero):     #se valida si esa posicion en x e y es valida en el tablero
            movimientos.append([nueva_x,nueva_y])           #en caso de ser valido se añade ese par de coordenadas a la lista de listas de movimientos validos
    return movimientos      #se retorna la lista del listas de movimientos validos

def distancia_chebyshev(punto_a,punto_b):       #se define la funcion que mide la distancia adaptada para movimiento en diagonales, horizontales y verticales
    distancia=max(abs(punto_a[0]-punto_b[0]),abs(punto_a[1]-punto_b[1]))    #almacena en la variable distancia el mayor valor ya sea de la diferencia postiva de las coordenadas en x o en y
    return distancia        #retorna la distancia chebyshev

def movimiento_random(animal,coord,tablero):    #funcion experimental para generar movimientos aleatorios, recibe el animal que lo usa, su coordenada, y el tablero en el que trabaja
    if obtener_movimientos_validos(coord[0],coord[1],tablero)!= None:       #si puede obtener movimientos validos desde la coordenada actual
        tablero[coord[0]][coord[1]]="|__|"                      #limpia su posicion actual del tablero
        dirs=obtener_movimientos_validos(coord[0],coord[1],tablero)         #almacena en dirs la lista de listas de movimientos validos en la coordenada actual
        rand=random.randint(0,(len(dirs)-1))                                #almacena en rand un numero aleatorio desde 0 a la cantidad de elementos que tenga dirs -1
        tablero[dirs[rand][0]][dirs[rand][1]]=animal                        #en el tablero en la posicion aleatoria definida por rand de la lista dirs inserta al animal 
        return [dirs[rand]]                                                 #retorna la lista de lista con la coordenada aleatoria
    else:                                                                   #en caso que no haya movimientos disponibles desde esa coordenada 
        print("sin movimientos disponibles")                                #imprime mensaje de sin movimientos disponibles

def evaluar_raton(coord_raton,coord_queso, coord_gato, coord_salida,tablero):
    distancia_gato= distancia_chebyshev(coord_gato,coord_raton)
    distancia_queso=distancia_chebyshev(coord_queso,coord_raton)
    distancia_salida=distancia_chebyshev(coord_salida,coord_raton)
    if tablero[coord_queso[0]][coord_queso[1]]=="|🧀|":
        puntaje=(distancia_gato*2)-(distancia_queso*1000)-(distancia_salida*10)
    else:
        puntaje=(distancia_gato*2)-(distancia_salida*10)
    return puntaje

def evaluar_gato(coord_gato, coord_raton,coord_queso,coord_salida):
    distancia_raton=distancia_chebyshev(coord_raton,coord_gato)
    distancia_queso=distancia_chebyshev(coord_gato,coord_queso)
    distancia_salida=distancia_chebyshev(coord_salida,coord_gato)
    puntaje=-distancia_raton*100#-distancia_queso-distancia_salida
    return puntaje

def juego_terminado(coord_raton, coord_gato, coord_salida):
    if coord_gato==coord_raton:
        return True
    if coord_raton== coord_salida:
        return True
    return False

def minimax(tablero, coord_raton, coord_gato, coord_queso, coord_salida,profundidad, turno_raton):
    if profundidad==0 or juego_terminado(coord_raton,coord_gato,coord_salida): #condicion de parada 
        if turno_raton:
            return evaluar_raton(coord_raton,coord_queso,coord_gato,coord_salida,tablero), None
        else:
            return evaluar_gato(coord_gato,coord_raton,coord_queso,coord_salida), None
        
    mejor_movimiento = None

    if turno_raton:#condicion de recursividad para raton
        mejor_puntaje=float('-inf')
        for movi in obtener_movimientos_validos(coord_raton[0],coord_raton[1],tablero):
            posicion = [movi[0],movi[1]]
            puntaje, _=minimax(tablero,posicion,coord_gato,coord_queso,coord_salida,profundidad-1,False)
            if puntaje>mejor_puntaje:
                mejor_puntaje=puntaje
                mejor_movimiento=movi
        return mejor_puntaje,mejor_movimiento
    else:
        mejor_puntaje=float('inf')
        for movi in obtener_movimientos_validos(coord_gato[0],coord_gato[1],tablero):
            posicion=[movi[0],movi[1]]
            puntaje,_=minimax(tablero,coord_raton,posicion,coord_queso,coord_salida,profundidad-1,True)
            if puntaje<mejor_puntaje:
                mejor_puntaje=puntaje
                mejor_movimiento=movi
        return mejor_puntaje,mejor_movimiento
    
# ====================== BUCLE PRINCIPAL CON DEBUG ======================
generar_tablero(x_de_tablero, y_de_tablero, tablero, True, coord_raton, coord_gato, coord_queso, coord_salida)
mostrar_tablero(x_de_tablero, y_de_tablero, tablero)
profundidad = 5
while turno < TURNO_MAX:
    time.sleep(1.0)

    print(f"\n--- Turno {turno + 1} ---")

    # Turno del Ratón
    puntaje_r, mejor_mov_raton = minimax(tablero, coord_raton, coord_gato, coord_queso, coord_salida, profundidad, True)
    print(f"Ratón - Puntaje: {puntaje_r} | Movimiento: {mejor_mov_raton}")

    if mejor_mov_raton:
        nx = mejor_mov_raton[0]
        ny = mejor_mov_raton[1]
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
        nx = mejor_mov_gato[0]
        ny = mejor_mov_gato[1]
        tablero[coord_gato[0]][coord_gato[1]] = "|__|"
        tablero[nx][ny] = "|🐱|"
        coord_gato = [nx, ny]
        print(f"   Gato se movió a {coord_gato}")
    else:
        print("   Gato: NO se pudo mover (None)")

    mostrar_tablero(x_de_tablero, y_de_tablero, tablero)
    print(distancia_chebyshev(coord_raton,coord_queso))
    turno += 1

    if juego_terminado(coord_raton, coord_gato, coord_salida):
        if coord_gato == coord_raton:
            print("¡El gato atrapó al ratón!")
        else:
            print("¡El ratón escapó por la salida!")
        break