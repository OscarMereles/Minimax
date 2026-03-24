import random
filas=[]

def jugar(dimensionx,dimensiony,obstaculo,filas):
    for i in range(0,dimensionx,1):
        if obstaculo==True:
            aleatorio=random.randint(1,5)
            columna=[]
            if aleatorio ==3:
                columna.append("|⚫|")
            else:
                columna.append("|  |")
        else:
            columna.append("|  |")
    filas.append(columna)
    print(columna,i)
    for x in range(dimensionx):
        print(filas[x])

jugar(4,3,True,filas)