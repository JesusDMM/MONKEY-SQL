class AnalizadorSemantico:
    def __init__(self):
        pass

    def analizar(self, arbol):
        self._analizar_nodo(arbol)

    def _analizar_nodo(self, nodo):
        if isinstance(nodo, tuple):
            tipo_nodo = nodo[0]
            if tipo_nodo == 'CONSULTA':
                print('consulta')
                self._analizar_consulta(nodo)
            else:
                print('otro nodo pa')

    def _analizar_consulta(self, nodo):
        for sub_nodo in nodo[1:]:
            if isinstance(sub_nodo, tuple):
                if sub_nodo[0] == 'FROM':
                    print('FROM')
                    self._analizar_from(sub_nodo)
                elif sub_nodo[0] == 'SELECT':
                    print('SELECT')
                    self._analizar_select(sub_nodo)
                elif sub_nodo[0] == 'WHERE':
                    print('WHERE')
                    self._analizar_where(sub_nodo)

    def _analizar_select(self, nodo):
        print(f'Analizando SELECT: {nodo}')

    def _analizar_from(self, nodo):
        print(f"Cláusula FROM detectada.")
        
        tablas = nodo[1]
        joins = nodo[2] if len(nodo) > 2 else None 

        print(f"Tablas involucradas: {tablas}")
        
        if joins:
            print("Join(s) detectado(s):")
            for join in joins:
                tipo_join = join[0]
                tabla_join = join[2]
                condicion = join[3:]
                print(f"{tipo_join} JOIN con la tabla {tabla_join} en la condición {condicion}")
        else:
            print("No se detectaron joins.")

    def _analizar_where(self, nodo):
        print(f'Analizando WHERE: {nodo}')
