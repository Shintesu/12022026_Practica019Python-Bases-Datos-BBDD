# Curso Python. BBDD IV. Vídeo 58
# Cláusula UNIQUE

import sqlite3

MiConexion = sqlite3.connect("GestionProductos03")

MiCursor = MiConexion.cursor()

# crear la tabla con los parámetros, incluido el parámetro clave // primary key debe añadirse al campo que queremos que sea clave------------------------------------------
# la cláusula UNIQUE permite que no se repita la información de un campo específico
# se añade la cláusula a la clase de la tabla deseado
MiCursor.execute(''' 
    CREATE TABLE PRODUCTOS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,            
    NOMBRE_ARTICULO VARCHAR(50) UNIQUE,      
    PRECIO INTEGER,
    SECCION VARCHAR(20))
''')

# cuando se crea la lista al tener la clave automatizada ya no tiene sentido que la añadamos nosotros----------------------------------------------------------------------
stock = [
    ("Balón", 20, "Juguetería"),
    ("Pantalón", 16, "Confección"),
    ("Destornillador", 25, "Ferretería"),
    ("Jarrón", 55, "Decorativos"),
    ("Pantaones", 32, "Confección"),

]

# ejecutar el script para crear la base de datos con la  tabla------------------------------------------------------------------------------------------------------------
MiCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", stock)      # tenemos que considerar la cantidad de parámetros (?) necesarios 

MiConexion.commit()
MiConexion.close()

