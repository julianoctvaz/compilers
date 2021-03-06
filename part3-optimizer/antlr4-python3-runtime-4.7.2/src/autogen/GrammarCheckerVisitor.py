# Generated from antlr4-python3-runtime-4.7.2/src/autogen/Grammar.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# retorne Type.INT, etc para fazer checagem de tipos
class Type:
    VOID = "void"
    INT = "int"
    FLOAT = "float"
    STRING = "char *"

# This class defines a complete generic visitor for a parse tree produced by GrammarParser.
class GrammarCheckerVisitor(ParseTreeVisitor):
    ids_defined = {} # armazenar informações necessárias para cada identifier definido [tabela de simbolos] nome: tipo, argumentos, nada
    inside_what_function = ""

    # Visit a parse tree produced by GrammarParser#fiile.
    def visitFiile(self, ctx:GrammarParser.FiileContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GrammarParser#function_definition.
    def visitFunction_definition(self, ctx:GrammarParser.Function_definitionContext):
        tyype = ctx.tyype().getText()  # mostra o tipo da funcao
        name = ctx.identifier().getText() #mostra o nome da funcao
        params = self.visit(ctx.arguments()) #pega os tipos do parametros e coloca na tabela de simbolos primeiro depois pega o tipo e nome da funcao
        self.ids_defined[name] = tyype, params, None
        #print(self.ids_defined)
        self.inside_what_function = name
        self.visit(ctx.body())
        #print(ctx.body())
        return

    # Visit a parse tree produced by GrammarParser#body.
    def visitBody(self, ctx:GrammarParser.BodyContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GrammarParser#statement.
    def visitStatement(self, ctx:GrammarParser.StatementContext):
        if ctx.RETURN() != None:
            token = ctx.RETURN().getPayload()
            tyype, cte_value = self.visit(ctx.expression())
            function_type, params, _ = self.ids_defined[self.inside_what_function]
            if function_type == Type.INT and tyype == Type.FLOAT:
                print("WARNING: possible loss of information returning float expression from int function '" + self.inside_what_function + "' in line " + str(token.line) + " and column " + str(token.column))
            elif function_type == Type.VOID and tyype != Type.VOID:
                print("ERROR: trying to return a non void expression from void function '" + self.inside_what_function + "' in line " + str(token.line) + " and column " + str(token.column))
            elif function_type != Type.VOID and tyype == Type.VOID:
                print("ERROR: trying to return void expression from function '" + self.inside_what_function + "' in line " + str(token.line) + " and column " + str(token.column))

        else:
            self.visitChildren(ctx)
        return

    # Visit a parse tree produced by GrammarParser#if_statement.
    def visitIf_statement(self, ctx:GrammarParser.If_statementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GrammarParser#else_statement.
    def visitElse_statement(self, ctx:GrammarParser.Else_statementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GrammarParser#for_loop.
    def visitFor_loop(self, ctx:GrammarParser.For_loopContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GrammarParser#for_initializer.
    def visitFor_initializer(self, ctx:GrammarParser.For_initializerContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GrammarParser#for_condition.
    def visitFor_condition(self, ctx:GrammarParser.For_conditionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GrammarParser#for_step.
    def visitFor_step(self, ctx:GrammarParser.For_stepContext):
        return self.visitChildren(ctx)

    def checkDic(self, name, value):
        if name in self.ids_defined:
            return self.ids_defined[name][2]
        else:
            new_dic = {}
            for item in self.ids_defined:
                new_dic[item] = self.ids_defined[item][2]
            return eval(value, new_dic)

    # Visit a parse tree produced by GrammarParser#variable_definition.
    def visitVariable_definition(self, ctx:GrammarParser.Variable_definitionContext):
        tyype = ctx.tyype().getText()
       # print("VD")
        for i in range(len(ctx.identifier())): # ver quantas atribuicoes tem na linha daquele valor para n variaveis (identifiers)
            name = ctx.identifier(i).getText() #guarda o nome da variavel n 
            token = ctx.identifier(i).IDENTIFIER().getPayload() #guarda a linha e coluna daquela variavel
            
            if ctx.expression(i) != None: #enquanto eu tiver uma definicao de variavel
                expr_type, cte_value = self.visit(ctx.expression(i)) #self retorna o tipo e NONE???
                cte_value = ctx.expression(i).getText()
                if expr_type == Type.VOID:
                    print("ERROR: trying to assign void expression to variable '" + name + "' in line " + str(token.line) + " and column " + str(token.column))
                elif expr_type == Type.FLOAT and tyype == Type.INT:
                    print("WARNING: possible loss of information assigning float expression to int variable '" + name + "' in line " + str(token.line) + " and column " + str(token.column))
            else:
                cte_value = None
            
            
            self.ids_defined[name] = tyype, -1, self.checkDic(name, cte_value) # -1 means not an array, therefore no length here (vide 15 lines below)

        for i in range(len(ctx.array())): #talvez aqui eu so mexa aqui
            name = ctx.array(i).identifier().getText()
            token = ctx.array(i).identifier().IDENTIFIER().getPayload()
            cte_value = ctx.array(i).getText()
        
            if ctx.array_literal(i) != None:
                expr_types, cte_values_array = self.visit(ctx.array_literal(i))

                for j in range(len(expr_types)):
                    if expr_types[j] == Type.VOID:
                        print("ERROR: trying to initialize void expression to array '" + name + "' at index " + str(j) + " of array literal in line " + str(token.line) + " and column " + str(token.column))
                    elif expr_types[j] == Type.FLOAT and tyype == Type.INT:
                        print("WARNING: possible loss of information initializing float expression to int array '" + name + "' at index " + str(j) + " of array literal in line " + str(token.line) + " and column " + str(token.column))
            else:
                cte_values_array = None

            array_length = self.visit(ctx.array(i))
            self.ids_defined[name] = tyype, array_length, cte_values_array
            # print(cte_values_array) #CORRIGIDO
            

        return

    # Visit a parse tree produced by GrammarParser#variable_assignment.
    def visitVariable_assignment(self, ctx:GrammarParser.Variable_assignmentContext):
        # print('visitVariable_assignment')
        if ctx.identifier() != None:
            name = ctx.identifier().getText()
            token = ctx.identifier().IDENTIFIER().getPayload()
            try:
                tyype, _, cte_value = self.ids_defined[name]
            except:
                print("ERROR: undefined variable '" + name + "' in line " + str(token.line) + " and column " + str(token.column))
                return
        else: # array
            name = ctx.array().identifier().getText()
            token = ctx.array().identifier().IDENTIFIER().getPayload()
            try:
                tyype, array_length, cte_values_array = self.ids_defined[name]
            except:
                print("ERROR: undefined array '" + name + "' in line " + str(token.line) + " and column " + str(token.column))
            array_index = self.visit(ctx.array())
            if cte_values_array != None:
                cte_value = cte_values_array[array_index]
                # print("CTE_VALUE", cte_value)
            else:
                cte_value = None

        # ATUALIZAR O VALOR DA VARIAVEL OU DO VALOR NAQUELA POSICAO DO ARRAY POR MEIO DE CTE_VALUE
        op = ctx.OP.text
        if op == '++' or op == '--':
            # print('PRINT 1')
            if op == '++':
                # print(self.ids_defined)
                cte_value = cte_value + 1
            elif op == '--':
                cte_value = cte_value - 1
            else:
                print('Erro - Operadores do For-Step')
        else:
            # print("PRINT 2")
            expr_type, expr_cte_value = self.visit(ctx.expression())
            if expr_type == Type.VOID:
                print("ERROR: trying to assign void expression to variable '" + name + "' in line " + str(token.line) + " and column " + str(token.column))
            elif expr_type == Type.FLOAT and tyype == Type.INT:
                print("WARNING: possible loss of information assigning float expression to int variable '" + name + "' in line " + str(token.line) + " and column " + str(token.column))
        
        if ctx.identifier() != None:
            # print("PRINT 3")
            # print(name, cte_value)
            self.ids_defined[name] = tyype, -1, cte_value
            # print(self.ids_defined)
        else: # array
            # print("PRINT 4")
            if cte_values_array != None:
                cte_values_array[array_index] = cte_value
            self.ids_defined[name] = tyype, array_length, cte_values_array
        return

    # Visit a parse tree produced by GrammarParser#expression.
    def visitExpression(self, ctx:GrammarParser.ExpressionContext):
        #print("EXP")
        tyype = Type.VOID
        cte_value = None # RETORNAR OS VALORES DAS CONTANTES, OU NONE SE NAO FOR CONSTANTE
        if len(ctx.expression()) == 0:
            if ctx.integer() != None:
                tyype = Type.INT    
                cte_value = int(ctx.integer().getText()) #coloquei

            elif ctx.floating() != None:
                tyype = Type.FLOAT
                cte_value = float(ctx.floating().getText()) #coloquei

            elif ctx.string() != None:
                tyype = Type.STRING
                cte_value = str(ctx.string().getText()) #coloquei

            elif ctx.identifier() != None:
                name = ctx.identifier().getText()
                try:
                    tyype, _, cte_value = self.ids_defined[name]
                except:
                    token = ctx.identifier().IDENTIFIER().getPayload()
                    print("ERROR: undefined variable '" + name + "' in line " + str(token.line) + " and column " + str(token.column))

            elif ctx.array() != None:
                name = ctx.array().identifier().getText()
                try:
                    # print("entrou no try do array do visit expression")
                    tyype, array_length, cte_values_array = self.ids_defined[name]
                    # print(cte_values_array, "valores pegando aqui dentro do visitexpression")
                except:
                    # print("entrou no expection do array")
                    token = ctx.array().identifier().IDENTIFIER().getPayload()
                    print("ERROR: undefined array '" + name + "' in line " + str(token.line) + " and column " + str(token.column))
                array_index = self.visit(ctx.array())
                # print(array_index, array_length)
                if array_index < array_length:
                    # print(array_index, "indice do array") 
                    # print(ctx.array().getText())
                    # print(self.ids_defined['tk'][2][2], "uhuuu")
                    if(tyype == Type.FLOAT):
                        cte_value = float(self.ids_defined[name][2][array_index])
                    elif(tyype == Type.INT):
                        cte_value = int(self.ids_defined[name][2][array_index])
                    else:
                        print("Erro voce ta acessando o array que nao é inteiro nem float para alguma operacao [aritmetica possivelmente]")
                else:
                    token = ctx.array().identifier().IDENTIFIER().getPayload()
                    print("Erro aqui no index do array, indice fora do comprimento do array " + name + " in line " + str(token.line) +  " and column " + str(token.column))
            
            elif ctx.function_call() != None:
                tyype, cte_value = self.visit(ctx.function_call())

        elif len(ctx.expression()) == 1:

            if ctx.OP != None: #unary operators
                text = ctx.OP.text
                token = ctx.OP
                tyype, cte_value = self.visit(ctx.expression(0)) #caso vem sem operacao unario tipo 3 != +3 ou -3
                if(text == '-'):
                    cte_value =  -cte_value # é negativo categoricamente
                elif (text == '+'):
                    cte_value = cte_value #é positivo categoricamente
                else:
                    print("Erro operador unario negativos e positivos")


                if tyype == Type.VOID:
                    print("ERROR: unary operator '" + text + "' used on type void in line " + str(token.line) + " and column " + str(token.column))

            else: # parentheses
                tyype, cte_value = self.visit(ctx.expression(0))


        elif len(ctx.expression()) == 2: # binary operators
            # print("PRINT 1")
            text = ctx.OP.text
            token = ctx.OP
            left, left_cte_value = self.visit(ctx.expression(0))
            right, right_cte_value = self.visit(ctx.expression(1))
            if left == Type.VOID or right == Type.VOID:
                print("ERROR: binary operator '" + text + "' used on type void in line " + str(token.line) + " and column " + str(token.column))

            if text == '*' or text == '/' or text == '+' or text == '-':
                if left == Type.FLOAT or right == Type.FLOAT:
                    tyype = Type.FLOAT
                else:
                    tyype = Type.INT
            else:
                tyype = Type.INT

            # print("TEXT", text)
            
            if(left_cte_value != None and right_cte_value != None):
                if text == '/':
                    cte_value = eval(str(left_cte_value)) / eval(str(right_cte_value))
                    #print(left_cte_value, right_cte_value, "valores")
                elif text == '*':
                    cte_value = eval(str(left_cte_value)) * eval(str(right_cte_value))
                    #print(left_cte_value, right_cte_value, "valores")
                elif text == '+':
                    cte_value = eval(str(left_cte_value)) + eval(str(right_cte_value))
                    #print(left_cte_value, right_cte_value, "valores")
                elif text == '-':
                    cte_value = eval(str(left_cte_value)) - eval(str(right_cte_value))
                    #print(left_cte_value, right_cte_value, "valores")
                elif text == '<':
                    if left_cte_value < right_cte_value:
                        cte_value = 1
                    else:
                        cte_value = 0
                elif text == '>':
                    if left_cte_value > right_cte_value:
                        cte_value = 1
                    else:
                        cte_value = 0
                elif text == '<=':
                    if left_cte_value <= right_cte_value:
                        cte_value = 1
                    else:
                        cte_value = 0
                elif text == '>=':
                    if left_cte_value >= right_cte_value:
                        cte_value = 1
                    else:
                        cte_value = 0
                elif text == '==':
                    if left_cte_value == right_cte_value:
                        cte_value = 1
                    else:
                        cte_value = 0
                elif text == '!=':
                    if left_cte_value != right_cte_value:
                        cte_value = 1
                    else:
                        cte_value = 0
                else:
                    print("ERRO: nao é uma operacao valida")
        

        print(str(tyype) + ": " + str(cte_value))
        #print(self.ids_defined)
        return tyype, cte_value

    # Visit a parse tree produced by GrammarParser#array.
    def visitArray(self, ctx:GrammarParser.ArrayContext):
        # print(ctx.getText(), "ctx do visit array")
        tyype, cte_value = self.visit(ctx.expression())
        name = ctx.identifier().getText()
        #print(name)
        if tyype != Type.INT:
            token = ctx.identifier().IDENTIFIER().getPayload()
            print("ERROR: array expression must be an integer, but it is " + str(tyype) + " in line " + str(token.line) + " and column " + str(token.column))
        # print(cte_value, "print final do no visit array")
        return cte_value

    # Visit a parse tree produced by GrammarParser#array_literal.
    def visitArray_literal(self, ctx:GrammarParser.Array_literalContext):
        types = []
        cte_values_array = []
        for i in range(len(ctx.expression())):
            tyype, cte_value = self.visit(ctx.expression(i))
            types += [tyype]
            cte_values_array += [cte_value]
        # print(cte_values_array, "valores do array")
        return types, cte_values_array

    # Visit a parse tree produced by GrammarParser#function_call.
    def visitFunction_call(self, ctx:GrammarParser.Function_callContext):
        name = ctx.identifier().getText()
        token = ctx.identifier().IDENTIFIER().getPayload()
        try:
            tyype, args, cte_value = self.ids_defined[name]
            if len(args) != len(ctx.expression()):
                print("ERROR: incorrect number of parameters for function '" + name + "' in line " + str(token.line) + " and column " + str(token.column) + ". Expecting " + str(len(args)) + ", but " + str(len(ctx.expression())) + " were given")
        except:
            print("ERROR: undefined function '" + name + "' in line " + str(token.line) + " and column " + str(token.column))

        for i in range(len(ctx.expression())):
            arg_type, arg_cte_value = self.visit(ctx.expression(i))
            if i < len(args):
                if arg_type == Type.VOID:
                    print("ERROR: void expression passed as parameter " + str(i) + " of function '" + name + "' in line " + str(token.line) + " and column " + str(token.column))
                elif arg_type == Type.FLOAT and args[i] == Type.INT:
                    print("WARNING: possible loss of information converting float expression to int expression in parameter " + str(i) + " of function '" + name + "' in line " + str(token.line) + " and column " + str(token.column))
        return tyype, cte_value

    # Visit a parse tree produced by GrammarParser#arguments.
    def visitArguments(self, ctx:GrammarParser.ArgumentsContext):
        params = []
        for i in range(len(ctx.identifier())):
            tyype = ctx.tyype(i).getText()
            name = ctx.identifier(i).getText()
            self.ids_defined[name] = tyype, -1, None
            params += [tyype]
        return params

    # Visit a parse tree produced by GrammarParser#tyype.
    def visitTyype(self, ctx:GrammarParser.TyypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GrammarParser#integer.
    def visitInteger(self, ctx:GrammarParser.IntegerContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GrammarParser#floating.
    def visitFloating(self, ctx:GrammarParser.FloatingContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GrammarParser#string.
    def visitString(self, ctx:GrammarParser.StringContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GrammarParser#identifier.
    def visitIdentifier(self, ctx:GrammarParser.IdentifierContext):
        return self.visitChildren(ctx)

    #del GrammarParser

    #def aggregateResult(self, aggregate:Type, next_result:Type):
        #return next_result if next_result != None else aggregate