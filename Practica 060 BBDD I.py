# Curso Python. BBDD I. Vídeo 55
# Creación de BBDD: Conexión con BBDD - Inserción de registros en BBDD.

import sqlite3                                                               # importar la librería SQLite3

# PASO 1: crear la base de datos
MiConexion = sqlite3.connect("Base1")  

# PASO 2: crear el cursor/puntero
MiCursor = MiConexion.cursor()                                               # crear una variable cursor y asociarla a MiConexión con el método .cursor

# PASO 3: ejecutar el query (consultar) SQL
# 1. Insertar, Leer, Actualizar, Borrar (Create, Read, Update, Delete)
# MiCursor.execute("Create table Productos (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCAR(20))") # debemos invalidar esta línea luego de la primera ejecución para evitar un ERROR
MiCursor.execute("INSERT INTO Productos VALUES('BALÓN', 15, 'DEPORTES')")    # insertar un registro
MiConexion.commit()                                                          # se debe confirmar la acción anterior usando MiConexion           


MiConexion.close()                                                           # ctrl b para ejecutar



