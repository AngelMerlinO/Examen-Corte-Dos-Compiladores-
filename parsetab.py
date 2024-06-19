
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASSIGN COMMA CONSOLE DIVIDE DOT EQ FLOAT FLOAT_LITERAL FOR GE GLOBAL GT ID IF IN INPUT INT LBRACE LE LOG LPAREN LT MINUS NE NUMBER OUT PLUS PRINTLN RANGE RBRACE RPAREN SEMICOLON SINGLE_QUOTE STRING STRING_LITERAL SYSTEM TIMES VAR WHILEprogram : declarations statementsdeclarations : declarations declaration\n                    | declarationdeclaration : INT ID ASSIGN NUMBER SEMICOLON\n                   | FLOAT ID ASSIGN FLOAT_LITERAL SEMICOLON\n                   | STRING ID ASSIGN STRING_LITERAL SEMICOLONstatements : statements statement\n                  | statementstatement : if_statement\n                 | while_statement\n                 | for_statement\n                 | input_statement\n                 | increment_statement\n                 | assignment_statementif_statement : IF LPAREN condition RPAREN LBRACE statements RBRACEcondition : expression AND expression\n                 | expressionexpression : simple_expression comparison_operator simple_expression\n                  | simple_expressionsimple_expression : ID\n                         | NUMBER\n                         | FLOAT_LITERAL\n                         | STRING_LITERALcomparison_operator : EQ\n                           | GT\n                           | GE\n                           | LT\n                           | LE\n                           | NEwhile_statement : WHILE LPAREN condition RPAREN LBRACE statements RBRACEfor_statement : FOR LPAREN ID IN RANGE LPAREN NUMBER COMMA NUMBER RPAREN RPAREN LBRACE statements RBRACEinput_statement : INPUT LPAREN simple_expression RPAREN SEMICOLONincrement_statement : ID PLUS PLUS SEMICOLONassignment_statement : ID ASSIGN expression SEMICOLON'
    
_lr_action_items = {'INT':([0,2,3,8,63,64,65,],[4,4,-3,-2,-4,-5,-6,]),'FLOAT':([0,2,3,8,63,64,65,],[5,5,-3,-2,-4,-5,-6,]),'STRING':([0,2,3,8,63,64,65,],[6,6,-3,-2,-4,-5,-6,]),'$end':([1,7,9,11,12,13,14,15,16,24,49,50,71,75,76,84,],[0,-1,-8,-9,-10,-11,-12,-13,-14,-7,-33,-34,-32,-15,-30,-31,]),'IF':([2,3,7,8,9,11,12,13,14,15,16,24,49,50,63,64,65,67,69,71,72,73,75,76,82,83,84,],[17,-3,17,-2,-8,-9,-10,-11,-12,-13,-14,-7,-33,-34,-4,-5,-6,17,17,-32,17,17,-15,-30,17,17,-31,]),'WHILE':([2,3,7,8,9,11,12,13,14,15,16,24,49,50,63,64,65,67,69,71,72,73,75,76,82,83,84,],[18,-3,18,-2,-8,-9,-10,-11,-12,-13,-14,-7,-33,-34,-4,-5,-6,18,18,-32,18,18,-15,-30,18,18,-31,]),'FOR':([2,3,7,8,9,11,12,13,14,15,16,24,49,50,63,64,65,67,69,71,72,73,75,76,82,83,84,],[19,-3,19,-2,-8,-9,-10,-11,-12,-13,-14,-7,-33,-34,-4,-5,-6,19,19,-32,19,19,-15,-30,19,19,-31,]),'INPUT':([2,3,7,8,9,11,12,13,14,15,16,24,49,50,63,64,65,67,69,71,72,73,75,76,82,83,84,],[20,-3,20,-2,-8,-9,-10,-11,-12,-13,-14,-7,-33,-34,-4,-5,-6,20,20,-32,20,20,-15,-30,20,20,-31,]),'ID':([2,3,4,5,6,7,8,9,11,12,13,14,15,16,24,26,27,28,29,30,49,50,51,52,53,54,55,56,57,59,63,64,65,67,69,71,72,73,75,76,82,83,84,],[10,-3,21,22,23,10,-2,-8,-9,-10,-11,-12,-13,-14,-7,35,35,35,44,35,-33,-34,35,-24,-25,-26,-27,-28,-29,35,-4,-5,-6,10,10,-32,10,10,-15,-30,10,10,-31,]),'RBRACE':([9,11,12,13,14,15,16,24,49,50,71,72,73,75,76,83,84,],[-8,-9,-10,-11,-12,-13,-14,-7,-33,-34,-32,75,76,-15,-30,84,-31,]),'PLUS':([10,25,],[25,34,]),'ASSIGN':([10,21,22,23,],[26,31,32,33,]),'LPAREN':([17,18,19,20,70,],[27,28,29,30,74,]),'NUMBER':([26,27,28,30,31,51,52,53,54,55,56,57,59,74,78,],[38,38,38,38,46,38,-24,-25,-26,-27,-28,-29,38,77,79,]),'FLOAT_LITERAL':([26,27,28,30,32,51,52,53,54,55,56,57,59,],[39,39,39,39,47,39,-24,-25,-26,-27,-28,-29,39,]),'STRING_LITERAL':([26,27,28,30,33,51,52,53,54,55,56,57,59,],[40,40,40,40,48,40,-24,-25,-26,-27,-28,-29,40,]),'SEMICOLON':([34,35,36,37,38,39,40,46,47,48,62,66,],[49,-20,50,-19,-21,-22,-23,63,64,65,71,-18,]),'EQ':([35,37,38,39,40,],[-20,52,-21,-22,-23,]),'GT':([35,37,38,39,40,],[-20,53,-21,-22,-23,]),'GE':([35,37,38,39,40,],[-20,54,-21,-22,-23,]),'LT':([35,37,38,39,40,],[-20,55,-21,-22,-23,]),'LE':([35,37,38,39,40,],[-20,56,-21,-22,-23,]),'NE':([35,37,38,39,40,],[-20,57,-21,-22,-23,]),'AND':([35,37,38,39,40,42,66,],[-20,-19,-21,-22,-23,59,-18,]),'RPAREN':([35,37,38,39,40,41,42,43,45,66,68,79,80,],[-20,-19,-21,-22,-23,58,-17,60,62,-18,-16,80,81,]),'IN':([44,],[61,]),'LBRACE':([58,60,81,],[67,69,82,]),'RANGE':([61,],[70,]),'COMMA':([77,],[78,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'declarations':([0,],[2,]),'declaration':([0,2,],[3,8,]),'statements':([2,67,69,82,],[7,72,73,83,]),'statement':([2,7,67,69,72,73,82,83,],[9,24,9,9,24,24,9,24,]),'if_statement':([2,7,67,69,72,73,82,83,],[11,11,11,11,11,11,11,11,]),'while_statement':([2,7,67,69,72,73,82,83,],[12,12,12,12,12,12,12,12,]),'for_statement':([2,7,67,69,72,73,82,83,],[13,13,13,13,13,13,13,13,]),'input_statement':([2,7,67,69,72,73,82,83,],[14,14,14,14,14,14,14,14,]),'increment_statement':([2,7,67,69,72,73,82,83,],[15,15,15,15,15,15,15,15,]),'assignment_statement':([2,7,67,69,72,73,82,83,],[16,16,16,16,16,16,16,16,]),'expression':([26,27,28,59,],[36,42,42,68,]),'simple_expression':([26,27,28,30,51,59,],[37,37,37,45,66,37,]),'condition':([27,28,],[41,43,]),'comparison_operator':([37,],[51,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> declarations statements','program',2,'p_program','parser_1.py',9),
  ('declarations -> declarations declaration','declarations',2,'p_declarations','parser_1.py',14),
  ('declarations -> declaration','declarations',1,'p_declarations','parser_1.py',15),
  ('declaration -> INT ID ASSIGN NUMBER SEMICOLON','declaration',5,'p_declaration','parser_1.py',18),
  ('declaration -> FLOAT ID ASSIGN FLOAT_LITERAL SEMICOLON','declaration',5,'p_declaration','parser_1.py',19),
  ('declaration -> STRING ID ASSIGN STRING_LITERAL SEMICOLON','declaration',5,'p_declaration','parser_1.py',20),
  ('statements -> statements statement','statements',2,'p_statements','parser_1.py',27),
  ('statements -> statement','statements',1,'p_statements','parser_1.py',28),
  ('statement -> if_statement','statement',1,'p_statement','parser_1.py',31),
  ('statement -> while_statement','statement',1,'p_statement','parser_1.py',32),
  ('statement -> for_statement','statement',1,'p_statement','parser_1.py',33),
  ('statement -> input_statement','statement',1,'p_statement','parser_1.py',34),
  ('statement -> increment_statement','statement',1,'p_statement','parser_1.py',35),
  ('statement -> assignment_statement','statement',1,'p_statement','parser_1.py',36),
  ('if_statement -> IF LPAREN condition RPAREN LBRACE statements RBRACE','if_statement',7,'p_if_statement','parser_1.py',39),
  ('condition -> expression AND expression','condition',3,'p_condition','parser_1.py',42),
  ('condition -> expression','condition',1,'p_condition','parser_1.py',43),
  ('expression -> simple_expression comparison_operator simple_expression','expression',3,'p_expression','parser_1.py',47),
  ('expression -> simple_expression','expression',1,'p_expression','parser_1.py',48),
  ('simple_expression -> ID','simple_expression',1,'p_simple_expression','parser_1.py',55),
  ('simple_expression -> NUMBER','simple_expression',1,'p_simple_expression','parser_1.py',56),
  ('simple_expression -> FLOAT_LITERAL','simple_expression',1,'p_simple_expression','parser_1.py',57),
  ('simple_expression -> STRING_LITERAL','simple_expression',1,'p_simple_expression','parser_1.py',58),
  ('comparison_operator -> EQ','comparison_operator',1,'p_comparison_operator','parser_1.py',64),
  ('comparison_operator -> GT','comparison_operator',1,'p_comparison_operator','parser_1.py',65),
  ('comparison_operator -> GE','comparison_operator',1,'p_comparison_operator','parser_1.py',66),
  ('comparison_operator -> LT','comparison_operator',1,'p_comparison_operator','parser_1.py',67),
  ('comparison_operator -> LE','comparison_operator',1,'p_comparison_operator','parser_1.py',68),
  ('comparison_operator -> NE','comparison_operator',1,'p_comparison_operator','parser_1.py',69),
  ('while_statement -> WHILE LPAREN condition RPAREN LBRACE statements RBRACE','while_statement',7,'p_while_statement','parser_1.py',73),
  ('for_statement -> FOR LPAREN ID IN RANGE LPAREN NUMBER COMMA NUMBER RPAREN RPAREN LBRACE statements RBRACE','for_statement',14,'p_for_statement','parser_1.py',76),
  ('input_statement -> INPUT LPAREN simple_expression RPAREN SEMICOLON','input_statement',5,'p_input_statement','parser_1.py',82),
  ('increment_statement -> ID PLUS PLUS SEMICOLON','increment_statement',4,'p_increment_statement','parser_1.py',87),
  ('assignment_statement -> ID ASSIGN expression SEMICOLON','assignment_statement',4,'p_assignment_statement','parser_1.py',91),
]