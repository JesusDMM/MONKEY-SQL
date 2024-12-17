class AnalizadorSemantico:
    def __init__(self, estructura):
        self.estructura_bd = estructura
        self.errores = []
        self.tablas = []
        self.n_tablas = 0

    def analizar(self, arbol):
        self._analizar_nodo(arbol)

    def _analizar_nodo(self, nodo):
        if isinstance(nodo, list) and nodo[0] == 'Consulta':
            self._analizar_consulta(nodo)

    def _analizar_consulta(self, nodo):
        for sub_nodo in nodo[1:]:
            if isinstance(sub_nodo, tuple):
                if sub_nodo[0] == 'Tablas':
                    self._analizar_from(sub_nodo)
        
        for sub_nodo in nodo[1:]:
            if isinstance(sub_nodo, tuple):
                if sub_nodo[0] == 'Columnas_where':
                    self._veriricar_columnas(sub_nodo)
                    datos_where = sub_nodo[1]
                    print('Datos where:', datos_where)

                    if isinstance(datos_where, list):
                        for dato_where in datos_where:
                            print('datos where list ', dato_where)
                            if isinstance(dato_where, list):
                                self._veriricar_columnas(('columnas_where', dato_where))
                                self._veriricar_tipos_operaciones(('columnas_where', [dato_where]))
                                print()
        
        for sub_nodo in nodo[1:]:
            if isinstance(sub_nodo, tuple):
                if sub_nodo[0] == 'Columnas_groupby':
                    self._veriricar_columnas(sub_nodo)
                    
        for sub_nodo in nodo[1:]:
            if isinstance(sub_nodo, tuple):
                print('Verificando nodo:', sub_nodo)
                
                if sub_nodo[0] == 'Columnas':
                    self._veriricar_columnas(sub_nodo)
                    self._veriricar_tipos_operaciones(sub_nodo)
                
                if sub_nodo[0] == 'funciones':
                    print('Funciones encontradas:', sub_nodo[1])
                    funciones = sub_nodo[1]
                    if isinstance(funciones, list):
                        for funcion in funciones:
                            if isinstance(funcion, tuple):
                                nombre_funcion, valores = funcion
                                print(f"Función: {nombre_funcion}, Valores: {valores}")
                                self._veriricar_columnas(('funciones', valores))
                                self._veriricar_tipos_operaciones(('funciones', [valores]))
                
                if len(sub_nodo) > 2 and sub_nodo[2] == 'funciones':  
                    print('Funciones encontradas:', sub_nodo[3])
                    funciones = sub_nodo[3]
                    if isinstance(funciones, list):
                        for funcion in funciones:
                            if isinstance(funcion, tuple):
                                nombre_funcion, valores = funcion
                                print(f"Función: {nombre_funcion}, Valores: {valores}")
                                self._veriricar_columnas(('funciones', valores))
                                self._veriricar_tipos_operaciones(('funciones', [valores]))
    
    def _veriricar_tipos_operaciones(self, nodo):
        columnas = nodo[1] if len(nodo) > 1 else []
        operadores = ['+', '-', '*', '/']

        for columna in columnas:
            tipos_encontrados = []  # Lista para almacenar los tipos de datos
            print('Evaluando lista de operaciones:', columna)
            
            if isinstance(columna, list):  # Procesar cada lista
                for sub_columna in columna:
                    if sub_columna in operadores:  # Ignorar operadores
                        continue

                    # Determinar tipo de dato
                    if isinstance(sub_columna, str):
                        sub_columna = sub_columna.lower()
                        if sub_columna.startswith("'") and sub_columna.endswith("'"):
                            print(f"'{sub_columna}' es una cadena de texto (VARCHAR).")
                            tipos_encontrados.append('VARCHAR')
                        else:
                            nombre_tabla, bandera = self._encontrar_columna(sub_columna)
                            if not bandera:
                                print(f"'{sub_columna}' no es una columna de la tabla {nombre_tabla}.")
                                break
                            tipo_columna = next((tipo for columna, tipo in self.estructura_bd[nombre_tabla] if columna.lower() == sub_columna), None)
                            print(f'columna {sub_columna} tipo {tipo_columna}')
                            tipos_encontrados.append(tipo_columna)
                    
                    elif isinstance(sub_columna, int):
                        print(f"{sub_columna} es un número ENTERO (INT).")
                        tipos_encontrados.append('INT')

                    elif isinstance(sub_columna, float):
                        print(f"{sub_columna} es un número DECIMAL (FLOAT).")
                        tipos_encontrados.append('FLOAT')

                    else:
                        print(f"{sub_columna} es un tipo desconocido.")

                tipos_unicos = set(tipos_encontrados)
                if len(tipos_unicos) > 1:
                    print(f"Error: Tipos inconsistentes en la lista {columna}. Tipos encontrados: {tipos_unicos}")
                    self.errores.append(f"Tipos inconsistentes: {tipos_unicos} en el conjunto de operaciones {columna}")
                else:
                    if not tipos_unicos:
                        print('pila de datos vacia')
                    else:
                        print(f"Todos los elementos tienen el tipo '{tipos_unicos.pop()}' en la lista {columna}.")

                            
    def _encontrar_columna(self, columna):
                columna = columna.lower()

                if '.' in columna:
                    tabla_columna = columna.split('.')
                    tabla, col = tabla_columna
                    
                    tabla = tabla.lower()
                    col = col.lower()  
                    
                    if tabla in [t.lower() for t in self.estructura_bd.keys()]:
                        if tabla in [t.lower() for t in self.tablas]:
                            columnas_tabla = [c[0].lower() for c in self.estructura_bd[tabla]]
                            if col not in columnas_tabla and col != '*':
                                mensaje_error = f"La columna '{col}' no existe en la tabla '{tabla}'."
                                self.errores.append(mensaje_error)
                                return '', False
                        else:
                            mensaje_error = f"La tabla '{tabla}' existe en la bd pero no se agrego a la consulta."
                            self.errores.append(mensaje_error)
                            return '', False
                    else:
                        mensaje_error = f"La tabla '{tabla}' no se encuentra en la bd."
                        self.errores.append(mensaje_error)
                        return '', False
                    return tabla, True
                elif columna == '*':
                    if self.n_tablas > 1:
                        self.errores.append('Especificar tabla en el apartado *')
                        return False
                else:
                    if self.n_tablas > 1:
                        self.errores.append(f'Especificar tabla en el apartado {columna}')
                        return '', False
                    else:
                        for tabla in self.tablas:
                            tabla = tabla.lower()
                            columnas_tabla = [c[0].lower() for c in self.estructura_bd[tabla]]
                            if tabla not in [t.lower() for t in self.estructura_bd.keys()]:
                                mensaje_error = f"La columna {columna} no puede existir en la tabla {tabla} por que la tabla no existe."
                                self.errores.append(mensaje_error)
                                return '', False
                            else:
                                if columna not in columnas_tabla:
                                    mensaje_error = f"La columna '{columna}' no existe en la tabla '{tabla}'."
                                    self.errores.append(mensaje_error)
                                    return '', False
                            return tabla, True
                return True
    
    def _veriricar_columnas(self, nodo):
        columnas = nodo[1] if len(nodo) > 1 else []
        operadores = ['+', '-', '*', '/']
        print(f'columnas {columnas}')
        
        for columna in columnas:
            print('columna ', columna)
            if isinstance(columna, str) and columna not in operadores and not columna.startswith("'"):
                columna = columna.lower()

                if '.' in columna:
                    tabla_columna = columna.split('.')
                    tabla, col = tabla_columna
                    
                    tabla = tabla.lower()
                    col = col.lower()  
                    
                    if tabla in [t.lower() for t in self.estructura_bd.keys()]:
                        if tabla in [t.lower() for t in self.tablas]:
                            columnas_tabla = [c[0].lower() for c in self.estructura_bd[tabla]]
                            if col not in columnas_tabla and col != '*':
                                mensaje_error = f"La columna '{col}' no existe en la tabla '{tabla}'."
                                self.errores.append(mensaje_error)
                        else:
                            mensaje_error = f"La tabla '{tabla}' existe en la bd pero no se agrego a la consulta."
                            self.errores.append(mensaje_error)
                    else:
                        mensaje_error = f"La tabla '{tabla}' no se encuentra en la bd."
                        self.errores.append(mensaje_error)
                
                elif columna == '*':
                    if self.n_tablas > 1:
                        self.errores.append('Especificar tabla en el apartado *')
                else:
                    if self.n_tablas > 1:
                        self.errores.append(f'Especificar tabla en el apartado {columna}')
                    else:
                        for tabla in self.tablas:
                            tabla = tabla.lower()
                            columnas_tabla = [c[0].lower() for c in self.estructura_bd[tabla]]
                            if tabla not in [t.lower() for t in self.estructura_bd.keys()]:
                                mensaje_error = f"La columna {columna} no puede existir en la tabla {tabla} por que la tabla no existe."
                                self.errores.append(mensaje_error)
                            else:
                                if columna not in columnas_tabla:
                                    mensaje_error = f"La columna '{columna}' no existe en la tabla '{tabla}'."
                                    self.errores.append(mensaje_error)


    def _analizar_from(self, nodo):
        tablas = nodo[1] if len(nodo) > 1 else []
        
        self.n_tablas += len(tablas)
        for t in tablas:
            self.tablas.append(t)
        
        tablas_no_existentes = [tabla for tabla in tablas if tabla not in self.estructura_bd]

        if tablas_no_existentes:
            mensaje_error = f"Las tablas no existen en la base de datos: {tablas_no_existentes}"
            return self.errores.append(mensaje_error)

    def obtener_errores(self):
        return self.errores