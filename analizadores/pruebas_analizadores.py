from analizador_lexico import *
from analizador_sintactico import *
from analizador_semantico import *
consulta = "SELECT EMPLEADO.ID, SUM(EMPLEADO.NOMBRE + 5) FROM EMPLEADOS INNER JOIN CATEGORIAS ON EMPLEADOS.CATEGORIAS = CATEGORIAS.ID WHERE EMPLEADOS.ID > 5 "
tokens, errores, tok = tokenizar(consulta)
arbol, errores_sintacticos = analizar_consulta(consulta)
objeto = AnalizadorSemantico()
print(f'Tokens {tokens}')
print(f'errores {errores}')
print(f'arbol {arbol}')
print(f'errores sintactivos {errores_sintacticos}')
print(tok)
if arbol != None:
    objeto.analizar(arbol)
else:
    print('si')