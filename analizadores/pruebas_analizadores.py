from analizador_lexico import *
from analizador_sintactico_DML import *
# from analizador_semantico import *
consulta = '''
            Select '88/88/8888', avg()
           '''
tokens, errores, tok = tokenizar(consulta)
arbol, errores_sintacticos = analizar_consulta(consulta)
# objeto = AnalizadorSemantico()
print(f'Tokens {tokens}')
print(f'errores {errores}')
print(f'arbol {arbol}')
print(f'errores sintactivos {errores_sintacticos}')
print(tok)
# if arbol != None:
#      objeto.analizar(arbol)
# else:
#     print('si')