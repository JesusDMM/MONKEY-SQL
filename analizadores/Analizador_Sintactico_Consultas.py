import ply.yacc as yacc
from analizador_lexico import tokens, posiciones

global errores_programas
errores_programas = []

start = 'Inicio_consultas'

def p_Inicio_consultas(p):
    '''Inicio_consultas : PALABRA_CLAVE_SELECT select_intermedio_funciones
                        | PALABRA_CLAVE_SELECT select_intermedio 
                        | PALABRA_CLAVE_SELECT select_individual'''
    p[0] = ['Consulta', p[2]]
    
def p_select_intermedio_funciones(p):
    '''select_intermedio_funciones : columnas
                                     | columnas COMA Funcion_agregada'''
    if len(p) > 2: 
        p[0] = ('Operaciones', [p[1]] + p[3])
    else:
        p[0] = ('Consultas', p[1])
                
def p_Funcion_agregada(p):
    '''Funcion_agregada : PALABRA_CLAVE_AVG PAR_IZQ expresion PAR_DER
                        | PALABRA_CLAVE_MAX PAR_IZQ expresion PAR_DER
                        | PALABRA_CLAVE_MIN PAR_IZQ expresion PAR_DER
                        | PALABRA_CLAVE_COUNT PAR_IZQ expresion PAR_DER
                        | PALABRA_CLAVE_SUM PAR_IZQ expresion PAR_DER'''
    p[0] = p[3]

def p_expresion(p):
    '''expresion : ID
                    | valores
                    | ID OPERADOR expresion
                    | valores OPERADOR expresion'''
    if len(p) == 2:
        p[0] = [p[1]] + p[3]
    else:
        p[0] = p[1]

def p_select_intermedio(p):
    '''select_intermedio : columnas'''
    p[0] = ('Columnas', p[1])

def p_select_individual(p):
    '''select_individual : valores
                            | valores COMA valores'''
    if len(p) > 2:
        p[0] = p[1]
    else:
        p[0] = p[1] + p[3]
    
def p_valores(p):
    '''valores : DATE
               | NUMERO_ENTERO
               | NUMERO_DECIMAL
               | CADENA
               '''
    p[0] = p[1]

def p_columnas(p):
    '''columnas : ID
                | valores
                | ID COMA columnas
                | valores COMA columnas'''
    if len(p) > 2: 
        p[0] = [p[1]] + p[3]
    else:
        p[0] = [p[1]]

def p_error(p):
    global errores_programas
    if p:
        errores_programas.append(f"Error de sintaxis en el token '{p.value}'")
    else:
        errores_programas.append('Error de sintaxis, verifica tu código por favor :)')

parser = yacc.yacc(start='Inicio_consultas')

def analizar_consulta(consulta):
    global errores_programas
    errores_programas = []
    return parser.parse(consulta, tracking=True), errores_programas
