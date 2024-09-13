import ply.lex as lex

tokens = [
    'PALABRA_CLAVE_SELECT',
    'PALABRA_CLAVE_FROM',
    'PALABRA_CLAVE_WHERE',
    'PALABRA_CLAVE_INSERT',
    'PALABRA_CLAVE_INTO',
    'PALABRA_CLAVE_VALUES',
    'PALABRA_CLAVE_UPDATE',
    'PALABRA_CLAVE_SET',
    'PALABRA_CLAVE_DELETE',
    'PALABRA_CLAVE_CREATE',
    'PALABRA_CLAVE_DATABASE',
    'PALABRA_CLAVE_USE',
    'PALABRA_CLAVE_TABLE',
    'PALABRA_CLAVE_PRIMARY',
    'PALABRA_CLAVE_KEY',
    'PALABRA_CLAVE_FOREIGN',
    'PALABRA_CLAVE_NOT',
    'PALABRA_CLAVE_NULL',
    'PALABRA_CLAVE_JOIN',
    'PALABRA_CLAVE_LEFT',
    'PALABRA_CLAVE_RIGHT',
    'PALABRA_CLAVE_FULL',
    'PALABRA_CLAVE_UNION',
    'PALABRA_CLAVE_GROUP_BY',
    'PALABRA_CLAVE_HAVING',
    'PALABRA_CLAVE_ON',
    'PALABRA_CLAVE_DROP',
    'PALABRA_CLAVE_TRUNCATE',
    'PALABRA_CLAVE_ALTER',
    'PALABRA_CLAVE_MAX',
    'PALABRA_CLAVE_INNER',
    'PALABRA_CLAVE_MIN',
    'PALABRA_CLAVE_COUNT',
    'PALABRA_CLAVE_SUM',
    'PALABRA_CLAVE_AVG',
    'PALABRA_CLAVE_LIKE',
    'PALABRA_CLAVE_LIMIT',
    'PALABRA_CLAVE_IN',
    'PALABRA_CLAVE_BETWEEN',
    'PALABRA_CLAVE_AS',
    'PALABRA_CLAVE_EXISTS',
    'PALABRA_CLAVE_AND',
    'PALABRA_CLAVE_DESC',
    'PALABRA_CLAVE_ASC',
    'ID',
    'CADENA',
    'NUMERO_ENTERO',
    'NUMERO_DECIMAL',
    'OPERADOR',
    'NUEVA_LINEA',
    'TIPO_DATO',
    'PAR_IZQ',
    'PAR_DER',
    'FINAL',
    'COMA',
    'IGUAL',
    'COMPARADOR',
    'INT',
    'DOUBLE',
    'TEXT',
    'VARCHAR',
    'TIMESTAMP',
    'DATE',
    'DATETIME',
    'TINYINT',
]

palabras_clave = {
    'SELECT': 'PALABRA_CLAVE_SELECT',
    'FROM': 'PALABRA_CLAVE_FROM',
    'WHERE': 'PALABRA_CLAVE_WHERE',
    'INSERT': 'PALABRA_CLAVE_INSERT',
    'INTO': 'PALABRA_CLAVE_INTO',
    'VALUES': 'PALABRA_CLAVE_VALUES',
    'UPDATE': 'PALABRA_CLAVE_UPDATE',
    'SET': 'PALABRA_CLAVE_SET',
    'DELETE': 'PALABRA_CLAVE_DELETE',
    'CREATE': 'PALABRA_CLAVE_CREATE',
    'DATABASE': 'PALABRA_CLAVE_DATABASE',
    'USE': 'PALABRA_CLAVE_USE',
    'TABLE': 'PALABRA_CLAVE_TABLE',
    'PRIMARY': 'PALABRA_CLAVE_PRIMARY',
    'KEY': 'PALABRA_CLAVE_KEY',
    'FOREIGN': 'PALABRA_CLAVE_FOREIGN',
    'NOT': 'PALABRA_CLAVE_NOT',
    'NULL': 'PALABRA_CLAVE_NULL',
    'JOIN': 'PALABRA_CLAVE_JOIN',
    'LEFT': 'PALABRA_CLAVE_LEFT',
    'RIGHT': 'PALABRA_CLAVE_RIGHT',
    'FULL': 'PALABRA_CLAVE_FULL',
    'INNER': 'PALABRA_CLAVE_INNER',
    'UNION': 'PALABRA_CLAVE_UNION',
    'GROUP_BY': 'PALABRA_CLAVE_GROUP_BY',
    'HAVING': 'PALABRA_CLAVE_HAVING',
    'ON': 'PALABRA_CLAVE_ON',
    'DROP': 'PALABRA_CLAVE_DROP',
    'TRUNCATE': 'PALABRA_CLAVE_TRUNCATE',
    'ALTER': 'PALABRA_CLAVE_ALTER',
    'MAX': 'PALABRA_CLAVE_MAX',
    'MIN': 'PALABRA_CLAVE_MIN',
    'COUNT': 'PALABRA_CLAVE_COUNT',
    'SUM': 'PALABRA_CLAVE_SUM',
    'AVG': 'PALABRA_CLAVE_AVG',
    'LIKE': 'PALABRA_CLAVE_LIKE',
    'IN': 'PALABRA_CLAVE_IN',
    'BETWEEN': 'PALABRA_CLAVE_BETWEEN',
    'DESC': 'PALABRA_CLAVE_DESC',
    'ASC': 'PALABRA_CLAVE_ASC',
    'AS': 'PALABRA_CLAVE_AS',
    'EXISTS': 'PALABRA_CLAVE_EXISTS',
    'AND': 'PALABRA_CLAVE_AND',
    'LIMIT': 'PALABRA_CLAVE_LIMIT',
    'INT': 'INT',
    'DOUBLE': 'DOUBLE',
    'TEXT': 'TEXT',
    'VARCHAR': 'VARCHAR',
    'TIMESTAMP': 'TIMESTAMP',
    'DATE': 'DATE',
    'DATETIME': 'DATETIME',
    'TINYINT': 'TINYINT'
}

states = (
    ('IDS','inclusive'),
    ('OPERADORES','inclusive')
)

t_IGUAL = r'\='
t_DATE = r'\'\b\d{2}/\d{2}/\d{4}\b\''
t_CADENA = r'\'[^\']*\''
t_OPERADOR = r'[\+\-\/!]+'
t_FINAL = r'[;]'
t_COMA = r'[,]'
t_COMPARADOR = r'<=|>=|==|!=|<|>'

def t_NUMERO_DECIMAL(t):
    r'\b\d+\.\d+\b'
    t.value = float(t.value)
    return t

def t_NUMERO_ENTERO(t):
    r'\b\d+\b'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'([a-zA-Z_][a-zA-Z_]*\.[a-zA-Z_][a-zA-Z_]*) | ([a-zA-Z_][a-zA-Z_]*\.\*) | ([a-zA-Z_][a-zA-Z_]*)'
    t.type = palabras_clave.get(t.value.upper(), 'ID')
    if t.type == 'PALABRA_CLAVE_SELECT':
        t.lexer.begin('IDS')
    if t.type == 'PALABRA_CLAVE_FROM':
        t.lexer.begin('OPERADORES')
    return t


def t_IDS_ID(t):
    r'\*'
    t.type = 'ID'
    return t

def t_OPERADORES_ID(t):
    r'\*'
    t.type = 'OPERADOR'
    return t

def t_PAR_IZQ(t):
    r'\('
    t.type = 'PAR_IZQ'
    return t

def t_PAR_DER(t):
    r'\)'
    t.type = 'PAR_DER'
    return t

def t_NUEVA_LINEA(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')
    t.lexer.column = 1

t_ignore = ' \t'

def t_error(t):
    columna = encontrar_columna(t.lexer.lexdata, t)
    mensaje_error = f"Carácter ilegal '{t.value[0]}' en la línea {t.lineno}, posicion {columna}"
    t.lexer.errors.append(mensaje_error)
    t.lexer.skip(1)

def encontrar_columna(entrada, token):
    inicio_linea = entrada.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - inicio_linea) + 1

def tokenizar(codigo_sql):
    global posiciones
    lexer.input(codigo_sql)
    lexer.lineno = 1
    lexer.column = 1
    lexer.errors = []
    tokens = []
    posiciones = {}
    while True:
        tok = lexer.token()
        if not tok:
            break
        tok.column = encontrar_columna(lexer.lexdata, tok)
        tokens.append((tok.type, tok.value, tok.lineno, tok.column))
        posiciones[tok.lineno] = tok.column
    return tokens, lexer.errors, posiciones
posiciones = {}
lexer = lex.lex()
lexer.errors = []