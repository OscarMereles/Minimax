import random,os,time    #se importan librerias para random y para limpiar la consola

tablero=[]          #se crea la lista quue va a guardar el tablero donde se desarrolla la partida
xtablero=random.randint(4,15)       #se define la cantidad de filas aleatoriamenten
ytablero=random.randint(4,15)       #se define la cantidad de columnas aleatoriamente
xtablero=20
ytablero=20
coord_raton=[0,0]                   #se define la coordenada inicial del raton
coord_gato=[xtablero-1,ytablero-1]  #se define la coordenada inicial del gato en el final del tablero
coord_queso=[xtablero//2,ytablero//2]   #se define la coordenada del queso aproximadamente a mitad del tablero
coord_salida=[0,ytablero-1]         #se define la salida del tablero en la esquina superior derecha del tablero
turno=0
TURNO_MAX = 200
def generar_tablero(xtablero,ytablero,tablero,obstaculos,coord_raton,coord_gato,coord_queso,coord_salida):#funcion que crea la matriz en la lista tablero
    for i in range(xtablero):
        fila=[]
        for j in range(ytablero):
            if coord_raton!=[i,j] and coord_gato!=[i,j] and coord_queso!=[i,j] and coord_salida!=[i,j]:
                if obstaculos==True:
                    aleatorio =random.randint(1,3)
                    if aleatorio==1:
                        #fila.append("|####|")
                        fila.append("|⬛|")
                    else:
                        #fila.append("|____|")
                        fila.append("|__|")
                else:
                    #fila.append("|____|")
                    fila.append("|__|")
            elif coord_raton==[i,j]:
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

def moviento_random(animal,coord,tablero):
    if obtener_movimientos_validos(coord[0],coord[1],tablero)!= None:
        tablero[coord[0]][coord[1]]="|__|"
        dirs=obtener_movimientos_validos(coord[0],coord[1],tablero)
        rand=random.randint(0,(len(dirs)-1))
        tablero[dirs[rand][0]][dirs[rand][1]]=animal
        return [dirs[rand]]
    else:
        print("sin movimientos disponibles")

generar_tablero(xtablero,ytablero,tablero,True,coord_raton,coord_gato,coord_queso,coord_salida)
mostrar_tablero(xtablero,ytablero,tablero)
print("\nMovimientos válidos desde la posición del ratón:")
print(obtener_movimientos_validos(coord_raton[0], coord_raton[1], tablero))
print("\nMovimientos válidos desde la posición del gato: ")
print(obtener_movimientos_validos(coord_gato[0], coord_gato[1], tablero))
while turno!=TURNO_MAX:
    time.sleep(0.00001)
    new_coord=moviento_random("|🐭|",coord_raton,tablero)
    coord_raton=new_coord[0]
    new_coord1=moviento_random("|🐱|",coord_gato,tablero)
    coord_gato=new_coord1[0]
    mostrar_tablero(xtablero,ytablero,tablero)
    print(coord_raton)
    print(coord_gato)
    turno+=1