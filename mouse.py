import random, time, math
from display import mapa
from display import crear_matriz
from display import imprimir_mapa

cord_libre=[]
cord_obts=[]
celda_spawn_raton=[]
celda_spawn_queso=[]
distancia_raton_queso=0
x=10
y=10

def visualizar_mapa():
    espacio_libre=0
    cant_obst=0
    ancho_mapa=len(mapa)
    #print("Ancho ",ancho_mapa)
    alto_mapa=len(mapa[0])
    #print("Alto ",alto_mapa)
    for i in range(ancho_mapa):
        for j in range(alto_mapa):
            if mapa[i][j]=="|__|":
                espacio_libre+=1
                cord_libre.append([i,j])
            elif mapa[i][j]=="|⬛|":
                cant_obst+=1
                cord_obts.append([i,j])
    print("libres",cord_libre)
    print("obstaculos",cord_obts)

def spawn_mickey(libres,celda_spawn_raton):
    aleatorio=random.randint(0,len(libres)-1)
    celda_spawn_raton=libres[aleatorio]
    #print(celda_spawn_raton)
    mapa[celda_spawn_raton[0]][celda_spawn_raton[1]]="|🐭|"
    return celda_spawn_raton

def plantar_queso(libres,celda_spawn_queso):
    aleatorio=random.randint(0,len(libres)-1)
    celda_spawn_queso=libres[aleatorio]
    #print(celda_spawn)
    mapa[celda_spawn_queso[0]][celda_spawn_queso[1]]="|🧀|"
    return celda_spawn_queso

def medir_distancia():
    distanciax=abs((celda_spawn_raton[0]-celda_spawn_queso[0]))
    distanciay=abs((celda_spawn_raton[1]-celda_spawn_queso[1]))
    if distanciax>=distanciay:
        distancia_raton_queso=distanciax
    else:
        distancia_raton_queso=distanciay
    print("distancia raton-queso: ",distancia_raton_queso)
    


crear_matriz(x,y,True,mapa)
visualizar_mapa()
imprimir_mapa(x,y,mapa)
celda_spawn_raton=spawn_mickey(cord_libre,celda_spawn_raton)
time.sleep(1)
imprimir_mapa(x,y,mapa)
visualizar_mapa()
time.sleep(1)
celda_spawn_queso = plantar_queso(cord_libre,celda_spawn_queso)
imprimir_mapa(x,y,mapa)
print(celda_spawn_queso)
print(celda_spawn_raton)
medir_distancia()
