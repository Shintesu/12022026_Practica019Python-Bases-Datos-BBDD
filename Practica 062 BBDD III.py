# Curso Python. BBDD III. Vídeo 57
# Claves principales en BBDD
# crear campo clave en las tablas e insertar

import sqlite3

MiConexion = sqlite3.connect("GestionProductos")

MiCursor = MiConexion.cursor()

# crear la tabla con los parámetros, incluido el parámetro clave // primary key debe añadirse al campo que queremos que sea clave------------------------------------------
#MiCursor.execute(''' 
    #CREATE TABLE PRODUCTOS (
    #CODIGO_ARTICULO VARCHAR (4) PRIMARY KEY,            
    #NOMBRE_ARTICULO VARCHAR(50),
    #PRECIO INTEGER,
    #SECCION VARCHAR(20))
#''')

# crear una lista con tuplas en su interior, cada una con un producto y su respectivo código------------------------------------------------------------------------------
#stock = [
    #("AR01", "Balón", 20, "Juguetería"),
    #("AR02", "Pantalón", 16, "Confección"),
    #("AR03", "Destornillador", 25, "Ferretería"),
    #("AR04", "Jarrón", 55, "Decorativos"),

#]

# ejecutar el script para crear la base de datos con la  tabla------------------------------------------------------------------------------------------------------------
#MiCursor.executemany("INSERT INTO PRODUCTOS VALUES (?, ?, ?, ?)", stock)


# insertar un producto con una clave nueva // y una repetida
MiCursor.execute("INSERT INTO PRODUCTOS VALUES ('AR05', 'Tren', '15', 'Jugueteria')")


MiConexion.commit()

MiConexion.close()