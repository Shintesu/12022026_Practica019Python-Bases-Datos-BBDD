# Curso Python. BBDD II. Vídeo 56
# Inserción de varios registros
# Recuperación de varios registros

import sqlite3                                                               # importar la librería SQLite3

# PASO 1: crear la base de datos
MiConexion = sqlite3.connect("Base1")  

# PASO 2: crear el cursor/puntero
MiCursor = MiConexion.cursor()                                                  # crear una variable cursor y asociarla a MiConexión con el método .cursor


# PASO 3: ejecutar el query (consultar) SQL
# 1. Insertar, Leer, Actualizar, Borrar (Create, Read, Update, Delete)
# MiCursor.execute("Create table Productos (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCAR(20))") # debemos invalidar esta línea luego de la primera ejecución para evitar un ERROR
#MiCursor.execute("INSERT INTO Productos VALUES('BALÓN', 15, 'DEPORTES')")      # insertar un registro
#MiConexion.commit()                                                            # se debe confirmar la acción anterior usando MiConexion     

#VariosProductos = [                                                            # crear una lista que albergue tuplas

    #("Camiseta", 19, "Deportes"),     
    #("Jarrón", 80, "Decorativos"), 
    #("Consola", 399, "Videojuegos"),
    #("Chaqueta", 16, "Moda")               
#]
#MiCursor.executemany("INSERT INTO Productos VALUES (?,?,?)", VariosProductos)  # método .executemany // "INSERT INTO NombreTabla VALUES (?,?,?)", NombreLista) // ?= parámetros a añadir


# leer información de la tabla
MiCursor.execute("SELECT * FROM Productos")    # usar la varible cursor con el método .execute con la instrucción del tipo SELECT * FROM NombreTabla
VariosProductos= MiCursor.fetchall() # almacenar los registros en una lista que llamaremos // fetchall retorna una lista
#print(VariosProductos)

# bucle for para que nos muestre la tabla elemento por elemento
for producto in VariosProductos:
    print("Nombre artículo: ", producto[0], " Precio: ", producto[1], " Sección: ", producto[2])     # usando el índice y string para dar forma al resultado del terminal

MiConexion.close()                                                             # ctrl b para ejecutar
