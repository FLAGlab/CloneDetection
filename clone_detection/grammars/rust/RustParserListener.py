# Generated from RustParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .RustParser import RustParser
else:
    from RustParser import RustParser

# This class defines a complete listener for a parse tree produced by RustParser.
class RustParserListener(ParseTreeListener):

    # Enter a parse tree produced by RustParser#crate.
    def enterCrate(self, ctx:RustParser.CrateContext):
        pass

    # Exit a parse tree produced by RustParser#crate.
    def exitCrate(self, ctx:RustParser.CrateContext):
        pass


    # Enter a parse tree produced by RustParser#macroInvocation.
    def enterMacroInvocation(self, ctx:RustParser.MacroInvocationContext):
        pass

    # Exit a parse tree produced by RustParser#macroInvocation.
    def exitMacroInvocation(self, ctx:RustParser.MacroInvocationContext):
        pass


    # Enter a parse tree produced by RustParser#delimTokenTree.
    def enterDelimTokenTree(self, ctx:RustParser.DelimTokenTreeContext):
        pass

    # Exit a parse tree produced by RustParser#delimTokenTree.
    def exitDelimTokenTree(self, ctx:RustParser.DelimTokenTreeContext):
        pass


    # Enter a parse tree produced by RustParser#tokenTree.
    def enterTokenTree(self, ctx:RustParser.TokenTreeContext):
        pass

    # Exit a parse tree produced by RustParser#tokenTree.
    def exitTokenTree(self, ctx:RustParser.TokenTreeContext):
        pass


    # Enter a parse tree produced by RustParser#tokenTreeToken.
    def enterTokenTreeToken(self, ctx:RustParser.TokenTreeTokenContext):
        pass

    # Exit a parse tree produced by RustParser#tokenTreeToken.
    def exitTokenTreeToken(self, ctx:RustParser.TokenTreeTokenContext):
        pass


    # Enter a parse tree produced by RustParser#macroInvocationSemi.
    def enterMacroInvocationSemi(self, ctx:RustParser.MacroInvocationSemiContext):
        pass

    # Exit a parse tree produced by RustParser#macroInvocationSemi.
    def exitMacroInvocationSemi(self, ctx:RustParser.MacroInvocationSemiContext):
        pass


    # Enter a parse tree produced by RustParser#macroRulesDefinition.
    def enterMacroRulesDefinition(self, ctx:RustParser.MacroRulesDefinitionContext):
        pass

    # Exit a parse tree produced by RustParser#macroRulesDefinition.
    def exitMacroRulesDefinition(self, ctx:RustParser.MacroRulesDefinitionContext):
        pass


    # Enter a parse tree produced by RustParser#macroRulesDef.
    def enterMacroRulesDef(self, ctx:RustParser.MacroRulesDefContext):
        pass

    # Exit a parse tree produced by RustParser#macroRulesDef.
    def exitMacroRulesDef(self, ctx:RustParser.MacroRulesDefContext):
        pass


    # Enter a parse tree produced by RustParser#macroRules.
    def enterMacroRules(self, ctx:RustParser.MacroRulesContext):
        pass

    # Exit a parse tree produced by RustParser#macroRules.
    def exitMacroRules(self, ctx:RustParser.MacroRulesContext):
        pass


    # Enter a parse tree produced by RustParser#macroRule.
    def enterMacroRule(self, ctx:RustParser.MacroRuleContext):
        pass

    # Exit a parse tree produced by RustParser#macroRule.
    def exitMacroRule(self, ctx:RustParser.MacroRuleContext):
        pass


    # Enter a parse tree produced by RustParser#macroMatcher.
    def enterMacroMatcher(self, ctx:RustParser.MacroMatcherContext):
        pass

    # Exit a parse tree produced by RustParser#macroMatcher.
    def exitMacroMatcher(self, ctx:RustParser.MacroMatcherContext):
        pass


    # Enter a parse tree produced by RustParser#macroMatch.
    def enterMacroMatch(self, ctx:RustParser.MacroMatchContext):
        pass

    # Exit a parse tree produced by RustParser#macroMatch.
    def exitMacroMatch(self, ctx:RustParser.MacroMatchContext):
        pass


    # Enter a parse tree produced by RustParser#macroMatchToken.
    def enterMacroMatchToken(self, ctx:RustParser.MacroMatchTokenContext):
        pass

    # Exit a parse tree produced by RustParser#macroMatchToken.
    def exitMacroMatchToken(self, ctx:RustParser.MacroMatchTokenContext):
        pass


    # Enter a parse tree produced by RustParser#macroFragSpec.
    def enterMacroFragSpec(self, ctx:RustParser.MacroFragSpecContext):
        pass

    # Exit a parse tree produced by RustParser#macroFragSpec.
    def exitMacroFragSpec(self, ctx:RustParser.MacroFragSpecContext):
        pass


    # Enter a parse tree produced by RustParser#macroRepSep.
    def enterMacroRepSep(self, ctx:RustParser.MacroRepSepContext):
        pass

    # Exit a parse tree produced by RustParser#macroRepSep.
    def exitMacroRepSep(self, ctx:RustParser.MacroRepSepContext):
        pass


    # Enter a parse tree produced by RustParser#macroRepOp.
    def enterMacroRepOp(self, ctx:RustParser.MacroRepOpContext):
        pass

    # Exit a parse tree produced by RustParser#macroRepOp.
    def exitMacroRepOp(self, ctx:RustParser.MacroRepOpContext):
        pass


    # Enter a parse tree produced by RustParser#macroTranscriber.
    def enterMacroTranscriber(self, ctx:RustParser.MacroTranscriberContext):
        pass

    # Exit a parse tree produced by RustParser#macroTranscriber.
    def exitMacroTranscriber(self, ctx:RustParser.MacroTranscriberContext):
        pass


    # Enter a parse tree produced by RustParser#item.
    def enterItem(self, ctx:RustParser.ItemContext):
        pass

    # Exit a parse tree produced by RustParser#item.
    def exitItem(self, ctx:RustParser.ItemContext):
        pass


    # Enter a parse tree produced by RustParser#visItem.
    def enterVisItem(self, ctx:RustParser.VisItemContext):
        pass

    # Exit a parse tree produced by RustParser#visItem.
    def exitVisItem(self, ctx:RustParser.VisItemContext):
        pass


    # Enter a parse tree produced by RustParser#macroItem.
    def enterMacroItem(self, ctx:RustParser.MacroItemContext):
        pass

    # Exit a parse tree produced by RustParser#macroItem.
    def exitMacroItem(self, ctx:RustParser.MacroItemContext):
        pass


    # Enter a parse tree produced by RustParser#module.
    def enterModule(self, ctx:RustParser.ModuleContext):
        pass

    # Exit a parse tree produced by RustParser#module.
    def exitModule(self, ctx:RustParser.ModuleContext):
        pass


    # Enter a parse tree produced by RustParser#externCrate.
    def enterExternCrate(self, ctx:RustParser.ExternCrateContext):
        pass

    # Exit a parse tree produced by RustParser#externCrate.
    def exitExternCrate(self, ctx:RustParser.ExternCrateContext):
        pass


    # Enter a parse tree produced by RustParser#crateRef.
    def enterCrateRef(self, ctx:RustParser.CrateRefContext):
        pass

    # Exit a parse tree produced by RustParser#crateRef.
    def exitCrateRef(self, ctx:RustParser.CrateRefContext):
        pass


    # Enter a parse tree produced by RustParser#asClause.
    def enterAsClause(self, ctx:RustParser.AsClauseContext):
        pass

    # Exit a parse tree produced by RustParser#asClause.
    def exitAsClause(self, ctx:RustParser.AsClauseContext):
        pass


    # Enter a parse tree produced by RustParser#useDeclaration.
    def enterUseDeclaration(self, ctx:RustParser.UseDeclarationContext):
        pass

    # Exit a parse tree produced by RustParser#useDeclaration.
    def exitUseDeclaration(self, ctx:RustParser.UseDeclarationContext):
        pass


    # Enter a parse tree produced by RustParser#useTree.
    def enterUseTree(self, ctx:RustParser.UseTreeContext):
        pass

    # Exit a parse tree produced by RustParser#useTree.
    def exitUseTree(self, ctx:RustParser.UseTreeContext):
        pass


    # Enter a parse tree produced by RustParser#function_.
    def enterFunction_(self, ctx:RustParser.Function_Context):
        pass

    # Exit a parse tree produced by RustParser#function_.
    def exitFunction_(self, ctx:RustParser.Function_Context):
        pass


    # Enter a parse tree produced by RustParser#functionQualifiers.
    def enterFunctionQualifiers(self, ctx:RustParser.FunctionQualifiersContext):
        pass

    # Exit a parse tree produced by RustParser#functionQualifiers.
    def exitFunctionQualifiers(self, ctx:RustParser.FunctionQualifiersContext):
        pass


    # Enter a parse tree produced by RustParser#abi.
    def enterAbi(self, ctx:RustParser.AbiContext):
        pass

    # Exit a parse tree produced by RustParser#abi.
    def exitAbi(self, ctx:RustParser.AbiContext):
        pass


    # Enter a parse tree produced by RustParser#functionParameters.
    def enterFunctionParameters(self, ctx:RustParser.FunctionParametersContext):
        pass

    # Exit a parse tree produced by RustParser#functionParameters.
    def exitFunctionParameters(self, ctx:RustParser.FunctionParametersContext):
        pass


    # Enter a parse tree produced by RustParser#selfParam.
    def enterSelfParam(self, ctx:RustParser.SelfParamContext):
        pass

    # Exit a parse tree produced by RustParser#selfParam.
    def exitSelfParam(self, ctx:RustParser.SelfParamContext):
        pass


    # Enter a parse tree produced by RustParser#shorthandSelf.
    def enterShorthandSelf(self, ctx:RustParser.ShorthandSelfContext):
        pass

    # Exit a parse tree produced by RustParser#shorthandSelf.
    def exitShorthandSelf(self, ctx:RustParser.ShorthandSelfContext):
        pass


    # Enter a parse tree produced by RustParser#typedSelf.
    def enterTypedSelf(self, ctx:RustParser.TypedSelfContext):
        pass

    # Exit a parse tree produced by RustParser#typedSelf.
    def exitTypedSelf(self, ctx:RustParser.TypedSelfContext):
        pass


    # Enter a parse tree produced by RustParser#functionParam.
    def enterFunctionParam(self, ctx:RustParser.FunctionParamContext):
        pass

    # Exit a parse tree produced by RustParser#functionParam.
    def exitFunctionParam(self, ctx:RustParser.FunctionParamContext):
        pass


    # Enter a parse tree produced by RustParser#functionParamPattern.
    def enterFunctionParamPattern(self, ctx:RustParser.FunctionParamPatternContext):
        pass

    # Exit a parse tree produced by RustParser#functionParamPattern.
    def exitFunctionParamPattern(self, ctx:RustParser.FunctionParamPatternContext):
        pass


    # Enter a parse tree produced by RustParser#functionReturnType.
    def enterFunctionReturnType(self, ctx:RustParser.FunctionReturnTypeContext):
        pass

    # Exit a parse tree produced by RustParser#functionReturnType.
    def exitFunctionReturnType(self, ctx:RustParser.FunctionReturnTypeContext):
        pass


    # Enter a parse tree produced by RustParser#typeAlias.
    def enterTypeAlias(self, ctx:RustParser.TypeAliasContext):
        pass

    # Exit a parse tree produced by RustParser#typeAlias.
    def exitTypeAlias(self, ctx:RustParser.TypeAliasContext):
        pass


    # Enter a parse tree produced by RustParser#struct_.
    def enterStruct_(self, ctx:RustParser.Struct_Context):
        pass

    # Exit a parse tree produced by RustParser#struct_.
    def exitStruct_(self, ctx:RustParser.Struct_Context):
        pass


    # Enter a parse tree produced by RustParser#structStruct.
    def enterStructStruct(self, ctx:RustParser.StructStructContext):
        pass

    # Exit a parse tree produced by RustParser#structStruct.
    def exitStructStruct(self, ctx:RustParser.StructStructContext):
        pass


    # Enter a parse tree produced by RustParser#tupleStruct.
    def enterTupleStruct(self, ctx:RustParser.TupleStructContext):
        pass

    # Exit a parse tree produced by RustParser#tupleStruct.
    def exitTupleStruct(self, ctx:RustParser.TupleStructContext):
        pass


    # Enter a parse tree produced by RustParser#structFields.
    def enterStructFields(self, ctx:RustParser.StructFieldsContext):
        pass

    # Exit a parse tree produced by RustParser#structFields.
    def exitStructFields(self, ctx:RustParser.StructFieldsContext):
        pass


    # Enter a parse tree produced by RustParser#structField.
    def enterStructField(self, ctx:RustParser.StructFieldContext):
        pass

    # Exit a parse tree produced by RustParser#structField.
    def exitStructField(self, ctx:RustParser.StructFieldContext):
        pass


    # Enter a parse tree produced by RustParser#tupleFields.
    def enterTupleFields(self, ctx:RustParser.TupleFieldsContext):
        pass

    # Exit a parse tree produced by RustParser#tupleFields.
    def exitTupleFields(self, ctx:RustParser.TupleFieldsContext):
        pass


    # Enter a parse tree produced by RustParser#tupleField.
    def enterTupleField(self, ctx:RustParser.TupleFieldContext):
        pass

    # Exit a parse tree produced by RustParser#tupleField.
    def exitTupleField(self, ctx:RustParser.TupleFieldContext):
        pass


    # Enter a parse tree produced by RustParser#enumeration.
    def enterEnumeration(self, ctx:RustParser.EnumerationContext):
        pass

    # Exit a parse tree produced by RustParser#enumeration.
    def exitEnumeration(self, ctx:RustParser.EnumerationContext):
        pass


    # Enter a parse tree produced by RustParser#enumItems.
    def enterEnumItems(self, ctx:RustParser.EnumItemsContext):
        pass

    # Exit a parse tree produced by RustParser#enumItems.
    def exitEnumItems(self, ctx:RustParser.EnumItemsContext):
        pass


    # Enter a parse tree produced by RustParser#enumItem.
    def enterEnumItem(self, ctx:RustParser.EnumItemContext):
        pass

    # Exit a parse tree produced by RustParser#enumItem.
    def exitEnumItem(self, ctx:RustParser.EnumItemContext):
        pass


    # Enter a parse tree produced by RustParser#enumItemTuple.
    def enterEnumItemTuple(self, ctx:RustParser.EnumItemTupleContext):
        pass

    # Exit a parse tree produced by RustParser#enumItemTuple.
    def exitEnumItemTuple(self, ctx:RustParser.EnumItemTupleContext):
        pass


    # Enter a parse tree produced by RustParser#enumItemStruct.
    def enterEnumItemStruct(self, ctx:RustParser.EnumItemStructContext):
        pass

    # Exit a parse tree produced by RustParser#enumItemStruct.
    def exitEnumItemStruct(self, ctx:RustParser.EnumItemStructContext):
        pass


    # Enter a parse tree produced by RustParser#enumItemDiscriminant.
    def enterEnumItemDiscriminant(self, ctx:RustParser.EnumItemDiscriminantContext):
        pass

    # Exit a parse tree produced by RustParser#enumItemDiscriminant.
    def exitEnumItemDiscriminant(self, ctx:RustParser.EnumItemDiscriminantContext):
        pass


    # Enter a parse tree produced by RustParser#union_.
    def enterUnion_(self, ctx:RustParser.Union_Context):
        pass

    # Exit a parse tree produced by RustParser#union_.
    def exitUnion_(self, ctx:RustParser.Union_Context):
        pass


    # Enter a parse tree produced by RustParser#constantItem.
    def enterConstantItem(self, ctx:RustParser.ConstantItemContext):
        pass

    # Exit a parse tree produced by RustParser#constantItem.
    def exitConstantItem(self, ctx:RustParser.ConstantItemContext):
        pass


    # Enter a parse tree produced by RustParser#staticItem.
    def enterStaticItem(self, ctx:RustParser.StaticItemContext):
        pass

    # Exit a parse tree produced by RustParser#staticItem.
    def exitStaticItem(self, ctx:RustParser.StaticItemContext):
        pass


    # Enter a parse tree produced by RustParser#trait_.
    def enterTrait_(self, ctx:RustParser.Trait_Context):
        pass

    # Exit a parse tree produced by RustParser#trait_.
    def exitTrait_(self, ctx:RustParser.Trait_Context):
        pass


    # Enter a parse tree produced by RustParser#implementation.
    def enterImplementation(self, ctx:RustParser.ImplementationContext):
        pass

    # Exit a parse tree produced by RustParser#implementation.
    def exitImplementation(self, ctx:RustParser.ImplementationContext):
        pass


    # Enter a parse tree produced by RustParser#inherentImpl.
    def enterInherentImpl(self, ctx:RustParser.InherentImplContext):
        pass

    # Exit a parse tree produced by RustParser#inherentImpl.
    def exitInherentImpl(self, ctx:RustParser.InherentImplContext):
        pass


    # Enter a parse tree produced by RustParser#traitImpl.
    def enterTraitImpl(self, ctx:RustParser.TraitImplContext):
        pass

    # Exit a parse tree produced by RustParser#traitImpl.
    def exitTraitImpl(self, ctx:RustParser.TraitImplContext):
        pass


    # Enter a parse tree produced by RustParser#externBlock.
    def enterExternBlock(self, ctx:RustParser.ExternBlockContext):
        pass

    # Exit a parse tree produced by RustParser#externBlock.
    def exitExternBlock(self, ctx:RustParser.ExternBlockContext):
        pass


    # Enter a parse tree produced by RustParser#externalItem.
    def enterExternalItem(self, ctx:RustParser.ExternalItemContext):
        pass

    # Exit a parse tree produced by RustParser#externalItem.
    def exitExternalItem(self, ctx:RustParser.ExternalItemContext):
        pass


    # Enter a parse tree produced by RustParser#genericParams.
    def enterGenericParams(self, ctx:RustParser.GenericParamsContext):
        pass

    # Exit a parse tree produced by RustParser#genericParams.
    def exitGenericParams(self, ctx:RustParser.GenericParamsContext):
        pass


    # Enter a parse tree produced by RustParser#genericParam.
    def enterGenericParam(self, ctx:RustParser.GenericParamContext):
        pass

    # Exit a parse tree produced by RustParser#genericParam.
    def exitGenericParam(self, ctx:RustParser.GenericParamContext):
        pass


    # Enter a parse tree produced by RustParser#lifetimeParam.
    def enterLifetimeParam(self, ctx:RustParser.LifetimeParamContext):
        pass

    # Exit a parse tree produced by RustParser#lifetimeParam.
    def exitLifetimeParam(self, ctx:RustParser.LifetimeParamContext):
        pass


    # Enter a parse tree produced by RustParser#typeParam.
    def enterTypeParam(self, ctx:RustParser.TypeParamContext):
        pass

    # Exit a parse tree produced by RustParser#typeParam.
    def exitTypeParam(self, ctx:RustParser.TypeParamContext):
        pass


    # Enter a parse tree produced by RustParser#constParam.
    def enterConstParam(self, ctx:RustParser.ConstParamContext):
        pass

    # Exit a parse tree produced by RustParser#constParam.
    def exitConstParam(self, ctx:RustParser.ConstParamContext):
        pass


    # Enter a parse tree produced by RustParser#whereClause.
    def enterWhereClause(self, ctx:RustParser.WhereClauseContext):
        pass

    # Exit a parse tree produced by RustParser#whereClause.
    def exitWhereClause(self, ctx:RustParser.WhereClauseContext):
        pass


    # Enter a parse tree produced by RustParser#whereClauseItem.
    def enterWhereClauseItem(self, ctx:RustParser.WhereClauseItemContext):
        pass

    # Exit a parse tree produced by RustParser#whereClauseItem.
    def exitWhereClauseItem(self, ctx:RustParser.WhereClauseItemContext):
        pass


    # Enter a parse tree produced by RustParser#lifetimeWhereClauseItem.
    def enterLifetimeWhereClauseItem(self, ctx:RustParser.LifetimeWhereClauseItemContext):
        pass

    # Exit a parse tree produced by RustParser#lifetimeWhereClauseItem.
    def exitLifetimeWhereClauseItem(self, ctx:RustParser.LifetimeWhereClauseItemContext):
        pass


    # Enter a parse tree produced by RustParser#typeBoundWhereClauseItem.
    def enterTypeBoundWhereClauseItem(self, ctx:RustParser.TypeBoundWhereClauseItemContext):
        pass

    # Exit a parse tree produced by RustParser#typeBoundWhereClauseItem.
    def exitTypeBoundWhereClauseItem(self, ctx:RustParser.TypeBoundWhereClauseItemContext):
        pass


    # Enter a parse tree produced by RustParser#forLifetimes.
    def enterForLifetimes(self, ctx:RustParser.ForLifetimesContext):
        pass

    # Exit a parse tree produced by RustParser#forLifetimes.
    def exitForLifetimes(self, ctx:RustParser.ForLifetimesContext):
        pass


    # Enter a parse tree produced by RustParser#associatedItem.
    def enterAssociatedItem(self, ctx:RustParser.AssociatedItemContext):
        pass

    # Exit a parse tree produced by RustParser#associatedItem.
    def exitAssociatedItem(self, ctx:RustParser.AssociatedItemContext):
        pass


    # Enter a parse tree produced by RustParser#innerAttribute.
    def enterInnerAttribute(self, ctx:RustParser.InnerAttributeContext):
        pass

    # Exit a parse tree produced by RustParser#innerAttribute.
    def exitInnerAttribute(self, ctx:RustParser.InnerAttributeContext):
        pass


    # Enter a parse tree produced by RustParser#outerAttribute.
    def enterOuterAttribute(self, ctx:RustParser.OuterAttributeContext):
        pass

    # Exit a parse tree produced by RustParser#outerAttribute.
    def exitOuterAttribute(self, ctx:RustParser.OuterAttributeContext):
        pass


    # Enter a parse tree produced by RustParser#attr.
    def enterAttr(self, ctx:RustParser.AttrContext):
        pass

    # Exit a parse tree produced by RustParser#attr.
    def exitAttr(self, ctx:RustParser.AttrContext):
        pass


    # Enter a parse tree produced by RustParser#attrInput.
    def enterAttrInput(self, ctx:RustParser.AttrInputContext):
        pass

    # Exit a parse tree produced by RustParser#attrInput.
    def exitAttrInput(self, ctx:RustParser.AttrInputContext):
        pass


    # Enter a parse tree produced by RustParser#statement.
    def enterStatement(self, ctx:RustParser.StatementContext):
        pass

    # Exit a parse tree produced by RustParser#statement.
    def exitStatement(self, ctx:RustParser.StatementContext):
        pass


    # Enter a parse tree produced by RustParser#letStatement.
    def enterLetStatement(self, ctx:RustParser.LetStatementContext):
        pass

    # Exit a parse tree produced by RustParser#letStatement.
    def exitLetStatement(self, ctx:RustParser.LetStatementContext):
        pass


    # Enter a parse tree produced by RustParser#expressionStatement.
    def enterExpressionStatement(self, ctx:RustParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by RustParser#expressionStatement.
    def exitExpressionStatement(self, ctx:RustParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by RustParser#TypeCastExpression.
    def enterTypeCastExpression(self, ctx:RustParser.TypeCastExpressionContext):
        pass

    # Exit a parse tree produced by RustParser#TypeCastExpression.
    def exitTypeCastExpression(self, ctx:RustParser.TypeCastExpressionContext):
        pass


    # Enter a parse tree produced by RustParser#PathExpression_.
    def enterPathExpression_(self, ctx:RustParser.PathExpression_Context):
        pass

    # Exit a parse tree produced by RustParser#PathExpression_.
    def exitPathExpression_(self, ctx:RustParser.PathExpression_Context):
        pass


    # Enter a parse tree produced by RustParser#TupleExpression.
    def enterTupleExpression(self, ctx:RustParser.TupleExpressionContext):
        pass

    # Exit a parse tree produced by RustParser#TupleExpression.
    def exitTupleExpression(self, ctx:RustParser.TupleExpressionContext):
        pass


    # Enter a parse tree produced by RustParser#IndexExpression.
    def enterIndexExpression(self, ctx:RustParser.IndexExpressionContext):
        pass

    # Exit a parse tree produced by RustParser#IndexExpression.
    def exitIndexExpression(self, ctx:RustParser.IndexExpressionContext):
        pass


    # Enter a parse tree produced by RustParser#RangeExpression.
    def enterRangeExpression(self, ctx:RustParser.RangeExpressionContext):
        pass

    # Exit a parse tree produced by RustParser#RangeExpression.
    def exitRangeExpression(self, ctx:RustParser.RangeExpressionContext):
        pass


    # Enter a parse tree produced by RustParser#MacroInvocationAsExpression.
    def enterMacroInvocationAsExpression(self, ctx:RustParser.MacroInvocationAsExpressionContext):
        pass

    # Exit a parse tree produced by RustParser#MacroInvocationAsExpression.
    def exitMacroInvocationAsExpression(self, ctx:RustParser.MacroInvocationAsExpressionContext):
        pass


    # Enter a parse tree produced by RustParser#ReturnExpression.
    def enterReturnExpression(self, ctx:RustParser.ReturnExpressionContext):
        pass

    # Exit a parse tree produced by RustParser#ReturnExpression.
    def exitReturnExpression(self, ctx:RustParser.ReturnExpressionContext):
        pass


    # Enter a parse tree produced by RustParser#AwaitExpression.
    def enterAwaitExpression(self, ctx:RustParser.AwaitExpressionContext):
        pass

    # Exit a parse tree produced by RustParser#AwaitExpression.
    def exitAwaitExpression(self, ctx:RustParser.AwaitExpressionContext):
        pass


    # Enter a parse tree produced by RustParser#ErrorPropagationExpression.
    def enterErrorPropagationExpression(self, ctx:RustParser.ErrorPropagationExpressionContext):
        pass

    # Exit a parse tree produced by RustParser#ErrorPropagationExpression.
    def exitErrorPropagationExpression(self, ctx:RustParser.ErrorPropagationExpressionContext):
        pass


    # Enter a parse tree produced by RustParser#ContinueExpression.
    def enterContinueExpression(self, ctx:RustParser.ContinueExpressionContext):
        pass

    # Exit a parse tree produced by RustParser#ContinueExpression.
    def exitContinueExpression(self, ctx:RustParser.ContinueExpressionContext):
        pass


    # Enter a parse tree produced by RustParser#AssignmentExpression.
    def enterAssignmentExpression(self, ctx:RustParser.AssignmentExpressionContext):
        pass

    # Exit a parse tree produced by RustParser#AssignmentExpression.
    def exitAssignmentExpression(self, ctx:RustParser.AssignmentExpressionContext):
        pass


    # Enter a parse tree produced by RustParser#MethodCallExpression.
    def enterMethodCallExpression(self, ctx:RustParser.MethodCallExpressionContext):
        pass

    # Exit a parse tree produced by RustParser#MethodCallExpression.
    def exitMethodCallExpression(self, ctx:RustParser.MethodCallExpressionContext):
        pass


    # Enter a parse tree produced by RustParser#LiteralExpression_.
    def enterLiteralExpression_(self, ctx:RustParser.LiteralExpression_Context):
        pass

    # Exit a parse tree produced by RustParser#LiteralExpression_.
    def exitLiteralExpression_(self, ctx:RustParser.LiteralExpression_Context):
        pass


    # Enter a parse tree produced by RustParser#StructExpression_.
    def enterStructExpression_(self, ctx:RustParser.StructExpression_Context):
        pass

    # Exit a parse tree produced by RustParser#StructExpression_.
    def exitStructExpression_(self, ctx:RustParser.StructExpression_Context):
        pass


    # Enter a parse tree produced by RustParser#TupleIndexingExpression.
    def enterTupleIndexingExpression(self, ctx:RustParser.TupleIndexingExpressionContext):
        pass

    # Exit a parse tree produced by RustParser#TupleIndexingExpression.
    def exitTupleIndexingExpression(self, ctx:RustParser.TupleIndexingExpressionContext):
        pass


    # Enter a parse tree produced by RustParser#NegationExpression.
    def enterNegationExpression(self, ctx:RustParser.NegationExpressionContext):
        pass

    # Exit a parse tree produced by RustParser#NegationExpression.
    def exitNegationExpression(self, ctx:RustParser.NegationExpressionContext):
        pass


    # Enter a parse tree produced by RustParser#CallExpression.
    def enterCallExpression(self, ctx:RustParser.CallExpressionContext):
        pass

    # Exit a parse tree produced by RustParser#CallExpression.
    def exitCallExpression(self, ctx:RustParser.CallExpressionContext):
        pass


    # Enter a parse tree produced by RustParser#LazyBooleanExpression.
    def enterLazyBooleanExpression(self, ctx:RustParser.LazyBooleanExpressionContext):
        pass

    # Exit a parse tree produced by RustParser#LazyBooleanExpression.
    def exitLazyBooleanExpression(self, ctx:RustParser.LazyBooleanExpressionContext):
        pass


    # Enter a parse tree produced by RustParser#DereferenceExpression.
    def enterDereferenceExpression(self, ctx:RustParser.DereferenceExpressionContext):
        pass

    # Exit a parse tree produced by RustParser#DereferenceExpression.
    def exitDereferenceExpression(self, ctx:RustParser.DereferenceExpressionContext):
        pass


    # Enter a parse tree produced by RustParser#ExpressionWithBlock_.
    def enterExpressionWithBlock_(self, ctx:RustParser.ExpressionWithBlock_Context):
        pass

    # Exit a parse tree produced by RustParser#ExpressionWithBlock_.
    def exitExpressionWithBlock_(self, ctx:RustParser.ExpressionWithBlock_Context):
        pass


    # Enter a parse tree produced by RustParser#GroupedExpression.
    def enterGroupedExpression(self, ctx:RustParser.GroupedExpressionContext):
        pass

    # Exit a parse tree produced by RustParser#GroupedExpression.
    def exitGroupedExpression(self, ctx:RustParser.GroupedExpressionContext):
        pass


    # Enter a parse tree produced by RustParser#BreakExpression.
    def enterBreakExpression(self, ctx:RustParser.BreakExpressionContext):
        pass

    # Exit a parse tree produced by RustParser#BreakExpression.
    def exitBreakExpression(self, ctx:RustParser.BreakExpressionContext):
        pass


    # Enter a parse tree produced by RustParser#ArithmeticOrLogicalExpression.
    def enterArithmeticOrLogicalExpression(self, ctx:RustParser.ArithmeticOrLogicalExpressionContext):
        pass

    # Exit a parse tree produced by RustParser#ArithmeticOrLogicalExpression.
    def exitArithmeticOrLogicalExpression(self, ctx:RustParser.ArithmeticOrLogicalExpressionContext):
        pass


    # Enter a parse tree produced by RustParser#FieldExpression.
    def enterFieldExpression(self, ctx:RustParser.FieldExpressionContext):
        pass

    # Exit a parse tree produced by RustParser#FieldExpression.
    def exitFieldExpression(self, ctx:RustParser.FieldExpressionContext):
        pass


    # Enter a parse tree produced by RustParser#EnumerationVariantExpression_.
    def enterEnumerationVariantExpression_(self, ctx:RustParser.EnumerationVariantExpression_Context):
        pass

    # Exit a parse tree produced by RustParser#EnumerationVariantExpression_.
    def exitEnumerationVariantExpression_(self, ctx:RustParser.EnumerationVariantExpression_Context):
        pass


    # Enter a parse tree produced by RustParser#ComparisonExpression.
    def enterComparisonExpression(self, ctx:RustParser.ComparisonExpressionContext):
        pass

    # Exit a parse tree produced by RustParser#ComparisonExpression.
    def exitComparisonExpression(self, ctx:RustParser.ComparisonExpressionContext):
        pass


    # Enter a parse tree produced by RustParser#AttributedExpression.
    def enterAttributedExpression(self, ctx:RustParser.AttributedExpressionContext):
        pass

    # Exit a parse tree produced by RustParser#AttributedExpression.
    def exitAttributedExpression(self, ctx:RustParser.AttributedExpressionContext):
        pass


    # Enter a parse tree produced by RustParser#BorrowExpression.
    def enterBorrowExpression(self, ctx:RustParser.BorrowExpressionContext):
        pass

    # Exit a parse tree produced by RustParser#BorrowExpression.
    def exitBorrowExpression(self, ctx:RustParser.BorrowExpressionContext):
        pass


    # Enter a parse tree produced by RustParser#CompoundAssignmentExpression.
    def enterCompoundAssignmentExpression(self, ctx:RustParser.CompoundAssignmentExpressionContext):
        pass

    # Exit a parse tree produced by RustParser#CompoundAssignmentExpression.
    def exitCompoundAssignmentExpression(self, ctx:RustParser.CompoundAssignmentExpressionContext):
        pass


    # Enter a parse tree produced by RustParser#ClosureExpression_.
    def enterClosureExpression_(self, ctx:RustParser.ClosureExpression_Context):
        pass

    # Exit a parse tree produced by RustParser#ClosureExpression_.
    def exitClosureExpression_(self, ctx:RustParser.ClosureExpression_Context):
        pass


    # Enter a parse tree produced by RustParser#ArrayExpression.
    def enterArrayExpression(self, ctx:RustParser.ArrayExpressionContext):
        pass

    # Exit a parse tree produced by RustParser#ArrayExpression.
    def exitArrayExpression(self, ctx:RustParser.ArrayExpressionContext):
        pass


    # Enter a parse tree produced by RustParser#comparisonOperator.
    def enterComparisonOperator(self, ctx:RustParser.ComparisonOperatorContext):
        pass

    # Exit a parse tree produced by RustParser#comparisonOperator.
    def exitComparisonOperator(self, ctx:RustParser.ComparisonOperatorContext):
        pass


    # Enter a parse tree produced by RustParser#compoundAssignOperator.
    def enterCompoundAssignOperator(self, ctx:RustParser.CompoundAssignOperatorContext):
        pass

    # Exit a parse tree produced by RustParser#compoundAssignOperator.
    def exitCompoundAssignOperator(self, ctx:RustParser.CompoundAssignOperatorContext):
        pass


    # Enter a parse tree produced by RustParser#expressionWithBlock.
    def enterExpressionWithBlock(self, ctx:RustParser.ExpressionWithBlockContext):
        pass

    # Exit a parse tree produced by RustParser#expressionWithBlock.
    def exitExpressionWithBlock(self, ctx:RustParser.ExpressionWithBlockContext):
        pass


    # Enter a parse tree produced by RustParser#literalExpression.
    def enterLiteralExpression(self, ctx:RustParser.LiteralExpressionContext):
        pass

    # Exit a parse tree produced by RustParser#literalExpression.
    def exitLiteralExpression(self, ctx:RustParser.LiteralExpressionContext):
        pass


    # Enter a parse tree produced by RustParser#pathExpression.
    def enterPathExpression(self, ctx:RustParser.PathExpressionContext):
        pass

    # Exit a parse tree produced by RustParser#pathExpression.
    def exitPathExpression(self, ctx:RustParser.PathExpressionContext):
        pass


    # Enter a parse tree produced by RustParser#blockExpression.
    def enterBlockExpression(self, ctx:RustParser.BlockExpressionContext):
        pass

    # Exit a parse tree produced by RustParser#blockExpression.
    def exitBlockExpression(self, ctx:RustParser.BlockExpressionContext):
        pass


    # Enter a parse tree produced by RustParser#statements.
    def enterStatements(self, ctx:RustParser.StatementsContext):
        pass

    # Exit a parse tree produced by RustParser#statements.
    def exitStatements(self, ctx:RustParser.StatementsContext):
        pass


    # Enter a parse tree produced by RustParser#asyncBlockExpression.
    def enterAsyncBlockExpression(self, ctx:RustParser.AsyncBlockExpressionContext):
        pass

    # Exit a parse tree produced by RustParser#asyncBlockExpression.
    def exitAsyncBlockExpression(self, ctx:RustParser.AsyncBlockExpressionContext):
        pass


    # Enter a parse tree produced by RustParser#unsafeBlockExpression.
    def enterUnsafeBlockExpression(self, ctx:RustParser.UnsafeBlockExpressionContext):
        pass

    # Exit a parse tree produced by RustParser#unsafeBlockExpression.
    def exitUnsafeBlockExpression(self, ctx:RustParser.UnsafeBlockExpressionContext):
        pass


    # Enter a parse tree produced by RustParser#arrayElements.
    def enterArrayElements(self, ctx:RustParser.ArrayElementsContext):
        pass

    # Exit a parse tree produced by RustParser#arrayElements.
    def exitArrayElements(self, ctx:RustParser.ArrayElementsContext):
        pass


    # Enter a parse tree produced by RustParser#tupleElements.
    def enterTupleElements(self, ctx:RustParser.TupleElementsContext):
        pass

    # Exit a parse tree produced by RustParser#tupleElements.
    def exitTupleElements(self, ctx:RustParser.TupleElementsContext):
        pass


    # Enter a parse tree produced by RustParser#tupleIndex.
    def enterTupleIndex(self, ctx:RustParser.TupleIndexContext):
        pass

    # Exit a parse tree produced by RustParser#tupleIndex.
    def exitTupleIndex(self, ctx:RustParser.TupleIndexContext):
        pass


    # Enter a parse tree produced by RustParser#structExpression.
    def enterStructExpression(self, ctx:RustParser.StructExpressionContext):
        pass

    # Exit a parse tree produced by RustParser#structExpression.
    def exitStructExpression(self, ctx:RustParser.StructExpressionContext):
        pass


    # Enter a parse tree produced by RustParser#structExprStruct.
    def enterStructExprStruct(self, ctx:RustParser.StructExprStructContext):
        pass

    # Exit a parse tree produced by RustParser#structExprStruct.
    def exitStructExprStruct(self, ctx:RustParser.StructExprStructContext):
        pass


    # Enter a parse tree produced by RustParser#structExprFields.
    def enterStructExprFields(self, ctx:RustParser.StructExprFieldsContext):
        pass

    # Exit a parse tree produced by RustParser#structExprFields.
    def exitStructExprFields(self, ctx:RustParser.StructExprFieldsContext):
        pass


    # Enter a parse tree produced by RustParser#structExprField.
    def enterStructExprField(self, ctx:RustParser.StructExprFieldContext):
        pass

    # Exit a parse tree produced by RustParser#structExprField.
    def exitStructExprField(self, ctx:RustParser.StructExprFieldContext):
        pass


    # Enter a parse tree produced by RustParser#structBase.
    def enterStructBase(self, ctx:RustParser.StructBaseContext):
        pass

    # Exit a parse tree produced by RustParser#structBase.
    def exitStructBase(self, ctx:RustParser.StructBaseContext):
        pass


    # Enter a parse tree produced by RustParser#structExprTuple.
    def enterStructExprTuple(self, ctx:RustParser.StructExprTupleContext):
        pass

    # Exit a parse tree produced by RustParser#structExprTuple.
    def exitStructExprTuple(self, ctx:RustParser.StructExprTupleContext):
        pass


    # Enter a parse tree produced by RustParser#structExprUnit.
    def enterStructExprUnit(self, ctx:RustParser.StructExprUnitContext):
        pass

    # Exit a parse tree produced by RustParser#structExprUnit.
    def exitStructExprUnit(self, ctx:RustParser.StructExprUnitContext):
        pass


    # Enter a parse tree produced by RustParser#enumerationVariantExpression.
    def enterEnumerationVariantExpression(self, ctx:RustParser.EnumerationVariantExpressionContext):
        pass

    # Exit a parse tree produced by RustParser#enumerationVariantExpression.
    def exitEnumerationVariantExpression(self, ctx:RustParser.EnumerationVariantExpressionContext):
        pass


    # Enter a parse tree produced by RustParser#enumExprStruct.
    def enterEnumExprStruct(self, ctx:RustParser.EnumExprStructContext):
        pass

    # Exit a parse tree produced by RustParser#enumExprStruct.
    def exitEnumExprStruct(self, ctx:RustParser.EnumExprStructContext):
        pass


    # Enter a parse tree produced by RustParser#enumExprFields.
    def enterEnumExprFields(self, ctx:RustParser.EnumExprFieldsContext):
        pass

    # Exit a parse tree produced by RustParser#enumExprFields.
    def exitEnumExprFields(self, ctx:RustParser.EnumExprFieldsContext):
        pass


    # Enter a parse tree produced by RustParser#enumExprField.
    def enterEnumExprField(self, ctx:RustParser.EnumExprFieldContext):
        pass

    # Exit a parse tree produced by RustParser#enumExprField.
    def exitEnumExprField(self, ctx:RustParser.EnumExprFieldContext):
        pass


    # Enter a parse tree produced by RustParser#enumExprTuple.
    def enterEnumExprTuple(self, ctx:RustParser.EnumExprTupleContext):
        pass

    # Exit a parse tree produced by RustParser#enumExprTuple.
    def exitEnumExprTuple(self, ctx:RustParser.EnumExprTupleContext):
        pass


    # Enter a parse tree produced by RustParser#enumExprFieldless.
    def enterEnumExprFieldless(self, ctx:RustParser.EnumExprFieldlessContext):
        pass

    # Exit a parse tree produced by RustParser#enumExprFieldless.
    def exitEnumExprFieldless(self, ctx:RustParser.EnumExprFieldlessContext):
        pass


    # Enter a parse tree produced by RustParser#callParams.
    def enterCallParams(self, ctx:RustParser.CallParamsContext):
        pass

    # Exit a parse tree produced by RustParser#callParams.
    def exitCallParams(self, ctx:RustParser.CallParamsContext):
        pass


    # Enter a parse tree produced by RustParser#closureExpression.
    def enterClosureExpression(self, ctx:RustParser.ClosureExpressionContext):
        pass

    # Exit a parse tree produced by RustParser#closureExpression.
    def exitClosureExpression(self, ctx:RustParser.ClosureExpressionContext):
        pass


    # Enter a parse tree produced by RustParser#closureParameters.
    def enterClosureParameters(self, ctx:RustParser.ClosureParametersContext):
        pass

    # Exit a parse tree produced by RustParser#closureParameters.
    def exitClosureParameters(self, ctx:RustParser.ClosureParametersContext):
        pass


    # Enter a parse tree produced by RustParser#closureParam.
    def enterClosureParam(self, ctx:RustParser.ClosureParamContext):
        pass

    # Exit a parse tree produced by RustParser#closureParam.
    def exitClosureParam(self, ctx:RustParser.ClosureParamContext):
        pass


    # Enter a parse tree produced by RustParser#loopExpression.
    def enterLoopExpression(self, ctx:RustParser.LoopExpressionContext):
        pass

    # Exit a parse tree produced by RustParser#loopExpression.
    def exitLoopExpression(self, ctx:RustParser.LoopExpressionContext):
        pass


    # Enter a parse tree produced by RustParser#infiniteLoopExpression.
    def enterInfiniteLoopExpression(self, ctx:RustParser.InfiniteLoopExpressionContext):
        pass

    # Exit a parse tree produced by RustParser#infiniteLoopExpression.
    def exitInfiniteLoopExpression(self, ctx:RustParser.InfiniteLoopExpressionContext):
        pass


    # Enter a parse tree produced by RustParser#predicateLoopExpression.
    def enterPredicateLoopExpression(self, ctx:RustParser.PredicateLoopExpressionContext):
        pass

    # Exit a parse tree produced by RustParser#predicateLoopExpression.
    def exitPredicateLoopExpression(self, ctx:RustParser.PredicateLoopExpressionContext):
        pass


    # Enter a parse tree produced by RustParser#predicatePatternLoopExpression.
    def enterPredicatePatternLoopExpression(self, ctx:RustParser.PredicatePatternLoopExpressionContext):
        pass

    # Exit a parse tree produced by RustParser#predicatePatternLoopExpression.
    def exitPredicatePatternLoopExpression(self, ctx:RustParser.PredicatePatternLoopExpressionContext):
        pass


    # Enter a parse tree produced by RustParser#iteratorLoopExpression.
    def enterIteratorLoopExpression(self, ctx:RustParser.IteratorLoopExpressionContext):
        pass

    # Exit a parse tree produced by RustParser#iteratorLoopExpression.
    def exitIteratorLoopExpression(self, ctx:RustParser.IteratorLoopExpressionContext):
        pass


    # Enter a parse tree produced by RustParser#loopLabel.
    def enterLoopLabel(self, ctx:RustParser.LoopLabelContext):
        pass

    # Exit a parse tree produced by RustParser#loopLabel.
    def exitLoopLabel(self, ctx:RustParser.LoopLabelContext):
        pass


    # Enter a parse tree produced by RustParser#ifExpression.
    def enterIfExpression(self, ctx:RustParser.IfExpressionContext):
        pass

    # Exit a parse tree produced by RustParser#ifExpression.
    def exitIfExpression(self, ctx:RustParser.IfExpressionContext):
        pass


    # Enter a parse tree produced by RustParser#ifLetExpression.
    def enterIfLetExpression(self, ctx:RustParser.IfLetExpressionContext):
        pass

    # Exit a parse tree produced by RustParser#ifLetExpression.
    def exitIfLetExpression(self, ctx:RustParser.IfLetExpressionContext):
        pass


    # Enter a parse tree produced by RustParser#matchExpression.
    def enterMatchExpression(self, ctx:RustParser.MatchExpressionContext):
        pass

    # Exit a parse tree produced by RustParser#matchExpression.
    def exitMatchExpression(self, ctx:RustParser.MatchExpressionContext):
        pass


    # Enter a parse tree produced by RustParser#matchArms.
    def enterMatchArms(self, ctx:RustParser.MatchArmsContext):
        pass

    # Exit a parse tree produced by RustParser#matchArms.
    def exitMatchArms(self, ctx:RustParser.MatchArmsContext):
        pass


    # Enter a parse tree produced by RustParser#matchArmExpression.
    def enterMatchArmExpression(self, ctx:RustParser.MatchArmExpressionContext):
        pass

    # Exit a parse tree produced by RustParser#matchArmExpression.
    def exitMatchArmExpression(self, ctx:RustParser.MatchArmExpressionContext):
        pass


    # Enter a parse tree produced by RustParser#matchArm.
    def enterMatchArm(self, ctx:RustParser.MatchArmContext):
        pass

    # Exit a parse tree produced by RustParser#matchArm.
    def exitMatchArm(self, ctx:RustParser.MatchArmContext):
        pass


    # Enter a parse tree produced by RustParser#matchArmGuard.
    def enterMatchArmGuard(self, ctx:RustParser.MatchArmGuardContext):
        pass

    # Exit a parse tree produced by RustParser#matchArmGuard.
    def exitMatchArmGuard(self, ctx:RustParser.MatchArmGuardContext):
        pass


    # Enter a parse tree produced by RustParser#pattern.
    def enterPattern(self, ctx:RustParser.PatternContext):
        pass

    # Exit a parse tree produced by RustParser#pattern.
    def exitPattern(self, ctx:RustParser.PatternContext):
        pass


    # Enter a parse tree produced by RustParser#patternNoTopAlt.
    def enterPatternNoTopAlt(self, ctx:RustParser.PatternNoTopAltContext):
        pass

    # Exit a parse tree produced by RustParser#patternNoTopAlt.
    def exitPatternNoTopAlt(self, ctx:RustParser.PatternNoTopAltContext):
        pass


    # Enter a parse tree produced by RustParser#patternWithoutRange.
    def enterPatternWithoutRange(self, ctx:RustParser.PatternWithoutRangeContext):
        pass

    # Exit a parse tree produced by RustParser#patternWithoutRange.
    def exitPatternWithoutRange(self, ctx:RustParser.PatternWithoutRangeContext):
        pass


    # Enter a parse tree produced by RustParser#literalPattern.
    def enterLiteralPattern(self, ctx:RustParser.LiteralPatternContext):
        pass

    # Exit a parse tree produced by RustParser#literalPattern.
    def exitLiteralPattern(self, ctx:RustParser.LiteralPatternContext):
        pass


    # Enter a parse tree produced by RustParser#identifierPattern.
    def enterIdentifierPattern(self, ctx:RustParser.IdentifierPatternContext):
        pass

    # Exit a parse tree produced by RustParser#identifierPattern.
    def exitIdentifierPattern(self, ctx:RustParser.IdentifierPatternContext):
        pass


    # Enter a parse tree produced by RustParser#wildcardPattern.
    def enterWildcardPattern(self, ctx:RustParser.WildcardPatternContext):
        pass

    # Exit a parse tree produced by RustParser#wildcardPattern.
    def exitWildcardPattern(self, ctx:RustParser.WildcardPatternContext):
        pass


    # Enter a parse tree produced by RustParser#restPattern.
    def enterRestPattern(self, ctx:RustParser.RestPatternContext):
        pass

    # Exit a parse tree produced by RustParser#restPattern.
    def exitRestPattern(self, ctx:RustParser.RestPatternContext):
        pass


    # Enter a parse tree produced by RustParser#InclusiveRangePattern.
    def enterInclusiveRangePattern(self, ctx:RustParser.InclusiveRangePatternContext):
        pass

    # Exit a parse tree produced by RustParser#InclusiveRangePattern.
    def exitInclusiveRangePattern(self, ctx:RustParser.InclusiveRangePatternContext):
        pass


    # Enter a parse tree produced by RustParser#HalfOpenRangePattern.
    def enterHalfOpenRangePattern(self, ctx:RustParser.HalfOpenRangePatternContext):
        pass

    # Exit a parse tree produced by RustParser#HalfOpenRangePattern.
    def exitHalfOpenRangePattern(self, ctx:RustParser.HalfOpenRangePatternContext):
        pass


    # Enter a parse tree produced by RustParser#ObsoleteRangePattern.
    def enterObsoleteRangePattern(self, ctx:RustParser.ObsoleteRangePatternContext):
        pass

    # Exit a parse tree produced by RustParser#ObsoleteRangePattern.
    def exitObsoleteRangePattern(self, ctx:RustParser.ObsoleteRangePatternContext):
        pass


    # Enter a parse tree produced by RustParser#rangePatternBound.
    def enterRangePatternBound(self, ctx:RustParser.RangePatternBoundContext):
        pass

    # Exit a parse tree produced by RustParser#rangePatternBound.
    def exitRangePatternBound(self, ctx:RustParser.RangePatternBoundContext):
        pass


    # Enter a parse tree produced by RustParser#referencePattern.
    def enterReferencePattern(self, ctx:RustParser.ReferencePatternContext):
        pass

    # Exit a parse tree produced by RustParser#referencePattern.
    def exitReferencePattern(self, ctx:RustParser.ReferencePatternContext):
        pass


    # Enter a parse tree produced by RustParser#structPattern.
    def enterStructPattern(self, ctx:RustParser.StructPatternContext):
        pass

    # Exit a parse tree produced by RustParser#structPattern.
    def exitStructPattern(self, ctx:RustParser.StructPatternContext):
        pass


    # Enter a parse tree produced by RustParser#structPatternElements.
    def enterStructPatternElements(self, ctx:RustParser.StructPatternElementsContext):
        pass

    # Exit a parse tree produced by RustParser#structPatternElements.
    def exitStructPatternElements(self, ctx:RustParser.StructPatternElementsContext):
        pass


    # Enter a parse tree produced by RustParser#structPatternFields.
    def enterStructPatternFields(self, ctx:RustParser.StructPatternFieldsContext):
        pass

    # Exit a parse tree produced by RustParser#structPatternFields.
    def exitStructPatternFields(self, ctx:RustParser.StructPatternFieldsContext):
        pass


    # Enter a parse tree produced by RustParser#structPatternField.
    def enterStructPatternField(self, ctx:RustParser.StructPatternFieldContext):
        pass

    # Exit a parse tree produced by RustParser#structPatternField.
    def exitStructPatternField(self, ctx:RustParser.StructPatternFieldContext):
        pass


    # Enter a parse tree produced by RustParser#structPatternEtCetera.
    def enterStructPatternEtCetera(self, ctx:RustParser.StructPatternEtCeteraContext):
        pass

    # Exit a parse tree produced by RustParser#structPatternEtCetera.
    def exitStructPatternEtCetera(self, ctx:RustParser.StructPatternEtCeteraContext):
        pass


    # Enter a parse tree produced by RustParser#tupleStructPattern.
    def enterTupleStructPattern(self, ctx:RustParser.TupleStructPatternContext):
        pass

    # Exit a parse tree produced by RustParser#tupleStructPattern.
    def exitTupleStructPattern(self, ctx:RustParser.TupleStructPatternContext):
        pass


    # Enter a parse tree produced by RustParser#tupleStructItems.
    def enterTupleStructItems(self, ctx:RustParser.TupleStructItemsContext):
        pass

    # Exit a parse tree produced by RustParser#tupleStructItems.
    def exitTupleStructItems(self, ctx:RustParser.TupleStructItemsContext):
        pass


    # Enter a parse tree produced by RustParser#tuplePattern.
    def enterTuplePattern(self, ctx:RustParser.TuplePatternContext):
        pass

    # Exit a parse tree produced by RustParser#tuplePattern.
    def exitTuplePattern(self, ctx:RustParser.TuplePatternContext):
        pass


    # Enter a parse tree produced by RustParser#tuplePatternItems.
    def enterTuplePatternItems(self, ctx:RustParser.TuplePatternItemsContext):
        pass

    # Exit a parse tree produced by RustParser#tuplePatternItems.
    def exitTuplePatternItems(self, ctx:RustParser.TuplePatternItemsContext):
        pass


    # Enter a parse tree produced by RustParser#groupedPattern.
    def enterGroupedPattern(self, ctx:RustParser.GroupedPatternContext):
        pass

    # Exit a parse tree produced by RustParser#groupedPattern.
    def exitGroupedPattern(self, ctx:RustParser.GroupedPatternContext):
        pass


    # Enter a parse tree produced by RustParser#slicePattern.
    def enterSlicePattern(self, ctx:RustParser.SlicePatternContext):
        pass

    # Exit a parse tree produced by RustParser#slicePattern.
    def exitSlicePattern(self, ctx:RustParser.SlicePatternContext):
        pass


    # Enter a parse tree produced by RustParser#slicePatternItems.
    def enterSlicePatternItems(self, ctx:RustParser.SlicePatternItemsContext):
        pass

    # Exit a parse tree produced by RustParser#slicePatternItems.
    def exitSlicePatternItems(self, ctx:RustParser.SlicePatternItemsContext):
        pass


    # Enter a parse tree produced by RustParser#pathPattern.
    def enterPathPattern(self, ctx:RustParser.PathPatternContext):
        pass

    # Exit a parse tree produced by RustParser#pathPattern.
    def exitPathPattern(self, ctx:RustParser.PathPatternContext):
        pass


    # Enter a parse tree produced by RustParser#type_.
    def enterType_(self, ctx:RustParser.Type_Context):
        pass

    # Exit a parse tree produced by RustParser#type_.
    def exitType_(self, ctx:RustParser.Type_Context):
        pass


    # Enter a parse tree produced by RustParser#typeNoBounds.
    def enterTypeNoBounds(self, ctx:RustParser.TypeNoBoundsContext):
        pass

    # Exit a parse tree produced by RustParser#typeNoBounds.
    def exitTypeNoBounds(self, ctx:RustParser.TypeNoBoundsContext):
        pass


    # Enter a parse tree produced by RustParser#parenthesizedType.
    def enterParenthesizedType(self, ctx:RustParser.ParenthesizedTypeContext):
        pass

    # Exit a parse tree produced by RustParser#parenthesizedType.
    def exitParenthesizedType(self, ctx:RustParser.ParenthesizedTypeContext):
        pass


    # Enter a parse tree produced by RustParser#neverType.
    def enterNeverType(self, ctx:RustParser.NeverTypeContext):
        pass

    # Exit a parse tree produced by RustParser#neverType.
    def exitNeverType(self, ctx:RustParser.NeverTypeContext):
        pass


    # Enter a parse tree produced by RustParser#tupleType.
    def enterTupleType(self, ctx:RustParser.TupleTypeContext):
        pass

    # Exit a parse tree produced by RustParser#tupleType.
    def exitTupleType(self, ctx:RustParser.TupleTypeContext):
        pass


    # Enter a parse tree produced by RustParser#arrayType.
    def enterArrayType(self, ctx:RustParser.ArrayTypeContext):
        pass

    # Exit a parse tree produced by RustParser#arrayType.
    def exitArrayType(self, ctx:RustParser.ArrayTypeContext):
        pass


    # Enter a parse tree produced by RustParser#sliceType.
    def enterSliceType(self, ctx:RustParser.SliceTypeContext):
        pass

    # Exit a parse tree produced by RustParser#sliceType.
    def exitSliceType(self, ctx:RustParser.SliceTypeContext):
        pass


    # Enter a parse tree produced by RustParser#referenceType.
    def enterReferenceType(self, ctx:RustParser.ReferenceTypeContext):
        pass

    # Exit a parse tree produced by RustParser#referenceType.
    def exitReferenceType(self, ctx:RustParser.ReferenceTypeContext):
        pass


    # Enter a parse tree produced by RustParser#rawPointerType.
    def enterRawPointerType(self, ctx:RustParser.RawPointerTypeContext):
        pass

    # Exit a parse tree produced by RustParser#rawPointerType.
    def exitRawPointerType(self, ctx:RustParser.RawPointerTypeContext):
        pass


    # Enter a parse tree produced by RustParser#bareFunctionType.
    def enterBareFunctionType(self, ctx:RustParser.BareFunctionTypeContext):
        pass

    # Exit a parse tree produced by RustParser#bareFunctionType.
    def exitBareFunctionType(self, ctx:RustParser.BareFunctionTypeContext):
        pass


    # Enter a parse tree produced by RustParser#functionTypeQualifiers.
    def enterFunctionTypeQualifiers(self, ctx:RustParser.FunctionTypeQualifiersContext):
        pass

    # Exit a parse tree produced by RustParser#functionTypeQualifiers.
    def exitFunctionTypeQualifiers(self, ctx:RustParser.FunctionTypeQualifiersContext):
        pass


    # Enter a parse tree produced by RustParser#bareFunctionReturnType.
    def enterBareFunctionReturnType(self, ctx:RustParser.BareFunctionReturnTypeContext):
        pass

    # Exit a parse tree produced by RustParser#bareFunctionReturnType.
    def exitBareFunctionReturnType(self, ctx:RustParser.BareFunctionReturnTypeContext):
        pass


    # Enter a parse tree produced by RustParser#functionParametersMaybeNamedVariadic.
    def enterFunctionParametersMaybeNamedVariadic(self, ctx:RustParser.FunctionParametersMaybeNamedVariadicContext):
        pass

    # Exit a parse tree produced by RustParser#functionParametersMaybeNamedVariadic.
    def exitFunctionParametersMaybeNamedVariadic(self, ctx:RustParser.FunctionParametersMaybeNamedVariadicContext):
        pass


    # Enter a parse tree produced by RustParser#maybeNamedFunctionParameters.
    def enterMaybeNamedFunctionParameters(self, ctx:RustParser.MaybeNamedFunctionParametersContext):
        pass

    # Exit a parse tree produced by RustParser#maybeNamedFunctionParameters.
    def exitMaybeNamedFunctionParameters(self, ctx:RustParser.MaybeNamedFunctionParametersContext):
        pass


    # Enter a parse tree produced by RustParser#maybeNamedParam.
    def enterMaybeNamedParam(self, ctx:RustParser.MaybeNamedParamContext):
        pass

    # Exit a parse tree produced by RustParser#maybeNamedParam.
    def exitMaybeNamedParam(self, ctx:RustParser.MaybeNamedParamContext):
        pass


    # Enter a parse tree produced by RustParser#maybeNamedFunctionParametersVariadic.
    def enterMaybeNamedFunctionParametersVariadic(self, ctx:RustParser.MaybeNamedFunctionParametersVariadicContext):
        pass

    # Exit a parse tree produced by RustParser#maybeNamedFunctionParametersVariadic.
    def exitMaybeNamedFunctionParametersVariadic(self, ctx:RustParser.MaybeNamedFunctionParametersVariadicContext):
        pass


    # Enter a parse tree produced by RustParser#traitObjectType.
    def enterTraitObjectType(self, ctx:RustParser.TraitObjectTypeContext):
        pass

    # Exit a parse tree produced by RustParser#traitObjectType.
    def exitTraitObjectType(self, ctx:RustParser.TraitObjectTypeContext):
        pass


    # Enter a parse tree produced by RustParser#traitObjectTypeOneBound.
    def enterTraitObjectTypeOneBound(self, ctx:RustParser.TraitObjectTypeOneBoundContext):
        pass

    # Exit a parse tree produced by RustParser#traitObjectTypeOneBound.
    def exitTraitObjectTypeOneBound(self, ctx:RustParser.TraitObjectTypeOneBoundContext):
        pass


    # Enter a parse tree produced by RustParser#implTraitType.
    def enterImplTraitType(self, ctx:RustParser.ImplTraitTypeContext):
        pass

    # Exit a parse tree produced by RustParser#implTraitType.
    def exitImplTraitType(self, ctx:RustParser.ImplTraitTypeContext):
        pass


    # Enter a parse tree produced by RustParser#implTraitTypeOneBound.
    def enterImplTraitTypeOneBound(self, ctx:RustParser.ImplTraitTypeOneBoundContext):
        pass

    # Exit a parse tree produced by RustParser#implTraitTypeOneBound.
    def exitImplTraitTypeOneBound(self, ctx:RustParser.ImplTraitTypeOneBoundContext):
        pass


    # Enter a parse tree produced by RustParser#inferredType.
    def enterInferredType(self, ctx:RustParser.InferredTypeContext):
        pass

    # Exit a parse tree produced by RustParser#inferredType.
    def exitInferredType(self, ctx:RustParser.InferredTypeContext):
        pass


    # Enter a parse tree produced by RustParser#typeParamBounds.
    def enterTypeParamBounds(self, ctx:RustParser.TypeParamBoundsContext):
        pass

    # Exit a parse tree produced by RustParser#typeParamBounds.
    def exitTypeParamBounds(self, ctx:RustParser.TypeParamBoundsContext):
        pass


    # Enter a parse tree produced by RustParser#typeParamBound.
    def enterTypeParamBound(self, ctx:RustParser.TypeParamBoundContext):
        pass

    # Exit a parse tree produced by RustParser#typeParamBound.
    def exitTypeParamBound(self, ctx:RustParser.TypeParamBoundContext):
        pass


    # Enter a parse tree produced by RustParser#traitBound.
    def enterTraitBound(self, ctx:RustParser.TraitBoundContext):
        pass

    # Exit a parse tree produced by RustParser#traitBound.
    def exitTraitBound(self, ctx:RustParser.TraitBoundContext):
        pass


    # Enter a parse tree produced by RustParser#lifetimeBounds.
    def enterLifetimeBounds(self, ctx:RustParser.LifetimeBoundsContext):
        pass

    # Exit a parse tree produced by RustParser#lifetimeBounds.
    def exitLifetimeBounds(self, ctx:RustParser.LifetimeBoundsContext):
        pass


    # Enter a parse tree produced by RustParser#lifetime.
    def enterLifetime(self, ctx:RustParser.LifetimeContext):
        pass

    # Exit a parse tree produced by RustParser#lifetime.
    def exitLifetime(self, ctx:RustParser.LifetimeContext):
        pass


    # Enter a parse tree produced by RustParser#simplePath.
    def enterSimplePath(self, ctx:RustParser.SimplePathContext):
        pass

    # Exit a parse tree produced by RustParser#simplePath.
    def exitSimplePath(self, ctx:RustParser.SimplePathContext):
        pass


    # Enter a parse tree produced by RustParser#simplePathSegment.
    def enterSimplePathSegment(self, ctx:RustParser.SimplePathSegmentContext):
        pass

    # Exit a parse tree produced by RustParser#simplePathSegment.
    def exitSimplePathSegment(self, ctx:RustParser.SimplePathSegmentContext):
        pass


    # Enter a parse tree produced by RustParser#pathInExpression.
    def enterPathInExpression(self, ctx:RustParser.PathInExpressionContext):
        pass

    # Exit a parse tree produced by RustParser#pathInExpression.
    def exitPathInExpression(self, ctx:RustParser.PathInExpressionContext):
        pass


    # Enter a parse tree produced by RustParser#pathExprSegment.
    def enterPathExprSegment(self, ctx:RustParser.PathExprSegmentContext):
        pass

    # Exit a parse tree produced by RustParser#pathExprSegment.
    def exitPathExprSegment(self, ctx:RustParser.PathExprSegmentContext):
        pass


    # Enter a parse tree produced by RustParser#pathIdentSegment.
    def enterPathIdentSegment(self, ctx:RustParser.PathIdentSegmentContext):
        pass

    # Exit a parse tree produced by RustParser#pathIdentSegment.
    def exitPathIdentSegment(self, ctx:RustParser.PathIdentSegmentContext):
        pass


    # Enter a parse tree produced by RustParser#genericArgs.
    def enterGenericArgs(self, ctx:RustParser.GenericArgsContext):
        pass

    # Exit a parse tree produced by RustParser#genericArgs.
    def exitGenericArgs(self, ctx:RustParser.GenericArgsContext):
        pass


    # Enter a parse tree produced by RustParser#genericArg.
    def enterGenericArg(self, ctx:RustParser.GenericArgContext):
        pass

    # Exit a parse tree produced by RustParser#genericArg.
    def exitGenericArg(self, ctx:RustParser.GenericArgContext):
        pass


    # Enter a parse tree produced by RustParser#genericArgsConst.
    def enterGenericArgsConst(self, ctx:RustParser.GenericArgsConstContext):
        pass

    # Exit a parse tree produced by RustParser#genericArgsConst.
    def exitGenericArgsConst(self, ctx:RustParser.GenericArgsConstContext):
        pass


    # Enter a parse tree produced by RustParser#genericArgsLifetimes.
    def enterGenericArgsLifetimes(self, ctx:RustParser.GenericArgsLifetimesContext):
        pass

    # Exit a parse tree produced by RustParser#genericArgsLifetimes.
    def exitGenericArgsLifetimes(self, ctx:RustParser.GenericArgsLifetimesContext):
        pass


    # Enter a parse tree produced by RustParser#genericArgsTypes.
    def enterGenericArgsTypes(self, ctx:RustParser.GenericArgsTypesContext):
        pass

    # Exit a parse tree produced by RustParser#genericArgsTypes.
    def exitGenericArgsTypes(self, ctx:RustParser.GenericArgsTypesContext):
        pass


    # Enter a parse tree produced by RustParser#genericArgsBindings.
    def enterGenericArgsBindings(self, ctx:RustParser.GenericArgsBindingsContext):
        pass

    # Exit a parse tree produced by RustParser#genericArgsBindings.
    def exitGenericArgsBindings(self, ctx:RustParser.GenericArgsBindingsContext):
        pass


    # Enter a parse tree produced by RustParser#genericArgsBinding.
    def enterGenericArgsBinding(self, ctx:RustParser.GenericArgsBindingContext):
        pass

    # Exit a parse tree produced by RustParser#genericArgsBinding.
    def exitGenericArgsBinding(self, ctx:RustParser.GenericArgsBindingContext):
        pass


    # Enter a parse tree produced by RustParser#qualifiedPathInExpression.
    def enterQualifiedPathInExpression(self, ctx:RustParser.QualifiedPathInExpressionContext):
        pass

    # Exit a parse tree produced by RustParser#qualifiedPathInExpression.
    def exitQualifiedPathInExpression(self, ctx:RustParser.QualifiedPathInExpressionContext):
        pass


    # Enter a parse tree produced by RustParser#qualifiedPathType.
    def enterQualifiedPathType(self, ctx:RustParser.QualifiedPathTypeContext):
        pass

    # Exit a parse tree produced by RustParser#qualifiedPathType.
    def exitQualifiedPathType(self, ctx:RustParser.QualifiedPathTypeContext):
        pass


    # Enter a parse tree produced by RustParser#qualifiedPathInType.
    def enterQualifiedPathInType(self, ctx:RustParser.QualifiedPathInTypeContext):
        pass

    # Exit a parse tree produced by RustParser#qualifiedPathInType.
    def exitQualifiedPathInType(self, ctx:RustParser.QualifiedPathInTypeContext):
        pass


    # Enter a parse tree produced by RustParser#typePath.
    def enterTypePath(self, ctx:RustParser.TypePathContext):
        pass

    # Exit a parse tree produced by RustParser#typePath.
    def exitTypePath(self, ctx:RustParser.TypePathContext):
        pass


    # Enter a parse tree produced by RustParser#typePathSegment.
    def enterTypePathSegment(self, ctx:RustParser.TypePathSegmentContext):
        pass

    # Exit a parse tree produced by RustParser#typePathSegment.
    def exitTypePathSegment(self, ctx:RustParser.TypePathSegmentContext):
        pass


    # Enter a parse tree produced by RustParser#typePathFn.
    def enterTypePathFn(self, ctx:RustParser.TypePathFnContext):
        pass

    # Exit a parse tree produced by RustParser#typePathFn.
    def exitTypePathFn(self, ctx:RustParser.TypePathFnContext):
        pass


    # Enter a parse tree produced by RustParser#typePathInputs.
    def enterTypePathInputs(self, ctx:RustParser.TypePathInputsContext):
        pass

    # Exit a parse tree produced by RustParser#typePathInputs.
    def exitTypePathInputs(self, ctx:RustParser.TypePathInputsContext):
        pass


    # Enter a parse tree produced by RustParser#visibility.
    def enterVisibility(self, ctx:RustParser.VisibilityContext):
        pass

    # Exit a parse tree produced by RustParser#visibility.
    def exitVisibility(self, ctx:RustParser.VisibilityContext):
        pass


    # Enter a parse tree produced by RustParser#identifier.
    def enterIdentifier(self, ctx:RustParser.IdentifierContext):
        pass

    # Exit a parse tree produced by RustParser#identifier.
    def exitIdentifier(self, ctx:RustParser.IdentifierContext):
        pass


    # Enter a parse tree produced by RustParser#keyword.
    def enterKeyword(self, ctx:RustParser.KeywordContext):
        pass

    # Exit a parse tree produced by RustParser#keyword.
    def exitKeyword(self, ctx:RustParser.KeywordContext):
        pass


    # Enter a parse tree produced by RustParser#macroIdentifierLikeToken.
    def enterMacroIdentifierLikeToken(self, ctx:RustParser.MacroIdentifierLikeTokenContext):
        pass

    # Exit a parse tree produced by RustParser#macroIdentifierLikeToken.
    def exitMacroIdentifierLikeToken(self, ctx:RustParser.MacroIdentifierLikeTokenContext):
        pass


    # Enter a parse tree produced by RustParser#macroLiteralToken.
    def enterMacroLiteralToken(self, ctx:RustParser.MacroLiteralTokenContext):
        pass

    # Exit a parse tree produced by RustParser#macroLiteralToken.
    def exitMacroLiteralToken(self, ctx:RustParser.MacroLiteralTokenContext):
        pass


    # Enter a parse tree produced by RustParser#macroPunctuationToken.
    def enterMacroPunctuationToken(self, ctx:RustParser.MacroPunctuationTokenContext):
        pass

    # Exit a parse tree produced by RustParser#macroPunctuationToken.
    def exitMacroPunctuationToken(self, ctx:RustParser.MacroPunctuationTokenContext):
        pass


    # Enter a parse tree produced by RustParser#shl.
    def enterShl(self, ctx:RustParser.ShlContext):
        pass

    # Exit a parse tree produced by RustParser#shl.
    def exitShl(self, ctx:RustParser.ShlContext):
        pass


    # Enter a parse tree produced by RustParser#shr.
    def enterShr(self, ctx:RustParser.ShrContext):
        pass

    # Exit a parse tree produced by RustParser#shr.
    def exitShr(self, ctx:RustParser.ShrContext):
        pass



del RustParser