from display import mapa
from display import matriz

def visualizar_mapa():
    ancho_mapa=len(mapa)
    print("Ancho ",ancho_mapa)
    alto_mapa=len(mapa[0])
    print("Alto ",alto_mapa)


matriz(19,10,True,mapa)
visualizar_mapa()