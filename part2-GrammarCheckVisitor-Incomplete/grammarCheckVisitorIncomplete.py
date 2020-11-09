# Generated from antlr4-python3-runtime-4.7.2/src/autogen/Grammar.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete generic visitor for a parse tree produced by GrammarParser.

'''
COMO RESGATAR INFORMAÇÕES DA ÁRVORE

Observe o seu Grammar.g4. Cada regra sintática gea uma função com o nome corespondente no Visitor e na ordem em que está na gramática. Para deixar na ordem em que você colocou, substitua as funções dentro de "class GrammarCheckerVisitor(ParseTreeVisitor)" pelas que apareem em autogem/GrammarVisitor.g4 depois do make ser rodado. Mas antes algumas mudanças precisam ser feitas em Grammar.g4. Primeiro copie-a do projeto1 para o projeto2. Depois adicione o tipo "VOID: 'void'" no lexer e na regra de "type" no parser (só "| VOID" aqui). Agora, por causa de conflitos com Python, substitua as regras file por fiile e type por type ("make adjust" substitui automaticamente). Use prints temporários para ver se está no caminho certo.  "make tree" agora desenha a árvore sintática, se quiser vê-la para qualquer input, enquanto "make" roda este visitor sobre o a árvore gerada a partir de Grammar.g4 alimentada pelo input.


expr = ctx.expression().accept(self)  # entra no nó expression e seus filhos e retorna alguma coisa

for i in range(len(ctx.identifier())): # para cada identficador que este nó possui...
    ident = ctx.identifier()[i].accept(self) # ...pegue o i-ésimo

if ctx.FLOAT() != None: # se houver um FLOAT (em vez de INT ou VOID) neste nó (parser)
    return Type.FLOAT # retorne float
'''

# retorne Type.INT, etc para fazer checagem de tipos
class Type:
    VOID = "void"
    INT = "int"
    FLOAT = "float"
    STRING = "string"

class GrammarCheckerVisitor(ParseTreeVisitor):
    ids_defined = {} # armazenar informações necessárias para cada identifier definido 
    #seria como uma especie de tabela de simbolos
    # a:int
    # Visit a parse tree produced by GrammarParser#fiile.
    def visitFiile(self, ctx:GrammarParser.FiileContext):
        print('Visiting an fiile')
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#function_definition.
    def visitFunction_definition(self, ctx:GrammarParser.Function_definitionContext):
        print("visiting a function definition")
    # pega  type da funcao e pega a lista de argumentos
    # se argumentos diferente de none
    #     itera
    #        visit (argumentos[i])
    #     }
    # }
    
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#body.
    def visitBody(self, ctx:GrammarParser.BodyContext):
        print('Visiting a body')
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#statement.
    def visitStatement(self, ctx:GrammarParser.StatementContext):
        print('Visiting a Statament')
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#if_statement.
    def visitIf_statement(self, ctx:GrammarParser.If_statementContext):
        print('Visiting a If Statement')
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#else_statement.
    def visitElse_statement(self, ctx:GrammarParser.Else_statementContext):
        print('Visiting a Else Statement')
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#for_loop.
    def visitFor_loop(self, ctx:GrammarParser.For_loopContext):
        print('Visiting a For Loop')
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#for_initializer.
    def visitFor_initializer(self, ctx:GrammarParser.For_initializerContext):
        print('Visiting a For Initializer')
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#for_condition.
    def visitFor_condition(self, ctx:GrammarParser.For_conditionContext):
        print('Visiting a For Condition')
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#for_step.
    def visitFor_step(self, ctx:GrammarParser.For_stepContext):
        print('Visiting a For Step')
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#variable_definition.
    def visitVariable_definition(self, ctx:GrammarParser.Variable_definitionContext):
        print('Visiting a Variable Definition')
        # text = ctx.variable_definition().getText()
        # tyype = self.ids_defined[text]
        # print("Texto do variable definition" + text)
        # print(self.ids_defined)
        return self.visitChildren(ctx)
        #aqui toda vez q eu fizer tenho q armazenar a ariavel no ids_defined dictionary


    # Visit a parse tree produced by GrammarParser#variable_assignment.
    def visitVariable_assignment(self, ctx:GrammarParser.Variable_assignmentContext):
        print('Visiting a Variable Assignment')
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#expression.
    def visitExpression(self, ctx:GrammarParser.ExpressionContext):
        print('Visiting an expression')
       # ids_defined[self.visitIdentifier()] = [self.visitTyype]
    #   quando checar uma expression devo verificar a exsitencia das variaveis, se elas nao exxistirem eu emito um erro.
        tyype = Type.VOID
        if len(ctx.expression()) == 0: 
            if ctx.integer() != None:
                text = ctx.integer().getText()
                token = ctx.integer().INTEGER().getPayload()
                print('integer ' + text + ':' + str(token.line) + '.' + str(token.column))
                tyype = Type.INT
                #print(ids_defined)

            elif ctx.floating() != None:
                text = ctx.floating().getText()
                token = ctx.floating().FLOATING().getPayload()
                print('floating ' + text + ':' + str(token.line) + '.' + str(token.column))
                tyype = Type.FLOAT

            elif ctx.string() != None:
                tyype = Type.STRING

            elif ctx.identifier() != None:
                text = ctx.identifier().getText()
                token = ctx.identifier().IDENTIFIER().getPayload()
                print('identifier ' + text + ':' + str(token.line) + '.' + str(token.column))
                # try: #se for acessar usa sempre o try
                tyype = self.ids_defined[text]
                print(self.ids_defined)
                print('Imprimindo o dicionario')
                # except:
                    # print('Identifier nao existe?')

            
            elif ctx.array() != None:
                print('éntrou')
                print(ctx.array().identifier().getText() + '[]')
                # tyype = self.visitArray(ctx.array())
                tyype = self.visit(ctx.array())

            elif ctx.function_call() != None:
                print("Function call  " + ctx.function_call().identifier().getText() + '()')
                for i in range(len(ctx.function_call().expression())):
                    arg_type = self.visit(ctx.function_call().expression(i))
                    print('arg[' + str[i] + ']')
                    print(arg_type)
                    tyype = self.visit(ctx.function_call())

        elif len(ctx.expression()) == 1: 
            if ctx.OP != None: #binary operators
                text = ctx.OP.text
                token = ctx.OP 
                print('Operador unario ' + text + ':' + str(token.line) + '.' + str(token.column))
                tyype = self.visit(ctx.expression(0))

            else: #parenteses
                print('(')
                tyype = self.visit(ctx.expression(1))
                print(')')

        elif len(ctx.expression()) == 2: # operadores binarios
            text = ctx.OP.text
            token = ctx.OP 
            print('Operador binario ' + text + ':' + str(token.line) + '.' + str(token.column))
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1))
            if left != right:
                if left == Type.INT and right == Type.FLOAT:
                    return Type.FLOAT
                elif left == Type.FLOAT and right == Type.INT:
                    return Type.FLOAT
                else:
                    print("Erro de tipo nas operacoes")
            else:
                right = left
        else:
            print('Atencao: Numero de operadores é maior que 2 ou diferente do range [0..2]')
        return tyype 


    # Visit a parse tree produced by GrammarParser#array.
    def visitArray(self, ctx:GrammarParser.ArrayContext):
        print('Visiting a Array - second function')
        #e1[e2] onde e1 precisa ser array e e2 preisa ser inteiro, se e2 é uma cte entao val(e2) deve estar no range de type(e1)
        arrayType = self.visit(ctx.expression())
        if arrayType != Type.INT:
            text = ctx.identifier().getText()
            token = ctx.identifier().IDENTIFIER().getPayload()
            print("Erro de tipo, index do array é diferente de int" + text + str(token.line) + "," + str(token.column))
        #return self.visitChildren(ctx)
        return


    # Visit a parse tree produced by GrammarParser#array_literal.
    def visitArray_literal(self, ctx:GrammarParser.Array_literalContext):
        print('Visiting a Array Literal')
        # type_exp = []
        # exp_type = 0
        # for i in range(len(ctx.expression())):
        return self.visitChildren(ctx)
        ##########
        # tyype = Type.INT
        # tyype_temp = Type.VOID
        # for i in range (len(ctx.expression())):
        #     tyype_temp = self.visit(ctx.expression(i))
        #     if tyype_temp == Type.VOID:
        #         tyype = Type.VOID
        #     elif tyype_temp == Type.FLOAT and tyype != Type.VOID:
        #         tyype = Type.FLOAT

        # return tyype
        ######


    # Visit a parse tree produced by GrammarParser#function_call.
    def visitFunction_call(self, ctx:GrammarParser.Function_callContext):
        # e1(e2); e1 precisa ser do tipo (t1,t2) e e2 precisa ser do tipo (t1)
        print("visiting a function call");
        # pega lista de argumentos
        # se lista é difernte de none 
        #  itera
        #    visita expressao(arg[i])
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#arguments.
    def visitArguments(self, ctx:GrammarParser.ArgumentsContext):
        print('Visiting Arguments')
        args = []
        for i in range(len(ctx.identifier())):
            args = args + [ctx.tyype(i).getText()]
            self.ids_defined[ctx.identifier(i).getText()] =  ctx.tyype(i).getText()
        print('Argumentos tipos: ')       
        print(args)
        return args


    # Visit a parse tree produced by GrammarParser#tyype.
    def visitTyype(self, ctx:GrammarParser.TyypeContext):
        print('Visiting Tyype')
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#integer. NaoPrecisaMExer
    def visitInteger(self, ctx:GrammarParser.IntegerContext):
        print('Visiting a Integer')
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#floating. NaoPrecisaMExer
    def visitFloating(self, ctx:GrammarParser.FloatingContext):
        print('Visiting a Floating')
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#string. NaoPrecisaMExer
    def visitString(self, ctx:GrammarParser.StringContext):
        print('Visiting a String')
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#identifier. NaoPrecisaMExer
    def visitIdentifier(self, ctx:GrammarParser.IdentifierContext):
        print("visiting a identifier")
        return self.visitChildren(ctx)


    #del GrammarParser

    #def aggregateResult(self, aggregate:Type, next_result:Type):
        #return next_result if next_result != None else aggregate