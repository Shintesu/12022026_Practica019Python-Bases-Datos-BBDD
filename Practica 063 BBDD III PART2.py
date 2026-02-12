# Curso Python. BBDD III. Vídeo 57
# Claves principales en BBDD
# crear campo clave en las tablas e insertar

import sqlite3

MiConexion = sqlite3.connect("GestionProductos02")

MiCursor = MiConexion.cursor()

# crear la tabla con los parámetros, incluido el parámetro clave // primary key debe añadirse al campo que queremos que sea clave------------------------------------------
# al campo CODIGO_ARTÍCULO lo renombraremos como ID para estandarizar (ID INTEGER PRIMARY KEY AUTOINCREMENT= AUTOMATIZAR)
MiCursor.execute(''' 
    CREATE TABLE PRODUCTOS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,            
    NOMBRE_ARTICULO VARCHAR(50),
    PRECIO INTEGER,
    SECCION VARCHAR(20))
''')

# cuando se crea la lista al tener la clave automatizada ya no tiene sentido que la añadamos nosotros----------------------------------------------------------------------
stock = [
    ("Balón", 20, "Juguetería"),
    ("Pantalón", 16, "Confección"),
    ("Destornillador", 25, "Ferretería"),
    ("Jarrón", 55, "Decorativos"),

]

# ejecutar el script para crear la base de datos con la  tabla------------------------------------------------------------------------------------------------------------
MiCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", stock)      # tenemos que considerar la cantidad de parámetros (?) necesarios // NULL asocia el campo clave con el espacio vacío

MiConexion.commit()
MiConexion.close()