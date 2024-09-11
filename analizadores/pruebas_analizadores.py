from analizador_lexico import *
from analizador_sintactico import *
from analizador_semantico import *
consulta = "SELECT EMPLEADO.ID FROM EMPLEADO "
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