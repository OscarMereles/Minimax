import random, time, math
from display import mapa,crear_matriz,imprimir_mapa

x=10
y=10
cord_libre=[]
cord_obts=[]
celda_spawn_raton=[]
celda_spawn_queso=[]
distancia_raton_queso=0
distancia_a_gato=int(0.7*(x+y)/2)
distancia_de_plantado=int(distancia_a_gato/2)

def visualizar_mapa():
    espacio_libre=0
    cant_obst=0
    ancho_mapa=len(mapa)
    alto_mapa=len(mapa[0])
    for i in range(ancho_mapa):
        for j in range(alto_mapa):
            if mapa[i][j]=="|__|":
                espacio_libre+=1
                cord_libre.append([i,j])
            elif mapa[i][j]=="|⬛|":
                cant_obst+=1
                cord_obts.append([i,j])
    #print("libres",cord_libre)
    #print("obstaculos",cord_obts)

def spawn_mickey(libres,celda_spawn_raton):
    aleatorio=random.randint(0,len(libres)-1)
    celda_spawn_raton=libres[aleatorio]
    mapa[celda_spawn_raton[0]][celda_spawn_raton[1]]="|🐭|"
    return celda_spawn_raton
def plantar_queso(libres,celda_spawn_queso,):
    aleatorio=random.randint(0,len(libres)-1)
    celda_spawn_queso=libres[aleatorio]
    mapa[celda_spawn_queso[0]][celda_spawn_queso[1]]="|🧀|"
    return celda_spawn_queso

def medir_distancia():
    distanciax=abs((celda_spawn_raton[0]-celda_spawn_queso[0]))
    distanciay=abs((celda_spawn_raton[1]-celda_spawn_queso[1]))
    if distanciax>=distanciay:
        distancia_raton_queso=distanciax
    else:
        distancia_raton_queso=distanciay
    #print("distancia raton-queso: ",distancia_raton_queso," pasos")

crear_matriz(x,y,True,mapa)
visualizar_mapa()
imprimir_mapa(x,y,mapa)
celda_spawn_raton=spawn_mickey(cord_libre,celda_spawn_raton)
#time.sleep(10)
imprimir_mapa(x,y,mapa)
visualizar_mapa()
#time.sleep(10)
celda_spawn_queso = plantar_queso(cord_libre,celda_spawn_queso)
imprimir_mapa(x,y,mapa)
#print("Coordenada del queso: ",celda_spawn_queso)
#print("Coordenada del raton: ",celda_spawn_raton)
#print("Distancia al gato ",distancia_a_gato)
medir_distancia()