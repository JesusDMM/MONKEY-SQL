import ply.yacc as yacc
from analizador_lexico import tokens, posiciones

global errores_programas
errores_programas = []

start = 'consulta'

def p_consulta(p):
    '''consulta : select_clause from_clause where_clause group_by
                | select_clause from_clause group_by 
                | select_clause from_clause where_clause
                | select_clause from_clause 
                | select_clause_sola'''
    if len(p) == 5:
        p[0] = ('CONSULTA', p[1], p[2], p[3], p[4])
    elif len(p) == 4:
        if p[3][0] == 'WHERE':
            p[0] = ('CONSULTA', p[1], p[2], p[3])
        else:
            p[0] = ('CONSULTA', p[1], p[2], p[3])
    elif len(p) == 3:
        p[0] = ('CONSULTA', p[1], p[2])
    else:
        p[0] = ('CONSULTA', p[1])

def p_group_by(p):
    '''group_by : PALABRA_CLAVE_GROUP_BY group_by_valor group_by_acomodo
                | PALABRA_CLAVE_GROUP_BY group_by_valor'''
    if len(p) == 4:
        p[0] = ('GROUP_BY', p[2], p[3])
    else:
        p[0] = ('GROUP_BY', p[2])

def p_group_by_valor(p):
    '''group_by_valor : ID
                      | ID COMA group_by_valor'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_group_by_acomodo(p):
    '''group_by_acomodo : PALABRA_CLAVE_DESC
                        | PALABRA_CLAVE_ASC'''
    p[0] = p[1]

def p_select_clause_sola(p):
    '''select_clause_sola : PALABRA_CLAVE_SELECT valor'''
    p[0] = ('SELECT', p[2])

# Clausula SELECT
def p_select_clause(p):
    '''select_clause : PALABRA_CLAVE_SELECT campos'''
    p[0] = ('SELECT', p[2])

def p_campos(p):
    '''campos : campo
              | campo COMA campos'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_campo(p):
    '''campo : ID
             | ID PALABRA_CLAVE_AS ID
             | funcion_agregada
             | funcion_agregada PALABRA_CLAVE_AS ID'''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = (p[1], p[2], p[3])

def p_funcion_agregada(p):
    '''funcion_agregada : PALABRA_CLAVE_AVG PAR_IZQ expression PAR_DER
                        | PALABRA_CLAVE_MAX PAR_IZQ expression PAR_DER
                        | PALABRA_CLAVE_MIN PAR_IZQ expression PAR_DER
                        | PALABRA_CLAVE_COUNT PAR_IZQ expression PAR_DER
                        | PALABRA_CLAVE_SUM PAR_IZQ expression PAR_DER'''
    p[0] = (p[1], p[3])

def p_expression(p):
    '''expression : ID
                  | NUMERO_ENTERO
                  | NUMERO_DECIMAL
                  | ID OPERADOR expression'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[1], p[2], p[3])

def p_id_lista(p):
    '''id_lista : ID
                | ID COMA id_lista'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_from_clause(p):
    '''from_clause : PALABRA_CLAVE_FROM id_lista joins
                   | PALABRA_CLAVE_FROM id_lista'''
    p.lineno = 2
    if len(p) == 3:
        p[0] = ('FROM', p[2])
    else:
        p[0] = ('FROM', p[2], p[3])

def p_joins(p):
    '''joins : join
             | join joins'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[2]

def p_join(p):
    '''join : join_type PALABRA_CLAVE_JOIN ID PALABRA_CLAVE_ON ID IGUAL ID
            | join_type PALABRA_CLAVE_JOIN ID ID PALABRA_CLAVE_ON ID IGUAL ID'''
    if len(p) == 8:
        p[0] = (p[1], 'JOIN', p[3], 'ON', p[5], p[6], p[7])
    else:
        p[0] = (p[1], 'JOIN', p[3], p[4], 'ON', p[6], p[7], p[8])

def p_join_type(p):
    '''join_type : PALABRA_CLAVE_LEFT
                 | PALABRA_CLAVE_RIGHT
                 | PALABRA_CLAVE_FULL
                 | PALABRA_CLAVE_INNER'''
    p[0] = p[1]

def p_where_clause(p):
    '''where_clause : PALABRA_CLAVE_WHERE condicion'''
    p[0] = ('WHERE', p[2])

def p_condicion(p):
    '''condicion : ID IGUAL datos
                 | ID PALABRA_CLAVE_IN datos
                 | ID COMPARADOR datos'''
    p[0] = (p[1], p[2], p[3])

def p_datos(p):
    '''datos : ID
             | valor
             | PAR_IZQ sub_consulta PAR_DER
             | valor OPERADOR datos
             | ID OPERADOR datos'''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4 and p[1] == '(':
        p[0] = ('SUBCONSULTA', p[2])
    else:
        p[0] = (p[1], p[2], p[3])

def p_sub_consulta(p):
    '''sub_consulta : select_clause_sola_sub from_clause where_clause group_by
                    | select_clause_sola_sub from_clause group_by
                    | select_clause_sola_sub from_clause where_clause
                    | select_clause_sola_sub from_clause'''
    if len(p) == 5:
        p[0] = ('SUBCONSULTA', p[1], p[2], p[3], p[4])
    elif len(p) == 4:
        p[0] = ('SUBCONSULTA', p[1], p[2], p[3])
    elif len(p) == 3:
        p[0] = ('SUBCONSULTA', p[1], p[2])
    else:
        p[0] = ('SUBCONSULTA', p[1])

def p_select_clause_sola_sub(p):
    '''select_clause_sola_sub : PALABRA_CLAVE_SELECT ID
                              | PALABRA_CLAVE_SELECT funcion_agregada'''
    p[0] = ('SELECT', p[2])

def p_valor(p):
    '''valor : NUMERO_ENTERO
             | NUMERO_DECIMAL
             | CADENA'''
    p[0] = p[1]

def p_error(p):
    global errores_programas
    if p:
        errores_programas.append(f"Sintaxis incorrecta en el token '{p.value}' en la línea {p.lineno}, posición {p.lexpos}.")
        #parser.errok()

parser = yacc.yacc(start = 'consulta')

def analizar_consulta(consulta):
    global errores_programas
    return parser.parse(consulta, tracking=True), errores_programas

        