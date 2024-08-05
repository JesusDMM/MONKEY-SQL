from analizador_lexico import *
consulta = '''
            CREATE DATABASE ESCUELA;
            USE ESCUELA;
            CREATE TABLE ALUMNO (
                ID INT NOT NULL PRIMARY KEY,
                NOMBRE TEXT NOT NULL,
                CARRERA TEXT NOT NULL
            );
           '''
tokens, errores = tokenizar(consulta)
print(f'Tokens {tokens}')
print(f'errores {errores}')