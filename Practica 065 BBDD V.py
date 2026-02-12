# Curso Python. BBDD IV. Vídeo 58
# Operaciones CRUD (leer, actualizar y eliminar)

import sqlite3

MiConexion = sqlite3.connect("GestionProductos03")

MiCursor = MiConexion.cursor()

# leer usando los métodos SELECT * FROM y WHERE------------------------------------------------------------------------------------------------
#MiCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION= 'Confección'")
#productos = MiCursor.fetchall()      # imprimir los productos seleccionados
#print(productos)
 
# actualizar el precio de un producto----------------------------------------------------------------------------------------------------------
# se usan los métodos SET para actualizar un valor y WHERE para indicar cuál producto modificará su valor
#MiCursor.execute("UPDATE PRODUCTOS SET PRECIO= 35 WHERE NOMBRE_ARTICULO= 'Balón'")
#MiCursor.execute("UPDATE PRODUCTOS SET NOMBRE_ARTICULO= 'Pantalones' WHERE NOMBRE_ARTICULO= 'Pantaones'")

# borrar un registro---------------------------------------------------------------------------------------------------------------------------
MiCursor.execute("DELETE FROM PRODUCTOS WHERE NOMBRE_ARTICULO= 'Pantalones'")


MiConexion.commit()
MiConexion.close()