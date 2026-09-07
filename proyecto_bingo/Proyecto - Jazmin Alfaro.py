# Jazmín Alfaro Castañeda
# Versión 0.1
# Proyecto Bingo (Primer Avance)

import random
# libreria investigada: random.choice(lista) para crear valores al azar en lista bolitas disponibles

def crear_partida():
    # entrada: n/a
    # proceso: crear listas de bolitas disponibles y extraidas
    # salida: retornar disponibles y extraidas
    
    disponibles = list(range(1, 76))
    extraidas = []
    return disponibles, extraidas

def sacar_bolita(disponibles, extraidas):
    # entrada: disponibles y extraidas
    # proceso: validar y sacar bolita al azar
    # salida: mostrar bolita extraida o mensaje
    
    if len(disponibles) == 0:
        print("\n (!) No quedan bolitas disponibles en la tómbola.")
    else:
        bolita = random.choice(disponibles)
        disponibles.remove(bolita)
        extraidas.append(bolita)
        print("\n ✪ La bolita extraida es: ", bolita)

def consultar_extraidas(extraidas):
    # entrada: extraidas
    # proceso: revisar lista de bolitas extraidas
    # salida: mostrar extraidas o mensaje
    
    if len(extraidas) == 0:
        print("\n (!) Aún no se ha sacado ninguna bolita (!)")
    else:
        print("\n ► Numeros extraidos:\n", str(extraidas).replace(',' ,' |'), "\n")

def consultar_estado(disponibles, extraidas):
    # entrada: disponibles / extraidas
    # proceso: contar valores en listas disponibles / extraidas
    # salida: mostrar estado de la partida
    
    print("\n ♥ Estado de la partida:",
          "\n   -► Bolitas extraidas:", len(extraidas),
          "\n   -► Bolitas disponibles:", len(disponibles))

def mostrar_menu():
    # entrada: n/a
    # proceso: mostrar menu principal
    # salida: desplegar opciones
    
    print("\n╔═════════════════════════════════════╗",
          "\n║          ♥ MENÚ PRINCIPAL ♥         ║"
          "\n╠═════════════════════════════════════╣",
          "\n║ 1. Crear partida                    ║",
          "\n║ 2. Sacar bolita                     ║",
          "\n║ 3. Consultar numeros extraidos      ║",
          "\n║ 4. Consultar estado de la partida   ║",
          "\n║ 5. Crear nueva partida              ║",
          "\n║ 6. Salir                            ║",
          "\n╚=====================================╝")

def main():
    # entrada: n/a
    # proceso: ejecutar opciones del menu principal
    # salida: permitir uso del programa
    
    mensaje_bienvenida()
    disponibles = []
    extraidas = []
    partida_creada = False

    while True:
        mostrar_menu()
        opcion = input(" ► Selecciona una opcion: ")

        if opcion == "1":
            disponibles, extraidas = crear_partida()
            partida_creada = True
            print("\n ► Partida creada correctamente!\n")

        elif opcion == "2":
            if partida_creada:
                sacar_bolita(disponibles, extraidas)
            else:
                print("\n (!) Primero debes crear una partida (!)\n")

        elif opcion == "3":
            if partida_creada:
                consultar_extraidas(extraidas)
            else:
                print("\n (!) Primero debes crear una partida (!)")

        elif opcion == "4":
            if partida_creada:
                consultar_estado(disponibles, extraidas)
            else:
                print("\n (!) Primero debes crear una partida (!)")

        elif opcion == "5":
            disponibles, extraidas = crear_partida()
            partida_creada = True
            print("\n ► Se ha iniciado una nueva partida!")

        elif opcion == "6":
            print("\n ♥ Gracias por usar nuestro bingo. Hasta luego!! :) \n\n")
            break

        else:
            print("\n (!) opcion inválida. Intente de nuevo (!)")

def mensaje_bienvenida(): # solo codigo decorativo :) ♥
    print("""
            ╔═════════════════════════════════════════════════════════════════╗
            ║            ♥ ¡BIENVENIDO A NUESTRO JUEGO DE BINGO! ♥            ║
            ╠═════════════════════════════════════════════════════════════════╣
            ║                                                                 ║
            ║                         :%#######%%                             ║
            ║                     %%###*%   #%  %%**#%                        ║
            ║                  :%#% %*%     #%    %*#%*#                      ║
            ║                 ##%  %#+=---=+#%     %##  *#                    ║
            ║               %#%    #+-------=#%%    %*%  %*%                  ║
            ║              %#   %%%#=--------+%%%%****#%%  *%                 ║
            ║             %#%%**%:*#+-------=#       %*%%#*#*%                ║
            ║            :%*%    :####+===+##%        *%   %##                ║
            ║            %#*   *=======*%%%%#%%%%%***%%#     #%               ║
            ║          *%%#* %*=========*   #% *-:::::-=*#*%%*%*%%%%%         ║
            ║         :#*##*%%*=========*   #%*-::::::::=  %%#%*#%%%#%        ║
            ║         :#####*% *=======*    #%*-::::::::=   %#%%%  %*%        ║
            ║           %#%#%#*#%#***#   #*+++**-::::::=%%#**%*%   %*%        ║
            ║           *#%%% *%###%%  #++++++++**===*#*#%%%# *%   %*%        ║
            ║           *#*:%%   %**%%%*+++++++++#%%%%#%  %*  *%   %*%        ║
            ║           *#*  %%* :##   #++++++++*    %*%%*#   *%   %*%        ║
            ║           *#*   *##*%#    #*+++++*     #%*#     *%  %%*%%       ║
            ║           *#*     :%#*%       #%     %*#%       *% #*****#      ║
            ║           *#*         %#***%%%*%%**#*%%         *%  %###%       ║
            ║           ###              ######%              *%              ║
            ║          ##+%#            %#    %%             ##+%#            ║
            ║         %#: :#%           #     #             %#: :#%           ║
            ║        ##:   %%%% #########################% ##:   %%%%         ║
            ║      *#*#     %%%%                          *#*#     %%%%       ║
            ║     *#*##%%%%%%%%%%                        *#*##%%%%%%%%%%      ║
            ╚═════════════════════════════════════════════════════════════════╝""")
    
if __name__ == "__main__":
    main()
    
### NOTAS ADICIONALES(consultar con profe):
# Se desea corregir el codigo para no imprimir el menu constantemente, sino que de la opcion de ver el menu y elegir (?).
# Uso de una mejor forma de desplegar numero extraidos (que se despliegue en sig linea de comando [tope min por renglon])
# Uso de metodos como: replace(), strip(), join(), split()...
# Crear partida y crear nueva partida en el mismo menu (?)