import ply.yacc as yacc
from .analizador_lexico import tokens, posiciones

global errores_programas
errores_programas = []

def crear_parser():
    start = 'Inicio_consultas'
    
    #Metodo inicial, ajustes en select intermedio
    '''
    def p_Inicio_consultas(p):
        Inicio_consultas : PALABRA_CLAVE_SELECT select_intermedio_funciones
                            | PALABRA_CLAVE_SELECT select_intermedio 
                            | PALABRA_CLAVE_SELECT select_individual
        p[0] = ['Consulta', p[2]]
    '''
    
    def p_Inicio_consultas(p):
        '''Inicio_consultas : PALABRA_CLAVE_SELECT select_intermedio PALABRA_CLAVE_FROM from_individual
                            | PALABRA_CLAVE_SELECT select_individual'''
        if len(p) == 5:
            p[0] = ['Consulta', p[2], p[4]]
        else:
            p[0] = ['Consulta', p[2]]
        
    def p_from_individual(p):
        '''from_individual : tabla'''
        p[0] = ('Tablas', p[1])
        
    def p_tabla(p):
        '''tabla : ID
                   | ID COMA tabla'''
        if len(p) > 2: 
            p[0] = [p[1]] + p[3]
        else:
            p[0] = [p[1]]
        
    def p_select_intermedio_funciones(p):
        '''select_intermedio_funciones : columnas
                                        | columnas COMA Funcion_agregada'''
        p[0] = ('Operaciones', [p[1]])
                    
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
            p[0] = p[1]
        elif len(p) == 4:
            p[0] = [p[1]] + [p[3]]
        else:
            p[0] = p[1]


    def p_select_intermedio(p):
        '''select_intermedio : columnas'''
        p[0] = ('Columnas', p[1])
        
    def p_select_individual(p):
        '''select_individual : valores
                            | valores COMA valores'''
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = [p[1]] + p[3] if isinstance(p[3], list) else [p[1], p[3]]

        
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
            errores_programas.append(f"Error de sintaxis en el token {p.value}")
        else:
            errores_programas.append('Error de sintaxis, verifica tu código por favor :)')

    return yacc.yacc(start='Inicio_consultas')

def analizar_consulta(consulta):
    global errores_programas
    errores_programas = []
    parser = crear_parser()
    return parser.parse(consulta, tracking=True), errores_programas
