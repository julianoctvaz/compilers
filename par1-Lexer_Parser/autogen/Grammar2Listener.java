// Generated from autogen/Grammar2.g4 by ANTLR 4.7.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link Grammar2Parser}.
 */
public interface Grammar2Listener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link Grammar2Parser#file}.
	 * @param ctx the parse tree
	 */
	void enterFile(Grammar2Parser.FileContext ctx);
	/**
	 * Exit a parse tree produced by {@link Grammar2Parser#file}.
	 * @param ctx the parse tree
	 */
	void exitFile(Grammar2Parser.FileContext ctx);
	/**
	 * Enter a parse tree produced by {@link Grammar2Parser#variable_definition}.
	 * @param ctx the parse tree
	 */
	void enterVariable_definition(Grammar2Parser.Variable_definitionContext ctx);
	/**
	 * Exit a parse tree produced by {@link Grammar2Parser#variable_definition}.
	 * @param ctx the parse tree
	 */
	void exitVariable_definition(Grammar2Parser.Variable_definitionContext ctx);
	/**
	 * Enter a parse tree produced by {@link Grammar2Parser#function_definition}.
	 * @param ctx the parse tree
	 */
	void enterFunction_definition(Grammar2Parser.Function_definitionContext ctx);
	/**
	 * Exit a parse tree produced by {@link Grammar2Parser#function_definition}.
	 * @param ctx the parse tree
	 */
	void exitFunction_definition(Grammar2Parser.Function_definitionContext ctx);
	/**
	 * Enter a parse tree produced by {@link Grammar2Parser#variable_assignment}.
	 * @param ctx the parse tree
	 */
	void enterVariable_assignment(Grammar2Parser.Variable_assignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link Grammar2Parser#variable_assignment}.
	 * @param ctx the parse tree
	 */
	void exitVariable_assignment(Grammar2Parser.Variable_assignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link Grammar2Parser#arguments}.
	 * @param ctx the parse tree
	 */
	void enterArguments(Grammar2Parser.ArgumentsContext ctx);
	/**
	 * Exit a parse tree produced by {@link Grammar2Parser#arguments}.
	 * @param ctx the parse tree
	 */
	void exitArguments(Grammar2Parser.ArgumentsContext ctx);
	/**
	 * Enter a parse tree produced by {@link Grammar2Parser#body}.
	 * @param ctx the parse tree
	 */
	void enterBody(Grammar2Parser.BodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link Grammar2Parser#body}.
	 * @param ctx the parse tree
	 */
	void exitBody(Grammar2Parser.BodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link Grammar2Parser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(Grammar2Parser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link Grammar2Parser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(Grammar2Parser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link Grammar2Parser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(Grammar2Parser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link Grammar2Parser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(Grammar2Parser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link Grammar2Parser#type}.
	 * @param ctx the parse tree
	 */
	void enterType(Grammar2Parser.TypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link Grammar2Parser#type}.
	 * @param ctx the parse tree
	 */
	void exitType(Grammar2Parser.TypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link Grammar2Parser#identifier}.
	 * @param ctx the parse tree
	 */
	void enterIdentifier(Grammar2Parser.IdentifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link Grammar2Parser#identifier}.
	 * @param ctx the parse tree
	 */
	void exitIdentifier(Grammar2Parser.IdentifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link Grammar2Parser#integer}.
	 * @param ctx the parse tree
	 */
	void enterInteger(Grammar2Parser.IntegerContext ctx);
	/**
	 * Exit a parse tree produced by {@link Grammar2Parser#integer}.
	 * @param ctx the parse tree
	 */
	void exitInteger(Grammar2Parser.IntegerContext ctx);
	/**
	 * Enter a parse tree produced by {@link Grammar2Parser#floating}.
	 * @param ctx the parse tree
	 */
	void enterFloating(Grammar2Parser.FloatingContext ctx);
	/**
	 * Exit a parse tree produced by {@link Grammar2Parser#floating}.
	 * @param ctx the parse tree
	 */
	void exitFloating(Grammar2Parser.FloatingContext ctx);
}