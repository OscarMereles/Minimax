import random
mapa=[]

def matriz(dimensionx,dimensiony,obstaculo,mapa):
    pantalla=""
    for i in range(dimensionx): #dibuja mapa desde una matriz con obstaculos opcionales
        columna=[]
        if obstaculo==True:  
            for j in range(dimensiony):
                aleatorio=random.randint(1,5)
                if aleatorio ==3:
                    columna.append("|⬛|")#obstaculo
                else:
                    columna.append("|  |")#celda vacia
        else:
            for j in range(dimensiony):
                columna.append("|  |")#celda vacia
        mapa.append(columna)
    #print(columna,i)
    for x in range(dimensionx):
        for y in range(dimensiony):
            pantalla=pantalla+mapa[x][y]
        print(pantalla)
        pantalla=""


matriz(10,10,True,mapa)