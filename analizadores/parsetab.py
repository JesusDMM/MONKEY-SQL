
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'Inicio_consultasCADENA COMA COMPARADOR DATE DATETIME DOUBLE FINAL ID IGUAL INT NUEVA_LINEA NUMERO_DECIMAL NUMERO_ENTERO OPERADOR PALABRA_CLAVE_ALTER PALABRA_CLAVE_AND PALABRA_CLAVE_AS PALABRA_CLAVE_ASC PALABRA_CLAVE_AVG PALABRA_CLAVE_BETWEEN PALABRA_CLAVE_COUNT PALABRA_CLAVE_CREATE PALABRA_CLAVE_DATABASE PALABRA_CLAVE_DELETE PALABRA_CLAVE_DESC PALABRA_CLAVE_DROP PALABRA_CLAVE_EXISTS PALABRA_CLAVE_FOREIGN PALABRA_CLAVE_FROM PALABRA_CLAVE_FULL PALABRA_CLAVE_GROUP_BY PALABRA_CLAVE_HAVING PALABRA_CLAVE_IN PALABRA_CLAVE_INNER PALABRA_CLAVE_INSERT PALABRA_CLAVE_INTO PALABRA_CLAVE_JOIN PALABRA_CLAVE_KEY PALABRA_CLAVE_LEFT PALABRA_CLAVE_LIKE PALABRA_CLAVE_LIMIT PALABRA_CLAVE_MAX PALABRA_CLAVE_MIN PALABRA_CLAVE_NOT PALABRA_CLAVE_NULL PALABRA_CLAVE_ON PALABRA_CLAVE_PRIMARY PALABRA_CLAVE_RIGHT PALABRA_CLAVE_SELECT PALABRA_CLAVE_SET PALABRA_CLAVE_SUM PALABRA_CLAVE_TABLE PALABRA_CLAVE_TRUNCATE PALABRA_CLAVE_UNION PALABRA_CLAVE_UPDATE PALABRA_CLAVE_USE PALABRA_CLAVE_VALUES PALABRA_CLAVE_WHERE PAR_DER PAR_IZQ TEXT TIMESTAMP TINYINT TIPO_DATO VARCHARInicio_consultas : PALABRA_CLAVE_SELECT select_intermedio_funciones\n                        | PALABRA_CLAVE_SELECT select_intermedio \n                        | PALABRA_CLAVE_SELECT select_individualselect_intermedio_funciones : columnas\n                                     | columnas COMA Funcion_agregadaFuncion_agregada : PALABRA_CLAVE_AVG PAR_IZQ expresion PAR_DER\n                        | PALABRA_CLAVE_MAX PAR_IZQ expresion PAR_DER\n                        | PALABRA_CLAVE_MIN PAR_IZQ expresion PAR_DER\n                        | PALABRA_CLAVE_COUNT PAR_IZQ expresion PAR_DER\n                        | PALABRA_CLAVE_SUM PAR_IZQ expresion PAR_DERexpresion : ID\n                    | valores\n                    | ID OPERADOR expresion\n                    | valores OPERADOR expresionselect_intermedio : columnasselect_individual : valores\n                            | valores COMA valoresvalores : DATE\n               | NUMERO_ENTERO\n               | NUMERO_DECIMAL\n               | CADENA\n               columnas : ID\n                | valores\n                | ID COMA columnas\n                | valores COMA columnas'
    
_lr_action_items = {'PALABRA_CLAVE_SELECT':([0,],[2,]),'$end':([1,3,4,5,6,7,8,9,10,11,12,16,22,23,24,25,39,42,43,44,45,],[0,-1,-2,-3,-4,-16,-22,-18,-19,-20,-21,-5,-17,-25,-24,-23,-6,-7,-8,-9,-10,]),'ID':([2,14,15,26,27,28,29,30,31,40,41,],[8,8,8,33,33,33,33,33,8,33,33,]),'DATE':([2,14,15,26,27,28,29,30,31,40,41,],[9,9,9,9,9,9,9,9,9,9,9,]),'NUMERO_ENTERO':([2,14,15,26,27,28,29,30,31,40,41,],[10,10,10,10,10,10,10,10,10,10,10,]),'NUMERO_DECIMAL':([2,14,15,26,27,28,29,30,31,40,41,],[11,11,11,11,11,11,11,11,11,11,11,]),'CADENA':([2,14,15,26,27,28,29,30,31,40,41,],[12,12,12,12,12,12,12,12,12,12,12,]),'COMA':([6,7,8,9,10,11,12,22,23,24,25,],[13,14,15,-18,-19,-20,-21,31,-25,-24,31,]),'OPERADOR':([9,10,11,12,33,34,],[-18,-19,-20,-21,40,41,]),'PAR_DER':([9,10,11,12,32,33,34,35,36,37,38,46,47,],[-18,-19,-20,-21,39,-11,-12,42,43,44,45,-13,-14,]),'PALABRA_CLAVE_AVG':([13,],[17,]),'PALABRA_CLAVE_MAX':([13,],[18,]),'PALABRA_CLAVE_MIN':([13,],[19,]),'PALABRA_CLAVE_COUNT':([13,],[20,]),'PALABRA_CLAVE_SUM':([13,],[21,]),'PAR_IZQ':([17,18,19,20,21,],[26,27,28,29,30,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Inicio_consultas':([0,],[1,]),'select_intermedio_funciones':([2,],[3,]),'select_intermedio':([2,],[4,]),'select_individual':([2,],[5,]),'columnas':([2,14,15,31,],[6,23,24,23,]),'valores':([2,14,15,26,27,28,29,30,31,40,41,],[7,22,25,34,34,34,34,34,25,34,34,]),'Funcion_agregada':([13,],[16,]),'expresion':([26,27,28,29,30,40,41,],[32,35,36,37,38,46,47,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Inicio_consultas","S'",1,None,None,None),
  ('Inicio_consultas -> PALABRA_CLAVE_SELECT select_intermedio_funciones','Inicio_consultas',2,'p_Inicio_consultas','Analizador_Sintactico_Consultas.py',10),
  ('Inicio_consultas -> PALABRA_CLAVE_SELECT select_intermedio','Inicio_consultas',2,'p_Inicio_consultas','Analizador_Sintactico_Consultas.py',11),
  ('Inicio_consultas -> PALABRA_CLAVE_SELECT select_individual','Inicio_consultas',2,'p_Inicio_consultas','Analizador_Sintactico_Consultas.py',12),
  ('select_intermedio_funciones -> columnas','select_intermedio_funciones',1,'p_select_intermedio_funciones','Analizador_Sintactico_Consultas.py',16),
  ('select_intermedio_funciones -> columnas COMA Funcion_agregada','select_intermedio_funciones',3,'p_select_intermedio_funciones','Analizador_Sintactico_Consultas.py',17),
  ('Funcion_agregada -> PALABRA_CLAVE_AVG PAR_IZQ expresion PAR_DER','Funcion_agregada',4,'p_Funcion_agregada','Analizador_Sintactico_Consultas.py',24),
  ('Funcion_agregada -> PALABRA_CLAVE_MAX PAR_IZQ expresion PAR_DER','Funcion_agregada',4,'p_Funcion_agregada','Analizador_Sintactico_Consultas.py',25),
  ('Funcion_agregada -> PALABRA_CLAVE_MIN PAR_IZQ expresion PAR_DER','Funcion_agregada',4,'p_Funcion_agregada','Analizador_Sintactico_Consultas.py',26),
  ('Funcion_agregada -> PALABRA_CLAVE_COUNT PAR_IZQ expresion PAR_DER','Funcion_agregada',4,'p_Funcion_agregada','Analizador_Sintactico_Consultas.py',27),
  ('Funcion_agregada -> PALABRA_CLAVE_SUM PAR_IZQ expresion PAR_DER','Funcion_agregada',4,'p_Funcion_agregada','Analizador_Sintactico_Consultas.py',28),
  ('expresion -> ID','expresion',1,'p_expresion','Analizador_Sintactico_Consultas.py',32),
  ('expresion -> valores','expresion',1,'p_expresion','Analizador_Sintactico_Consultas.py',33),
  ('expresion -> ID OPERADOR expresion','expresion',3,'p_expresion','Analizador_Sintactico_Consultas.py',34),
  ('expresion -> valores OPERADOR expresion','expresion',3,'p_expresion','Analizador_Sintactico_Consultas.py',35),
  ('select_intermedio -> columnas','select_intermedio',1,'p_select_intermedio','Analizador_Sintactico_Consultas.py',42),
  ('select_individual -> valores','select_individual',1,'p_select_individual','Analizador_Sintactico_Consultas.py',46),
  ('select_individual -> valores COMA valores','select_individual',3,'p_select_individual','Analizador_Sintactico_Consultas.py',47),
  ('valores -> DATE','valores',1,'p_valores','Analizador_Sintactico_Consultas.py',54),
  ('valores -> NUMERO_ENTERO','valores',1,'p_valores','Analizador_Sintactico_Consultas.py',55),
  ('valores -> NUMERO_DECIMAL','valores',1,'p_valores','Analizador_Sintactico_Consultas.py',56),
  ('valores -> CADENA','valores',1,'p_valores','Analizador_Sintactico_Consultas.py',57),
  ('columnas -> ID','columnas',1,'p_columnas','Analizador_Sintactico_Consultas.py',62),
  ('columnas -> valores','columnas',1,'p_columnas','Analizador_Sintactico_Consultas.py',63),
  ('columnas -> ID COMA columnas','columnas',3,'p_columnas','Analizador_Sintactico_Consultas.py',64),
  ('columnas -> valores COMA columnas','columnas',3,'p_columnas','Analizador_Sintactico_Consultas.py',65),
]
