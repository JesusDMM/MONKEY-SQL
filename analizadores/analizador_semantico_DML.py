class AnalizadorSemanticoDML:
    def __init__(self):
        pass

    def analizar(self, arbol):
        self._analizar_nodo(arbol)

    def _analizar_nodo(self, nodo):
        if isinstance(nodo, tuple):
            tipo_nodo = nodo[0]
            if tipo_nodo == 'INSERT':
                print('Operación INSERT detectada')
                self._analizar_insert(nodo)
            elif tipo_nodo == 'UPDATE':
                print('Operación UPDATE detectada')
                self._analizar_update(nodo)
            elif tipo_nodo == 'DELETE':
                print('Operación DELETE detectada')
                self._analizar_delete(nodo)
            else:
                print('Otro tipo de nodo')

    def _analizar_insert(self, nodo):
        """
        Analiza la operación INSERT.
        El nodo contiene la estructura del árbol para la operación INSERT.
        """
        print(f'Analizando INSERT: {nodo}')
        tabla = nodo[1]  # Tabla en la que se va a insertar
        columnas = nodo[2]  # Columnas afectadas
        valores = nodo[3]  # Valores a insertar

        print(f"Tabla: {tabla}")
        print(f"Columnas: {columnas}")
        print(f"Valores: {valores}")

    def _analizar_update(self, nodo):
        """
        Analiza la operación UPDATE.
        El nodo contiene la estructura del árbol para la operación UPDATE.
        """
        print(f'Analizando UPDATE: {nodo}')
        tabla = nodo[1]  # Tabla que se va a actualizar
        cambios = nodo[2]  # Cambios a realizar (columna=valor)
        where = nodo[3] if len(nodo) > 3 else None  # Condición WHERE

        print(f"Tabla: {tabla}")
        print(f"Cambios: {cambios}")
        
        if where:
            print(f"Condición WHERE: {where}")
        else:
            print("No se detectó condición WHERE.")

    def _analizar_delete(self, nodo):
        """
        Analiza la operación DELETE.
        El nodo contiene la estructura del árbol para la operación DELETE.
        """
        print(f'Analizando DELETE: {nodo}')
        tabla = nodo[1]  # Tabla de la que se van a eliminar los registros
        where = nodo[2] if len(nodo) > 2 else None  # Condición WHERE

        print(f"Tabla: {tabla}")
        
        if where:
            print(f"Condición WHERE: {where}")
        else:
            print("No se detectó condición WHERE.")

# Ejemplo de uso:
# arbol = ('INSERT', 'mi_tabla', ['col1', 'col2'], ['valor1', 'valor2'])
# arbol = ('UPDATE', 'mi_tabla', [('col1', 'nuevo_valor')], ('WHERE', 'col1 = valor1'))
# arbol = ('DELETE', 'mi_tabla', ('WHERE', 'col1 = valor1'))

analizador = AnalizadorSemanticoDML()
# Ejemplo para analizar un árbol de DML
arbol = ('INSERT', 'clientes', ['nombre', 'edad'], ['Juan', 30])
analizador.analizar(arbol)
