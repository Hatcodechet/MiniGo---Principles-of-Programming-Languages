# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete generic visitor for a parse tree produced by MiniGoParser.

class MiniGoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniGoParser#program.
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literal.
    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literal1.
    def visitLiteral1(self, ctx:MiniGoParser.Literal1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literal3.
    def visitLiteral3(self, ctx:MiniGoParser.Literal3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literal4.
    def visitLiteral4(self, ctx:MiniGoParser.Literal4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_literal.
    def visitArray_literal(self, ctx:MiniGoParser.Array_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_literal_rest.
    def visitArray_literal_rest(self, ctx:MiniGoParser.Array_literal_restContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arraySupport.
    def visitArraySupport(self, ctx:MiniGoParser.ArraySupportContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literal3List.
    def visitLiteral3List(self, ctx:MiniGoParser.Literal3ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_literalSP.
    def visitStruct_literalSP(self, ctx:MiniGoParser.Struct_literalSPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_literal.
    def visitStruct_literal(self, ctx:MiniGoParser.Struct_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_literal3.
    def visitStruct_literal3(self, ctx:MiniGoParser.Struct_literal3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#field_init_list.
    def visitField_init_list(self, ctx:MiniGoParser.Field_init_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#field_init.
    def visitField_init(self, ctx:MiniGoParser.Field_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_expression.
    def visitList_expression(self, ctx:MiniGoParser.List_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression.
    def visitExpression(self, ctx:MiniGoParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#logicalOrExpr.
    def visitLogicalOrExpr(self, ctx:MiniGoParser.LogicalOrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#logicalAndExpr.
    def visitLogicalAndExpr(self, ctx:MiniGoParser.LogicalAndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#equalityExpr.
    def visitEqualityExpr(self, ctx:MiniGoParser.EqualityExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#relationalExpr.
    def visitRelationalExpr(self, ctx:MiniGoParser.RelationalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#additiveExpr.
    def visitAdditiveExpr(self, ctx:MiniGoParser.AdditiveExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#multiplicativeExpr.
    def visitMultiplicativeExpr(self, ctx:MiniGoParser.MultiplicativeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#unaryExpr.
    def visitUnaryExpr(self, ctx:MiniGoParser.UnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#primaryExpr.
    def visitPrimaryExpr(self, ctx:MiniGoParser.PrimaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#primaryExpr1.
    def visitPrimaryExpr1(self, ctx:MiniGoParser.PrimaryExpr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#postfixOps.
    def visitPostfixOps(self, ctx:MiniGoParser.PostfixOpsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#basePrimary.
    def visitBasePrimary(self, ctx:MiniGoParser.BasePrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#basePrimary1.
    def visitBasePrimary1(self, ctx:MiniGoParser.BasePrimary1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#postfixOp.
    def visitPostfixOp(self, ctx:MiniGoParser.PostfixOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrayAccess.
    def visitArrayAccess(self, ctx:MiniGoParser.ArrayAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#memberAccess.
    def visitMemberAccess(self, ctx:MiniGoParser.MemberAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#functionCall.
    def visitFunctionCall(self, ctx:MiniGoParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#argumentList.
    def visitArgumentList(self, ctx:MiniGoParser.ArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_statement.
    def visitList_statement(self, ctx:MiniGoParser.List_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#statement.
    def visitStatement(self, ctx:MiniGoParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#statement2.
    def visitStatement2(self, ctx:MiniGoParser.Statement2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#statement3.
    def visitStatement3(self, ctx:MiniGoParser.Statement3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#declared_statement.
    def visitDeclared_statement(self, ctx:MiniGoParser.Declared_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#declared_statement2.
    def visitDeclared_statement2(self, ctx:MiniGoParser.Declared_statement2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assign_statement.
    def visitAssign_statement(self, ctx:MiniGoParser.Assign_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assign_statement2.
    def visitAssign_statement2(self, ctx:MiniGoParser.Assign_statement2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignable2.
    def visitAssignable2(self, ctx:MiniGoParser.Assignable2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignable.
    def visitAssignable(self, ctx:MiniGoParser.AssignableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#tail.
    def visitTail(self, ctx:MiniGoParser.TailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#tail2.
    def visitTail2(self, ctx:MiniGoParser.Tail2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#if_block.
    def visitIf_block(self, ctx:MiniGoParser.If_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#if_statement1.
    def visitIf_statement1(self, ctx:MiniGoParser.If_statement1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#else_statement.
    def visitElse_statement(self, ctx:MiniGoParser.Else_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#bodyBLOCK.
    def visitBodyBLOCK(self, ctx:MiniGoParser.BodyBLOCKContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#else_if_statement.
    def visitElse_if_statement(self, ctx:MiniGoParser.Else_if_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#conditional_body_block.
    def visitConditional_body_block(self, ctx:MiniGoParser.Conditional_body_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#if_statement.
    def visitIf_statement(self, ctx:MiniGoParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#block.
    def visitBlock(self, ctx:MiniGoParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#blockIF.
    def visitBlockIF(self, ctx:MiniGoParser.BlockIFContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#blockIF2.
    def visitBlockIF2(self, ctx:MiniGoParser.BlockIF2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_statement.
    def visitFor_statement(self, ctx:MiniGoParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#break_statement.
    def visitBreak_statement(self, ctx:MiniGoParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#continue_statement.
    def visitContinue_statement(self, ctx:MiniGoParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#call_statement.
    def visitCall_statement(self, ctx:MiniGoParser.Call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#return_statement.
    def visitReturn_statement(self, ctx:MiniGoParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#declared.
    def visitDeclared(self, ctx:MiniGoParser.DeclaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#declared2.
    def visitDeclared2(self, ctx:MiniGoParser.Declared2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#declared3.
    def visitDeclared3(self, ctx:MiniGoParser.Declared3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#variables_declared.
    def visitVariables_declared(self, ctx:MiniGoParser.Variables_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#type_spec.
    def visitType_spec(self, ctx:MiniGoParser.Type_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#constants_declared.
    def visitConstants_declared(self, ctx:MiniGoParser.Constants_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#constants_declared2.
    def visitConstants_declared2(self, ctx:MiniGoParser.Constants_declared2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#constant_expression.
    def visitConstant_expression(self, ctx:MiniGoParser.Constant_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#function_declared.
    def visitFunction_declared(self, ctx:MiniGoParser.Function_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#parameter_list.
    def visitParameter_list(self, ctx:MiniGoParser.Parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#parameter.
    def visitParameter(self, ctx:MiniGoParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#parameter_type.
    def visitParameter_type(self, ctx:MiniGoParser.Parameter_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#return_type.
    def visitReturn_type(self, ctx:MiniGoParser.Return_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_type.
    def visitArray_type(self, ctx:MiniGoParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#function_body.
    def visitFunction_body(self, ctx:MiniGoParser.Function_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#statement_with_newlines.
    def visitStatement_with_newlines(self, ctx:MiniGoParser.Statement_with_newlinesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#statement_list.
    def visitStatement_list(self, ctx:MiniGoParser.Statement_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_declared.
    def visitMethod_declared(self, ctx:MiniGoParser.Method_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#parameter_list2.
    def visitParameter_list2(self, ctx:MiniGoParser.Parameter_list2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#parameter2.
    def visitParameter2(self, ctx:MiniGoParser.Parameter2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#receiver.
    def visitReceiver(self, ctx:MiniGoParser.ReceiverContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#receiver2.
    def visitReceiver2(self, ctx:MiniGoParser.Receiver2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_declared.
    def visitStruct_declared(self, ctx:MiniGoParser.Struct_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#field_list.
    def visitField_list(self, ctx:MiniGoParser.Field_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#field.
    def visitField(self, ctx:MiniGoParser.FieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_declared.
    def visitInterface_declared(self, ctx:MiniGoParser.Interface_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#optional_newlines.
    def visitOptional_newlines(self, ctx:MiniGoParser.Optional_newlinesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_list.
    def visitMethod_list(self, ctx:MiniGoParser.Method_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#recursive_newlines.
    def visitRecursive_newlines(self, ctx:MiniGoParser.Recursive_newlinesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_decl.
    def visitMethod_decl(self, ctx:MiniGoParser.Method_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_signature.
    def visitMethod_signature(self, ctx:MiniGoParser.Method_signatureContext):
        return self.visitChildren(ctx)



del MiniGoParser