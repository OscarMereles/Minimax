import random,os,time,copy    #se importan librerias para random, os para limpiar la consola y time para generar tiempos de espera

def generar_tablero(x_de_tablero,y_de_tablero,tablero,obstaculos,coord_raton,coord_gato,coord_queso,coord_salida):#funcion que crea la matriz en la lista tablero
    for i in range(x_de_tablero):       #desde 0 a x nro de filas -1
        fila=[]                     # crea la lista vacia: fila
        for j in range(y_de_tablero):   #desde 0 a y nro de columnas -1
            if coord_raton!=[i,j] and coord_gato!=[i,j] and coord_queso!=[i,j] and coord_salida!=[i,j]:     #si las cordenadas del raton, el gato, el queso y la salida son distintas de la coordenada actual 
                if obstaculos==True:#si los obstaculos estan activados
                    aleatorio =random.randint(1,4) #guarda en aleatorio un valor al azar entre 1 y 3
                    if aleatorio==1:    #si el valor al azar es 1
                        fila.append("|⬛|")  #añade un obstaculo a la lista fila
                    else:       #sino
                        fila.append("|__|") #añade un espacio vacio a la lista fila
                else:       #si no estan activados los obstaculos
                    fila.append("|__|")     #añade un espacio vacio a la lista fila
            elif coord_raton==[i,j]:        #si la cordenada es igual a la del raton
                fila.append("|🐭|")         #añade un espacio con el raton a la lista fila
            elif coord_gato==[i,j]:         #si la coordenada es igual a la del gato
                fila.append("|🐱|")         #añade un espacio con el gato a la lista fila
            elif coord_queso==[i,j]:        #si la coordenada es igual a la del queso
                fila.append("|🧀|")         #añade un espacio con el queso a la lista fila
            elif coord_salida==[i,j]:       #si la coordenada es igual a la de la salida
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
    return max(abs(punto_a[0]-punto_b[0]),abs(punto_a[1]-punto_b[1]))        #retorna la distancia chebyshev:el mayor valor ya sea de la diferencia postiva de las coordenadas en x o en y

def movimiento_random(animal,coord,tablero):    #funcion experimental para generar movimientos aleatorios, recibe el animal que lo usa, su coordenada, y el tablero en el que trabaja
    if obtener_movimientos_validos(coord[0],coord[1],tablero)!= None:       #si puede obtener movimientos validos desde la coordenada actual
        tablero[coord[0]][coord[1]]="|__|"                      #limpia su posicion actual del tablero
        dirs=obtener_movimientos_validos(coord[0],coord[1],tablero)         #almacena en dirs la lista de listas de movimientos validos en la coordenada actual
        rand=random.randint(0,(len(dirs)-1))                                #almacena en rand un numero aleatorio desde 0 a la cantidad de elementos que tenga dirs -1
        tablero[dirs[rand][0]][dirs[rand][1]]=animal                        #en el tablero en la posicion aleatoria definida por rand de la lista dirs inserta al animal 
        return [dirs[rand]]                                                 #retorna la lista de lista con la coordenada aleatoria
    else:                                                                   #en caso que no haya movimientos disponibles desde esa coordenada 
        print("sin movimientos disponibles")                                #imprime mensaje de sin movimientos disponibles

def evaluar_raton(coord_raton, coord_queso, coord_gato, coord_salida, tablero):
    dist_gato = distancia_chebyshev(coord_raton, coord_gato)
    dist_queso = distancia_chebyshev(coord_raton, coord_queso)
    dist_salida = distancia_chebyshev(coord_raton, coord_salida)
    
    if tablero[coord_queso[0]][coord_queso[1]] == "|🧀|":
        return (dist_gato * 25) - (dist_queso * 5) - (dist_salida * 12)
    else:
        return (dist_gato * 25) - (dist_salida * 38)

def evaluar_gato(coord_gato, coord_raton, coord_queso, coord_salida, tablero):
    dist_raton = distancia_chebyshev(coord_gato, coord_raton)
    dist_queso = distancia_chebyshev(coord_gato, coord_queso)
    dist_salida = distancia_chebyshev(coord_gato, coord_salida)
    
    if tablero[coord_queso[0]][coord_queso[1]] == "|🧀|":
        return (dist_raton * 26) - (dist_queso * 8) - (dist_salida * 10)
    else:
        return (dist_raton * 26) - (dist_salida * 18)

def juego_terminado(coord_raton, coord_gato, coord_salida):
    if coord_gato==coord_raton:
        return True, "gato"
    if coord_raton== coord_salida:
        return True, "raton"
    return False, None

def minimax(tablero, coord_raton, coord_gato, coord_queso, coord_salida, profundidad, turno_raton):
    terminado, ganador = juego_terminado(coord_raton, coord_gato, coord_salida)
    
    if profundidad == 0 or terminado:
        if terminado and ganador == "gato":
            return -10000, None
        if terminado and ganador == "raton":
            return 10000, None
        if turno_raton:
            return evaluar_raton(coord_raton, coord_queso, coord_gato, coord_salida, tablero), None
        else:
            return evaluar_gato(coord_gato, coord_raton, coord_queso, coord_salida, tablero), None

    if turno_raton:
        mejor_puntaje = float('-inf')
        mejor_movimiento = None
        movimientos = obtener_movimientos_validos(coord_raton[0], coord_raton[1], tablero)

        for mov in movimientos:
            tablero_copia = copy.deepcopy(tablero)
            tablero_copia[coord_raton[0]][coord_raton[1]] = "|__|"
            tablero_copia[mov[0]][mov[1]] = "|🐭|"
            
            puntaje, _ = minimax(tablero_copia, mov, coord_gato, coord_queso, coord_salida, profundidad-1, False)
            
            if puntaje > mejor_puntaje:
                mejor_puntaje = puntaje
                mejor_movimiento = mov
            elif puntaje == mejor_puntaje and random.random() < 0.5:
                mejor_movimiento = mov

        return mejor_puntaje, mejor_movimiento

    else:
        mejor_puntaje = float('inf')
        mejor_movimiento = None
        movimientos = obtener_movimientos_validos(coord_gato[0], coord_gato[1], tablero)

        for mov in movimientos:
            tablero_copia = copy.deepcopy(tablero)
            tablero_copia[coord_gato[0]][coord_gato[1]] = "|__|"
            tablero_copia[mov[0]][mov[1]] = "|🐱|"
            
            puntaje, _ = minimax(tablero_copia, coord_raton, mov, coord_queso, coord_salida, profundidad-1, True)
            
            if puntaje < mejor_puntaje:
                mejor_puntaje = puntaje
                mejor_movimiento = mov
            elif puntaje == mejor_puntaje and random.random() < 0.5:
                mejor_movimiento = mov

        return mejor_puntaje, mejor_movimiento


tablero=[]          #se crea la lista quue va a guardar el tablero donde se desarrolla la partida
#x_de_tablero=random.randint(5,20)       #se define la cantidad de filas aleatoriamenten
#y_de_tablero=random.randint(5,20)       #se define la cantidad de columnas aleatoriamente

turno=0                             # se inicializa el contador de turnos
TURNO_MAX = 35                     # se define la constante de maxima cantidad de turnos
PROFUNDIDAD = 5
x_de_tablero=int(input("Ingrese alto de laberinto: "))
y_de_tablero=int(input("Ingrese ancho de laberinto: "))
coord_raton = [0, 0]
coord_gato = [x_de_tablero-1, y_de_tablero-1]
coord_queso = [x_de_tablero//2, y_de_tablero//2]
coord_salida = [0, y_de_tablero-1]

generar_tablero(x_de_tablero, y_de_tablero, tablero, True, coord_raton, coord_gato, coord_queso, coord_salida)
mostrar_tablero(x_de_tablero, y_de_tablero, tablero)

turno = 0

while turno < TURNO_MAX:
    _, mejor_mov_raton = minimax(tablero, coord_raton, coord_gato, coord_queso, coord_salida, PROFUNDIDAD, True)
    
    if mejor_mov_raton:
        tablero[coord_raton[0]][coord_raton[1]] = "|__|"
        tablero[mejor_mov_raton[0]][mejor_mov_raton[1]] = "|🐭|"
        coord_raton = mejor_mov_raton[:]

    _, mejor_mov_gato = minimax(tablero, coord_raton, coord_gato, coord_queso, coord_salida, PROFUNDIDAD, False)
    
    if mejor_mov_gato:
        tablero[coord_gato[0]][coord_gato[1]] = "|__|"
        tablero[mejor_mov_gato[0]][mejor_mov_gato[1]] = "|🐱|"
        coord_gato = mejor_mov_gato[:]

    mostrar_tablero(x_de_tablero, y_de_tablero, tablero)
    turno += 1

    terminado, ganador = juego_terminado(coord_raton, coord_gato, coord_salida)
    if terminado:
        if ganador == "gato":
            print("\n¡EL GATO ATRAPÓ AL RATÓN! 🐱")
        else:
            print("\n¡EL RATÓN ESCAPÓ POR LA SALIDA! 🐭")
        break
else:
    print(f"\n¡El ratón sobrevivió {turno} turnos! El gato no logró atraparlo.")

print(f"Juego terminado después de {turno} turnos.")