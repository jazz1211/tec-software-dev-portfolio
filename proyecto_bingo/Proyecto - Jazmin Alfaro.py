# Jazmín Alfaro
# Versión 0.2
# Proyecto Bingo (Segundo Avance)
import random # libreria investigada: random.choice(lista) para crear valores al azar

def crear_partida():
    # entrada: n/a
    # proceso: crear las listas de bolitas disponibles y extraídas
    # salida: retornar las listas disponibles y extraídas
    disponibles = list(range(1, 76))
    extraidas = []

    return disponibles, extraidas

def sacar_bolita(disponibles, extraidas):
    # entrada: disponibles y extraidas
    # proceso: validar y sacar bolita al azar
    # salida: mostrar bolita extraida o mensaje
    if not disponibles:
        print("\n (!) No quedan bolitas disponibles en la tómbola.")
        return
    
    bolita = random.choice(disponibles)
    disponibles.remove(bolita)
    extraidas.append(bolita)
    print("\n ✪ La bolita extraída es:", bolita)
        
def bolitas_extraidas(extraidas):
    # entrada: extraidas
    # proceso: revisar lista de bolitas extraidas
    # salida: mostrar extraidas o mensaje
    if not extraidas:
        print("\n (!) Aún no se ha sacado ninguna bolita (!)")
        return

    ancho = 57
    print("\n╔" + "═" * ancho + "╗", # titulo del cuadro :)
          "\n║" + " ♥ NUMEROS EXTRAIDOS ♥ ".center(ancho) + "║",
          "\n╠" + "═" * ancho + "╣")

    for i in range(0, len(extraidas), 10):
        fila = " | ".join(f"{num:02}" for num in extraidas[i:i + 10])
        print("║" + fila.center(ancho) + "║")

    print("╚" + "═" * ancho + "╝")

def estado_partida(disponibles, extraidas):
    # entrada: disponibles / extraidas
    # proceso: contar valores en listas disponibles / extraidas
    # salida: mostrar estado de la partida
    print("\n ♥ Estado de la partida:",
          "\n   -► Bolitas extraídas:", len(extraidas),
          "\n   -► Bolitas disponibles:", len(disponibles))

def menu_inicio():
    # entrada: n/a
    # proceso: mostrar menu inicial
    # salida: desplegar opciones crear / salir
    print("""
╔═════════════════════════════════════════════════════════════════╗
║                       ♥ ELIGE UNA OPCIÓN ♥                      ║
╠═════════════════════════════════════════════════════════════════╣
║     1. Crear partida                                            ║
║     6. Salir                                                    ║
╚═════════════════════════════════════════════════════════════════╝""")

def menu_principal():
    # entrada: n/a
    # proceso: mostrar menu principal
    # salida: desplegar opciones durante partida
    print(
        "\n╔═════════════════════════════════════╗",
        "\n║          ♥ MENÚ PRINCIPAL ♥         ║",
        "\n╠═════════════════════════════════════╣",
        "\n║ 2. Sacar bolita                     ║",
        "\n║ 3. Consultar números extraídos      ║",
        "\n║ 4. Consultar estado de la partida   ║",
        "\n║ 5. Crear nueva partida              ║",
        "\n║ 6. Salir                            ║",
        "\n╚═════════════════════════════════════╝")

def main():
    # entrada: opciones seleccionadas
    # proceso: ejecutar opciones del menu inicial y menu principal
    # salida: permitir uso del programa
    disponibles = []
    extraidas = []
    
    tombola()
    while True: # menu inicial
        opcion = input(" ► Selecciona una opción: ")
        if opcion == "1":
            disponibles, extraidas = crear_partida()
            print("\n ► Partida creada correctamente!\n")
            break

        elif opcion == "6":
            confirmar = input("\n (!) ¿Está seguro que desea salir? (ingresa 's' para confirmar): ").strip().lower()

            if confirmar == "s":
                print("\n ♥ Gracias por usar nuestro bingo. Hasta luego!! :) \n")
                return
            
            else:
                print("\n ► Se canceló la salida.")
                menu_inicio()
        else:
            print("\n (!) Opción inválida. Intente de nuevo (!)\n")

    menu_principal()
    while True: # menu principal
        opcion = input(" ► Selecciona una opción o '0' para ver el menú: ")
        if opcion == "0":
            menu_principal()

        elif opcion == "2":
            sacar_bolita(disponibles, extraidas)

        elif opcion == "3":
            bolitas_extraidas(extraidas)

        elif opcion == "4":
            estado_partida(disponibles, extraidas)

        elif opcion == "5":
            confirmar = input("\n (!) Hay una partida en juego, ¿Está seguro que desea crear una nueva partida? (ingresa 's' para confirmar): ").strip().lower()

            if confirmar == "s":
                disponibles, extraidas = crear_partida()
                print("\n ► Se ha iniciado una nueva partida!")
                menu_principal()                    
            else:
                print("\n ► Se canceló la creación de una nueva partida.")
                    
        elif opcion == "6":
            confirmar = input("\n (!) Hay una partida en juego, ¿Está seguro que desea salir? (ingresa 's' para confirmar): ").strip().lower()

            if confirmar == "s":
                print("\n ♥ Gracias por usar nuestro bingo. Hasta luego!! :) \n")
                break
            else:
                print("\n ► Se canceló la salida, digite 0 para ver el menú.")

        else:
            print("\n (!) Opción inválida. Intente de nuevo (!)")

def tombola(): # solo texto decorativo :)
    # entrada: n/a
    # proceso: mostrar tombola y menu inicial
    # salida: desplegar opciones tombola + opciones crear / salir
    
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
╠═════════════════════════════════════════════════════════════════╣
║                       ♥ ELIGE UNA OPCIÓN ♥                      ║
╠═════════════════════════════════════════════════════════════════╣
║     1. Crear partida                                            ║
║     6. Salir                                                    ║
╚═════════════════════════════════════════════════════════════════╝""")

if __name__ == "__main__":
    main()
