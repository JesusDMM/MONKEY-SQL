import json
import mysql.connector
from mysql.connector import errorcode

def conexion(direccion, usuario, contra, nombre_bd):
    conexion = None
    try:
        conexion = mysql.connector.connect(
            host=direccion,
            user=usuario,
            password=contra,
            database=nombre_bd
        )
        
        return conexion, True, ''
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            return conexion, False, "Usuario o contraseña incorrectos"
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            return conexion, False, "Base de datos no existe"
        else:
            return conexion, False, "Direccion incorrecta de host"

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
        #conexion.close()

    return estructura_bd

def obtener_consulta_bd(conexion, sql):
    json_data = None
    try:
        cursor = conexion.cursor()
        cursor.execute(sql)

        # Obtener los nombres de las columnas
        column_names = [desc[0] for desc in cursor.description]

        # Obtener los resultados de la consulta como una lista de diccionarios
        resultados = []
        for row in cursor:
            row_dict = dict(zip(column_names, row))
            resultados.append(row_dict)

        # Convertir la lista de diccionarios a formato JSON
        json_data = json.dumps(resultados)

        return json_data
    
    except:
        return json_data

    finally:
        cursor.close()