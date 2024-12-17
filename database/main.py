import json
import mysql.connector
from mysql.connector import errorcode
from decimal import Decimal

def mapear_tipo_dato(tipo_sql):
    
    if tipo_sql.startswith('int'):
        return 'INT'
    elif tipo_sql.startswith('varchar'):
        return 'VARCHAR'
    elif tipo_sql.startswith('float') or tipo_sql.startswith('double'):
        return 'FLOAT'
    elif tipo_sql.startswith('date'):
        return 'DATE'
    else:
        return tipo_sql


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
    """
    Extrae la estructura de la base de datos con los tipos de datos mapeados.
    """
    estructura_bd = {}

    try:
        cursor = conexion.cursor()
        cursor.execute("SHOW TABLES")
        tablas = [tabla[0] for tabla in cursor.fetchall()]

        for tabla in tablas:
            cursor.execute(f"DESCRIBE {tabla}")
            columnas = cursor.fetchall()
            # Mapeamos los nombres de columna y sus tipos
            estructura_bd[tabla] = [
                (columna[0], mapear_tipo_dato(columna[1])) for columna in columnas
            ]
    finally:
        cursor.close()

    return estructura_bd

def decimal_default(obj):
    if isinstance(obj, Decimal):
        return float(obj)  # Convertir Decimal a float
    raise TypeError("Type not serializable")  # Lanza un error si no es un tipo serializable

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

        # Convertir la lista de diccionarios a formato JSON usando 'default' para convertir Decimal
        json_data = json.dumps(resultados, default=decimal_default)

        return json_data
    
    except Exception as e:
        print(e)
        return json_data

    finally:
        cursor.close()
