import sqlite3

# Conectar a la base de datos (se crea si no existe)
conn = sqlite3.connect("gym_da2.db")
cursor = conn.cursor()

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

# Funciones CRUD


#Insertar,leer,borrar y  actualizar clientes

def insertar_cliente():
    nombre = input("Nombre del cliente: ")
    edad = input("Edad del cliente: ")
    cursor.execute("INSERT INTO Clientes (nombre, edad) VALUES (?, ?)", (nombre, edad))
    conn.commit()
    print("Cliente añadido.")

def leer_clientes():
    cursor.execute("SELECT * FROM Clientes")
    for fila in cursor.fetchall():
        print(fila)

def actualizar_cliente():
    id_cliente = input("ID del cliente a actualizar: ")
    nombre = input("Nuevo nombre: ")
    edad = input("Nueva edad: ")
    cursor.execute("UPDATE Clientes SET nombre = ?, edad = ? WHERE id = ?", (nombre, edad, id_cliente))
    conn.commit()
    print("Cliente actualizado.")

def borrar_cliente():
    id_cliente = input("ID del cliente a eliminar: ")
    cursor.execute("DELETE FROM Clientes WHERE id = ?", (id_cliente,))
    conn.commit()
    print("Cliente eliminado.")


#Funciones CRUD clases

#Insertar y leer clases

def insertar_clase():
    nombre = input("Nombre de la clase: ")
    horario = input("Horario de la clase: ")
    cursor.execute("INSERT INTO Clases (nombre, horario) VALUES (?, ?)", (nombre, horario))
    conn.commit()
    print("Clase añadida.")

def leer_clases():
    cursor.execute("SELECT * FROM Clases")
    for fila in cursor.fetchall():
        print(fila)