import random, os, sys
mapa=[]

def crear_matriz(dimensionx,dimensiony,obstaculo,mapa):
    

    for i in range(dimensionx): #dibuja mapa desde una matriz con obstaculos opcionales
        fila=[]
        if obstaculo==True:  
            for j in range(dimensiony):
                aleatorio=random.randint(1,5)
                if aleatorio ==1:
                    fila.append("|⬛|")#obstaculo
                else:
                    fila.append("|__|")#celda vacia
        else:
            for j in range(dimensiony):
                fila.append("|__|")#celda vacia
        mapa.append(fila)

def imprimir_mapa(dimensionx,dimensiony,mapa):
    pantalla=""
    os.system('cls')
    for x in range(dimensionx):
        for y in range(dimensiony):
            pantalla=pantalla+mapa[x][y]    
        print(pantalla)
        pantalla=""

def prueba():
    os.system('cls')
    crear_matriz(10,10,True,mapa)
    imprimir_mapa(10,10,True,mapa)

#prueba()
#sys.exit("fin")