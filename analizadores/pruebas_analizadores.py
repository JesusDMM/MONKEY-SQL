from analizador_lexico import *
from Analizador_Sintactico_Consultas import *
from analizador_semantico_Consultas import *
#(SELECT AVG(salario) FROM empleados)
consulta = '''SELECT * FROM empleados WHERE salario > (SELECT AVG(salario) FROM empleados)
'''
tokens, errores, tok = tokenizar(consulta)
arbol, errores_sintacticos = analizar_consulta(consulta)
'''
objeto = AnalizadorSemantico()
analizador_semantico = objeto.analizar(arbol)    
errores_semanticos = objeto.errores
'''
print(f'Tokens {tokens}')
print(f'errores {errores}')
print(f'arbol {arbol}')
print(f'errores sintactivos {errores_sintacticos}')
'''
print(f'analizador semantico {analizador_semantico}')
print(f'errores semanticos {errores_semanticos}')
'''
