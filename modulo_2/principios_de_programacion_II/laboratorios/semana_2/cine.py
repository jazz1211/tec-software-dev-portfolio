# ============================================================================================
# CONCEPTOS DEL CÓDIGO UTILIZADO: Esta documentación sirve como guía para revisar en clase
#                                 los conceptos utilizados en el programa, incluyendo clases,
#                                 ordenamiento y búsqueda binaria con bisect_left.
# ============================================================================================
#
# Clases y atributos:
#   - self                : referencia a la instancia actual.
#   - dataclass           : genera métodos para una clase de datos.
#   - order=True          : permite ordenar por edad y turno.
#   - slots=True          : limita atributos y puede ahorrar memoria.
#   - field(compare=False): excluye un atributo de las comparaciones.
#   - __init__            : inicializa los atributos de una instancia.
#
# Búsqueda:
#   - bisect_left         : realiza búsqueda binaria en una lista ordenada.
#   - startswith          : comprueba si un nombre empieza con el texto.
#
# Control del programa:
#   - lambda              : define una función breve.
#   - __name__            : permite iniciar el programa directamente.
#
# ============================================================================================

from bisect import bisect_left
from dataclasses import dataclass, field


@dataclass(order=True, slots=True)
class Cliente:
    edad: int
    turno: int
    nombre: str = field(compare=False)
    boletos: int = field(compare=False)


class ColaCine:
    def __init__(self) -> None:
        self.clientes: list[Cliente] = []
        self.total_boletos = 0
        self.boletos_gratis = 0
        self.ordenada = True

        # Índice separado para buscar por nombre.
        self.indice_nombres: list[Cliente] = []
        self.nombres_ordenados: list[str] = []
        self.indice_actualizado = True

    def agregar(self, nombre: str, edad: int, boletos: int) -> None:
        cliente = Cliente(edad, len(self.clientes) + 1, nombre, boletos)
        self.clientes.append(cliente)

        self.total_boletos += boletos
        if edad < 12:
            self.boletos_gratis += 1


        self.ordenada = False
        self.indice_actualizado = False

    def obtener_ordenada(self) -> list[Cliente]:
        if not self.ordenada:
            self.clientes.sort()
            self.ordenada = True

        return self.clientes

    def actualizar_indice_nombres(self) -> None:
        if not self.indice_actualizado:
            self.indice_nombres = sorted(
                self.clientes,
                key=lambda cliente: cliente.nombre.casefold(),
            )
            self.nombres_ordenados = [
                cliente.nombre.casefold()
                for cliente in self.indice_nombres
            ]
            self.indice_actualizado = True


def leer_numero(mensaje: str, minimo: int) -> int:
    while True:
        try:
            valor = int(input(mensaje))
            if valor >= minimo:
                return valor

            print(f"Ingrese un número mayor o igual a {minimo}.")
        except ValueError:
            print("Ingrese un número entero válido.")


def registrar(cola: ColaCine) -> None:
    nombre = input("Nombre: ").strip().capitalize()
    if not nombre:
        print("El nombre no puede estar vacío.")
        return

    edad = leer_numero("Edad: ", 0)
    boletos = leer_numero("Boletos a comprar: ", 1)

    cola.agregar(nombre, edad, boletos)
    print("Cliente registrado.")


def mostrar_cola(cola: ColaCine) -> None:
    if not cola.clientes:
        print("La cola está vacía.")
        return

    for posicion, cliente in enumerate(cola.obtener_ordenada(), start=1):
        print(
            f"{posicion}. {cliente.nombre}: {cliente.edad} años, "
            f"{cliente.boletos} boletos."
        )


def buscar(cola: ColaCine) -> None:
    if not cola.clientes:
        print("No hay clientes registrados todavía.")
        return

    texto = input("Nombre a buscar: ").strip().casefold()
    if not texto:
        print("El nombre no puede estar vacío.")
        return

    cola.actualizar_indice_nombres()

    # Búsqueda binaria de la primera posición posible.
    posicion = bisect_left(cola.nombres_ordenados, texto)
    encontrado = False

    # Los nombres que coinciden están juntos en el índice.
    while (
        posicion < len(cola.indice_nombres)
        and cola.nombres_ordenados[posicion].startswith(texto)
    ):
        cliente = cola.indice_nombres[posicion]
        print(
            f"{cliente.nombre}: {cliente.edad} años, "
            f"{cliente.boletos} boletos."
        )
        encontrado = True
        posicion += 1

    if not encontrado:
        print("No se encontraron nombres relacionados.")


def ver_totales(cola: ColaCine) -> None:
    print(
        f"\n- Clientes registrados: {len(cola.clientes)}"
        f"\n- Boletos a comprar: {cola.total_boletos}"
        f"\n- Boletos gratis previstos: {cola.boletos_gratis}"
    )


def ejecutar_menu(menu: str, acciones: dict, salida: str) -> None:
    print(menu)

    while True:
        opcion = input(
            "\nElige una opción o presiona 0 para ver el menú: "
        ).strip()

        if opcion == salida:
            return
        if opcion == "0":
            print(menu)
        elif opcion in acciones:
            acciones[opcion]()
        else:
            print("Opción inválida. Presiona 0 para ver el menú.")


def menu_cine(cola: ColaCine) -> None:
    menu = (
        "\nMENÚ DE CINE:"
        "\n1. Registrarse"
        "\n2. Mostrar cola"
        "\n3. Buscar por nombre"
        "\n4. Ver totales"
        "\n5. Volver"
    )

    ejecutar_menu(
        menu,
        {
            "1": lambda: registrar(cola),
            "2": lambda: mostrar_cola(cola),
            "3": lambda: buscar(cola),
            "4": lambda: ver_totales(cola),
        },
        salida="5",
    )


def main() -> None:
    cola = ColaCine()
    menu = "\nMENÚ INICIAL\n1. Cine\n2. Salir"

    try:
        ejecutar_menu(menu, {"1": lambda: menu_cine(cola)}, salida="2")
    except (EOFError, KeyboardInterrupt):
        print("\nEntrada interrumpida.")

    print("\nPrograma finalizado.")


if __name__ == "__main__":
    main()


