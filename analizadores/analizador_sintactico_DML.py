import ply.yacc as yacc
from analizador_lexico import tokens, posiciones

# Variable global para almacenar errores
global errores_programas
errores_programas = []

# Regla de inicio
start = 'dml'

# Producción inicial que cubre las operaciones DML
def p_dml(p):
    '''dml : insert_statement
           | update_statement
           | delete_statement'''
    p[0] = p[1]

# Producción para la operación INSERT
def p_insert_statement(p):
    '''insert_statement : PALABRA_CLAVE_INSERT PALABRA_CLAVE_INTO ID PAR_IZQ columnas PAR_DER PALABRA_CLAVE_VALUES PAR_IZQ valores PAR_DER'''
    p[0] = ('INSERT', p[3], p[5], p[10])

# Producción para la operación UPDATE
def p_update_statement(p):
    '''update_statement : PALABRA_CLAVE_UPDATE ID PALABRA_CLAVE_SET asignaciones where_clause'''
    p[0] = ('UPDATE', p[2], p[4], p[5])

# Producción para la operación DELETE
def p_delete_statement(p):
    '''delete_statement : PALABRA_CLAVE_DELETE PALABRA_CLAVE_FROM ID where_clause'''
    p[0] = ('DELETE', p[3], p[4])

# Producción para las columnas en INSERT
def p_columnas(p):
    '''columnas : ID
                | ID COMA columnas'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

# Producción para los valores en INSERT
def p_valores(p):
    '''valores : valor
               | valor COMA valores'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

# Producción para los valores individuales
def p_valor(p):
    '''valor : NUMERO_ENTERO
             | NUMERO_DECIMAL
             | CADENA'''
    p[0] = p[1]

# Producción para las asignaciones en UPDATE
def p_asignaciones(p):
    '''asignaciones : ID IGUAL valor
                    | ID IGUAL valor COMA asignaciones'''
    if len(p) == 4:
        p[0] = [(p[1], p[3])]
    else:
        p[0] = [(p[1], p[3])] + p[5]

# Producción para la cláusula WHERE (usada en UPDATE y DELETE)
def p_where_clause(p):
    '''where_clause : PALABRA_CLAVE_WHERE condicion
                    | empty'''
    if len(p) == 3:
        p[0] = ('WHERE', p[2])
    else:
        p[0] = None

# Producción para las condiciones del WHERE
def p_condicion(p):
    '''condicion : ID COMPARADOR valor'''
    p[0] = (p[1], p[2], p[3])

# Producción para manejar entradas vacías (opcional en WHERE)
def p_empty(p):
    '''empty :'''
    p[0] = None

# Manejador de errores
def p_error(p):
    global errores_programas
    if p:
        errores_programas.append(f"Sintaxis incorrecta en el token '{p.value}' en la línea {p.lineno}, posición {p.lexpos}.")
        yacc.errok()  # Manejo de errores
    else:
        errores_programas.append('Error de sintaxis, verifica tu código por favor.')

# Crear el parser
parser = yacc.yacc(start='dml')

# Función para analizar una consulta DML
def analizar_dml(consulta):
    global errores_programas
    return parser.parse(consulta, tracking=True), errores_programas
