# Generated from ../clone_detection/grammars/kotlin/KotlinParser.g4 by ANTLR 4.7.1
from antlr4 import *
from .KotlinParser import KotlinParser

from clone_detection.grammars.grammars_registry import VISITORS


# This class defines a complete generic visitor for a parse tree produced by KotlinParser.
@VISITORS.register('kt')
class KotlinParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by KotlinParser#kotlinFile.
    def visitKotlinFile(self, ctx:KotlinParser.KotlinFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#script.
    def visitScript(self, ctx:KotlinParser.ScriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#preamble.
    def visitPreamble(self, ctx:KotlinParser.PreambleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#fileAnnotations.
    def visitFileAnnotations(self, ctx:KotlinParser.FileAnnotationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#fileAnnotation.
    def visitFileAnnotation(self, ctx:KotlinParser.FileAnnotationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#packageHeader.
    def visitPackageHeader(self, ctx:KotlinParser.PackageHeaderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#importList.
    def visitImportList(self, ctx:KotlinParser.ImportListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#importHeader.
    def visitImportHeader(self, ctx:KotlinParser.ImportHeaderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#importAlias.
    def visitImportAlias(self, ctx:KotlinParser.ImportAliasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#topLevelObject.
    def visitTopLevelObject(self, ctx:KotlinParser.TopLevelObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#classDeclaration.
    def visitClassDeclaration(self, ctx:KotlinParser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#primaryConstructor.
    def visitPrimaryConstructor(self, ctx:KotlinParser.PrimaryConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#classParameters.
    def visitClassParameters(self, ctx:KotlinParser.ClassParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#classParameter.
    def visitClassParameter(self, ctx:KotlinParser.ClassParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#delegationSpecifiers.
    def visitDelegationSpecifiers(self, ctx:KotlinParser.DelegationSpecifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#delegationSpecifier.
    def visitDelegationSpecifier(self, ctx:KotlinParser.DelegationSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#constructorInvocation.
    def visitConstructorInvocation(self, ctx:KotlinParser.ConstructorInvocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#explicitDelegation.
    def visitExplicitDelegation(self, ctx:KotlinParser.ExplicitDelegationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#classBody.
    def visitClassBody(self, ctx:KotlinParser.ClassBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#classMemberDeclaration.
    def visitClassMemberDeclaration(self, ctx:KotlinParser.ClassMemberDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#anonymousInitializer.
    def visitAnonymousInitializer(self, ctx:KotlinParser.AnonymousInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#secondaryConstructor.
    def visitSecondaryConstructor(self, ctx:KotlinParser.SecondaryConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#constructorDelegationCall.
    def visitConstructorDelegationCall(self, ctx:KotlinParser.ConstructorDelegationCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#enumClassBody.
    def visitEnumClassBody(self, ctx:KotlinParser.EnumClassBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#enumEntries.
    def visitEnumEntries(self, ctx:KotlinParser.EnumEntriesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#enumEntry.
    def visitEnumEntry(self, ctx:KotlinParser.EnumEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:KotlinParser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#functionValueParameters.
    def visitFunctionValueParameters(self, ctx:KotlinParser.FunctionValueParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#functionValueParameter.
    def visitFunctionValueParameter(self, ctx:KotlinParser.FunctionValueParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#parameter.
    def visitParameter(self, ctx:KotlinParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#functionBody.
    def visitFunctionBody(self, ctx:KotlinParser.FunctionBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#objectDeclaration.
    def visitObjectDeclaration(self, ctx:KotlinParser.ObjectDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#companionObject.
    def visitCompanionObject(self, ctx:KotlinParser.CompanionObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#propertyDeclaration.
    def visitPropertyDeclaration(self, ctx:KotlinParser.PropertyDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#multiVariableDeclaration.
    def visitMultiVariableDeclaration(self, ctx:KotlinParser.MultiVariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:KotlinParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#getter.
    def visitGetter(self, ctx:KotlinParser.GetterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#setter.
    def visitSetter(self, ctx:KotlinParser.SetterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#typeAlias.
    def visitTypeAlias(self, ctx:KotlinParser.TypeAliasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#typeParameters.
    def visitTypeParameters(self, ctx:KotlinParser.TypeParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#typeParameter.
    def visitTypeParameter(self, ctx:KotlinParser.TypeParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#type.
    def visitType(self, ctx:KotlinParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#typeModifierList.
    def visitTypeModifierList(self, ctx:KotlinParser.TypeModifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#parenthesizedType.
    def visitParenthesizedType(self, ctx:KotlinParser.ParenthesizedTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#nullableType.
    def visitNullableType(self, ctx:KotlinParser.NullableTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#typeReference.
    def visitTypeReference(self, ctx:KotlinParser.TypeReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#functionType.
    def visitFunctionType(self, ctx:KotlinParser.FunctionTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#functionTypeReceiver.
    def visitFunctionTypeReceiver(self, ctx:KotlinParser.FunctionTypeReceiverContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#userType.
    def visitUserType(self, ctx:KotlinParser.UserTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#simpleUserType.
    def visitSimpleUserType(self, ctx:KotlinParser.SimpleUserTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#functionTypeParameters.
    def visitFunctionTypeParameters(self, ctx:KotlinParser.FunctionTypeParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#typeConstraints.
    def visitTypeConstraints(self, ctx:KotlinParser.TypeConstraintsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#typeConstraint.
    def visitTypeConstraint(self, ctx:KotlinParser.TypeConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#block.
    def visitBlock(self, ctx:KotlinParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#statements.
    def visitStatements(self, ctx:KotlinParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#statement.
    def visitStatement(self, ctx:KotlinParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#blockLevelExpression.
    def visitBlockLevelExpression(self, ctx:KotlinParser.BlockLevelExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#declaration.
    def visitDeclaration(self, ctx:KotlinParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#expression.
    def visitExpression(self, ctx:KotlinParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#disjunction.
    def visitDisjunction(self, ctx:KotlinParser.DisjunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#conjunction.
    def visitConjunction(self, ctx:KotlinParser.ConjunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#equalityComparison.
    def visitEqualityComparison(self, ctx:KotlinParser.EqualityComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#comparison.
    def visitComparison(self, ctx:KotlinParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#namedInfix.
    def visitNamedInfix(self, ctx:KotlinParser.NamedInfixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#elvisExpression.
    def visitElvisExpression(self, ctx:KotlinParser.ElvisExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#infixFunctionCall.
    def visitInfixFunctionCall(self, ctx:KotlinParser.InfixFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#rangeExpression.
    def visitRangeExpression(self, ctx:KotlinParser.RangeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:KotlinParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:KotlinParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#typeRHS.
    def visitTypeRHS(self, ctx:KotlinParser.TypeRHSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#prefixUnaryExpression.
    def visitPrefixUnaryExpression(self, ctx:KotlinParser.PrefixUnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#postfixUnaryExpression.
    def visitPostfixUnaryExpression(self, ctx:KotlinParser.PostfixUnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#atomicExpression.
    def visitAtomicExpression(self, ctx:KotlinParser.AtomicExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#parenthesizedExpression.
    def visitParenthesizedExpression(self, ctx:KotlinParser.ParenthesizedExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#callSuffix.
    def visitCallSuffix(self, ctx:KotlinParser.CallSuffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#annotatedLambda.
    def visitAnnotatedLambda(self, ctx:KotlinParser.AnnotatedLambdaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#arrayAccess.
    def visitArrayAccess(self, ctx:KotlinParser.ArrayAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#valueArguments.
    def visitValueArguments(self, ctx:KotlinParser.ValueArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#typeArguments.
    def visitTypeArguments(self, ctx:KotlinParser.TypeArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#typeProjection.
    def visitTypeProjection(self, ctx:KotlinParser.TypeProjectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#typeProjectionModifierList.
    def visitTypeProjectionModifierList(self, ctx:KotlinParser.TypeProjectionModifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#valueArgument.
    def visitValueArgument(self, ctx:KotlinParser.ValueArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#literalConstant.
    def visitLiteralConstant(self, ctx:KotlinParser.LiteralConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#stringLiteral.
    def visitStringLiteral(self, ctx:KotlinParser.StringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#lineStringLiteral.
    def visitLineStringLiteral(self, ctx:KotlinParser.LineStringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#multiLineStringLiteral.
    def visitMultiLineStringLiteral(self, ctx:KotlinParser.MultiLineStringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#lineStringContent.
    def visitLineStringContent(self, ctx:KotlinParser.LineStringContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#lineStringExpression.
    def visitLineStringExpression(self, ctx:KotlinParser.LineStringExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#multiLineStringContent.
    def visitMultiLineStringContent(self, ctx:KotlinParser.MultiLineStringContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#multiLineStringExpression.
    def visitMultiLineStringExpression(self, ctx:KotlinParser.MultiLineStringExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#functionLiteral.
    def visitFunctionLiteral(self, ctx:KotlinParser.FunctionLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#lambdaParameters.
    def visitLambdaParameters(self, ctx:KotlinParser.LambdaParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#lambdaParameter.
    def visitLambdaParameter(self, ctx:KotlinParser.LambdaParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#objectLiteral.
    def visitObjectLiteral(self, ctx:KotlinParser.ObjectLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#collectionLiteral.
    def visitCollectionLiteral(self, ctx:KotlinParser.CollectionLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#thisExpression.
    def visitThisExpression(self, ctx:KotlinParser.ThisExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#superExpression.
    def visitSuperExpression(self, ctx:KotlinParser.SuperExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#conditionalExpression.
    def visitConditionalExpression(self, ctx:KotlinParser.ConditionalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#ifExpression.
    def visitIfExpression(self, ctx:KotlinParser.IfExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#controlStructureBody.
    def visitControlStructureBody(self, ctx:KotlinParser.ControlStructureBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#whenExpression.
    def visitWhenExpression(self, ctx:KotlinParser.WhenExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#whenEntry.
    def visitWhenEntry(self, ctx:KotlinParser.WhenEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#whenCondition.
    def visitWhenCondition(self, ctx:KotlinParser.WhenConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#rangeTest.
    def visitRangeTest(self, ctx:KotlinParser.RangeTestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#typeTest.
    def visitTypeTest(self, ctx:KotlinParser.TypeTestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#tryExpression.
    def visitTryExpression(self, ctx:KotlinParser.TryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#catchBlock.
    def visitCatchBlock(self, ctx:KotlinParser.CatchBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#finallyBlock.
    def visitFinallyBlock(self, ctx:KotlinParser.FinallyBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#loopExpression.
    def visitLoopExpression(self, ctx:KotlinParser.LoopExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#forExpression.
    def visitForExpression(self, ctx:KotlinParser.ForExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#whileExpression.
    def visitWhileExpression(self, ctx:KotlinParser.WhileExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#doWhileExpression.
    def visitDoWhileExpression(self, ctx:KotlinParser.DoWhileExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#jumpExpression.
    def visitJumpExpression(self, ctx:KotlinParser.JumpExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#callableReference.
    def visitCallableReference(self, ctx:KotlinParser.CallableReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx:KotlinParser.AssignmentOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#equalityOperation.
    def visitEqualityOperation(self, ctx:KotlinParser.EqualityOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#comparisonOperator.
    def visitComparisonOperator(self, ctx:KotlinParser.ComparisonOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#inOperator.
    def visitInOperator(self, ctx:KotlinParser.InOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#isOperator.
    def visitIsOperator(self, ctx:KotlinParser.IsOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#additiveOperator.
    def visitAdditiveOperator(self, ctx:KotlinParser.AdditiveOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#multiplicativeOperation.
    def visitMultiplicativeOperation(self, ctx:KotlinParser.MultiplicativeOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#typeOperation.
    def visitTypeOperation(self, ctx:KotlinParser.TypeOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#prefixUnaryOperation.
    def visitPrefixUnaryOperation(self, ctx:KotlinParser.PrefixUnaryOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#postfixUnaryOperation.
    def visitPostfixUnaryOperation(self, ctx:KotlinParser.PostfixUnaryOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#memberAccessOperator.
    def visitMemberAccessOperator(self, ctx:KotlinParser.MemberAccessOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#modifierList.
    def visitModifierList(self, ctx:KotlinParser.ModifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#modifier.
    def visitModifier(self, ctx:KotlinParser.ModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#classModifier.
    def visitClassModifier(self, ctx:KotlinParser.ClassModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#memberModifier.
    def visitMemberModifier(self, ctx:KotlinParser.MemberModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#visibilityModifier.
    def visitVisibilityModifier(self, ctx:KotlinParser.VisibilityModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#varianceAnnotation.
    def visitVarianceAnnotation(self, ctx:KotlinParser.VarianceAnnotationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#functionModifier.
    def visitFunctionModifier(self, ctx:KotlinParser.FunctionModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#propertyModifier.
    def visitPropertyModifier(self, ctx:KotlinParser.PropertyModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#inheritanceModifier.
    def visitInheritanceModifier(self, ctx:KotlinParser.InheritanceModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#parameterModifier.
    def visitParameterModifier(self, ctx:KotlinParser.ParameterModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#typeParameterModifier.
    def visitTypeParameterModifier(self, ctx:KotlinParser.TypeParameterModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#labelDefinition.
    def visitLabelDefinition(self, ctx:KotlinParser.LabelDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#annotations.
    def visitAnnotations(self, ctx:KotlinParser.AnnotationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#annotation.
    def visitAnnotation(self, ctx:KotlinParser.AnnotationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#annotationList.
    def visitAnnotationList(self, ctx:KotlinParser.AnnotationListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#annotationUseSiteTarget.
    def visitAnnotationUseSiteTarget(self, ctx:KotlinParser.AnnotationUseSiteTargetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#unescapedAnnotation.
    def visitUnescapedAnnotation(self, ctx:KotlinParser.UnescapedAnnotationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#identifier.
    def visitIdentifier(self, ctx:KotlinParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#simpleIdentifier.
    def visitSimpleIdentifier(self, ctx:KotlinParser.SimpleIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#semi.
    def visitSemi(self, ctx:KotlinParser.SemiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#anysemi.
    def visitAnysemi(self, ctx:KotlinParser.AnysemiContext):
        return self.visitChildren(ctx)



del KotlinParser