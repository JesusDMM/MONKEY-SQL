import mysql.connector

def conexion(nombre_bd):
    conexion = None
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="JESUSdaniel444",
            database=nombre_bd
        )
        
        return conexion
    except:
        return conexion
        

def obtener_estructura_bd(conexion):

    estructura_bd = {}

    try:
        cursor = conexion.cursor()
        
        cursor.execute("SHOW TABLES")
        tablas = [tabla[0] for tabla in cursor.fetchall()]

        for tabla in tablas:
            
            cursor.execute(f"DESCRIBE {tabla}")
            columnas = [columna[0] for columna in cursor.fetchall()]

            estructura_bd[tabla] = columnas

    finally:
        
        cursor.close()
        conexion.close()

    return estructura_bd
