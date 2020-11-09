/* nome da gramática -- deve ser o mesmo nome do arquivo .g4 e começar com letra maiúscula*/
grammar Grammar;
/* 


/* parser */
/* regra raiz */
file
	// : (variable_definition ';' | function_definition | directivePreProcessing )* 
	: (variable_definition ';' | function_definition )* 
	;


variable_definition
//   : (type identifier '=' expression ?)* 
    : (type identifier '=' expression ?)*  (',' identifier '=' expression)*
	| type array '=' array_literal 
//	| ';'
	;

function_definition
	: type identifier arguments body
	;

function_call
//	: identifier '('(expression*) ',' ')'
	//: identifier '('expression ',' expression ')'
	: identifier '(' expression* (',' expression)* ')'
	//: identifier '(' expression* ')'
	;

variable_assignment
    : (identifier '/='  expression ?)* 
	| (identifier '*='  expression ?)* 
	| identifier ( '++' | '--')
	| identifier ( '-=' | '+=' ) expression
	;

arguments
    : '(' type identifier* (',' type identifier)* ')'
    | '('')'
	|'(' type identifier ')'
    ;

body
    : '{' statement* '}'
//	|   statement ';'
    ;

statement
	: RETURN expression ';'  
	//| expression ';' 
    | variable_assignment ';'
//	| variable_assignment ';'
	| variable_definition ';' 
	| expression ';'
	| for_loop
	| if_statement
    ;

expression
    : '(' expression ')'
	// | expression ',' 
//	| expression ';' 
	//| expression '-' 
	| function_call
    | expression ('*'|'/') expression
	| expression ('+'|'-') expression
	| '-' expression
//	| '+' expression //mesmo colocado aqui nao sai la
//	| '-' integer
	| '-' expression floating
	| expression ( '<' | '>' | '<=' | '>=' | '==' ) expression
    | identifier
    | integer
    | floating
	| string
	| array
	// | symbol_number
 	;

// symbol_number
// 	: SYMBOL_NUMBER
// 	;
type
	: 'int'
	| 'float'
	| 'string'
	;

array
	: identifier '[' expression ']'
	;

array_literal
	: '{' expression* (',' expression)* '}'
	;

for_loop
	: 'for' '(' for_initializer ';' for_condition ';' for_step ')' body
	;

for_initializer
	: variable_definition
	;


for_condition
	: expression
	; 

for_step
	: variable_assignment
	;

if_statement
	: 'if' '(' expression ')' statement 
	| 'if' '(' expression ')' body else_statement
	;

else_statement
	: 'else' body
	| 'else' statement
	;
// printf
// 	: 'printf'
// 	;

identifier
   : IDENTIFIER 
   ;

integer
   : INTEGER_NUMBER 
   ;

floating
  : FLOAT_NUMBER
  ;
	
string
  : STRING
  ;
 


/* implementar mais regras gramaticais, se precisar */

/* lexer */
STRING :  ["].*?["] ;
RETURN : 'return' ;
IDENTIFIER : [_a-zA-Z][a-zA-Z0-9_]* ;
INTEGER_NUMBER : [0-9]+ ;
FLOAT_NUMBER: ([0-9]*[.])?[0-9]+ ; 
//SYMBOL_NUMBER: [+-]? ;
WHITESPACE  : [ \t\r\n]+ -> skip ;
INCLUDE : '#' .*? '\n' -> skip ;
COMMENTARY_SINGLE : '//' .*? '\n' -> skip ;
COMMENTARY_MULTIPLE : '/*' .*? '*/' -> skip ;


/* implementar mais expressões regulares, se precisar*/


/*
MANUAL

caracteres especiais para expressões regulares {
	'xyz'   :  os caracteres rodeados por ' ' são interpretados literalmente 
	\x		:  altera a interpretação do caracter x, se ele tiver outra (\t: tab, \(: o caracter que abre parênteses)
	a(bc)d  :  destaca a subexpressão bc
	x | y   :  aceita a subexpressão x ou y
	[x\yz]	:  equivalente a ('x'|\y|'z'), tal que x, \y e z são caracteres
	[x]		:  equivalente a 'x'
	x*		:  aceita 0 ou mais x's
	x+		:  aceita 1 ou mais x's
	x?		:  aceita 0 ou 1 x
	.       :  aceita qualquer caracter
	.*      :  aceita 0 ou mais caracteres diferentes de \n (guloso)
	.*?     :  aceita 0 ou mais caracteres diferentes de \n (não-guloso)

	regex -> skip : qualquer instância da expressão regular regex não é passada para o parser, sendo assim ignorada (usado em comentários, espaços em branco, ou (no caso deste exercício) diretivas de preprocessamento)


	no ANTLR alguns desses caracteres especiais podem ser utilizados nas regras da gramática também
	ex.:
		expr ('+'|'-') expr
	estabelece que os dois sinais têm a mesma precedência
		'(' (expr (',' expr)*)? ')'
	indica que dentro destes parênteses pode haver zero ou mais expressões separadas por vírgulas
}

regras da gramática {
	nome_da_regra
		: uma seqüência de regras que satisfazem esta
		| outra
		| e mais outra
		;

	NOME_DA_EXPRESSÃO_REGULAR : a_expressão_regular ;

	dentro de uma regra a primeira opção tem maior precedência (útil em expressões matemáticas)
}
*/
