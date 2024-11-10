from analizador_lexico import *
from Analizador_Sintactico_Consultas import *
consulta = '''select id, id, id, max(id), max(id), avg(nombre) from usuarios
           '''
tokens, errores, tok = tokenizar(consulta)
arbol, errores_sintacticos = analizar_consulta(consulta)
print(f'Tokens {tokens}')
print(f'errores {errores}')
print(f'arbol {arbol}')
print(f'errores sintactivos {errores_sintacticos}')

'''
if len(p) == 2:
            print(2)
            if isinstance(p[1], tuple) and p[1][0] in ['AVG', 'MAX', 'MIN', 'COUNT', 'SUM']:
                print(2.1)
                p[0] = ('Funciones', [p[1]])
            else:
                print(2.2)
                p[0] = ('Columnas', [p[1]])
        elif len(p) == 4: 
            print(4)
            if isinstance(p[1], tuple) and p[1][0] in ['AVG', 'MAX', 'MIN', 'COUNT', 'SUM']:
                p[0] = ('Funciones', [p[1]] + [p[3]])
            else:
                p[0] = ('Columnas', [p[1]] + [p[3]]) 
'''