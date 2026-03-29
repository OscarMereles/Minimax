import random,os    #se importan librerias para random y para limpiar la consola
tablero=[]          #se crea la lista quue va a guardar el tablero donde se desarrolla la partida
xtablero=10       #se define la
ytablero=random.randint(4,15)
coord_raton=[0,0]
coord_gato=[xtablero-1,ytablero-1]
coord_queso=[xtablero//2,ytablero//2]
coord_salida=[0,ytablero-1]

def generar_tablero(xtablero,ytablero,tablero,obstaculos,coord_raton,coord_gato,coord_queso,coord_salida):
    
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

def distancia_chebyshev(punto_a,punto_b):
    distancia=max(abs(punto_a[0]-punto_b[0]),abs(punto_a[1]-punto_b[1]))
    return distancia

generar_tablero(xtablero,ytablero,tablero,True,coord_raton,coord_gato,coord_queso,coord_salida)
mostrar_tablero(xtablero,ytablero,tablero)