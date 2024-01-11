import uuid
from clone_detection.ecst.ecst_tree import ECSTree
from clone_detection.ecst.ecst_node import ECSTNode, ShortToken
from .KotlinParserListener import KotlinParserListener
from .KotlinParser import KotlinParser
from clone_detection.grammars.grammars_registry import LISTENERS


@LISTENERS.register('kt')
class KotlinECSTListener(KotlinParserListener):
    def __init__(self):
        self.tree = ECSTree()
        self.current_node = self.tree

    # Enter a parse tree produced by KotlinParser#kotlinFile.
    def enterKotlinFile(self, ctx: KotlinParser.KotlinFileContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token, 'FILE')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by KotlinParser#kotlinFile.
    def exitKotlinFile(self, ctx: KotlinParser.KotlinFileContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#script.
    def enterScript(self, ctx: KotlinParser.ScriptContext):
        act_token = ShortToken('', 0, 0)
        script_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token, 'SCRIPT')
        self.current_node.add_child(script_node)
        self.current_node = script_node

    # Exit a parse tree produced by KotlinParser#script.
    def exitScript(self, ctx: KotlinParser.ScriptContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#preamble.
    def enterPreamble(self, ctx: KotlinParser.PreambleContext):
        pass

    # Exit a parse tree produced by KotlinParser#preamble.
    def exitPreamble(self, ctx: KotlinParser.PreambleContext):
        pass

    # Enter a parse tree produced by KotlinParser#fileAnnotations.
    def enterFileAnnotations(self, ctx: KotlinParser.FileAnnotationsContext):
        pass

    # Exit a parse tree produced by KotlinParser#fileAnnotations.
    def exitFileAnnotations(self, ctx: KotlinParser.FileAnnotationsContext):
        pass

    # Enter a parse tree produced by KotlinParser#fileAnnotation.
    def enterFileAnnotation(self, ctx: KotlinParser.FileAnnotationContext):
        pass

    # Exit a parse tree produced by KotlinParser#fileAnnotation.
    def exitFileAnnotation(self, ctx: KotlinParser.FileAnnotationContext):
        pass

    # Enter a parse tree produced by KotlinParser#packageHeader.
    def enterPackageHeader(self, ctx: KotlinParser.PackageHeaderContext):
        pass

    # Exit a parse tree produced by KotlinParser#packageHeader.
    def exitPackageHeader(self, ctx: KotlinParser.PackageHeaderContext):
        pass

    # Enter a parse tree produced by KotlinParser#importList.
    def enterImportList(self, ctx: KotlinParser.ImportListContext):
        pass

    # Exit a parse tree produced by KotlinParser#importList.
    def exitImportList(self, ctx: KotlinParser.ImportListContext):
        pass

    # Enter a parse tree produced by KotlinParser#importHeader.
    def enterImportHeader(self, ctx: KotlinParser.ImportHeaderContext):
        pass

    # Exit a parse tree produced by KotlinParser#importHeader.
    def exitImportHeader(self, ctx: KotlinParser.ImportHeaderContext):
        pass

    # Enter a parse tree produced by KotlinParser#importAlias.
    def enterImportAlias(self, ctx: KotlinParser.ImportAliasContext):
        pass

    # Exit a parse tree produced by KotlinParser#importAlias.
    def exitImportAlias(self, ctx: KotlinParser.ImportAliasContext):
        pass

    # Enter a parse tree produced by KotlinParser#topLevelObject.
    def enterTopLevelObject(self, ctx: KotlinParser.TopLevelObjectContext):
        pass

    # Exit a parse tree produced by KotlinParser#topLevelObject.
    def exitTopLevelObject(self, ctx: KotlinParser.TopLevelObjectContext):
        pass

    # Enter a parse tree produced by KotlinParser#classDeclaration.
    def enterClassDeclaration(self, ctx: KotlinParser.ClassDeclarationContext):
        if ctx.CLASS():
            token = ctx.CLASS().symbol
            act_token = ShortToken(token.text, token.line, token.column)
            class_dcl_node = ECSTNode(
                str(uuid.uuid4()), self.current_node, act_token, 'CLASS_DECL'
            )
        else:
            token = ctx.INTERFACE().symbol
            act_token = ShortToken(token.text, token.line, token.column)
            class_dcl_node = ECSTNode(
                str(uuid.uuid4()), self.current_node, act_token,
                'INTERFACE_DECL'
            )
        self.current_node.add_child(class_dcl_node)
        self.current_node = class_dcl_node

    # Exit a parse tree produced by KotlinParser#classDeclaration.
    def exitClassDeclaration(self, ctx: KotlinParser.ClassDeclarationContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#primaryConstructor.
    def enterPrimaryConstructor(
            self, ctx: KotlinParser.PrimaryConstructorContext):
        try:
            token = ctx.CONSTRUCTOR().symbol
            act_token = ShortToken(token.text, token.line, token.column)
        except AttributeError:
            act_token = ShortToken('', 0, 0)
        class_dcl_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token, 'CONSTRUCTOR_DECL'
        )
        self.current_node.add_child(class_dcl_node)
        self.current_node = class_dcl_node

    # Exit a parse tree produced by KotlinParser#primaryConstructor.
    def exitPrimaryConstructor(
            self, ctx: KotlinParser.PrimaryConstructorContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#classParameters.
    def enterClassParameters(self, ctx: KotlinParser.ClassParametersContext):
        act_token = ShortToken('', 0, 0)
        class_param_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token, 'PARAMETER_LIST'
        )
        self.current_node.add_child(class_param_node)
        self.current_node = class_param_node

    # Exit a parse tree produced by KotlinParser#classParameters.
    def exitClassParameters(self, ctx: KotlinParser.ClassParametersContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#classParameter.
    def enterClassParameter(self, ctx: KotlinParser.ClassParameterContext):
        try:
            token = ctx.VAL() or ctx.VAR()
            token = token.symbol
            act_token = ShortToken(token.text, token.line, token.column)
        except AttributeError:
            act_token = ShortToken('', -1, -1)
        class_param_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token, 'PARAMETER'
        )
        self.current_node.add_child(class_param_node)
        self.current_node = class_param_node

    # Exit a parse tree produced by KotlinParser#classParameter.
    def exitClassParameter(self, ctx: KotlinParser.ClassParameterContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#delegationSpecifiers.
    def enterDelegationSpecifiers(
            self, ctx: KotlinParser.DelegationSpecifiersContext):
        pass

    # Exit a parse tree produced by KotlinParser#delegationSpecifiers.
    def exitDelegationSpecifiers(
            self, ctx: KotlinParser.DelegationSpecifiersContext):
        pass

    # Enter a parse tree produced by KotlinParser#delegationSpecifier.
    def enterDelegationSpecifier(
            self, ctx: KotlinParser.DelegationSpecifierContext):
        pass

    # Exit a parse tree produced by KotlinParser#delegationSpecifier.
    def exitDelegationSpecifier(
            self, ctx: KotlinParser.DelegationSpecifierContext):
        pass

    # Enter a parse tree produced by KotlinParser#constructorInvocation.
    def enterConstructorInvocation(
            self, ctx: KotlinParser.ConstructorInvocationContext):
        act_token = ShortToken('', 0, 0)
        class_call_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token, 'CONSTRUCTOR_CALL'
        )
        self.current_node.add_child(class_call_node)
        self.current_node = class_call_node

    # Exit a parse tree produced by KotlinParser#constructorInvocation.
    def exitConstructorInvocation(
            self, ctx: KotlinParser.ConstructorInvocationContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#explicitDelegation.
    def enterExplicitDelegation(
            self, ctx: KotlinParser.ExplicitDelegationContext):
        pass

    # Exit a parse tree produced by KotlinParser#explicitDelegation.
    def exitExplicitDelegation(
            self, ctx: KotlinParser.ExplicitDelegationContext):
        pass

    # Enter a parse tree produced by KotlinParser#classBody.
    def enterClassBody(self, ctx: KotlinParser.ClassBodyContext):
        act_token = ShortToken('', 0, 0)
        class_body_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token, 'CLASS_BODY'
        )
        self.current_node.add_child(class_body_node)
        self.current_node = class_body_node

    # Exit a parse tree produced by KotlinParser#classBody.
    def exitClassBody(self, ctx: KotlinParser.ClassBodyContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#classMemberDeclaration.
    def enterClassMemberDeclaration(
            self, ctx: KotlinParser.ClassMemberDeclarationContext):
        act_token = ShortToken('', 0, 0)
        class_member_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token, 'CLASS_MEMBER'
        )
        self.current_node.add_child(class_member_node)
        self.current_node = class_member_node

    # Exit a parse tree produced by KotlinParser#classMemberDeclaration.
    def exitClassMemberDeclaration(
            self, ctx: KotlinParser.ClassMemberDeclarationContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#anonymousInitializer.
    def enterAnonymousInitializer(
            self, ctx: KotlinParser.AnonymousInitializerContext):
        pass

    # Exit a parse tree produced by KotlinParser#anonymousInitializer.
    def exitAnonymousInitializer(
            self, ctx: KotlinParser.AnonymousInitializerContext):
        pass

    # Enter a parse tree produced by KotlinParser#secondaryConstructor.
    def enterSecondaryConstructor(
            self, ctx: KotlinParser.SecondaryConstructorContext):
        pass

    # Exit a parse tree produced by KotlinParser#secondaryConstructor.
    def exitSecondaryConstructor(
            self, ctx: KotlinParser.SecondaryConstructorContext):
        pass

    # Enter a parse tree produced by KotlinParser#constructorDelegationCall.
    def enterConstructorDelegationCall(
            self, ctx: KotlinParser.ConstructorDelegationCallContext):
        pass

    # Exit a parse tree produced by KotlinParser#constructorDelegationCall.
    def exitConstructorDelegationCall(
            self, ctx: KotlinParser.ConstructorDelegationCallContext):
        pass

    # Enter a parse tree produced by KotlinParser#enumClassBody.
    def enterEnumClassBody(self, ctx: KotlinParser.EnumClassBodyContext):
        act_token = ShortToken('', 0, 0)
        class_member_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token, 'ENUM_BODY'
        )
        self.current_node.add_child(class_member_node)
        self.current_node = class_member_node

    # Exit a parse tree produced by KotlinParser#enumClassBody.
    def exitEnumClassBody(self, ctx: KotlinParser.EnumClassBodyContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#enumEntries.
    def enterEnumEntries(self, ctx: KotlinParser.EnumEntriesContext):
        pass

    # Exit a parse tree produced by KotlinParser#enumEntries.
    def exitEnumEntries(self, ctx: KotlinParser.EnumEntriesContext):
        pass

    # Enter a parse tree produced by KotlinParser#enumEntry.
    def enterEnumEntry(self, ctx: KotlinParser.EnumEntryContext):
        act_token = ShortToken('', 0, 0)
        class_member_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token, 'ENUM_MEMBER'
        )
        self.current_node.add_child(class_member_node)
        self.current_node = class_member_node

    # Exit a parse tree produced by KotlinParser#enumEntry.
    def exitEnumEntry(self, ctx: KotlinParser.EnumEntryContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#functionDeclaration.
    def enterFunctionDeclaration(
            self, ctx: KotlinParser.FunctionDeclarationContext):
        fun = ctx.FUN().symbol
        act_token = ShortToken(fun.text, fun.line, fun.column)
        function_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token, 'FUNCTION_DECL')
        self.current_node.add_child(function_node)
        self.current_node = function_node

    # Exit a parse tree produced by KotlinParser#functionDeclaration.
    def exitFunctionDeclaration(
            self, ctx: KotlinParser.FunctionDeclarationContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#functionValueParameters.
    def enterFunctionValueParameters(
            self, ctx: KotlinParser.FunctionValueParametersContext):
        act_token = ShortToken('', 0, 0)
        class_param_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token, 'PARAMETER_LIST'
        )
        self.current_node.add_child(class_param_node)
        self.current_node = class_param_node

    # Exit a parse tree produced by KotlinParser#functionValueParameters.
    def exitFunctionValueParameters(
            self, ctx: KotlinParser.FunctionValueParametersContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#functionValueParameter.
    def enterFunctionValueParameter(
            self, ctx: KotlinParser.FunctionValueParameterContext):
        act_token = ShortToken('', 0, 0)
        class_param_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token, 'PARAMETER'
        )
        self.current_node.add_child(class_param_node)
        self.current_node = class_param_node

    # Exit a parse tree produced by KotlinParser#functionValueParameter.
    def exitFunctionValueParameter(
            self, ctx: KotlinParser.FunctionValueParameterContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#parameter.
    def enterParameter(self, ctx: KotlinParser.ParameterContext):
        pass

    # Exit a parse tree produced by KotlinParser#parameter.
    def exitParameter(self, ctx: KotlinParser.ParameterContext):
        pass

    # Enter a parse tree produced by KotlinParser#functionBody.
    def enterFunctionBody(self, ctx: KotlinParser.FunctionBodyContext):
        try:
            act_token = ctx.ASSIGNMENT().symbol
            act_type = 'ASSIGNMENT_OPERATOR'
            act_token = ShortToken(
                act_token.text, act_token.line, act_token.column)
        except AttributeError:
            act_token = ShortToken('', 0, 0)
            act_type = 'FUNCTION_BODY'
        class_param_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token, act_type
        )
        self.current_node.add_child(class_param_node)
        self.current_node = class_param_node

    # Exit a parse tree produced by KotlinParser#functionBody.
    def exitFunctionBody(self, ctx: KotlinParser.FunctionBodyContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#objectDeclaration.
    def enterObjectDeclaration(
            self, ctx: KotlinParser.ObjectDeclarationContext):
        fun = ctx.OBJECT().symbol
        act_token = ShortToken(fun.text, fun.line, fun.column)
        function_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token, 'CLASS_DECL')
        self.current_node.add_child(function_node)
        self.current_node = function_node

    # Exit a parse tree produced by KotlinParser#objectDeclaration.
    def exitObjectDeclaration(
            self, ctx: KotlinParser.ObjectDeclarationContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#companionObject.
    def enterCompanionObject(self, ctx: KotlinParser.CompanionObjectContext):
        pass

    # Exit a parse tree produced by KotlinParser#companionObject.
    def exitCompanionObject(self, ctx: KotlinParser.CompanionObjectContext):
        pass

    # Enter a parse tree produced by KotlinParser#propertyDeclaration.
    def enterPropertyDeclaration(
            self, ctx: KotlinParser.PropertyDeclarationContext):
        token = ctx.VAL() or ctx.VAR()
        token = token.symbol
        act_token = ShortToken(token.text, token.line, token.column)
        class_param_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token, 'ATTRIBUTE_DECL'
        )
        self.current_node.add_child(class_param_node)
        self.current_node = class_param_node
        try:
            token_2 = ctx.DOT()
            token = token_2.symbol
            act_token = ShortToken(token.text, token.line, token.column)
            class_param_node = ECSTNode(
                str(uuid.uuid4()), self.current_node, act_token,
                'ACCESS_OPERATOR'
            )
            self.current_node.add_child(class_param_node)
            self.current_node = class_param_node
        except AttributeError:
            pass
        try:
            token_2 = ctx.ASSIGNMENT() or ctx.BY()
            token = token_2.symbol
            act_token = ShortToken(token.text, token.line, token.column)
            class_param_node = ECSTNode(
                str(uuid.uuid4()), self.current_node, act_token,
                'ASSIGNMENT_OPERATOR'
            )
            self.current_node.add_child(class_param_node)
            self.current_node = class_param_node
        except AttributeError:
            pass

    # Exit a parse tree produced by KotlinParser#propertyDeclaration.
    def exitPropertyDeclaration(
            self, ctx: KotlinParser.PropertyDeclarationContext):
        if self.current_node.type == 'ASSIGNMENT_OPERATOR':
            self.current_node = self.current_node.parent
        if self.current_node.type == 'ACCESS_OPERATOR':
            self.current_node = self.current_node
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#multiVariableDeclaration.
    def enterMultiVariableDeclaration(
            self, ctx: KotlinParser.MultiVariableDeclarationContext):
        pass

    # Exit a parse tree produced by KotlinParser#multiVariableDeclaration.
    def exitMultiVariableDeclaration(
            self, ctx: KotlinParser.MultiVariableDeclarationContext):
        pass

    # Enter a parse tree produced by KotlinParser#variableDeclaration.
    def enterVariableDeclaration(
            self, ctx: KotlinParser.VariableDeclarationContext):
        act_token = ShortToken('', 0, 0)
        class_param_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token, 'VARIABLE_DECL'
        )
        self.current_node.add_child(class_param_node)
        self.current_node = class_param_node

    # Exit a parse tree produced by KotlinParser#variableDeclaration.
    def exitVariableDeclaration(
            self, ctx: KotlinParser.VariableDeclarationContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#getter.
    def enterGetter(self, ctx: KotlinParser.GetterContext):
        fun = ctx.GETTER().symbol
        act_token = ShortToken(fun.text, fun.line, fun.column)
        function_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token, 'GETTER')
        self.current_node.add_child(function_node)
        self.current_node = function_node

    # Exit a parse tree produced by KotlinParser#getter.
    def exitGetter(self, ctx: KotlinParser.GetterContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#setter.
    def enterSetter(self, ctx: KotlinParser.SetterContext):
        fun = ctx.SETTER().symbol
        act_token = ShortToken(fun.text, fun.line, fun.column)
        function_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token, 'SETTER')
        self.current_node.add_child(function_node)
        self.current_node = function_node

    # Exit a parse tree produced by KotlinParser#setter.
    def exitSetter(self, ctx: KotlinParser.SetterContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#typeAlias.
    def enterTypeAlias(self, ctx: KotlinParser.TypeAliasContext):
        fun = ctx.TYPE_ALIAS().symbol
        act_token = ShortToken(fun.text, fun.line, fun.column)
        function_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token, 'TYPE_ALIAS')
        self.current_node.add_child(function_node)
        self.current_node = function_node

    # Exit a parse tree produced by KotlinParser#typeAlias.
    def exitTypeAlias(self, ctx: KotlinParser.TypeAliasContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#typeParameters.
    def enterTypeParameters(self, ctx: KotlinParser.TypeParametersContext):
        pass

    # Exit a parse tree produced by KotlinParser#typeParameters.
    def exitTypeParameters(self, ctx: KotlinParser.TypeParametersContext):
        pass

    # Enter a parse tree produced by KotlinParser#typeParameter.
    def enterTypeParameter(self, ctx: KotlinParser.TypeParameterContext):
        act_token = ShortToken('', 0, 0)
        class_param_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token, 'PARAMETER_TYPE'
        )
        self.current_node.add_child(class_param_node)
        self.current_node = class_param_node

    # Exit a parse tree produced by KotlinParser#typeParameter.
    def exitTypeParameter(self, ctx: KotlinParser.TypeParameterContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#type.
    def enterType(self, ctx: KotlinParser.TypeContext):
        act_token = ShortToken('', 0, 0)
        class_param_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token, 'TYPE'
        )
        self.current_node.add_child(class_param_node)
        self.current_node = class_param_node

    # Exit a parse tree produced by KotlinParser#type.
    def exitType(self, ctx: KotlinParser.TypeContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#typeModifierList.
    def enterTypeModifierList(self, ctx: KotlinParser.TypeModifierListContext):
        pass

    # Exit a parse tree produced by KotlinParser#typeModifierList.
    def exitTypeModifierList(self, ctx: KotlinParser.TypeModifierListContext):
        pass

    # Enter a parse tree produced by KotlinParser#parenthesizedType.
    def enterParenthesizedType(
            self, ctx: KotlinParser.ParenthesizedTypeContext):
        pass

    # Exit a parse tree produced by KotlinParser#parenthesizedType.
    def exitParenthesizedType(
            self, ctx: KotlinParser.ParenthesizedTypeContext):
        pass

    # Enter a parse tree produced by KotlinParser#nullableType.
    def enterNullableType(self, ctx: KotlinParser.NullableTypeContext):
        act_token = ShortToken('', 0, 0)
        class_param_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token, 'NULLABLE_TYPE'
        )
        self.current_node.add_child(class_param_node)
        self.current_node = class_param_node

    # Exit a parse tree produced by KotlinParser#nullableType.
    def exitNullableType(self, ctx: KotlinParser.NullableTypeContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#typeReference.
    def enterTypeReference(self, ctx: KotlinParser.TypeReferenceContext):
        pass

    # Exit a parse tree produced by KotlinParser#typeReference.
    def exitTypeReference(self, ctx: KotlinParser.TypeReferenceContext):
        pass

    # Enter a parse tree produced by KotlinParser#functionType.
    def enterFunctionType(self, ctx: KotlinParser.FunctionTypeContext):
        act_token = ShortToken('', 0, 0)
        class_param_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token, 'FUNCTION_TYPE'
        )
        self.current_node.add_child(class_param_node)
        self.current_node = class_param_node

    # Exit a parse tree produced by KotlinParser#functionType.
    def exitFunctionType(self, ctx: KotlinParser.FunctionTypeContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#functionTypeReceiver.
    def enterFunctionTypeReceiver(
            self, ctx: KotlinParser.FunctionTypeReceiverContext):
        pass

    # Exit a parse tree produced by KotlinParser#functionTypeReceiver.
    def exitFunctionTypeReceiver(
            self, ctx: KotlinParser.FunctionTypeReceiverContext):
        pass

    # Enter a parse tree produced by KotlinParser#userType.
    def enterUserType(self, ctx: KotlinParser.UserTypeContext):
        pass

    # Exit a parse tree produced by KotlinParser#userType.
    def exitUserType(self, ctx: KotlinParser.UserTypeContext):
        pass

    # Enter a parse tree produced by KotlinParser#simpleUserType.
    def enterSimpleUserType(self, ctx: KotlinParser.SimpleUserTypeContext):
        # act_token = ShortToken('', 0, 0)
        # class_param_node = ECSTNode(
        #     str(uuid.uuid4()), self.current_node, act_token, 'USER_TYPE'
        # )
        # self.current_node.add_child(class_param_node)
        # self.current_node = class_param_node
        pass

    # Exit a parse tree produced by KotlinParser#simpleUserType.
    def exitSimpleUserType(self, ctx: KotlinParser.SimpleUserTypeContext):
        # self.current_node = self.current_node.parent
        pass

    # Enter a parse tree produced by KotlinParser#functionTypeParameters.
    def enterFunctionTypeParameters(
            self, ctx: KotlinParser.FunctionTypeParametersContext):
        pass

    # Exit a parse tree produced by KotlinParser#functionTypeParameters.
    def exitFunctionTypeParameters(
            self, ctx: KotlinParser.FunctionTypeParametersContext):
        pass

    # Enter a parse tree produced by KotlinParser#typeConstraints.
    def enterTypeConstraints(self, ctx: KotlinParser.TypeConstraintsContext):
        pass

    # Exit a parse tree produced by KotlinParser#typeConstraints.
    def exitTypeConstraints(self, ctx: KotlinParser.TypeConstraintsContext):
        pass

    # Enter a parse tree produced by KotlinParser#typeConstraint.
    def enterTypeConstraint(self, ctx: KotlinParser.TypeConstraintContext):
        pass

    # Exit a parse tree produced by KotlinParser#typeConstraint.
    def exitTypeConstraint(self, ctx: KotlinParser.TypeConstraintContext):
        pass

    # Enter a parse tree produced by KotlinParser#block.
    def enterBlock(self, ctx: KotlinParser.BlockContext):
        pass

    # Exit a parse tree produced by KotlinParser#block.
    def exitBlock(self, ctx: KotlinParser.BlockContext):
        pass

    # Enter a parse tree produced by KotlinParser#statements.
    def enterStatements(self, ctx: KotlinParser.StatementsContext):
        pass

    # Exit a parse tree produced by KotlinParser#statements.
    def exitStatements(self, ctx: KotlinParser.StatementsContext):
        pass

    # Enter a parse tree produced by KotlinParser#statement.
    def enterStatement(self, ctx: KotlinParser.StatementContext):
        pass

    # Exit a parse tree produced by KotlinParser#statement.
    def exitStatement(self, ctx: KotlinParser.StatementContext):
        pass

    # Enter a parse tree produced by KotlinParser#blockLevelExpression.
    def enterBlockLevelExpression(
            self, ctx: KotlinParser.BlockLevelExpressionContext):
        pass

    # Exit a parse tree produced by KotlinParser#blockLevelExpression.
    def exitBlockLevelExpression(
            self, ctx: KotlinParser.BlockLevelExpressionContext):
        pass

    # Enter a parse tree produced by KotlinParser#declaration.
    def enterDeclaration(self, ctx: KotlinParser.DeclarationContext):
        pass

    # Exit a parse tree produced by KotlinParser#declaration.
    def exitDeclaration(self, ctx: KotlinParser.DeclarationContext):
        pass

    # Enter a parse tree produced by KotlinParser#expression.
    def enterExpression(self, ctx: KotlinParser.ExpressionContext):
        act_token = ShortToken('', 0, 0)
        class_param_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token, 'EXPRESSION')
        self.current_node.add_child(class_param_node)
        self.current_node = class_param_node

    # Exit a parse tree produced by KotlinParser#expression.
    def exitExpression(self, ctx: KotlinParser.ExpressionContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#disjunction.
    def enterDisjunction(self, ctx: KotlinParser.DisjunctionContext):
        try:
            act_token = ctx.DISJ()
            if len(act_token) > 0:
                token = act_token[0].symbol
                act_token = ShortToken(token.text, token.line, token.column)
                class_param_node = ECSTNode(
                    str(uuid.uuid4()), self.current_node, act_token, 'OR'
                )
                self.current_node.add_child(class_param_node)
                self.current_node = class_param_node
        except AttributeError:
            pass

    # Exit a parse tree produced by KotlinParser#disjunction.
    def exitDisjunction(self, ctx: KotlinParser.DisjunctionContext):
        if self.current_node.type == 'OR':
            self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#conjunction.
    def enterConjunction(self, ctx: KotlinParser.ConjunctionContext):
        try:
            act_token = ctx.CONJ()
            if len(act_token) > 0:
                token = act_token[0].symbol
                act_token = ShortToken(token.text, token.line, token.column)
                class_param_node = ECSTNode(
                    str(uuid.uuid4()), self.current_node, act_token, 'AND'
                )
                self.current_node.add_child(class_param_node)
                self.current_node = class_param_node
        except AttributeError:
            pass

    # Exit a parse tree produced by KotlinParser#conjunction.
    def exitConjunction(self, ctx: KotlinParser.ConjunctionContext):
        if self.current_node.type == 'AND':
            self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#equalityComparison.
    def enterEqualityComparison(
            self, ctx: KotlinParser.EqualityComparisonContext):
        pass

    # Exit a parse tree produced by KotlinParser#equalityComparison.
    def exitEqualityComparison(
            self, ctx: KotlinParser.EqualityComparisonContext):
        pass

    # Enter a parse tree produced by KotlinParser#comparison.
    def enterComparison(self, ctx: KotlinParser.ComparisonContext):
        pass

    # Exit a parse tree produced by KotlinParser#comparison.
    def exitComparison(self, ctx: KotlinParser.ComparisonContext):
        pass

    # Enter a parse tree produced by KotlinParser#namedInfix.
    def enterNamedInfix(self, ctx: KotlinParser.NamedInfixContext):
        pass

    # Exit a parse tree produced by KotlinParser#namedInfix.
    def exitNamedInfix(self, ctx: KotlinParser.NamedInfixContext):
        pass

    # Enter a parse tree produced by KotlinParser#elvisExpression.
    def enterElvisExpression(self, ctx: KotlinParser.ElvisExpressionContext):
        try:
            act_token = ctx.ELVIS()
            if len(act_token) > 0:
                token = act_token[0].symbol
                act_token = ShortToken(token.text, token.line, token.column)
                class_param_node = ECSTNode(
                    str(uuid.uuid4()), self.current_node, act_token, 'TERNARY'
                )
                self.current_node.add_child(class_param_node)
                self.current_node = class_param_node
        except AttributeError:
            pass

    # Exit a parse tree produced by KotlinParser#elvisExpression.
    def exitElvisExpression(self, ctx: KotlinParser.ElvisExpressionContext):
        if self.current_node.type == 'TERNARY':
            self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#infixFunctionCall.
    def enterInfixFunctionCall(
            self, ctx: KotlinParser.InfixFunctionCallContext):
        pass

    # Exit a parse tree produced by KotlinParser#infixFunctionCall.
    def exitInfixFunctionCall(
            self, ctx: KotlinParser.InfixFunctionCallContext):
        pass

    # Enter a parse tree produced by KotlinParser#rangeExpression.
    def enterRangeExpression(self, ctx: KotlinParser.RangeExpressionContext):
        pass

    # Exit a parse tree produced by KotlinParser#rangeExpression.
    def exitRangeExpression(self, ctx: KotlinParser.RangeExpressionContext):
        pass

    # Enter a parse tree produced by KotlinParser#additiveExpression.
    def enterAdditiveExpression(
            self, ctx: KotlinParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by KotlinParser#additiveExpression.
    def exitAdditiveExpression(
            self, ctx: KotlinParser.AdditiveExpressionContext):
        pass

    # Enter a parse tree produced by KotlinParser#multiplicativeExpression.
    def enterMultiplicativeExpression(
            self, ctx: KotlinParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by KotlinParser#multiplicativeExpression.
    def exitMultiplicativeExpression(
            self, ctx: KotlinParser.MultiplicativeExpressionContext):
        pass

    # Enter a parse tree produced by KotlinParser#typeRHS.
    def enterTypeRHS(self, ctx: KotlinParser.TypeRHSContext):
        # act_token = ShortToken('', 0, 0)
        # class_param_node = ECSTNode(
        #     str(uuid.uuid4()), self.current_node, act_token, 'AS'
        # )
        # self.current_node.add_child(class_param_node)
        # self.current_node = class_param_node
        pass

    # Exit a parse tree produced by KotlinParser#typeRHS.
    def exitTypeRHS(self, ctx: KotlinParser.TypeRHSContext):
        # self.current_node = self.current_node.parent
        pass

    # Enter a parse tree produced by KotlinParser#prefixUnaryExpression.
    def enterPrefixUnaryExpression(
            self, ctx: KotlinParser.PrefixUnaryExpressionContext):
        # act_token = ShortToken('', 0, 0)
        # class_param_node = ECSTNode(
        #     str(uuid.uuid4()), self.current_node, act_token, 'PREFIX'
        # )
        # self.current_node.add_child(class_param_node)
        # self.current_node = class_param_node
        pass

    # Exit a parse tree produced by KotlinParser#prefixUnaryExpression.
    def exitPrefixUnaryExpression(
            self, ctx: KotlinParser.PrefixUnaryExpressionContext):
        # self.current_node = self.current_node.parent
        pass

    # Enter a parse tree produced by KotlinParser#postfixUnaryExpression.
    def enterPostfixUnaryExpression(
            self, ctx: KotlinParser.PostfixUnaryExpressionContext):
        # act_token = ShortToken('', 0, 0)
        # class_param_node = ECSTNode(
        #     str(uuid.uuid4()), self.current_node, act_token, 'POSFIX'
        # )
        # self.current_node.add_child(class_param_node)
        # self.current_node = class_param_node
        pass

    # Exit a parse tree produced by KotlinParser#postfixUnaryExpression.
    def exitPostfixUnaryExpression(
            self, ctx: KotlinParser.PostfixUnaryExpressionContext):
        # self.current_node = self.current_node.parent
        pass

    # Enter a parse tree produced by KotlinParser#atomicExpression.
    def enterAtomicExpression(self, ctx: KotlinParser.AtomicExpressionContext):
        pass

    # Exit a parse tree produced by KotlinParser#atomicExpression.
    def exitAtomicExpression(self, ctx: KotlinParser.AtomicExpressionContext):
        pass

    # Enter a parse tree produced by KotlinParser#parenthesizedExpression.
    def enterParenthesizedExpression(
            self, ctx: KotlinParser.ParenthesizedExpressionContext):
        pass

    # Exit a parse tree produced by KotlinParser#parenthesizedExpression.
    def exitParenthesizedExpression(
            self, ctx: KotlinParser.ParenthesizedExpressionContext):
        pass

    # Enter a parse tree produced by KotlinParser#callSuffix.
    def enterCallSuffix(self, ctx: KotlinParser.CallSuffixContext):
        pass

    # Exit a parse tree produced by KotlinParser#callSuffix.
    def exitCallSuffix(self, ctx: KotlinParser.CallSuffixContext):
        pass

    # Enter a parse tree produced by KotlinParser#annotatedLambda.
    def enterAnnotatedLambda(self, ctx: KotlinParser.AnnotatedLambdaContext):
        if ctx.LabelDefinition():
            token = ctx.LabelDefinition().symbol
            act_token = ShortToken(token.text, token.line, token.column)
            class_param_node = ECSTNode(
                str(uuid.uuid4()), self.current_node, act_token, 'FUNCTION_DECL'
            )
            self.current_node.add_child(class_param_node)
            self.current_node = class_param_node

    # Exit a parse tree produced by KotlinParser#annotatedLambda.
    def exitAnnotatedLambda(self, ctx: KotlinParser.AnnotatedLambdaContext):
        if ctx.LabelDefinition():
            self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#arrayAccess.
    def enterArrayAccess(self, ctx: KotlinParser.ArrayAccessContext):
        act_token = ShortToken('', 0, 0)
        class_param_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'COLLECTION_INDEXING'
        )
        self.current_node.add_child(class_param_node)
        self.current_node = class_param_node

    # Exit a parse tree produced by KotlinParser#arrayAccess.
    def exitArrayAccess(self, ctx: KotlinParser.ArrayAccessContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#valueArguments.
    def enterValueArguments(self, ctx: KotlinParser.ValueArgumentsContext):
        act_token = ShortToken('', 0, 0)
        class_param_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'VALUE_ARGUMENT_LIST'
        )
        self.current_node.add_child(class_param_node)
        self.current_node = class_param_node

    # Exit a parse tree produced by KotlinParser#valueArguments.
    def exitValueArguments(self, ctx: KotlinParser.ValueArgumentsContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#typeArguments.
    def enterTypeArguments(self, ctx: KotlinParser.TypeArgumentsContext):
        act_token = ShortToken('', 0, 0)
        class_param_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'TYPE_ARGUMENT_LIST'
        )
        self.current_node.add_child(class_param_node)
        self.current_node = class_param_node

    # Exit a parse tree produced by KotlinParser#typeArguments.
    def exitTypeArguments(self, ctx: KotlinParser.TypeArgumentsContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#typeProjection.
    def enterTypeProjection(self, ctx: KotlinParser.TypeProjectionContext):
        act_token = ShortToken('', 0, 0)
        class_param_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'TYPE_ARGUMENT'
        )
        self.current_node.add_child(class_param_node)
        self.current_node = class_param_node

    # Exit a parse tree produced by KotlinParser#typeProjection.
    def exitTypeProjection(self, ctx: KotlinParser.TypeProjectionContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#typeProjectionModifierList.
    def enterTypeProjectionModifierList(
            self, ctx: KotlinParser.TypeProjectionModifierListContext):
        pass

    # Exit a parse tree produced by KotlinParser#typeProjectionModifierList.
    def exitTypeProjectionModifierList(
            self, ctx: KotlinParser.TypeProjectionModifierListContext):
        pass

    # Enter a parse tree produced by KotlinParser#valueArgument.
    def enterValueArgument(self, ctx: KotlinParser.ValueArgumentContext):
        act_token = ShortToken('', 0, 0)
        class_param_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'VALUE_ARGUMENT'
        )
        self.current_node.add_child(class_param_node)
        self.current_node = class_param_node

    # Exit a parse tree produced by KotlinParser#valueArgument.
    def exitValueArgument(self, ctx: KotlinParser.ValueArgumentContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#literalConstant.
    def enterLiteralConstant(self, ctx: KotlinParser.LiteralConstantContext):
        try:
            act_token = (
                ctx.BinLiteral() or ctx.BooleanLiteral() or
                ctx.CharacterLiteral() or ctx.HexLiteral() or
                ctx.IntegerLiteral() or ctx.LongLiteral() or
                ctx.NullLiteral() or ctx.RealLiteral())
            token = act_token.symbol
            act_token = ShortToken(token.text, token.line, token.column)
        except AttributeError:
            act_token = ShortToken('', 0, 0)
        class_param_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token, 'LITERAL')
        self.current_node.add_child(class_param_node)
        self.current_node = class_param_node

    # Exit a parse tree produced by KotlinParser#literalConstant.
    def exitLiteralConstant(self, ctx: KotlinParser.LiteralConstantContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#stringLiteral.
    def enterStringLiteral(self, ctx: KotlinParser.StringLiteralContext):
        pass

    # Exit a parse tree produced by KotlinParser#stringLiteral.
    def exitStringLiteral(self, ctx: KotlinParser.StringLiteralContext):
        pass

    # Enter a parse tree produced by KotlinParser#lineStringLiteral.
    def enterLineStringLiteral(
            self, ctx: KotlinParser.LineStringLiteralContext):
        pass

    # Exit a parse tree produced by KotlinParser#lineStringLiteral.
    def exitLineStringLiteral(
            self, ctx: KotlinParser.LineStringLiteralContext):
        pass

    # Enter a parse tree produced by KotlinParser#multiLineStringLiteral.
    def enterMultiLineStringLiteral(
            self, ctx: KotlinParser.MultiLineStringLiteralContext):
        pass

    # Exit a parse tree produced by KotlinParser#multiLineStringLiteral.
    def exitMultiLineStringLiteral(
            self, ctx: KotlinParser.MultiLineStringLiteralContext):
        pass

    # Enter a parse tree produced by KotlinParser#lineStringContent.
    def enterLineStringContent(
            self, ctx: KotlinParser.LineStringContentContext):
        try:
            token = (ctx.LineStrEscapedChar() or ctx.LineStrText() or
                     ctx.LineStrRef())
            token = token.symbol
            act_token = ShortToken(token.text, token.line, token.column)
        except AttributeError:
            act_token = ShortToken('', 0, 0)
        class_param_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token, 'STRING'
        )
        self.current_node.add_child(class_param_node)
        self.current_node = class_param_node

    # Exit a parse tree produced by KotlinParser#lineStringContent.
    def exitLineStringContent(
            self, ctx: KotlinParser.LineStringContentContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#lineStringExpression.
    def enterLineStringExpression(
            self, ctx: KotlinParser.LineStringExpressionContext):
        pass

    # Exit a parse tree produced by KotlinParser#lineStringExpression.
    def exitLineStringExpression(
            self, ctx: KotlinParser.LineStringExpressionContext):
        pass

    # Enter a parse tree produced by KotlinParser#multiLineStringContent.
    def enterMultiLineStringContent(
            self, ctx: KotlinParser.MultiLineStringContentContext):
        try:
            token = (ctx.MultiLineStrRef() or ctx.MultiLineStrText() or ctx.MultiLineStrEscapedChar())
            print(token)
            token = token.symbol
            act_token = ShortToken(token.text, token.line, token.column)
        except AttributeError:
            act_token = ShortToken('', 0, 0)
        class_param_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token, 'STRING'
        )
        self.current_node.add_child(class_param_node)
        self.current_node = class_param_node

    # Exit a parse tree produced by KotlinParser#multiLineStringContent.
    def exitMultiLineStringContent(
            self, ctx: KotlinParser.MultiLineStringContentContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#multiLineStringExpression.
    def enterMultiLineStringExpression(
            self, ctx: KotlinParser.MultiLineStringExpressionContext):
        pass

    # Exit a parse tree produced by KotlinParser#multiLineStringExpression.
    def exitMultiLineStringExpression(
            self, ctx: KotlinParser.MultiLineStringExpressionContext):
        pass

    # Enter a parse tree produced by KotlinParser#functionLiteral.
    def enterFunctionLiteral(self, ctx: KotlinParser.FunctionLiteralContext):
        pass

    # Exit a parse tree produced by KotlinParser#functionLiteral.
    def exitFunctionLiteral(self, ctx: KotlinParser.FunctionLiteralContext):
        pass

    # Enter a parse tree produced by KotlinParser#lambdaParameters.
    def enterLambdaParameters(self, ctx: KotlinParser.LambdaParametersContext):
        act_token = ShortToken('', 0, 0)
        class_param_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'PARAMETER_LIST'
        )
        self.current_node.add_child(class_param_node)
        self.current_node = class_param_node

    # Exit a parse tree produced by KotlinParser#lambdaParameters.
    def exitLambdaParameters(self, ctx: KotlinParser.LambdaParametersContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#lambdaParameter.
    def enterLambdaParameter(self, ctx: KotlinParser.LambdaParameterContext):
        act_token = ShortToken('', 0, 0)
        class_param_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'PARAMETER'
        )
        self.current_node.add_child(class_param_node)
        self.current_node = class_param_node

    # Exit a parse tree produced by KotlinParser#lambdaParameter.
    def exitLambdaParameter(self, ctx: KotlinParser.LambdaParameterContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#objectLiteral.
    def enterObjectLiteral(self, ctx: KotlinParser.ObjectLiteralContext):
        pass

    # Exit a parse tree produced by KotlinParser#objectLiteral.
    def exitObjectLiteral(self, ctx: KotlinParser.ObjectLiteralContext):
        pass

    # Enter a parse tree produced by KotlinParser#collectionLiteral.
    def enterCollectionLiteral(
            self, ctx: KotlinParser.CollectionLiteralContext):
        act_token = ShortToken('', 0, 0)
        class_param_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'COLLECTION'
        )
        self.current_node.add_child(class_param_node)
        self.current_node = class_param_node

    # Exit a parse tree produced by KotlinParser#collectionLiteral.
    def exitCollectionLiteral(
            self, ctx: KotlinParser.CollectionLiteralContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#thisExpression.
    def enterThisExpression(self, ctx: KotlinParser.ThisExpressionContext):
        token = ctx.THIS().symbol
        act_token = ShortToken(token.text, token.line, token.column)
        class_param_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'THIS'
        )
        self.current_node.add_child(class_param_node)
        self.current_node = class_param_node

    # Exit a parse tree produced by KotlinParser#thisExpression.
    def exitThisExpression(self, ctx: KotlinParser.ThisExpressionContext):
        pass

    # Enter a parse tree produced by KotlinParser#superExpression.
    def enterSuperExpression(self, ctx: KotlinParser.SuperExpressionContext):
        token = ctx.SUPER().symbol
        act_token = ShortToken(token.text, token.line, token.column)
        class_param_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token, 'SUPER_CALL'
        )
        self.current_node.add_child(class_param_node)
        self.current_node = class_param_node

    # Exit a parse tree produced by KotlinParser#superExpression.
    def exitSuperExpression(self, ctx: KotlinParser.SuperExpressionContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#conditionalExpression.
    def enterConditionalExpression(
            self, ctx: KotlinParser.ConditionalExpressionContext):
        act_token = ShortToken('', 0, 0)
        class_param_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token, 'CONDITION'
        )
        self.current_node.add_child(class_param_node)
        self.current_node = class_param_node

    # Exit a parse tree produced by KotlinParser#conditionalExpression.
    def exitConditionalExpression(
            self, ctx: KotlinParser.ConditionalExpressionContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#ifExpression.
    def enterIfExpression(self, ctx: KotlinParser.IfExpressionContext):
        pass

    # Exit a parse tree produced by KotlinParser#ifExpression.
    def exitIfExpression(self, ctx: KotlinParser.IfExpressionContext):
        pass

    # Enter a parse tree produced by KotlinParser#controlStructureBody.
    def enterControlStructureBody(
            self, ctx: KotlinParser.ControlStructureBodyContext):
        act_token = ShortToken('', 0, 0)
        class_param_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token, 'BODY'
        )
        self.current_node.add_child(class_param_node)
        self.current_node = class_param_node

    # Exit a parse tree produced by KotlinParser#controlStructureBody.
    def exitControlStructureBody(
            self, ctx: KotlinParser.ControlStructureBodyContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#whenExpression.
    def enterWhenExpression(self, ctx: KotlinParser.WhenExpressionContext):
        pass

    # Exit a parse tree produced by KotlinParser#whenExpression.
    def exitWhenExpression(self, ctx: KotlinParser.WhenExpressionContext):
        pass

    # Enter a parse tree produced by KotlinParser#whenEntry.
    def enterWhenEntry(self, ctx: KotlinParser.WhenEntryContext):
        pass

    # Exit a parse tree produced by KotlinParser#whenEntry.
    def exitWhenEntry(self, ctx: KotlinParser.WhenEntryContext):
        pass

    # Enter a parse tree produced by KotlinParser#whenCondition.
    def enterWhenCondition(self, ctx: KotlinParser.WhenConditionContext):
        pass

    # Exit a parse tree produced by KotlinParser#whenCondition.
    def exitWhenCondition(self, ctx: KotlinParser.WhenConditionContext):
        pass

    # Enter a parse tree produced by KotlinParser#rangeTest.
    def enterRangeTest(self, ctx: KotlinParser.RangeTestContext):
        pass

    # Exit a parse tree produced by KotlinParser#rangeTest.
    def exitRangeTest(self, ctx: KotlinParser.RangeTestContext):
        pass

    # Enter a parse tree produced by KotlinParser#typeTest.
    def enterTypeTest(self, ctx: KotlinParser.TypeTestContext):
        pass

    # Exit a parse tree produced by KotlinParser#typeTest.
    def exitTypeTest(self, ctx: KotlinParser.TypeTestContext):
        pass

    # Enter a parse tree produced by KotlinParser#tryExpression.
    def enterTryExpression(self, ctx: KotlinParser.TryExpressionContext):
        token = ctx.TRY().symbol
        act_token = ShortToken(token.text, token.line, token.column)
        class_param_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token, 'TRY'
        )
        self.current_node.add_child(class_param_node)
        self.current_node = class_param_node

    # Exit a parse tree produced by KotlinParser#tryExpression.
    def exitTryExpression(self, ctx: KotlinParser.TryExpressionContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#catchBlock.
    def enterCatchBlock(self, ctx: KotlinParser.CatchBlockContext):
        token = ctx.CATCH().symbol
        act_token = ShortToken(token.text, token.line, token.column)
        class_param_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token, 'CATCH'
        )
        self.current_node.add_child(class_param_node)
        self.current_node = class_param_node

    # Exit a parse tree produced by KotlinParser#catchBlock.
    def exitCatchBlock(self, ctx: KotlinParser.CatchBlockContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#finallyBlock.
    def enterFinallyBlock(self, ctx: KotlinParser.FinallyBlockContext):
        token = ctx.FINALLY().symbol
        act_token = ShortToken(token.text, token.line, token.column)
        class_param_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token, 'FINALLY'
        )
        self.current_node.add_child(class_param_node)
        self.current_node = class_param_node

    # Exit a parse tree produced by KotlinParser#finallyBlock.
    def exitFinallyBlock(self, ctx: KotlinParser.FinallyBlockContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#loopExpression.
    def enterLoopExpression(self, ctx: KotlinParser.LoopExpressionContext):
        act_token = ShortToken('', 0, 0)
        class_param_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token, 'LOOP_STATEMENT'
        )
        self.current_node.add_child(class_param_node)
        self.current_node = class_param_node

    # Exit a parse tree produced by KotlinParser#loopExpression.
    def exitLoopExpression(self, ctx: KotlinParser.LoopExpressionContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#forExpression.
    def enterForExpression(self, ctx: KotlinParser.ForExpressionContext):
        pass

    # Exit a parse tree produced by KotlinParser#forExpression.
    def exitForExpression(self, ctx: KotlinParser.ForExpressionContext):
        pass

    # Enter a parse tree produced by KotlinParser#whileExpression.
    def enterWhileExpression(self, ctx: KotlinParser.WhileExpressionContext):
        pass

    # Exit a parse tree produced by KotlinParser#whileExpression.
    def exitWhileExpression(self, ctx: KotlinParser.WhileExpressionContext):
        pass

    # Enter a parse tree produced by KotlinParser#doWhileExpression.
    def enterDoWhileExpression(
            self, ctx: KotlinParser.DoWhileExpressionContext):
        pass

    # Exit a parse tree produced by KotlinParser#doWhileExpression.
    def exitDoWhileExpression(self, ctx: KotlinParser.DoWhileExpressionContext):
        pass

    # Enter a parse tree produced by KotlinParser#jumpExpression.
    def enterJumpExpression(self, ctx: KotlinParser.JumpExpressionContext):
        act_token = (ctx.THROW() or ctx.RETURN() or ctx.RETURN_AT() or
                     ctx.CONTINUE() or ctx.CONTINUE_AT() or ctx.BREAK() or
                     ctx.BREAK_AT())
        token = act_token.symbol
        act_token = ShortToken(token.text, token.line, token.column)
        class_param_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token, 'JUMP_STATEMENT'
        )
        self.current_node.add_child(class_param_node)
        self.current_node = class_param_node

    # Exit a parse tree produced by KotlinParser#jumpExpression.
    def exitJumpExpression(self, ctx: KotlinParser.JumpExpressionContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#callableReference.
    def enterCallableReference(
            self, ctx: KotlinParser.CallableReferenceContext):
        pass

    # Exit a parse tree produced by KotlinParser#callableReference.
    def exitCallableReference(
            self, ctx: KotlinParser.CallableReferenceContext):
        pass

    # Enter a parse tree produced by KotlinParser#assignmentOperator.
    def enterAssignmentOperator(
            self, ctx: KotlinParser.AssignmentOperatorContext):
        act_token = (ctx.ASSIGNMENT() or ctx.ADD_ASSIGNMENT() or
                     ctx.SUB_ASSIGNMENT() or ctx.MULT_ASSIGNMENT() or
                     ctx.DIV_ASSIGNMENT() or ctx.MOD_ASSIGNMENT())
        token = act_token.symbol
        act_token = ShortToken(token.text, token.line, token.column)
        class_param_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'ASSIGNMENT_OPERATOR')
        self.current_node.add_child(class_param_node)
        self.current_node = class_param_node

    # Exit a parse tree produced by KotlinParser#assignmentOperator.
    def exitAssignmentOperator(
            self, ctx: KotlinParser.AssignmentOperatorContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#equalityOperation.
    def enterEqualityOperation(
            self, ctx: KotlinParser.EqualityOperationContext):
        act_token = (ctx.EXCL_EQ() or ctx.EXCL_EQEQ() or ctx.EQEQ() or
                     ctx.EQEQEQ())
        token = act_token.symbol
        act_token = ShortToken(token.text, token.line, token.column)
        class_param_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'EQUALITY_OPERATOR')
        self.current_node.add_child(class_param_node)
        self.current_node = class_param_node

    # Exit a parse tree produced by KotlinParser#equalityOperation.
    def exitEqualityOperation(self, ctx: KotlinParser.EqualityOperationContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#comparisonOperator.
    def enterComparisonOperator(
            self, ctx: KotlinParser.ComparisonOperatorContext):
        act_token = ctx.LANGLE() or ctx.RANGLE() or ctx.LE() or ctx.GE()
        token = act_token.symbol
        act_token = ShortToken(token.text, token.line, token.column)
        class_param_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'COMPARISON_OPERATOR')
        self.current_node.add_child(class_param_node)
        self.current_node = class_param_node

    # Exit a parse tree produced by KotlinParser#comparisonOperator.
    def exitComparisonOperator(
            self, ctx: KotlinParser.ComparisonOperatorContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#inOperator.
    def enterInOperator(self, ctx: KotlinParser.InOperatorContext):
        token = ctx.IN() or ctx.NOT_IN()
        token = token.symbol
        act_token = ShortToken(token.text, token.line, token.column)
        class_param_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token, 'MEMBER_OF')
        self.current_node.add_child(class_param_node)
        self.current_node = class_param_node

    # Exit a parse tree produced by KotlinParser#inOperator.
    def exitInOperator(self, ctx: KotlinParser.InOperatorContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#isOperator.
    def enterIsOperator(self, ctx: KotlinParser.IsOperatorContext):
        token = ctx.IS() or ctx.NOT_IS()
        token = token.symbol
        act_token = ShortToken(token.text, token.line, token.column)
        class_param_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token, 'IS_TYPE')
        self.current_node.add_child(class_param_node)
        self.current_node = class_param_node

    # Exit a parse tree produced by KotlinParser#isOperator.
    def exitIsOperator(self, ctx: KotlinParser.IsOperatorContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#additiveOperator.
    def enterAdditiveOperator(self, ctx: KotlinParser.AdditiveOperatorContext):
        try:
            act_token = ctx.ADD() or ctx.SUB()
            token = act_token.symbol
            act_token = ShortToken(token.text, token.line, token.column)
        except AttributeError:
            act_token = ShortToken('', 0, 0)
        class_param_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'ADDITIVE_OPERATOR')
        self.current_node.add_child(class_param_node)
        self.current_node = class_param_node

    # Exit a parse tree produced by KotlinParser#additiveOperator.
    def exitAdditiveOperator(self, ctx: KotlinParser.AdditiveOperatorContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#multiplicativeOperation.
    def enterMultiplicativeOperation(
            self, ctx: KotlinParser.MultiplicativeOperationContext):
        act_token = ctx.DIV() or ctx.MOD() or ctx.MULT()
        token = act_token.symbol
        act_token = ShortToken(token.text, token.line, token.column)
        class_param_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'ADDITIVE_OPERATOR')
        self.current_node.add_child(class_param_node)
        self.current_node = class_param_node

    # Exit a parse tree produced by KotlinParser#multiplicativeOperation.
    def exitMultiplicativeOperation(
            self, ctx: KotlinParser.MultiplicativeOperationContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#typeOperation.
    def enterTypeOperation(self, ctx: KotlinParser.TypeOperationContext):
        pass

    # Exit a parse tree produced by KotlinParser#typeOperation.
    def exitTypeOperation(self, ctx: KotlinParser.TypeOperationContext):
        pass

    # Enter a parse tree produced by KotlinParser#prefixUnaryOperation.
    def enterPrefixUnaryOperation(
            self, ctx: KotlinParser.PrefixUnaryOperationContext):
        if ctx.EXCL():
            token = ctx.EXCL().symbol
            act_token = ShortToken(token.text, token.line, token.column)
            cur_type = 'LOGICAL_OPERATOR'
        else:
            act_token = ctx.ADD() or ctx.DECR() or ctx.INCR() or ctx.SUB()
            try:
                token = act_token.symbol
                act_token = ShortToken(token.text, token.line, token.column)
            except AttributeError:
                act_token = ShortToken('+/-', -1, -1)
            cur_type = 'ADDITIVE_OPERATOR'
        class_param_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            cur_type)
        self.current_node.add_child(class_param_node)
        self.current_node = class_param_node

    # Exit a parse tree produced by KotlinParser#prefixUnaryOperation.
    def exitPrefixUnaryOperation(
            self, ctx: KotlinParser.PrefixUnaryOperationContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#postfixUnaryOperation.
    def enterPostfixUnaryOperation(
            self, ctx: KotlinParser.PostfixUnaryOperationContext):
        try:
            if ctx.EXCL():
                act_token = ctx.EXCL().symbol
                cur_type = 'LOGICAL_OPERATOR'
            else:
                act_token = ctx.DECR() or ctx.INCR()
                token = act_token.symbol
                act_token = ShortToken(token.text, token.line, token.column)
                cur_type = 'ADDITIVE_OPERATOR'
            class_param_node = ECSTNode(
                str(uuid.uuid4()), self.current_node, act_token,
                cur_type)
            self.current_node.add_child(class_param_node)
            self.current_node = class_param_node
        except AttributeError:
            pass

    # Exit a parse tree produced by KotlinParser#postfixUnaryOperation.
    def exitPostfixUnaryOperation(
            self, ctx: KotlinParser.PostfixUnaryOperationContext):
        if (self.current_node.type == 'ADDITIVE_OPERATOR' or
                self.current_node.type == 'LOGICAL_OPERATOR'):
            self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#memberAccessOperator.
    def enterMemberAccessOperator(
            self, ctx: KotlinParser.MemberAccessOperatorContext):
        act_token = ctx.DOT() or ctx.QUEST()
        token = act_token.symbol
        act_token = ShortToken(token.text, token.line, token.column)
        class_param_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'ACCESS_OPERATOR')
        self.current_node.add_child(class_param_node)
        self.current_node = class_param_node

    # Exit a parse tree produced by KotlinParser#memberAccessOperator.
    def exitMemberAccessOperator(
            self, ctx: KotlinParser.MemberAccessOperatorContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#modifierList.
    def enterModifierList(self, ctx: KotlinParser.ModifierListContext):
        pass

    # Exit a parse tree produced by KotlinParser#modifierList.
    def exitModifierList(self, ctx: KotlinParser.ModifierListContext):
        pass

    # Enter a parse tree produced by KotlinParser#modifier.
    def enterModifier(self, ctx: KotlinParser.ModifierContext):
        pass

    # Exit a parse tree produced by KotlinParser#modifier.
    def exitModifier(self, ctx: KotlinParser.ModifierContext):
        pass

    # Enter a parse tree produced by KotlinParser#classModifier.
    def enterClassModifier(self, ctx: KotlinParser.ClassModifierContext):
        act_token = (ctx.ANNOTATION() or ctx.DATA() or ctx.ENUM() or
                     ctx.INNER() or ctx.SEALED())
        token = act_token.symbol
        act_token = ShortToken(token.text, token.line, token.column)
        class_param_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'CLASS_DECL')
        self.current_node.add_child(class_param_node)
        self.current_node = class_param_node

    # Exit a parse tree produced by KotlinParser#classModifier.
    def exitClassModifier(self, ctx: KotlinParser.ClassModifierContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#memberModifier.
    def enterMemberModifier(self, ctx: KotlinParser.MemberModifierContext):
        pass

    # Exit a parse tree produced by KotlinParser#memberModifier.
    def exitMemberModifier(self, ctx: KotlinParser.MemberModifierContext):
        pass

    # Enter a parse tree produced by KotlinParser#visibilityModifier.
    def enterVisibilityModifier(
            self, ctx: KotlinParser.VisibilityModifierContext):
        act_token = (ctx.INTERNAL() or ctx.PRIVATE() or ctx.PROTECTED() or
                     ctx.PUBLIC())
        token = act_token.symbol
        act_token = ShortToken(token.text, token.line, token.column)
        class_param_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'VISIBILITY_MODIFIER')
        self.current_node.add_child(class_param_node)
        self.current_node = class_param_node

    # Exit a parse tree produced by KotlinParser#visibilityModifier.
    def exitVisibilityModifier(
            self, ctx: KotlinParser.VisibilityModifierContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#varianceAnnotation.
    def enterVarianceAnnotation(
            self, ctx: KotlinParser.VarianceAnnotationContext):
        act_token = ctx.IN() or ctx.OUT()
        token = act_token.symbol
        act_token = ShortToken(token.text, token.line, token.column)
        class_param_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'MEMBER_OF')
        self.current_node.add_child(class_param_node)
        self.current_node = class_param_node

    # Exit a parse tree produced by KotlinParser#varianceAnnotation.
    def exitVarianceAnnotation(
            self, ctx: KotlinParser.VarianceAnnotationContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#functionModifier.
    def enterFunctionModifier(self, ctx: KotlinParser.FunctionModifierContext):
        pass

    # Exit a parse tree produced by KotlinParser#functionModifier.
    def exitFunctionModifier(self, ctx: KotlinParser.FunctionModifierContext):
        pass

    # Enter a parse tree produced by KotlinParser#propertyModifier.
    def enterPropertyModifier(self, ctx: KotlinParser.PropertyModifierContext):
        act_token = ctx.CONST()
        token = act_token.symbol
        act_token = ShortToken(token.text, token.line, token.column)
        class_param_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'CONST_DECL')
        self.current_node.add_child(class_param_node)
        self.current_node = class_param_node

    # Exit a parse tree produced by KotlinParser#propertyModifier.
    def exitPropertyModifier(self, ctx: KotlinParser.PropertyModifierContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#inheritanceModifier.
    def enterInheritanceModifier(
            self, ctx: KotlinParser.InheritanceModifierContext):
        act_token = ctx.ABSTRACT() or ctx.FINAL() or ctx.OPEN()
        token = act_token.symbol
        act_token = ShortToken(token.text, token.line, token.column)
        class_param_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'INHERITANCE_MODIFIER')
        self.current_node.add_child(class_param_node)
        self.current_node = class_param_node

    # Exit a parse tree produced by KotlinParser#inheritanceModifier.
    def exitInheritanceModifier(
            self, ctx: KotlinParser.InheritanceModifierContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#parameterModifier.
    def enterParameterModifier(
            self, ctx: KotlinParser.ParameterModifierContext):
        pass

    # Exit a parse tree produced by KotlinParser#parameterModifier.
    def exitParameterModifier(
            self, ctx: KotlinParser.ParameterModifierContext):
        pass

    # Enter a parse tree produced by KotlinParser#typeParameterModifier.
    def enterTypeParameterModifier(
            self, ctx: KotlinParser.TypeParameterModifierContext):
        pass

    # Exit a parse tree produced by KotlinParser#typeParameterModifier.
    def exitTypeParameterModifier(
            self, ctx: KotlinParser.TypeParameterModifierContext):
        pass

    # Enter a parse tree produced by KotlinParser#labelDefinition.
    def enterLabelDefinition(self, ctx: KotlinParser.LabelDefinitionContext):
        pass

    # Exit a parse tree produced by KotlinParser#labelDefinition.
    def exitLabelDefinition(self, ctx: KotlinParser.LabelDefinitionContext):
        pass

    # Enter a parse tree produced by KotlinParser#annotations.
    def enterAnnotations(self, ctx: KotlinParser.AnnotationsContext):
        pass

    # Exit a parse tree produced by KotlinParser#annotations.
    def exitAnnotations(self, ctx: KotlinParser.AnnotationsContext):
        pass

    # Enter a parse tree produced by KotlinParser#annotation.
    def enterAnnotation(self, ctx: KotlinParser.AnnotationContext):
        pass

    # Exit a parse tree produced by KotlinParser#annotation.
    def exitAnnotation(self, ctx: KotlinParser.AnnotationContext):
        pass

    # Enter a parse tree produced by KotlinParser#annotationList.
    def enterAnnotationList(self, ctx: KotlinParser.AnnotationListContext):
        pass

    # Exit a parse tree produced by KotlinParser#annotationList.
    def exitAnnotationList(self, ctx: KotlinParser.AnnotationListContext):
        pass

    # Enter a parse tree produced by KotlinParser#annotationUseSiteTarget.
    def enterAnnotationUseSiteTarget(
            self, ctx: KotlinParser.AnnotationUseSiteTargetContext):
        pass

    # Exit a parse tree produced by KotlinParser#annotationUseSiteTarget.
    def exitAnnotationUseSiteTarget(
            self, ctx: KotlinParser.AnnotationUseSiteTargetContext):
        pass

    # Enter a parse tree produced by KotlinParser#unescapedAnnotation.
    def enterUnescapedAnnotation(
            self, ctx: KotlinParser.UnescapedAnnotationContext):
        pass

    # Exit a parse tree produced by KotlinParser#unescapedAnnotation.
    def exitUnescapedAnnotation(
            self, ctx: KotlinParser.UnescapedAnnotationContext):
        pass

    # Enter a parse tree produced by KotlinParser#identifier.
    def enterIdentifier(self, ctx: KotlinParser.IdentifierContext):
        pass

    # Exit a parse tree produced by KotlinParser#identifier.
    def exitIdentifier(self, ctx: KotlinParser.IdentifierContext):
        pass

    # Enter a parse tree produced by KotlinParser#simpleIdentifier.
    def enterSimpleIdentifier(self, ctx: KotlinParser.SimpleIdentifierContext):
        if ctx.Identifier():
            identifier = ctx.Identifier().symbol
            act_token = ShortToken(
                identifier.text, identifier.line, identifier.column)
            identifier_node = ECSTNode(
                str(uuid.uuid4()), self.current_node, act_token, 'IDENTIFIER')
            self.current_node.add_child(identifier_node)
            self.current_node = identifier_node

    # Exit a parse tree produced by KotlinParser#simpleIdentifier.
    def exitSimpleIdentifier(self, ctx: KotlinParser.SimpleIdentifierContext):
        if ctx.Identifier():
            self.current_node = self.current_node.parent

    # Enter a parse tree produced by KotlinParser#semi.
    def enterSemi(self, ctx: KotlinParser.SemiContext):
        pass

    # Exit a parse tree produced by KotlinParser#semi.
    def exitSemi(self, ctx: KotlinParser.SemiContext):
        pass

    # Enter a parse tree produced by KotlinParser#anysemi.
    def enterAnysemi(self, ctx: KotlinParser.AnysemiContext):
        pass

    # Exit a parse tree produced by KotlinParser#anysemi.
    def exitAnysemi(self, ctx: KotlinParser.AnysemiContext):
        pass
