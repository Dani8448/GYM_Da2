import sqlite3

# Conectar a la base de datos (se crea si no existe)
conexion = sqlite3.connect("gym_da2.db")
cursor = conexion.cursor()

#Tabla cientes

cursor.execute("""
CREATE TABLE IF NOT EXISTS Clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    edad INTEGER
)
""")

#Tabla clases

cursor.execute("""
CREATE TABLE IF NOT EXISTS Clases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    horario TEXT
)
""")

#Tabla Inscripciones

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
# Funciones CRUD


#Insertar,leer,borrar y  actualizar clientes

def insertar_cliente():
    try:
        conexion.execute("BEGIN")
        nombre = input("Nombre del cliente: ")
        edad = input("Edad del cliente: ")
        cursor.execute("INSERT INTO Clientes (nombre, edad) VALUES (?, ?)", (nombre, edad))
        conexion.commit()
        print("Cliente añadido.")
    except Exception as e:
        conexion.rollback()
        print("Error:", e)
    finally:
        conexion.close()


def leer_cliente():
    try:
        propiedad = input("Consultar por (id/nombre): ")
        valor = input("Ingrese el valor: ")
        cursor.execute(f"SELECT * FROM Clientes WHERE {propiedad} = ?", (valor,))
        for fila in cursor.fetchall():
            print(fila)
    except Exception as e:
        print("Error:", e)
    finally:
        conexion.close()

def actualizar_cliente():
    try:
        conexion.execute("BEGIN")
        id_cliente = input("ID del cliente a actualizar: ")
        nombre = input("Nuevo nombre: ")
        edad = input("Nueva edad: ")
        cursor.execute("UPDATE Clientes SET nombre = ?, edad = ? WHERE id = ?", (nombre, edad, id_cliente))
        conexion.commit()
        print("Cliente actualizado.")
    except Exception as e:
        conexion.rollback()
        print("Error:", e)
    finally:
        conexion.close()

def borrar_cliente():
    try:
        conexion.execute("BEGIN")
        id_cliente = input("ID del cliente a eliminar: ")
        cursor.execute("DELETE FROM Clientes WHERE id = ?", (id_cliente,))
        conexion.commit()
        print("Cliente eliminado.")
    except Exception as e:
        conexion.rollback()
        print("Error:", e)
    finally:
        conexion.close()


#Funciones CRUD clases

#Insertar y leer clases

def insertar_clase():
    try:
        conexion.execute("BEGIN")
        nombre = input("Nombre de la clase: ")
        horario = input("Horario de la clase: ")
        cursor.execute("INSERT INTO Clases (nombre, horario) VALUES (?, ?)", (nombre, horario))
        conexion.commit()
        print("Clase añadida.")
    except Exception as e:
        conexion.rollback()
        print("Error:", e)
    finally:
        conexion.close()

def leer_clase():
    try:
        propiedad = input("Consultar por (id/nombre): ")
        valor = input("Ingrese el valor: ")
        cursor.execute(f"SELECT * FROM Clases WHERE {propiedad} = ?", (valor,))
        for fila in cursor.fetchall():
            print(fila)
    except Exception as e:
        print("Error:", e)
    finally:
        conexion.close()


#Funciones CRUD inscripciones

#Inscribir cliente y leer inscripciones

def inscribir_cliente():
    try:
        conexion.execute("BEGIN")
        id_cliente = input("ID del cliente: ")
        id_clase = input("ID de la clase: ")
        cursor.execute("INSERT INTO Inscripciones (cliente_id, clase_id) VALUES (?, ?)", (id_cliente, id_clase))
        conexion.commit()
        print("Cliente inscrito en la clase.")
    except Exception as e:
        conexion.rollback()
        print("Error:", e)
    finally:
        conexion.close()