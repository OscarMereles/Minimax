import random
from display import mapa, crear_matriz, imprimir_mapa
from mouse import celda_spawn_raton , celda_spawn_queso,cord_libre,cord_obts,distancia_a_gato,x,y


def spawn_michi(cord_libre,celda_spawn_raton,distancia_a_raton):
    dir_comp=[]
    dir_comp2=[]
    for i in range(len(cord_libre)-1):
        if (cord_libre[i]!=celda_spawn_raton or cord_libre[i]!=celda_spawn_queso) and (abs(cord_libre[i][0]-celda_spawn_raton[0])==distancia_a_raton or abs(cord_libre[i][1]-celda_spawn_raton[1])==distancia_a_raton) : #si la cordenada libre es distinta a la coordenada del raton, del queso y esta a x cantidad de distancia a la redonda 
            dir_comp.append(cord_libre[i]) #agrega la cordenada a la lista de direcciones compatibles
    #print("-",dir_comp," direcciones compatibles")
    aleatorio=random.randint(0,(len(dir_comp)-1))
    celda_spawn_gato=dir_comp[aleatorio]
    #print(celda_spawn_gato)
    mapa[celda_spawn_gato[0]][celda_spawn_gato[1]]="|🐱|"
    return celda_spawn_gato

crear_matriz(19,10,True,mapa)
distancia_a_raton=distancia_a_gato
celda_spawn_gato=spawn_michi(cord_libre,celda_spawn_raton,distancia_a_raton)
imprimir_mapa(x,y,mapa)