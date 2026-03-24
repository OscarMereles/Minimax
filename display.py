import random
filas=[]

def matriz(dimensionx,dimensiony,obstaculo,filas):
    for i in range(dimensionx):
        columna=[]
        if obstaculo==True:
            aleatorio=random.randint(1,5)
            for j in range(dimensiony):

                if aleatorio ==3:
                    columna.append("|⚫|")#obstaculo
                else:
                    columna.append("|  |")#celda vacia
        else:
            for j in range(dimensiony):
                columna.append("|  |")#celda vacia
                filas.append(columna)
    #print(columna,i)
    for x in range(dimensionx):
        print(filas[x])


matriz(4,3,False,filas)