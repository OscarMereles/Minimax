import random#importa libreria random (aleatorio)
from display import mapa, crear_matriz, imprimir_mapa#importa metodos y variables de display.py
from mouse import celda_spawn_raton , celda_spawn_queso,cord_libre,cord_obts,distancia_a_gato,x,y,distancia_raton_queso #importa metodos y variables de mouse.py
direccion=[(-1,-1),()]

def spawn_michi(cord_libre,celda_spawn_raton,distancia_a_raton,distancia_raton_queso):#funcion de spawn del gato en el mapa
    dir_comp=[]#lista que filtra las coordenadas de distancia con el raton
    dir_comp2=[]#lista que filtra las coordenadas de distancia con el queso
    for i in range(len(cord_libre)-1):
        if (cord_libre[i]!=celda_spawn_raton or cord_libre[i]!=celda_spawn_queso) and (abs(cord_libre[i][0]-celda_spawn_raton[0])==distancia_a_raton or abs(cord_libre[i][1]-celda_spawn_raton[1])==distancia_a_raton) : #si la cordenada libre es distinta a la coordenada del raton, del queso y esta a x cantidad de distancia a la redonda del raton
            dir_comp.append(cord_libre[i]) #agrega la cordenada a la lista de direcciones compatibles
    #print("-",dir_comp," direcciones compatibles")
    for j in range(len(dir_comp)-1):
        if (abs(dir_comp[j][0]-celda_spawn_queso[0])==distancia_raton_queso or abs(dir_comp[j][1]-celda_spawn_queso[1])==distancia_raton_queso) : #si la cordenada filtrada es distinta a la coordenada del raton, del queso y esta a x cantidad de distancia a la redonda del queso 
            dir_comp2.append(dir_comp[j]) #agrega la cordenada a la lista de direcciones compatibles
    if len(dir_comp2)!=0:
        aleatorio=random.randint(0,(len(dir_comp2)-1))
        celda_spawn_gato=dir_comp2[aleatorio]
        mapa[celda_spawn_gato[0]][celda_spawn_gato[1]]="|🐱|"
    else:
        if mapa[celda_spawn_raton[0]*-1][celda_spawn_raton[1]*-1]!="|⬛|":
            celda_spawn_gato=[celda_spawn_raton[0]*-1,celda_spawn_raton[1]*-1]
            mapa[celda_spawn_raton[0]*-1][celda_spawn_raton[1]*-1]="|🐱|"
    #print(celda_spawn_gato)
    return celda_spawn_gato

#def mover(direccion):


#crear_matriz(19,10,True,mapa)
distancia_a_raton=distancia_a_gato
celda_spawn_gato=spawn_michi(cord_libre,celda_spawn_raton,distancia_a_raton,distancia_raton_queso)
imprimir_mapa(x,y,mapa)
print(celda_spawn_gato)