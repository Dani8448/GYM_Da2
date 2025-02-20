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
