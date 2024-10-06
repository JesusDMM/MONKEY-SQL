
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'Inicio_consultasCADENA COMA COMPARADOR DATE DATETIME DOUBLE FINAL ID IGUAL INT NUEVA_LINEA NUMERO_DECIMAL NUMERO_ENTERO OPERADOR PALABRA_CLAVE_ALTER PALABRA_CLAVE_AND PALABRA_CLAVE_AS PALABRA_CLAVE_ASC PALABRA_CLAVE_AVG PALABRA_CLAVE_BETWEEN PALABRA_CLAVE_COUNT PALABRA_CLAVE_CREATE PALABRA_CLAVE_DATABASE PALABRA_CLAVE_DELETE PALABRA_CLAVE_DESC PALABRA_CLAVE_DROP PALABRA_CLAVE_EXISTS PALABRA_CLAVE_FOREIGN PALABRA_CLAVE_FROM PALABRA_CLAVE_FULL PALABRA_CLAVE_GROUP_BY PALABRA_CLAVE_HAVING PALABRA_CLAVE_IN PALABRA_CLAVE_INNER PALABRA_CLAVE_INSERT PALABRA_CLAVE_INTO PALABRA_CLAVE_JOIN PALABRA_CLAVE_KEY PALABRA_CLAVE_LEFT PALABRA_CLAVE_LIKE PALABRA_CLAVE_LIMIT PALABRA_CLAVE_MAX PALABRA_CLAVE_MIN PALABRA_CLAVE_NOT PALABRA_CLAVE_NULL PALABRA_CLAVE_ON PALABRA_CLAVE_PRIMARY PALABRA_CLAVE_RIGHT PALABRA_CLAVE_SELECT PALABRA_CLAVE_SET PALABRA_CLAVE_SUM PALABRA_CLAVE_TABLE PALABRA_CLAVE_TRUNCATE PALABRA_CLAVE_UNION PALABRA_CLAVE_UPDATE PALABRA_CLAVE_USE PALABRA_CLAVE_VALUES PALABRA_CLAVE_WHERE PAR_DER PAR_IZQ TEXT TIMESTAMP TINYINT TIPO_DATO VARCHARInicio_consultas : PALABRA_CLAVE_SELECT select_intermedio PALABRA_CLAVE_FROM from_individual\n                            | PALABRA_CLAVE_SELECT select_individualfrom_individual : tablatabla : ID\n                   | ID COMA tablaselect_intermedio_funciones : columnas\n                                        | columnas COMA Funcion_agregadaFuncion_agregada : PALABRA_CLAVE_AVG PAR_IZQ expresion PAR_DER\n                            | PALABRA_CLAVE_MAX PAR_IZQ expresion PAR_DER\n                            | PALABRA_CLAVE_MIN PAR_IZQ expresion PAR_DER\n                            | PALABRA_CLAVE_COUNT PAR_IZQ expresion PAR_DER\n                            | PALABRA_CLAVE_SUM PAR_IZQ expresion PAR_DERexpresion : ID\n                    | valores\n                    | ID OPERADOR expresion\n                    | valores OPERADOR expresionselect_intermedio : columnasselect_individual : valores\n                            | valores COMA valoresvalores : DATE\n                   | NUMERO_ENTERO\n                   | NUMERO_DECIMAL\n                   | CADENA\n                   columnas : ID\n                    | valores\n                    | ID COMA columnas\n                    | valores COMA columnas'
    
_lr_action_items = {'PALABRA_CLAVE_SELECT':([0,],[2,]),'$end':([1,4,6,8,9,10,11,15,16,17,18,24,],[0,-2,-18,-20,-21,-22,-23,-1,-3,-4,-19,-5,]),'ID':([2,12,13,14,22,23,],[7,17,7,7,17,7,]),'DATE':([2,13,14,23,],[8,8,8,8,]),'NUMERO_ENTERO':([2,13,14,23,],[9,9,9,9,]),'NUMERO_DECIMAL':([2,13,14,23,],[10,10,10,10,]),'CADENA':([2,13,14,23,],[11,11,11,11,]),'PALABRA_CLAVE_FROM':([3,5,6,7,8,9,10,11,18,19,20,21,],[12,-17,-25,-24,-20,-21,-22,-23,-25,-27,-26,-25,]),'COMA':([6,7,8,9,10,11,17,18,21,],[13,14,-20,-21,-22,-23,22,23,23,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Inicio_consultas':([0,],[1,]),'select_intermedio':([2,],[3,]),'select_individual':([2,],[4,]),'columnas':([2,13,14,23,],[5,19,20,19,]),'valores':([2,13,14,23,],[6,18,21,21,]),'from_individual':([12,],[15,]),'tabla':([12,22,],[16,24,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Inicio_consultas","S'",1,None,None,None),
  ('Inicio_consultas -> PALABRA_CLAVE_SELECT select_intermedio PALABRA_CLAVE_FROM from_individual','Inicio_consultas',4,'p_Inicio_consultas','Analizador_Sintactico_Consultas.py',20),
  ('Inicio_consultas -> PALABRA_CLAVE_SELECT select_individual','Inicio_consultas',2,'p_Inicio_consultas','Analizador_Sintactico_Consultas.py',21),
  ('from_individual -> tabla','from_individual',1,'p_from_individual','Analizador_Sintactico_Consultas.py',25),
  ('tabla -> ID','tabla',1,'p_tabla','Analizador_Sintactico_Consultas.py',29),
  ('tabla -> ID COMA tabla','tabla',3,'p_tabla','Analizador_Sintactico_Consultas.py',30),
  ('select_intermedio_funciones -> columnas','select_intermedio_funciones',1,'p_select_intermedio_funciones','Analizador_Sintactico_Consultas.py',37),
  ('select_intermedio_funciones -> columnas COMA Funcion_agregada','select_intermedio_funciones',3,'p_select_intermedio_funciones','Analizador_Sintactico_Consultas.py',38),
  ('Funcion_agregada -> PALABRA_CLAVE_AVG PAR_IZQ expresion PAR_DER','Funcion_agregada',4,'p_Funcion_agregada','Analizador_Sintactico_Consultas.py',42),
  ('Funcion_agregada -> PALABRA_CLAVE_MAX PAR_IZQ expresion PAR_DER','Funcion_agregada',4,'p_Funcion_agregada','Analizador_Sintactico_Consultas.py',43),
  ('Funcion_agregada -> PALABRA_CLAVE_MIN PAR_IZQ expresion PAR_DER','Funcion_agregada',4,'p_Funcion_agregada','Analizador_Sintactico_Consultas.py',44),
  ('Funcion_agregada -> PALABRA_CLAVE_COUNT PAR_IZQ expresion PAR_DER','Funcion_agregada',4,'p_Funcion_agregada','Analizador_Sintactico_Consultas.py',45),
  ('Funcion_agregada -> PALABRA_CLAVE_SUM PAR_IZQ expresion PAR_DER','Funcion_agregada',4,'p_Funcion_agregada','Analizador_Sintactico_Consultas.py',46),
  ('expresion -> ID','expresion',1,'p_expresion','Analizador_Sintactico_Consultas.py',50),
  ('expresion -> valores','expresion',1,'p_expresion','Analizador_Sintactico_Consultas.py',51),
  ('expresion -> ID OPERADOR expresion','expresion',3,'p_expresion','Analizador_Sintactico_Consultas.py',52),
  ('expresion -> valores OPERADOR expresion','expresion',3,'p_expresion','Analizador_Sintactico_Consultas.py',53),
  ('select_intermedio -> columnas','select_intermedio',1,'p_select_intermedio','Analizador_Sintactico_Consultas.py',63),
  ('select_individual -> valores','select_individual',1,'p_select_individual','Analizador_Sintactico_Consultas.py',67),
  ('select_individual -> valores COMA valores','select_individual',3,'p_select_individual','Analizador_Sintactico_Consultas.py',68),
  ('valores -> DATE','valores',1,'p_valores','Analizador_Sintactico_Consultas.py',76),
  ('valores -> NUMERO_ENTERO','valores',1,'p_valores','Analizador_Sintactico_Consultas.py',77),
  ('valores -> NUMERO_DECIMAL','valores',1,'p_valores','Analizador_Sintactico_Consultas.py',78),
  ('valores -> CADENA','valores',1,'p_valores','Analizador_Sintactico_Consultas.py',79),
  ('columnas -> ID','columnas',1,'p_columnas','Analizador_Sintactico_Consultas.py',84),
  ('columnas -> valores','columnas',1,'p_columnas','Analizador_Sintactico_Consultas.py',85),
  ('columnas -> ID COMA columnas','columnas',3,'p_columnas','Analizador_Sintactico_Consultas.py',86),
  ('columnas -> valores COMA columnas','columnas',3,'p_columnas','Analizador_Sintactico_Consultas.py',87),
]
