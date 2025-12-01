import re
from dataclasses import dataclass
from datetime import datetime
import getpass

NOMBRE_CINE = "Lúmen Cinema Universitario UdeA"

# Lista de funciones
PELICULAS = [
    ("Sábado", "10:00", "Wicked: Por Siempre"),
    ("Sábado", "13:00", "Avatar: Fuego y Ceniza"),
    ("Sábado", "16:00", "Midsommar"),
    ("Domingo", "10:00", "Eterno resplandor de una mente sin recuerdos"),
    ("Domingo", "13:00", "Wicked: Por Siempre")
]

# Precios por tipo de vínculo (obligatorio Mayúscula inicial)
PRECIOS = {
    "Estudiante": 7500,
    "Docente": 10000,
    "Administrativo": 8500,
    "Oficial interno": 7000,
    "Público externo": 15000
}

ADMIN = {"admin": "1234"}  # Simple: usuario y contraseña

usuarios = []
reservas = []


# ====================== ESTRUCTURAS DATACLASS ======================
@dataclass
class Usuario:
    nombre: str
    apellido: str
    documento: str
    tipo: str


@dataclass
class Reserva:
    codigo: str
    usuario: Usuario
    funcion_id: int
    pelicula: str
    asientos: list
    precio_total: int
    fecha: str


# =============================== CINE ===============================
class Cine:
    def __init__(self):
        self.filas = ["A","B","C","D","E","F","G","H","I","J","K"]
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
        for i in range(1, self.columnas+1):
            print(f"{i:>4}", end="")
        print("\n")

        for fila in self.filas:
            print(f"{fila}  ", end="")
            for asiento in m[fila]:
                print(f"{asiento:>4}", end="")
            print()

    def asiento_disponible(self, funcion_id, asiento):
        asiento = asiento.strip().upper()
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
        asiento = asiento.strip().upper()
        fila, num = asiento[0], asiento[1:]
        col = int(num) - 1
        if fila in self.funciones_asientos[funcion_id] and 0 <= col < self.columnas:
            self.funciones_asientos[funcion_id][fila][col] = estado
            return True
        return False

    def disponibles_totales(self, funcion_id):
        m = self.funciones_asientos[funcion_id]
        return sum(fila.count("O") for fila in m.values())


cine = Cine()


# ========================== VALIDACIONES ==========================
def validar_nombre(texto):
    texto = texto.strip()
    return len(texto) >= 3 and all(c.isalpha() or c.isspace() for c in texto)


def validar_documento(doc):
    return doc.isdigit() and 3 <= len(doc) <= 15


# ========================== REGISTRAR USUARIO ==========================
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

    # Evitar duplicados
    if any(u.documento == documento for u in usuarios):
        print("Ya existe un usuario con ese documento.")
        return

    print("\nTIPOS DE VÍNCULO (Debe iniciar EXACTAMENTE igual, con Mayúscula inicial):")
    for tipo in PRECIOS:
        print(f"- {tipo} → ${PRECIOS[tipo]}")

    tipo = input("Tipo de vínculo (respetar mayúscula): ").strip()

    if tipo not in PRECIOS:
        print("Tipo de vínculo inválido. Recuerde escribirlo tal cual aparece (Mayúscula inicial).")
        return

    usuario = Usuario(nombre, apellido, documento, tipo)
    usuarios.append(usuario)

    print("Usuario registrado correctamente\n")


# ========================== CONSULTAR MIS RESERVAS ==========================
def consultar_mis_reservas():
    doc = input("\nDocumento del usuario: ").strip()

    mis = [r for r in reservas if r.usuario.documento == doc]

    if not mis:
        print("No tienes reservas registradas.")
        return

    print("\n=========== MIS RESERVAS ===========")
    for r in mis:
        print(f"Código: {r.codigo}")
        print(f"Película: {r.pelicula}")
        print(f"Asientos: {', '.join(r.asientos)}")
        print(f"Fecha: {r.fecha}")
        print("------------------------------------")
    print()


# ========================== CANCELAR RESERVA ==========================
def cancelar_reserva():
    print("\n---- CANCELAR RESERVA ----")
    doc = input("Documento: ").strip()
    codigo = input("Código de reserva: ").strip()

    # Buscar reserva
    reserva = next((r for r in reservas if r.codigo == codigo and r.usuario.documento == doc), None)

    if not reserva:
        print("Reserva no encontrada.")
        return

    # Liberar asientos
    for a in reserva.asientos:
        cine.cambiar_estado(reserva.funcion_id, a, "O")

    reservas.remove(reserva)

    print("Reserva cancelada exitosamente.\n")


# ========================== REGISTRAR RESERVA ==========================
def registrar_reserva():
    if not usuarios:
        print("No hay usuarios registrados")
        return

    documento = input("Documento del usuario: ").strip()
    usuario = next((u for u in usuarios if u.documento == documento), None)

    if not usuario:
        print("Usuario no encontrado")
        return

    print("\nFUNCIONES DISPONIBLES (Debe elegir el NÚMERO de la función):\n")
    for i, p in enumerate(PELICULAS, 1):
        print(f"{i}. {p[0]} - {p[1]} - {p[2]}")

    opcion = input("Seleccione la película escribiendo SOLO el número: ").strip()

    if not opcion.isdigit() or int(opcion) not in range(1, len(PELICULAS) + 1):
        print("Selección inválida. Debe ingresar únicamente el número correspondiente.")
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
    rollback = []

    for n in range(1, cantidad+1):
        cine.mostrar_asientos(funcion_id)
        asiento = input(f"\nSeleccione asiento #{n} (Ej: B7): ").upper().strip()

        if not cine.asiento_disponible(funcion_id, asiento):
            print("Asiento inválido u ocupado")

            # REGRESAR los asientos ya tomados
            for a in rollback:
                cine.cambiar_estado(funcion_id, a, "O")
            return

        cine.cambiar_estado(funcion_id, asiento, "X")
        rollback.append(asiento)
        asientos_seleccionados.append(asiento)

    precio = PRECIOS[usuario.tipo] * len(asientos_seleccionados)
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M")

    # Crear código de reserva
    codigo = f"R{len(reservas)+1:04d}-{usuario.documento[-4:]}"

    nueva = Reserva(codigo, usuario, funcion_id, pelicula, asientos_seleccionados, precio, fecha)
    reservas.append(nueva)

    # FACTURA
    print("\n===============================================")
    print("      LÚMEN CINEMA UNIVERSITARIO UDEA")
    print("-----------------------------------------------")
    print(f"Código de reserva: {codigo}")
    print(f"Película: {pelicula.upper()}")
    print(f"Fecha y hora: {fecha}")
    print("Asientos:")
    for a in asientos_seleccionados:
        print(f"  - {a}")
    print("-----------------------------------------------")
    print(f"Total: ${precio}")
    print("Gracias por su compra")
    print("===============================================\n")


# =============================== ADMIN ===============================
def administrador():
    print("\n---- ÁREA DE ADMINISTRADOR ----")
    user = input("Usuario: ").strip()
    pwd = getpass.getpass("Contraseña: ").strip()

    if user not in ADMIN or ADMIN[user] != pwd:
        print("Credenciales inválidas")
        return

    print("\nOpciones:")
    print("1. Ver usuarios")
    print("2. Ver reservas")
    print("3. Ver ocupación de funciones")
    print("4. Salir")

    op = input("Seleccione: ").strip()

    if op == "1":
        print("\n---- USUARIOS ----")
        for u in usuarios:
            print(f"{u.documento} - {u.nombre} {u.apellido} ({u.tipo})")
        print()

    elif op == "2":
        print("\n---- RESERVAS ----")
        for r in reservas:
            print(f"{r.codigo} - {r.pelicula} - {r.usuario.nombre} - Asientos: {', '.join(r.asientos)}")
        print()

    elif op == "3":
        print("\n---- OCUPACIÓN ----")
        for i, p in enumerate(PELICULAS):
            disp = cine.disponibles_totales(i)
            print(f"Función {i+1}: {p[2]} → {disp} libres")

    print()


# =============================== CONSULTAR FUNCIONES ===============================
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
        disponibles = cine.disponibles_totales(i-1)
        print(f"{i:<5}{p[0]:<12}{p[1]:<10}{p[2]:<40}{disponibles}")

    print("\n" + "="*70 + "\n")


# =============================== MENÚ ===============================
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
                            5. Consultar Mis Reservas
                            6. Administrador
                            7. Salir
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
            consultar_mis_reservas()
        elif op == "6":
            administrador()
        elif op == "7":
            print("Programa finalizado")
            break
        else:
            print("Opción inválida")


menu()
