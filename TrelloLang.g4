grammar TrelloLang;


prog      : KEY ID TOKEN ID comando+ ;
comando   : CRIAR BOARD STRING 
          | CRIAR LISTA STRING NO ID 
          | CRIAR CARD STRING NO ID 
          | MOVER CARD ID AO ID 
          | MOSTRAR BOARDS 
          | MOSTRAR LISTAS NO ID 
          | REPITA NUM APAR comando+ FPAR
          ;
          

CRIAR       : 'CRIAR'           ;
MOSTRAR     : 'MOSTRAR'         ;
MOVER       : 'MOVER'           ;
BOARD       : 'BOARD'           ;
BOARDS      : 'BOARDS'          ;
LISTA       : 'LISTA'           ;
LISTAS      : 'LISTAS'          ;
CARD        : 'CARD'            ;
REPITA      : 'REPITA'          ;
AO          : 'AO'              ;
NO          : 'NO'              ;
KEY         : 'KEY'             ;
TOKEN       : 'TOKEN'           ;
APAR        : '{'               ;    
FPAR        : '}'               ;
NUM         : [0-9]+            ;
ID          : [a-zA-Z0-9]+      ;
STRING      : '"' .*? '"'       ;
PULAR       : [ \t\r\n]+ -> skip ;