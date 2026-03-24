import sys, os, time

def bienvenida():
    print("Bienvenid@ al juego del gato y el raton")

def mostrar_menu():
    print("______________________________")
    print("|          🐱JUGAR (1)       |")
    print("______________________________")
    print("______________________________")
    print("|         🐭OPCIONES (2)     |")
    print("______________________________")
    print("______________________________")
    print("|          🧀SALIR (3)       |")
    print("______________________________")

def capturar_opcion():
    opcion=input("Ingrese opción: ")
    if opcion=="1" or opcion.lower()=="jugar":
        
        return 1
    elif opcion=="2" or opcion.lower()=="opciones":
        return 2
    elif opcion=="3" or opcion.lower()=="salir":
        os.system('cls')
        sys.exit("Gracias vuelvas prontos -Apu")
    else:
        os.system('cls')
        print("Error, opcion invalida")
        mostrar_menu()
        opcion_elegida=capturar_opcion()

def validar_nro(numero):
    if numero.isdigit():
        return int(numero)
    else:
        return False



def enviar_a_pantalla(eleccion):
    if eleccion==1:
        print("")    #añadir direccion al juego
    elif eleccion==2:
        print("-----------Opciones------------")
        ancho=input("Ancho del mapa: ")
        alto=input("Alto del mapa: ")
        obstaculos=input("Obstaculos del mapa: ")
        validar_nro(ancho)
    



bienvenida()
time.sleep(3)
mostrar_menu()
opcion_elegida=capturar_opcion()
pantalla_destino=enviar_a_pantalla(opcion_elegida)