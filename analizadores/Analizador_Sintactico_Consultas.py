import ply.yacc as yacc
from .analizador_lexico import tokens, posiciones

global errores_programas
errores_programas = []

global lista_columnas
lista_columnas = []
global lista_funciones
lista_funciones = []

global operadores
operadores = ['+', '-', '*', '/']


def crear_parser():
    start = 'Inicio_consultas'
        
    def p_Inicio_consultas(p):
        '''Inicio_consultas : PALABRA_CLAVE_SELECT select_individual
                            | PALABRA_CLAVE_SELECT select_individual_funciones
                            | PALABRA_CLAVE_SELECT select_intermedio PALABRA_CLAVE_FROM from_individual PALABRA_CLAVE_WHERE where
                            | PALABRA_CLAVE_SELECT select_intermedio_funciones PALABRA_CLAVE_FROM from_individual
                            | PALABRA_CLAVE_SELECT select_intermedio PALABRA_CLAVE_FROM from_individual   
                            | PALABRA_CLAVE_SELECT select_finales_funciones PALABRA_CLAVE_FROM from_individual PALABRA_CLAVE_GROUP_BY datos_groupby
                            | PALABRA_CLAVE_SELECT select_finales_funciones PALABRA_CLAVE_FROM from_individual PALABRA_CLAVE_WHERE where PALABRA_CLAVE_GROUP_BY datos_groupby PALABRA_CLAVE_HAVING datos_having
                            '''
        if len(p) == 7:
            print('7')
            p[0] = ['Consulta', p[2], p[4], p[6]]
        if len(p) == 11:
            print('11')
            p[0] = ['Consulta', p[2], p[4], p[6], p[8], p[10]]
        if len(p) == 9:
            print('9')
            p[0] = ['Consulta', p[2], p[4], p[6], p[8]]
        elif len(p) == 5:
            print('5')
            p[0] = ['Consulta', p[2], p[4]]
        elif len(p) == 3:
            print('3')
            p[0] = ['Consulta', p[2]]
    
    def p_datos_having(p):
        '''datos_having : column_having '''
        p[0] = ('Columnas_having', p[1])
        #p[0] = [[p[1]] + p[4] if isinstance(p[4], list) else [p[1], p[4]]]
    
    def p_column_having(p):
        '''column_having : Funcion_agregada COMPARADOR valores'''
        p[0] = [p[1], p[3]]
        #p[0] = [[p[1]] + p[4] if isinstance(p[4], list) else [p[1], p[4]]]
            
    def p_select_intermedio(p):
        '''select_intermedio : columnas'''
        print('select intermedio ')
        p[0] = ('Columnas', p[1])
    
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
                | valores COMA columnas
                | ID OPERADOR ID
                | ID OPERADOR valores
                | valores OPERADOR valores
                | valores OPERADOR ID
                | ID OPERADOR ID COMA columnas
                | ID OPERADOR valores COMA columnas
                | valores OPERADOR valores COMA columnas
                | valores OPERADOR ID COMA columnas'''
        global operadores
        if len(p) > 2: 
            if p[2] in operadores:
                if len(p) > 5: 
                    print('operador')
                    #print(p[1])
                    #print(p[5])
                    p[0] = [flatten([p[1]] + [p[2]] + [p[3]])] + p[5]
                else:
                    p[0] = [flatten([p[1]] + [p[2]] + [p[3]])]
            else:
                print(' no operador')
                #print(p[1])
                #print(p[3])
                p[0] = [p[1]] + p[3]
        else:
            print('solo')
            print(p[1])
            p[0] = [p[1]]
    
    def p_datos_groupby(p):
        '''datos_groupby : INFO'''
        print('group')
        p[0] = ('Columnas_groupby', flatten(p[1]))
        
    
    def p_INFO(p):
        '''INFO : ID
                | ID COMA INFO'''
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = [[p[1]] + p[3] if isinstance(p[3], list) else [p[1], p[3]]]
            
    def p_select_individual_funciones(p):
        '''select_individual_funciones : Funcion_agregada_individual'''
        p[0] = ('funciones', p[1])
            
    def p_Funcion_agregada_individual(p):
        '''Funcion_agregada_individual : PALABRA_CLAVE_AVG PAR_IZQ expresion_individual PAR_DER
                            | PALABRA_CLAVE_MAX PAR_IZQ expresion_individual PAR_DER
                            | PALABRA_CLAVE_MIN PAR_IZQ expresion_individual PAR_DER
                            | PALABRA_CLAVE_COUNT PAR_IZQ expresion_individual PAR_DER
                            | PALABRA_CLAVE_SUM PAR_IZQ expresion_individual PAR_DER'''
        p[0] = (p[1].upper(), flatten(p[3]))
        
    def p_expresion_individual(p):
        '''expresion_individual : valores_funciones
                    | valores_funciones OPERADOR expresion_individual'''
        if len(p) == 2:
            p[0] = p[1]
        elif len(p) == 4:
            p[0] = [p[1]] + [p[3]]
    
    def p_valores_funciones(p):
        '''valores_funciones : NUMERO_ENTERO
                   | NUMERO_DECIMAL
                   '''
        p[0] = p[1]
    
    def p_select_intermedio_funciones(p):
        '''select_intermedio_funciones :  Funcion_agregada'''
        print('que onda')
        global lista_funciones
        try:
            if len(p) == 2:
                if isinstance(p[1], tuple) and p[1][0] in ['AVG', 'MAX', 'MIN', 'COUNT', 'SUM']:
                    print(2)
                    lista_funciones.append(p[1])
                    #p[0] = ('funciones', lista_funciones)
                    pass
            elif len(p) == 4: 
                if isinstance(p[1], tuple) and p[1][0] in ['AVG', 'MAX', 'MIN', 'COUNT', 'SUM']:
                    print(4)
                    lista_funciones.append(p[1])
                    #p[0] =  ('funciones', lista_funciones)
                    pass
            print(lista_funciones)
        finally:
            print(1)
            print(lista_funciones)
            p[0] = ('funciones', lista_funciones)
            
    def p_Funcion_agregada(p):
        '''Funcion_agregada : PALABRA_CLAVE_AVG PAR_IZQ expresion PAR_DER
                            | PALABRA_CLAVE_MAX PAR_IZQ expresion PAR_DER
                            | PALABRA_CLAVE_MIN PAR_IZQ expresion PAR_DER
                            | PALABRA_CLAVE_COUNT PAR_IZQ expresion PAR_DER
                            | PALABRA_CLAVE_SUM PAR_IZQ expresion PAR_DER'''
        p[0] = (p[1].upper(), flatten(p[3]))
        
    def p_expresion(p):
        '''expresion : ID
                    | valores_funciones
                    | ID OPERADOR expresion
                    | valores_funciones OPERADOR expresion'''
        if len(p) == 2:
            p[0] = p[1]
        elif len(p) == 4:
            p[0] = [p[1]] + [p[3]]
        
    def p_select_finales_funciones(p):
        '''select_finales_funciones :  ID COMA select_finales_funciones
                                        | valores COMA select_finales_funciones
                                        | Funcion_agregada COMA select_finales_funciones
                                        | ID
                                        | valores
                                        | Funcion_agregada'''
        global lista_funciones
        global lista_columnas
        try:
            if len(p) == 2:
                if isinstance(p[1], tuple) and p[1][0] in ['AVG', 'MAX', 'MIN', 'COUNT', 'SUM']:
                    print(2)
                    lista_funciones.append(p[1])
                    #p[0] = ('funciones', lista_funciones)
                    pass
                else:
                    print(p[1], 'columa')
                    lista_columnas.append(p[1])
                    #p[0] = ('columnas', lista_columnas) 
                    pass
            elif len(p) == 4: 
                if isinstance(p[1], tuple) and p[1][0] in ['AVG', 'MAX', 'MIN', 'COUNT', 'SUM']:
                    print(4)
                    lista_funciones.append(p[1])
                    #p[0] =  ('funciones', lista_funciones)
                    pass
                else:
                    print(p[1], 'columa')
                    lista_columnas.append(p[1])
                    #p[0] = ('columnas', lista_columnas) 
                    pass
        finally:
            print(1)
            print(lista_funciones)
            p[0] = ('Columnas', lista_columnas) + ('funciones', lista_funciones)
            
    def p_Funcion_agregada_final(p):
        '''Funcion_agregada_final : PALABRA_CLAVE_AVG PAR_IZQ expresion_final PAR_DER
                            | PALABRA_CLAVE_MAX PAR_IZQ expresion_final PAR_DER
                            | PALABRA_CLAVE_MIN PAR_IZQ expresion_final PAR_DER
                            | PALABRA_CLAVE_COUNT PAR_IZQ expresion_final PAR_DER
                            | PALABRA_CLAVE_SUM PAR_IZQ expresion_final PAR_DER'''
        p[0] = (p[1].upper(), p[3])
        
    def p_expresion_final(p):
        '''expresion_final : ID
                    | valores_funciones
                    | ID OPERADOR expresion_final
                    | valores_funciones OPERADOR expresion_final'''
        if len(p) == 2:
            p[0] = p[1]
        elif len(p) == 4:
            p[0] = [p[1]] + [p[3]]
    
    def p_where(p):
        '''where : condicion_where'''
        print('where')
        p[0] = ('Columnas_where_subconsultas', p[1])
    
    def p_condicion_where(p):
        '''condicion_where : ID IGUAL PAR_IZQ PALABRA_CLAVE_SELECT select_intermedio_funciones PALABRA_CLAVE_FROM from_individual PAR_DER '''
        p[0] = [p[1], p[5], p[7]]
        #p[0] = [p[1]] + [flatten([flatten(p[3])] if isinstance(p[3], list) else [[flatten(p[3])]])]  # Guarda la columna y el valor no numérico
    
    def p_datos_where(p):
        '''datos_where : ID
                | valores
                | valores OPERADOR datos_where
                | ID OPERADOR datos_where'''
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = [[p[1]] + [p[2]] + p[3] if isinstance(p[3], list) else [p[1], p[2], p[3]]]
        
    def p_from_individual(p):
        '''from_individual : tabla'''
        p[0] = ('Tablas', p[1])
        
    def p_tabla(p):
        '''tabla : ID
                   | ID COMA tabla'''
        print('tablas chidas')
        if len(p) > 2: 
            p[0] = [p[1]] + p[3]
        else:
            p[0] = [p[1]]
        
    def p_select_individual(p):
        '''select_individual : colum_indiv'''
        p[0] = ('Columnas', p[1])
        
    
    def p_colum_indiv(p):
        '''colum_indiv : valores
                            | valores COMA colum_indiv'''
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = [p[1]] + p[3] if isinstance(p[3], list) else [p[1], p[3]]
            
    def flatten(expresion):
        if isinstance(expresion, list):
            # Si la expresión es una lista, iteramos y aplanamos sus elementos recursivamente
            result = []
            for elem in expresion:
                result.extend(flatten(elem))
            return result
        else:
            # Si no es una lista, simplemente devolvemos el elemento
            return [expresion]
    
    def p_error(p):
        global errores_programas
        if p:
            errores_programas.append(f"Error de sintaxis en el token {p.value}")
        else:
            errores_programas.append('Error de sintaxis, verifica tu código por favor :)')

    return yacc.yacc(start='Inicio_consultas')

def analizar_consulta(consulta):
    global lista_columnas
    lista_columnas = []
    global lista_funciones
    lista_funciones = []

    global errores_programas
    errores_programas = []
    parser = crear_parser()
    return parser.parse(consulta, tracking=True), errores_programas
