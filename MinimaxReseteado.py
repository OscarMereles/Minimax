import random,os
tablero=[]
xtablero=10
ytablero=10
coord_raton=[0,0]
coord_gato=[xtablero-1,ytablero-1]
coord_queso=[xtablero//2,xtablero//2]
coord_salida=[0,ytablero-1]
def generar_tablero(xtablero,ytablero,tablero,obstaculos,coord_raton,coord_gato,coord_queso,coord_salida):
    
    for i in range(xtablero):
        fila=[]
        for j in range(ytablero):
            if coord_raton!=[i,j] and coord_gato!=[i,j] and coord_queso!=[i,j] and coord_salida!=[i,j]:
                if obstaculos==True:
                    aleatorio =random.randint(1,4)
                    if aleatorio==1:
                        fila.append("|####|")
                    else:
                        fila.append("|____|")
                else:
                    fila.append("|____|")
            elif coord_raton==[i,j]:
                fila.append("|ᘛ⁐̤ᕐᐷ|")
            elif coord_gato==[i,j]:
                fila.append("|ᓚᘏᗢ |")
            elif coord_queso==[i,j]:
                fila.append("|⪩. .|")
            elif coord_salida==[i,j]:
                fila.append("|exit|")
        tablero.append(fila)


def mostrar_tablero(xtablero,ytablero,tablero):
    os.system('cls')
    cadena=""
    for x in range(xtablero):
        for y in range(ytablero):
            cadena=cadena + tablero[x][y]
        print(cadena)
        cadena=""
        
def validar_movimiento(x,y,tablero):
    return tablero[x][y]!="|####|"

generar_tablero(xtablero,ytablero,tablero,True,coord_raton,coord_gato,coord_queso,coord_salida)
mostrar_tablero(xtablero,ytablero,tablero)
print(validar_movimiento(1,0,tablero))
