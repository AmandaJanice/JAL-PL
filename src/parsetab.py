
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

<<<<<<< HEAD
_lr_signature = 'BODY COLON COMMA CREATEDATA CREATESERVER EQUAL HELP HTTPGET ID INT JSON LC LP OBJECT PORT RC READDATA RP SEMICOLON SETROUTES START STRING URLExp : HELPExp : ID EQUAL JSON COLON LC RC SEMICOLONExp : ID EQUAL ID SEMICOLONExp : ID EQUAL INT SEMICOLONExp : ID EQUAL JSON COLON LC Inside RC SEMICOLONInside : InsideRecInside :  STRING COLON STRING InsideRec : Inside COMMA Inside Exp : ID SEMICOLONExp : ID EQUAL CREATESERVER LP PORT EQUAL INT RP SEMICOLONExp : ID EQUAL CREATESERVER LP RP SEMICOLONExp : ID COLON START SEMICOLONExp : ID EQUAL HTTPGET LP URL EQUAL STRING RP SEMICOLONExp : HTTPGET LP URL EQUAL STRING RP SEMICOLONExp : ID EQUAL ID COLON SETROUTES LP URL EQUAL STRING RP SEMICOLONExp : ID COLON READDATA LP BODY EQUAL ID RP SEMICOLONExp : ID EQUAL ID COLON CREATEDATA LP OBJECT EQUAL ID RP SEMICOLONExp : ID EQUAL ID COLON READDATA LP BODY EQUAL ID RP SEMICOLONExp : ID COLON CREATEDATA LP OBJECT EQUAL ID RP SEMICOLONExp : ID COLON SETROUTES LP URL EQUAL STRING RP COLON READDATA LP BODY EQUAL ID RP SEMICOLONExp : ID COLON SETROUTES LP URL EQUAL STRING RP COLON CREATEDATA LP OBJECT EQUAL ID RP SEMICOLON'
    
_lr_action_items = {'HELP':([0,],[2,]),'ID':([0,5,51,52,69,70,99,100,],[3,9,64,65,80,81,101,102,]),'HTTPGET':([0,5,],[4,13,]),'$end':([1,2,7,19,22,25,49,58,67,71,82,83,84,85,92,93,94,105,106,],[0,-1,-9,-3,-4,-12,-11,-2,-14,-5,-10,-13,-16,-19,-15,-17,-18,-20,-21,]),'EQUAL':([3,18,34,36,37,38,39,55,56,57,97,98,],[5,29,48,50,51,52,53,68,69,70,99,100,]),'SEMICOLON':([3,9,11,14,35,44,54,59,74,75,76,77,87,88,89,103,104,],[7,19,22,25,49,58,67,71,82,83,84,85,92,93,94,105,106,]),'COLON':([3,9,10,47,78,],[6,20,21,61,86,]),'LP':([4,12,13,15,16,17,30,31,32,90,91,],[8,23,24,26,27,28,41,42,43,95,96,]),'JSON':([5,],[10,]),'INT':([5,48,],[11,62,]),'CREATESERVER':([5,],[12,]),'START':([6,],[14,]),'READDATA':([6,20,86,],[15,32,90,]),'CREATEDATA':([6,20,86,],[16,31,91,]),'SETROUTES':([6,20,],[17,30,]),'URL':([8,24,28,41,],[18,36,39,55,]),'LC':([21,],[33,]),'PORT':([23,],[34,]),'RP':([23,40,62,63,64,65,66,79,80,81,101,102,],[35,54,74,75,76,77,78,87,88,89,103,104,]),'BODY':([26,43,95,],[37,57,97,]),'OBJECT':([27,42,96,],[38,56,98,]),'STRING':([29,33,50,53,60,61,68,],[40,47,63,66,47,73,79,]),'RC':([33,45,46,72,73,],[44,59,-6,-8,-7,]),'COMMA':([45,46,72,73,],[60,-6,60,-7,]),}
=======
_lr_signature = 'BODY COLON COMMA CREATEDATA CREATESERVER EQUAL HELP HTTPGET ID INT JSON LC LP OBJECT PORT RC READDATA RP SEMICOLON SETROUTES START STRING URLExp : HELPExp : ID EQUAL JSON COLON LC RC SEMICOLONExp : ID EQUAL JSON COLON LC Inside RC SEMICOLONExp : ID EQUAL JSON COLON LC InsideRec RC SEMICOLONInside :  STRING COLON STRING InsideRec : Inside COMMA Inside COMMA InsideExp : ID SEMICOLONExp : ID EQUAL CREATESERVER LP PORT EQUAL INT RP SEMICOLONExp : ID EQUAL CREATESERVER LP RP SEMICOLONExp : ID COLON START SEMICOLONExp : ID EQUAL HTTPGET LP URL EQUAL STRING RP SEMICOLONExp : HTTPGET LP URL EQUAL STRING RP SEMICOLONExp : ID EQUAL ID COLON SETROUTES LP URL EQUAL STRING RP SEMICOLONExp : ID COLON READDATA LP BODY EQUAL ID RP SEMICOLONExp : ID EQUAL ID COLON READDATA LP BODY EQUAL ID RP SEMICOLONExp : ID COLON CREATEDATA LP OBJECT EQUAL ID RP SEMICOLONExp : ID COLON SETROUTES LP URL EQUAL STRING RP COLON READDATA LP BODY EQUAL ID RP SEMICOLONExp : ID COLON SETROUTES LP URL EQUAL STRING RP COLON CREATEDATA LP OBJECT EQUAL ID RP SEMICOLONExp : ID COLON SETROUTES LP URL EQUAL STRING RP SEMICOLON'
    
_lr_action_items = {'HELP':([0,],[2,]),'ID':([0,5,46,47,64,94,95,],[3,9,59,60,75,96,97,]),'HTTPGET':([0,5,],[4,12,]),'$end':([1,2,7,22,44,52,62,65,67,77,78,79,80,82,88,89,100,101,],[0,-1,-7,-10,-9,-2,-12,-3,-4,-8,-11,-14,-16,-19,-13,-15,-17,-18,]),'EQUAL':([3,17,30,32,33,34,35,50,51,92,93,],[5,26,43,45,46,47,48,63,64,94,95,]),'SEMICOLON':([3,13,31,39,49,53,55,69,70,71,72,73,83,84,98,99,],[7,22,44,52,62,65,67,77,78,79,80,82,88,89,100,101,]),'COLON':([3,9,10,42,73,],[6,18,19,56,81,]),'LP':([4,11,12,14,15,16,27,28,86,87,],[8,20,21,23,24,25,37,38,90,91,]),'JSON':([5,],[10,]),'CREATESERVER':([5,],[11,]),'START':([6,],[13,]),'READDATA':([6,18,81,],[14,28,86,]),'CREATEDATA':([6,81,],[15,87,]),'SETROUTES':([6,18,],[16,27,]),'URL':([8,21,25,37,],[17,32,35,50,]),'LC':([19,],[29,]),'PORT':([20,],[30,]),'RP':([20,36,57,58,59,60,61,74,75,96,97,],[31,49,69,70,71,72,73,83,84,98,99,]),'BODY':([23,38,90,],[33,51,92,]),'OBJECT':([24,91,],[34,93,]),'STRING':([26,29,45,48,54,56,63,76,],[36,42,58,61,42,68,74,42,]),'RC':([29,40,41,68,85,],[39,53,55,-5,-6,]),'COMMA':([40,66,68,],[54,76,-5,]),'INT':([43,],[57,]),}
>>>>>>> add-grammar

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

<<<<<<< HEAD
_lr_goto_items = {'Exp':([0,],[1,]),'Inside':([33,60,],[45,72,]),'InsideRec':([33,60,],[46,46,]),}
=======
_lr_goto_items = {'Exp':([0,],[1,]),'Inside':([29,54,76,],[40,66,85,]),'InsideRec':([29,],[41,]),}
>>>>>>> add-grammar

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Exp","S'",1,None,None,None),
  ('Exp -> HELP','Exp',1,'p_help','ViSeParser.py',10),
<<<<<<< HEAD
  ('Exp -> ID EQUAL JSON COLON LC RC SEMICOLON','Exp',7,'p_object_def_empty','ViSeParser.py',15),
  ('Exp -> ID EQUAL ID SEMICOLON','Exp',4,'p_id_id','ViSeParser.py',21),
  ('Exp -> ID EQUAL INT SEMICOLON','Exp',4,'p_id_int','ViSeParser.py',30),
  ('Exp -> ID EQUAL JSON COLON LC Inside RC SEMICOLON','Exp',8,'p_object_def','ViSeParser.py',36),
  ('Inside -> InsideRec','Inside',1,'p_inside_object_rec','ViSeParser.py',42),
  ('Inside -> STRING COLON STRING','Inside',3,'p_inside_object','ViSeParser.py',47),
  ('InsideRec -> Inside COMMA Inside','InsideRec',3,'p_inside_rec','ViSeParser.py',52),
  ('Exp -> ID SEMICOLON','Exp',2,'p_variable','ViSeParser.py',57),
  ('Exp -> ID EQUAL CREATESERVER LP PORT EQUAL INT RP SEMICOLON','Exp',9,'p_create_server','ViSeParser.py',68),
  ('Exp -> ID EQUAL CREATESERVER LP RP SEMICOLON','Exp',6,'p_create_server_empty_port','ViSeParser.py',73),
  ('Exp -> ID COLON START SEMICOLON','Exp',4,'p_server_start','ViSeParser.py',78),
  ('Exp -> ID EQUAL HTTPGET LP URL EQUAL STRING RP SEMICOLON','Exp',9,'p_communicate_id','ViSeParser.py',86),
  ('Exp -> HTTPGET LP URL EQUAL STRING RP SEMICOLON','Exp',7,'p_communicate','ViSeParser.py',92),
  ('Exp -> ID EQUAL ID COLON SETROUTES LP URL EQUAL STRING RP SEMICOLON','Exp',11,'p_server_sets','ViSeParser.py',97),
  ('Exp -> ID COLON READDATA LP BODY EQUAL ID RP SEMICOLON','Exp',9,'p_server_reads','ViSeParser.py',106),
  ('Exp -> ID EQUAL ID COLON CREATEDATA LP OBJECT EQUAL ID RP SEMICOLON','Exp',11,'p_server_creates_id','ViSeParser.py',115),
  ('Exp -> ID EQUAL ID COLON READDATA LP BODY EQUAL ID RP SEMICOLON','Exp',11,'p_server_read_id','ViSeParser.py',125),
  ('Exp -> ID COLON CREATEDATA LP OBJECT EQUAL ID RP SEMICOLON','Exp',9,'p_server_creates','ViSeParser.py',135),
  ('Exp -> ID COLON SETROUTES LP URL EQUAL STRING RP COLON READDATA LP BODY EQUAL ID RP SEMICOLON','Exp',16,'p_set_routes_read','ViSeParser.py',145),
  ('Exp -> ID COLON SETROUTES LP URL EQUAL STRING RP COLON CREATEDATA LP OBJECT EQUAL ID RP SEMICOLON','Exp',16,'p_set_routes_create','ViSeParser.py',155),
=======
  ('Exp -> ID EQUAL JSON COLON LC RC SEMICOLON','Exp',7,'p_object_def_empty','ViSeParser.py',14),
  ('Exp -> ID EQUAL JSON COLON LC Inside RC SEMICOLON','Exp',8,'p_object_def','ViSeParser.py',20),
  ('Exp -> ID EQUAL JSON COLON LC InsideRec RC SEMICOLON','Exp',8,'p_object_def_rec','ViSeParser.py',26),
  ('Inside -> STRING COLON STRING','Inside',3,'p_inside_object','ViSeParser.py',32),
  ('InsideRec -> Inside COMMA Inside COMMA Inside','InsideRec',5,'p_inside_rec','ViSeParser.py',37),
  ('Exp -> ID SEMICOLON','Exp',2,'p_variable','ViSeParser.py',42),
  ('Exp -> ID EQUAL CREATESERVER LP PORT EQUAL INT RP SEMICOLON','Exp',9,'p_create_server','ViSeParser.py',53),
  ('Exp -> ID EQUAL CREATESERVER LP RP SEMICOLON','Exp',6,'p_create_server_empty_port','ViSeParser.py',58),
  ('Exp -> ID COLON START SEMICOLON','Exp',4,'p_server_start','ViSeParser.py',63),
  ('Exp -> ID EQUAL HTTPGET LP URL EQUAL STRING RP SEMICOLON','Exp',9,'p_communicate_id','ViSeParser.py',71),
  ('Exp -> HTTPGET LP URL EQUAL STRING RP SEMICOLON','Exp',7,'p_communicate','ViSeParser.py',77),
  ('Exp -> ID EQUAL ID COLON SETROUTES LP URL EQUAL STRING RP SEMICOLON','Exp',11,'p_server_sets','ViSeParser.py',82),
  ('Exp -> ID COLON READDATA LP BODY EQUAL ID RP SEMICOLON','Exp',9,'p_server_reads','ViSeParser.py',91),
  ('Exp -> ID EQUAL ID COLON READDATA LP BODY EQUAL ID RP SEMICOLON','Exp',11,'p_server_read_id','ViSeParser.py',100),
  ('Exp -> ID COLON CREATEDATA LP OBJECT EQUAL ID RP SEMICOLON','Exp',9,'p_server_creates','ViSeParser.py',110),
  ('Exp -> ID COLON SETROUTES LP URL EQUAL STRING RP COLON READDATA LP BODY EQUAL ID RP SEMICOLON','Exp',16,'p_set_routes_read','ViSeParser.py',120),
  ('Exp -> ID COLON SETROUTES LP URL EQUAL STRING RP COLON CREATEDATA LP OBJECT EQUAL ID RP SEMICOLON','Exp',16,'p_set_routes_create','ViSeParser.py',130),
  ('Exp -> ID COLON SETROUTES LP URL EQUAL STRING RP SEMICOLON','Exp',9,'p_set_routes_non_id','ViSeParser.py',139),
>>>>>>> add-grammar
]
