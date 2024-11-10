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
                print('Verificando nodo:', sub_nodo)
                
                if sub_nodo[0] == 'columnas':
                    self._analizar_select(sub_nodo)
                
                if len(sub_nodo) > 2 and sub_nodo[2] == 'funciones':  
                    print('Funciones encontradas:', sub_nodo[3])

    def _analizar_select(self, nodo):
        columnas = nodo[1] if len(nodo) > 1 else []
        
        for columna in columnas:
            if isinstance(columna, str):
                columna = columna.lower()

                if '.' in columna:
                    tabla_columna = columna.split('.')
                    tabla, col = tabla_columna
                    
                    tabla = tabla.lower()
                    col = col.lower()  
                    
                    if tabla in [t.lower() for t in self.estructura_bd.keys()]:
                        if tabla in [t.lower() for t in self.tablas]:
                            if col not in [c.lower() for c in self.estructura_bd[tabla]] and col != '*':
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
                            if tabla not in [t.lower() for t in self.estructura_bd.keys()]:
                                mensaje_error = f"La columna {columna} no puede existir en la tabla {tabla} por que la tabla no existe."
                                self.errores.append(mensaje_error)
                            else:
                                if columna not in [c.lower() for c in self.estructura_bd[tabla]]:
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