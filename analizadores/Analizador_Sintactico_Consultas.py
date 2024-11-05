import ply.yacc as yacc # type: ignore
from analizador_lexico import tokens, posiciones

global errores_programas
errores_programas = []

start = 'Inicio_consultas'

def p_Inicio_consultas(p):
    '''Inicio_consultas : select from where group_by
                |select from where
                | select from group_by
                | select from 
                | select_individual'''
def p_select():
    

def p_select_individual():
    '''select_infividual : valores'''
    
def p_valores():
    '''valores : DATE
                | NUMERO_ENTERO
                | NUMERO_DECIMAL
                | CADENA
                | DATE COMA valores
                | NUMERO_ENTERO COMA valores
                | NUMERO_DECIMAL COMA valores
                | CADENA COMA valores'''


def p_error(p):
    global errores_programas
    if p:
        errores_programas.append(f"Sintaxis incorrecta en el token '{p.value}' en la línea {p.lineno}, posición {p.lexpos}.")
        parser.errok()
    else:
        errores_programas.append('Error de sintaxis, verifica tu codigo porfis :)')

parser = yacc.yacc(start = 'consulta')

def analizar_consulta(consulta):
    global errores_programas
    return parser.parse(consulta, tracking=True), errores_programas
