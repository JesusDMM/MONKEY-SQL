class AnalizadorSemantico:
    def __init__(self):
        self.estructura_bd = {
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
                if sub_nodo[0] == 'Columnas':
                    self._analizar_select(sub_nodo)


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
                    
                    if tabla in [t.lower() for t in self.tablas]:
                        if col not in [c.lower() for c in self.estructura_bd[tabla]] and col != '*':
                            mensaje_error = f"La columna '{col}' no existe en la tabla '{tabla}'."
                            self.errores.append(mensaje_error)
                    else:
                        mensaje_error = f"La tabla '{tabla}' no está en la lista de tablas seleccionadas."
                        self.errores.append(mensaje_error)
                
                elif columna == '*':
                    if self.n_tablas > 1:
                        self.errores.append('Especificar tabla en el apartado *')
                else:
                    if self.n_tablas > 1:
                        print('h')
                        self.errores.append(f'Especificar tabla en el apartado {columna}')
                    else:
                        for tabla in self.tablas:
                            tabla = tabla.lower()
                            if columna not in [col.lower() for col in self.estructura_bd[tabla]]:
                                mensaje_error = f"La columna '{columna}' no existe en las tablas especificadas."
                                self.errores.append(mensaje_error)

    def _analizar_from(self, nodo):
        tablas = nodo[1] if len(nodo) > 1 else []
        
        self.n_tablas = len(tablas)
        self.tablas = [t.lower() for t in tablas]
        
        tablas_no_existentes = [tabla for tabla in tablas if tabla not in self.estructura_bd]

        if tablas_no_existentes:
            mensaje_error = f"Las tablas no existen en la base de datos: {tablas_no_existentes}"
            return self.errores.append(mensaje_error)

    def obtener_errores(self):
        return self.errores