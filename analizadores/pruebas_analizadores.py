from analizador_lexico import *
from Analizador_Sintactico_Consultas import *
from analizador_semantico_pruebas import *
'''
'empleados': [
                'CustomerID',
                'CustomerName',
                'ContactName',
                'Address',
                'City',
                'PostalCode',
                'Country'
            ],
            'productos': [
                'ProductID',
                'ProductName',
                'SupplierID',
                'CategoryID',
                'Unit',
                'Price'
            ]
        }
'''
consulta = '''SELECT Productid, sum(productid + 1) from productos, productos where productmid = 1 + 'ds' group_by productid, idsss
'''
tokens, errores, tok = tokenizar(consulta)
arbol, errores_sintacticos = analizar_consulta(consulta)
objeto = AnalizadorSemantico()
analizador_semantico = objeto.analizar(arbol)    
errores_semanticos = objeto.errores
print(f'Tokens {tokens}')
print(f'errores {errores}')
print(f'arbol {arbol}')
print(f'errores sintactivos {errores_sintacticos}')
print(f'analizador semantico {analizador_semantico}')
print(f'errores semanticos {errores_semanticos}')

'''
if len(p) == 2:
            print(2)
            if isinstance(p[1], tuple) and p[1][0] in ['AVG', 'MAX', 'MIN', 'COUNT', 'SUM']:
                print(2.1)
                p[0] = ('Funciones', [p[1]])
            else:
                print(2.2)
                p[0] = ('Columnas', [p[1]])
        elif len(p) == 4: 
            print(4)
            if isinstance(p[1], tuple) and p[1][0] in ['AVG', 'MAX', 'MIN', 'COUNT', 'SUM']:
                p[0] = ('Funciones', [p[1]] + [p[3]])
            else:
                p[0] = ('Columnas', [p[1]] + [p[3]]) 
'''