import sqlite3

# Conectar a la base de datos 
conexion = sqlite3.connect("gym_da2.db")
cursor = conexion.cursor()

# Tabla Clientes
cursor.execute("""
CREATE TABLE IF NOT EXISTS Clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellidos TEXT NOT NULL,
    edad INTEGER,
    DNI TEXT NOT NULL
)
""")

# Tabla Clases
cursor.execute("""
CREATE TABLE IF NOT EXISTS Clases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    horario TEXT
)
""")

# Tabla Inscripciones
cursor.execute("""
CREATE TABLE IF NOT EXISTS Inscripciones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER,
    clase_id INTEGER,
    FOREIGN KEY (cliente_id) REFERENCES Clientes(id),
    FOREIGN KEY (clase_id) REFERENCES Clases(id)
)
""")

conexion.commit()

# Funciones CRUD Clientes
def insertar_cliente():
    try:
        nombre = input("Nombre del cliente: ")
        apellidos = input("Apellidos del cliente: ")
        edad = input("Edad del cliente: ")
        DNI = input("DNI del cliente: ")
        
        cursor.execute("INSERT INTO Clientes (nombre, apellidos, edad, DNI) VALUES (?, ?, ?, ?)", (nombre, apellidos, edad, DNI))
        conexion.commit()
        print("\n✅ Cliente añadido con éxito.")
    except Exception as e:
        conexion.rollback()
        print("Error:", e)


def leer_cliente():
    try:
        propiedad = input("Consultar por (id/nombre): ").strip().lower()
        if propiedad not in ["id", "nombre"]:
            print("❌ Propiedad no válida. Usa 'id' o 'nombre'.")
            return
        
        valor = input("Ingrese el valor: ")
        cursor.execute(f"SELECT * FROM Clientes WHERE {propiedad} = ?", (valor,))
        
        resultados = cursor.fetchall()
        if resultados:
            for fila in resultados:
                print(fila)
        else:
            print("❌ No se encontraron resultados.")
    except Exception as e:
        print("Error:", e)


def actualizar_cliente():
    try:
        id_cliente = input("ID del cliente a actualizar: ").strip()
        cursor.execute("SELECT * FROM Clientes WHERE id = ?", (id_cliente,))
        cliente = cursor.fetchone()

        if not cliente:
            print("❌ Cliente no encontrado.")
            return

        nombre = input("Nuevo nombre (deja en blanco para no cambiar): ").strip() or cliente[1]
        edad = input("Nueva edad (deja en blanco para no cambiar): ").strip() or cliente[3]

        cursor.execute("UPDATE Clientes SET nombre = ?, edad = ? WHERE id = ?", (nombre, edad, id_cliente))
        conexion.commit()
        print("✅ Cliente actualizado.")
    except Exception as e:
        conexion.rollback()
        print("Error:", e)


def borrar_cliente():
    try:
        id_cliente = input("ID del cliente a eliminar: ").strip()
        cursor.execute("SELECT * FROM Clientes WHERE id = ?", (id_cliente,))
        cliente = cursor.fetchone()

        if not cliente:
            print("❌ Cliente no encontrado.")
            return

        confirmar = input("¿Estás seguro de que quieres eliminar este cliente? (s/n): ").strip().lower()
        if confirmar != "s":
            print("❌ Operación cancelada.")
            return

        cursor.execute("DELETE FROM Inscripciones WHERE cliente_id = ?", (id_cliente,))
        cursor.execute("DELETE FROM Clientes WHERE id = ?", (id_cliente,))
        conexion.commit()
        print("✅ Cliente eliminado.")
    except Exception as e:
        conexion.rollback()
        print("Error:", e)


# Funciones CRUD Clases
def insertar_clase():
    try:
        nombre = input("Nombre de la clase: ").strip()
        horario = input("Horario de la clase: ").strip()
        
        cursor.execute("INSERT INTO Clases (nombre, horario) VALUES (?, ?)", (nombre, horario))
        conexion.commit()
        print("✅ Clase añadida.")
    except Exception as e:
        conexion.rollback()
        print("Error:", e)


def leer_clase():
    try:
        propiedad = input("Consultar por (id/nombre): ").strip().lower()
        if propiedad not in ["id", "nombre"]:
            print("❌ Propiedad no válida.")
            return
        
        valor = input("Ingrese el valor: ").strip()
        cursor.execute(f"SELECT * FROM Clases WHERE {propiedad} = ?", (valor,))
        
        resultados = cursor.fetchall()
        if resultados:
            for clase in resultados:
                print(f"ID: {clase[0]} | Nombre: {clase[1]} | Horario: {clase[2]}")
        else:
            print("❌ No se encontraron resultados.")
    except Exception as e:
        print("Error:", e)


# Inscripciones
def inscribir_cliente():
    try:
        id_cliente = input("ID del cliente: ").strip()
        id_clase = input("ID de la clase: ").strip()
        
        cursor.execute("INSERT INTO Inscripciones (cliente_id, clase_id) VALUES (?, ?)", (id_cliente, id_clase))
        conexion.commit()
        print("✅ Inscripción realizada.")
    except Exception as e:
        conexion.rollback()
        print("Error:", e)


def leer_inscripciones():
    try:
        cursor.execute("SELECT * FROM Inscripciones")
        for fila in cursor.fetchall():
            print(fila)
    except Exception as e:
        print("Error:", e)


# Menú principal
def menu():
    while True:
        print("\n--- 🏋️‍♂️ GYM DA2 ---")
        print("1️⃣  Añadir cliente")
        print("2️⃣  Consultar cliente")
        print("3️⃣  Actualizar cliente")
        print("4️⃣  Eliminar cliente")
        print("5️⃣  Añadir clase")
        print("6️⃣  Consultar clase")
        print("7️⃣  Inscribir cliente en clase")
        print("8️⃣  Consultar inscripciones")
        print("9️⃣  Salir")

        opcion = input("\n👉 Selecciona una opción: ").strip()

        if opcion == "1":
            insertar_cliente()
        elif opcion == "2":
            leer_cliente()
        elif opcion == "3":
            actualizar_cliente()
        elif opcion == "4":
            borrar_cliente()
        elif opcion == "5":
            insertar_clase()
        elif opcion == "6":
            leer_clase()
        elif opcion == "7":
            inscribir_cliente()
        elif opcion == "8":
            leer_inscripciones()
        elif opcion == "9":
            print("\n👋 Saliendo del programa...")
            break
        else:
            print("❌ Opción no válida.")

menu()
conexion.close()