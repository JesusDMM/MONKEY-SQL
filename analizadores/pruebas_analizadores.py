from analizador_lexico import *
from Analizador_Sintactico_Consultas import *
consulta = '''select id from usuarios
           '''
tokens, errores, tok = tokenizar(consulta)
arbol, errores_sintacticos = analizar_consulta(consulta)
print(f'Tokens {tokens}')
print(f'errores {errores}')
print(f'arbol {arbol}')
print(f'errores sintactivos {errores_sintacticos}')