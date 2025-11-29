import re
from dataclasses import dataclass
from datetime import datetime

NOMBRE_CINE = "Lúmen Cinema Universitario UdeA"

# Lista de funciones
PELICULAS = [
    ("Sábado", "10:00", "Wicked: Por Siempre"),
    ("Sábado", "13:00", "Avatar: Fuego y Ceniza"),
    ("Sábado", "16:00", "Midsommar"),
    ("Domingo", "10:00", "Eterno resplandor de una mente sin recuerdos"),
    ("Domingo", "13:00", "Wicked: Por Siempre")
]

PRECIOS = {
    "Estudiante": 7500,
    "Docente": 10000,
    "Administrativo": 8500,
    "Oficial interno": 7000,
    "Público externo": 15000
}

ADMIN = {"admin": "1234"}

usuarios = []
reservas = []


@dataclass
class Usuario:
    nombre: str
    apellido: str
    documento: str
    tipo: str


@dataclass
class Reserva:
    usuario: Usuario
    funcion_id: int
    pelicula: str
    asientos: list
    precio_total: int
    fecha: str


class Cine:
    def __init__(self):
        self.filas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
        self.columnas = 11

        self.funciones_asientos = {
            i: {fila: ["O"] * self.columnas for fila in self.filas}
            for i in range(len(PELICULAS))
        }

    def mostrar_asientos(self, funcion_id):
        m = self.funciones_asientos[funcion_id]

        print("\n================= PANTALLA DEL CINE =================\n")
        print("LUMEN Cinema UdeA (O Disponible) (X Ocupado)")
        print("La pantalla se encuentra frente a la FILA A\n")

        print("    ", end="")
        for i in range(1, self.columnas + 1):
            print(f"{i:>4}", end="")
        print("\n")

        for fila in self.filas:
            print(f"{fila}  ", end="")
            for asiento in m[fila]:
                print(f"{asiento:>4}", end="")
            print()

    def asiento_disponible(self, funcion_id, asiento):
        fila, num = asiento[0], asiento[1:]
        if fila not in self.funciones_asientos[funcion_id]:
            return False
        if not num.isdigit():
            return False
        col = int(num) - 1
        if col < 0 or col >= self.columnas:
            return False
        return self.funciones_asientos[funcion_id][fila][col] == "O"

    def cambiar_estado(self, funcion_id, asiento, estado):
        fila = asiento[0]
        num = asiento[1:]
        if fila in self.funciones_asientos[funcion_id] and num.isdigit():
            col = int(num) - 1
            if 0 <= col < self.columnas:
                self.funciones_asientos[funcion_id][fila][col] = estado
                return True
        return False

    def disponibles_totales(self, funcion_id):
        m = self.funciones_asientos[funcion_id]
        return sum(fila.count("O") for fila in m.values())


cine = Cine()


# ========================= VALIDACIONES ========================
def validar_nombre(texto):
    texto = texto.strip()
    return len(texto) >= 3 and all(c.isalpha() or c.isspace() for c in texto)


def validar_documento(doc):
    return doc.isdigit() and 3 <= len(doc) <= 15


# ========================= REGISTRO USUARIO ========================
def registrar_usuario():
    print("\n---- REGISTRAR USUARIO ----")

    nombre = input("Nombre: ").strip()
    if not validar_nombre(nombre):
        print("Error en nombre")
        return

    apellido = input("Apellido: ").strip()
    if not validar_nombre(apellido):
        print("Error en apellido")
        return

    documento = input("Documento: ").strip()
    if not validar_documento(documento):
        print("Documento inválido")
        return

    print("\nTIPOS DE VÍNCULO:")
    for tipo in PRECIOS:
        print(f"- {tipo} → ${PRECIOS[tipo]}")

    tipo = input("Tipo de vínculo: ").strip()
    if tipo not in PRECIOS:
        print("Tipo de vínculo inválido")
        return

    usuario = Usuario(nombre, apellido, documento, tipo)
    usuarios.append(usuario)
    print("Usuario registrado correctamente\n")


# ========================= REGISTRO RESERVA ========================
def registrar_reserva():
    if not usuarios:
        print("No hay usuarios registrados")
        return

    documento = input("Documento del usuario: ").strip()
    usuario = next((u for u in usuarios if u.documento == documento), None)

    if not usuario:
        print("Usuario no encontrado")
        return

    print("\nFUNCIONES DISPONIBLES:\n")
    for i, p in enumerate(PELICULAS, 1):
        print(f"{i}. {p[0]} - {p[1]} - {p[2]}")

    opcion = input("Seleccione película: ").strip()

    if not opcion.isdigit() or int(opcion) not in range(1, len(PELICULAS) + 1):
        print("Selección inválida")
        return

    funcion_id = int(opcion) - 1
    funcion = PELICULAS[funcion_id]
    pelicula = funcion[2]

    disponibles = cine.disponibles_totales(funcion_id)
    print(f"\nAsientos disponibles en esta función: {disponibles}")

    cantidad = input("¿Cuántos asientos desea reservar? ").strip()
    if not cantidad.isdigit():
        print("Cantidad inválida")
        return
    cantidad = int(cantidad)

    if cantidad <= 0 or cantidad > disponibles:
        print("Cantidad fuera de rango")
        return

    asientos_seleccionados = []

    for n in range(1, cantidad + 1):
        cine.mostrar_asientos(funcion_id)
        asiento = input(f"\nSeleccione asiento #{n} (Ej: B7): ").upper().strip()

        if not asiento or asiento[0] not in cine.filas or not asiento[1:].isdigit():
            print("Asiento inválido")
            return

        if not cine.asiento_disponible(funcion_id, asiento):
            print("Asiento ocupado o inválido")
            return

        cine.cambiar_estado(funcion_id, asiento, "X")
        asientos_seleccionados.append(asiento)

    precio = PRECIOS[usuario.tipo] * len(asientos_seleccionados)
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M")

    nueva = Reserva(usuario, funcion_id, pelicula, asientos_seleccionados, precio, fecha)
    reservas.append(nueva)

    print("\n===============================================")
    print("      LÚMEN CINEMA UNIVERSITARIO UDEA")
    print("            NIT 900000000-0")
    print("     Ciudad Universitaria - Medellín")
    print("-----------------------------------------------")
    print("Documento equivalente a factura")
    print("-----------------------------------------------")

    codigo = f"T{len(reservas):04d}-{usuario.documento[-4:]}"
    print(f"Nro: {codigo}")
    print("Boleto de entrada al cine")
    print(f"Película: {pelicula.upper()}")
    print(f"Fecha y hora: {fecha}")
    print("-----------------------------------------------")
    print("UBICACIÓN (Múltiples asientos):")
    for a in asientos_seleccionados:
        print(f" PF           {a}")
    print("-----------------------------------------------")
    print(f"Vlr Total: ${precio}")
    print("Universidad de Antioquia")
    print("LÚMEN CINEMA - UdeA")
    print("Sala Principal UdeA")
    print("-----------------------------------------------")
    print(datetime.now().strftime("%d/%m/%Y   %H:%M:%S"))
    print("Gracias por su compra")
    print("===============================================\n")


# ========================= CONSULTAR FUNCIONES ========================
def consultar_funciones():
    print("\n" + "="*70)
    print("🎬 CARTELERA DEL FIN DE SEMANA – LÚMEN CINEMA UdeA 🎬".center(70))
    print("="*70 + "\n")

    print("📅 Total de funciones programadas:", len(PELICULAS))
    print("🎞️ Películas en cartelera:", len(set(p[2] for p in PELICULAS)))
    print("\n")

    print("🎬 PELÍCULAS EN CARTELERA:")
    print("-"*70)
    for p in set(p[2] for p in PELICULAS):
        print(f"• {p}")
    print("\n")

    print("🕒 HORARIOS Y DISPONIBILIDAD:")
    print("-"*70)
    print(f"{'ID':<5}{'Día':<12}{'Hora':<10}{'Película':<40}{'Disp.'}")
    print("-"*70)

    for i, p in enumerate(PELICULAS, 1):
        disponibles = cine.disponibles_totales(i - 1)
        print(f"{i:<5}{p[0]:<12}{p[1]:<10}{p[2]:<40}{disponibles}")

    print("\n" + "="*70 + "\n")


# ========================= MENÚ ========================
def menu():
    while True:
        print(r"""
                           ██╗     ██╗   ██╗███╗   ███╗███████╗███╗   ██╗
                           ██║     ██║   ██║████╗ ████║██╔════╝████╗  ██║
                           ██║     ██║   ██║██╔████╔██║█████╗  ██╔██╗ ██║
                           ██║     ██║   ██║██║╚██╔╝██║██╔══╝  ██║╚██╗██║
                           ███████╗╚██████╔╝██║ ╚═╝ ██║███████╗██║ ╚████║
                           ╚══════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝

                                CINEMA UNIVERSITARIO UdeA
        =======================================================================
                                 Bienvenido al Cinema UdeA
        =======================================================================
                            1. Registrar Usuario
                            2. Registrar Reserva
                            3. Cancelar Reserva
                            4. Consultar Funciones Fin de Semana
                            5. Administrador
                            6. Salir
        =======================================================================
        """)

        op = input("Seleccione una opción: ").strip()

        if op == "1":
            registrar_usuario()
        elif op == "2":
            registrar_reserva()
        elif op == "3":
            cancelar_reserva()
        elif op == "4":
            consultar_funciones()
        elif op == "5":
            administrador()
        elif op == "6":
            print("Programa finalizado")
            break
        else:
            print("Opción inválida")


menu()
