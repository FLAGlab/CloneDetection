# Generated from ./clone_detection/grammars/dart/Dart2.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .Dart2Parser import Dart2Parser
else:
    from Dart2Parser import Dart2Parser

# This class defines a complete generic visitor for a parse tree produced by Dart2Parser.

class Dart2Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by Dart2Parser#compilationUnit.
    def visitCompilationUnit(self, ctx:Dart2Parser.CompilationUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:Dart2Parser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#declaredIdentifier.
    def visitDeclaredIdentifier(self, ctx:Dart2Parser.DeclaredIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#finalConstVarOrType.
    def visitFinalConstVarOrType(self, ctx:Dart2Parser.FinalConstVarOrTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#varOrType.
    def visitVarOrType(self, ctx:Dart2Parser.VarOrTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#initializedVariableDeclaration.
    def visitInitializedVariableDeclaration(self, ctx:Dart2Parser.InitializedVariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#initializedIdentifier.
    def visitInitializedIdentifier(self, ctx:Dart2Parser.InitializedIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#initializedIdentifierList.
    def visitInitializedIdentifierList(self, ctx:Dart2Parser.InitializedIdentifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#functionSignature.
    def visitFunctionSignature(self, ctx:Dart2Parser.FunctionSignatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#formalParameterPart.
    def visitFormalParameterPart(self, ctx:Dart2Parser.FormalParameterPartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#returnType.
    def visitReturnType(self, ctx:Dart2Parser.ReturnTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#functionBody.
    def visitFunctionBody(self, ctx:Dart2Parser.FunctionBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#block.
    def visitBlock(self, ctx:Dart2Parser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#formalParameterList.
    def visitFormalParameterList(self, ctx:Dart2Parser.FormalParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#normalFormalParameters.
    def visitNormalFormalParameters(self, ctx:Dart2Parser.NormalFormalParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#optionalFormalParameters.
    def visitOptionalFormalParameters(self, ctx:Dart2Parser.OptionalFormalParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#optionalPositionalFormalParameters.
    def visitOptionalPositionalFormalParameters(self, ctx:Dart2Parser.OptionalPositionalFormalParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#namedFormalParameters.
    def visitNamedFormalParameters(self, ctx:Dart2Parser.NamedFormalParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#normalFormalParameter.
    def visitNormalFormalParameter(self, ctx:Dart2Parser.NormalFormalParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#functionFormalParameter.
    def visitFunctionFormalParameter(self, ctx:Dart2Parser.FunctionFormalParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#simpleFormalParameter.
    def visitSimpleFormalParameter(self, ctx:Dart2Parser.SimpleFormalParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#fieldFormalParameter.
    def visitFieldFormalParameter(self, ctx:Dart2Parser.FieldFormalParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#defaultFormalParameter.
    def visitDefaultFormalParameter(self, ctx:Dart2Parser.DefaultFormalParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#defaultNamedParameter.
    def visitDefaultNamedParameter(self, ctx:Dart2Parser.DefaultNamedParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#classDefinition.
    def visitClassDefinition(self, ctx:Dart2Parser.ClassDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#mixins.
    def visitMixins(self, ctx:Dart2Parser.MixinsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#classMemberDefinition.
    def visitClassMemberDefinition(self, ctx:Dart2Parser.ClassMemberDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#methodSignature.
    def visitMethodSignature(self, ctx:Dart2Parser.MethodSignatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#declaration.
    def visitDeclaration(self, ctx:Dart2Parser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#staticFinalDeclarationList.
    def visitStaticFinalDeclarationList(self, ctx:Dart2Parser.StaticFinalDeclarationListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#staticFinalDeclaration.
    def visitStaticFinalDeclaration(self, ctx:Dart2Parser.StaticFinalDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#operatorSignature.
    def visitOperatorSignature(self, ctx:Dart2Parser.OperatorSignatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#operator_.
    def visitOperator_(self, ctx:Dart2Parser.Operator_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#binaryOperator.
    def visitBinaryOperator(self, ctx:Dart2Parser.BinaryOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#getterSignature.
    def visitGetterSignature(self, ctx:Dart2Parser.GetterSignatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#setterSignature.
    def visitSetterSignature(self, ctx:Dart2Parser.SetterSignatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#constructorSignature.
    def visitConstructorSignature(self, ctx:Dart2Parser.ConstructorSignatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#redirection.
    def visitRedirection(self, ctx:Dart2Parser.RedirectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#initializers.
    def visitInitializers(self, ctx:Dart2Parser.InitializersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#initializerListEntry.
    def visitInitializerListEntry(self, ctx:Dart2Parser.InitializerListEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#fieldInitializer.
    def visitFieldInitializer(self, ctx:Dart2Parser.FieldInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#factoryConstructorSignature.
    def visitFactoryConstructorSignature(self, ctx:Dart2Parser.FactoryConstructorSignatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#redirectingFactoryConstructorSignature.
    def visitRedirectingFactoryConstructorSignature(self, ctx:Dart2Parser.RedirectingFactoryConstructorSignatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#constantConstructorSignature.
    def visitConstantConstructorSignature(self, ctx:Dart2Parser.ConstantConstructorSignatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#superclass.
    def visitSuperclass(self, ctx:Dart2Parser.SuperclassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#interfaces.
    def visitInterfaces(self, ctx:Dart2Parser.InterfacesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#mixinApplicationClass.
    def visitMixinApplicationClass(self, ctx:Dart2Parser.MixinApplicationClassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#mixinApplication.
    def visitMixinApplication(self, ctx:Dart2Parser.MixinApplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#enumType.
    def visitEnumType(self, ctx:Dart2Parser.EnumTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#enumEntry.
    def visitEnumEntry(self, ctx:Dart2Parser.EnumEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#typeParameter.
    def visitTypeParameter(self, ctx:Dart2Parser.TypeParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#typeParameters.
    def visitTypeParameters(self, ctx:Dart2Parser.TypeParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#metadata.
    def visitMetadata(self, ctx:Dart2Parser.MetadataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#expression.
    def visitExpression(self, ctx:Dart2Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#expressionWithoutCascade.
    def visitExpressionWithoutCascade(self, ctx:Dart2Parser.ExpressionWithoutCascadeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#expressionList.
    def visitExpressionList(self, ctx:Dart2Parser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#primary.
    def visitPrimary(self, ctx:Dart2Parser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#literal.
    def visitLiteral(self, ctx:Dart2Parser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#nullLiteral.
    def visitNullLiteral(self, ctx:Dart2Parser.NullLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#numericLiteral.
    def visitNumericLiteral(self, ctx:Dart2Parser.NumericLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#booleanLiteral.
    def visitBooleanLiteral(self, ctx:Dart2Parser.BooleanLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#stringLiteral.
    def visitStringLiteral(self, ctx:Dart2Parser.StringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#stringInterpolation.
    def visitStringInterpolation(self, ctx:Dart2Parser.StringInterpolationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#symbolLiteral.
    def visitSymbolLiteral(self, ctx:Dart2Parser.SymbolLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#listLiteral.
    def visitListLiteral(self, ctx:Dart2Parser.ListLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#mapLiteral.
    def visitMapLiteral(self, ctx:Dart2Parser.MapLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#mapLiteralEntry.
    def visitMapLiteralEntry(self, ctx:Dart2Parser.MapLiteralEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#throwExpression.
    def visitThrowExpression(self, ctx:Dart2Parser.ThrowExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#throwExpressionWithoutCascade.
    def visitThrowExpressionWithoutCascade(self, ctx:Dart2Parser.ThrowExpressionWithoutCascadeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#functionExpression.
    def visitFunctionExpression(self, ctx:Dart2Parser.FunctionExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#thisExpression.
    def visitThisExpression(self, ctx:Dart2Parser.ThisExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#nayaExpression.
    def visitNayaExpression(self, ctx:Dart2Parser.NayaExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#constObjectExpression.
    def visitConstObjectExpression(self, ctx:Dart2Parser.ConstObjectExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#arguments.
    def visitArguments(self, ctx:Dart2Parser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#argumentList.
    def visitArgumentList(self, ctx:Dart2Parser.ArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#namedArgument.
    def visitNamedArgument(self, ctx:Dart2Parser.NamedArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#cascadeSection.
    def visitCascadeSection(self, ctx:Dart2Parser.CascadeSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#cascadeSelector.
    def visitCascadeSelector(self, ctx:Dart2Parser.CascadeSelectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#argumentPart.
    def visitArgumentPart(self, ctx:Dart2Parser.ArgumentPartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#assignmentOperator.
    def visitAssignmentOperator(self, ctx:Dart2Parser.AssignmentOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#compoundAssignmentOperator.
    def visitCompoundAssignmentOperator(self, ctx:Dart2Parser.CompoundAssignmentOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#conditionalExpression.
    def visitConditionalExpression(self, ctx:Dart2Parser.ConditionalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#ifNullExpression.
    def visitIfNullExpression(self, ctx:Dart2Parser.IfNullExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#logicalOrExpression.
    def visitLogicalOrExpression(self, ctx:Dart2Parser.LogicalOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#logicalAndExpression.
    def visitLogicalAndExpression(self, ctx:Dart2Parser.LogicalAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#equalityExpression.
    def visitEqualityExpression(self, ctx:Dart2Parser.EqualityExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#equalityOperator.
    def visitEqualityOperator(self, ctx:Dart2Parser.EqualityOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#relationalExpression.
    def visitRelationalExpression(self, ctx:Dart2Parser.RelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#relationalOperator.
    def visitRelationalOperator(self, ctx:Dart2Parser.RelationalOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#bitwiseOrExpression.
    def visitBitwiseOrExpression(self, ctx:Dart2Parser.BitwiseOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#bitwiseXorExpression.
    def visitBitwiseXorExpression(self, ctx:Dart2Parser.BitwiseXorExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#bitwiseAndExpression.
    def visitBitwiseAndExpression(self, ctx:Dart2Parser.BitwiseAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#bitwiseOperator.
    def visitBitwiseOperator(self, ctx:Dart2Parser.BitwiseOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#shiftExpression.
    def visitShiftExpression(self, ctx:Dart2Parser.ShiftExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#shiftOperator.
    def visitShiftOperator(self, ctx:Dart2Parser.ShiftOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#additiveExpression.
    def visitAdditiveExpression(self, ctx:Dart2Parser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#additiveOperator.
    def visitAdditiveOperator(self, ctx:Dart2Parser.AdditiveOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:Dart2Parser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#multiplicativeOperator.
    def visitMultiplicativeOperator(self, ctx:Dart2Parser.MultiplicativeOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#unaryExpression.
    def visitUnaryExpression(self, ctx:Dart2Parser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#prefixOperator.
    def visitPrefixOperator(self, ctx:Dart2Parser.PrefixOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#minusOperator.
    def visitMinusOperator(self, ctx:Dart2Parser.MinusOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#negationOperator.
    def visitNegationOperator(self, ctx:Dart2Parser.NegationOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#tildeOperator.
    def visitTildeOperator(self, ctx:Dart2Parser.TildeOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#awaitExpression.
    def visitAwaitExpression(self, ctx:Dart2Parser.AwaitExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#postfixExpression.
    def visitPostfixExpression(self, ctx:Dart2Parser.PostfixExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#postfixOperator.
    def visitPostfixOperator(self, ctx:Dart2Parser.PostfixOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#selector.
    def visitSelector(self, ctx:Dart2Parser.SelectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#incrementOperator.
    def visitIncrementOperator(self, ctx:Dart2Parser.IncrementOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#assignableExpression.
    def visitAssignableExpression(self, ctx:Dart2Parser.AssignableExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#unconditionalAssignableSelector.
    def visitUnconditionalAssignableSelector(self, ctx:Dart2Parser.UnconditionalAssignableSelectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#assignableSelector.
    def visitAssignableSelector(self, ctx:Dart2Parser.AssignableSelectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#identifier.
    def visitIdentifier(self, ctx:Dart2Parser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#qualified.
    def visitQualified(self, ctx:Dart2Parser.QualifiedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#typeTest.
    def visitTypeTest(self, ctx:Dart2Parser.TypeTestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#isOperator.
    def visitIsOperator(self, ctx:Dart2Parser.IsOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#typeCast.
    def visitTypeCast(self, ctx:Dart2Parser.TypeCastContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#asOperator.
    def visitAsOperator(self, ctx:Dart2Parser.AsOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#statements.
    def visitStatements(self, ctx:Dart2Parser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#statement.
    def visitStatement(self, ctx:Dart2Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#nonLabledStatment.
    def visitNonLabledStatment(self, ctx:Dart2Parser.NonLabledStatmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#expressionStatement.
    def visitExpressionStatement(self, ctx:Dart2Parser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#localVariableDeclaration.
    def visitLocalVariableDeclaration(self, ctx:Dart2Parser.LocalVariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#localFunctionDeclaration.
    def visitLocalFunctionDeclaration(self, ctx:Dart2Parser.LocalFunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#ifStatement.
    def visitIfStatement(self, ctx:Dart2Parser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#forStatement.
    def visitForStatement(self, ctx:Dart2Parser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#forLoopParts.
    def visitForLoopParts(self, ctx:Dart2Parser.ForLoopPartsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#forInitializerStatement.
    def visitForInitializerStatement(self, ctx:Dart2Parser.ForInitializerStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#whileStatement.
    def visitWhileStatement(self, ctx:Dart2Parser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#doStatement.
    def visitDoStatement(self, ctx:Dart2Parser.DoStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#switchStatement.
    def visitSwitchStatement(self, ctx:Dart2Parser.SwitchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#switchCase.
    def visitSwitchCase(self, ctx:Dart2Parser.SwitchCaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#defaultCase.
    def visitDefaultCase(self, ctx:Dart2Parser.DefaultCaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#rethrowStatment.
    def visitRethrowStatment(self, ctx:Dart2Parser.RethrowStatmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#tryStatement.
    def visitTryStatement(self, ctx:Dart2Parser.TryStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#onPart.
    def visitOnPart(self, ctx:Dart2Parser.OnPartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#catchPart.
    def visitCatchPart(self, ctx:Dart2Parser.CatchPartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#finallyPart.
    def visitFinallyPart(self, ctx:Dart2Parser.FinallyPartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#returnStatement.
    def visitReturnStatement(self, ctx:Dart2Parser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#label.
    def visitLabel(self, ctx:Dart2Parser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#breakStatement.
    def visitBreakStatement(self, ctx:Dart2Parser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#continueStatement.
    def visitContinueStatement(self, ctx:Dart2Parser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#yieldStatement.
    def visitYieldStatement(self, ctx:Dart2Parser.YieldStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#yieldEachStatement.
    def visitYieldEachStatement(self, ctx:Dart2Parser.YieldEachStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#assertStatement.
    def visitAssertStatement(self, ctx:Dart2Parser.AssertStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#assertion.
    def visitAssertion(self, ctx:Dart2Parser.AssertionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#topLevelDefinition.
    def visitTopLevelDefinition(self, ctx:Dart2Parser.TopLevelDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#getOrSet.
    def visitGetOrSet(self, ctx:Dart2Parser.GetOrSetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#libraryDefinition.
    def visitLibraryDefinition(self, ctx:Dart2Parser.LibraryDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#scriptTag.
    def visitScriptTag(self, ctx:Dart2Parser.ScriptTagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#libraryName.
    def visitLibraryName(self, ctx:Dart2Parser.LibraryNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#importOrExport.
    def visitImportOrExport(self, ctx:Dart2Parser.ImportOrExportContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#dottedIdentifierList.
    def visitDottedIdentifierList(self, ctx:Dart2Parser.DottedIdentifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#libraryimport.
    def visitLibraryimport(self, ctx:Dart2Parser.LibraryimportContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#importSpecification.
    def visitImportSpecification(self, ctx:Dart2Parser.ImportSpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#combinator.
    def visitCombinator(self, ctx:Dart2Parser.CombinatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#identifierList.
    def visitIdentifierList(self, ctx:Dart2Parser.IdentifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#libraryExport.
    def visitLibraryExport(self, ctx:Dart2Parser.LibraryExportContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#partDirective.
    def visitPartDirective(self, ctx:Dart2Parser.PartDirectiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#partHeader.
    def visitPartHeader(self, ctx:Dart2Parser.PartHeaderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#partDeclaration.
    def visitPartDeclaration(self, ctx:Dart2Parser.PartDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#uri.
    def visitUri(self, ctx:Dart2Parser.UriContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#configurableUri.
    def visitConfigurableUri(self, ctx:Dart2Parser.ConfigurableUriContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#configurationUri.
    def visitConfigurationUri(self, ctx:Dart2Parser.ConfigurationUriContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#uriTest.
    def visitUriTest(self, ctx:Dart2Parser.UriTestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#dtype.
    def visitDtype(self, ctx:Dart2Parser.DtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#typeName.
    def visitTypeName(self, ctx:Dart2Parser.TypeNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#typeArguments.
    def visitTypeArguments(self, ctx:Dart2Parser.TypeArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#typeList.
    def visitTypeList(self, ctx:Dart2Parser.TypeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#typeAlias.
    def visitTypeAlias(self, ctx:Dart2Parser.TypeAliasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#typeAliasBody.
    def visitTypeAliasBody(self, ctx:Dart2Parser.TypeAliasBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#functionTypeAlias.
    def visitFunctionTypeAlias(self, ctx:Dart2Parser.FunctionTypeAliasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Dart2Parser#functionPrefix.
    def visitFunctionPrefix(self, ctx:Dart2Parser.FunctionPrefixContext):
        return self.visitChildren(ctx)



del Dart2Parser