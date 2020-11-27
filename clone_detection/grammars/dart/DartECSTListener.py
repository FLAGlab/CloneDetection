from antlr4 import *
import uuid
from clone_detection.ecst.ecst_tree import ECSTree
from clone_detection.ecst.ecst_node import ECSTNode, ShortToken
from .Dart2Parser import Dart2Parser
from clone_detection.grammars.grammars_registry import LISTENERS


# This class defines a complete listener for a parse tree produced by
# Dart2Parser.
@LISTENERS.register('dart')
class DartECSTListener(ParseTreeListener):
    def __init__(self):
        self.tree = ECSTree()
        self.current_node = self.tree

    # Enter a parse tree produced by Dart2Parser#compilationUnit.
    def enterCompilationUnit(self, ctx: Dart2Parser.CompilationUnitContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token, 'FILE')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#compilationUnit.
    def exitCompilationUnit(self, ctx: Dart2Parser.CompilationUnitContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#variableDeclaration.
    def enterVariableDeclaration(
            self, ctx: Dart2Parser.VariableDeclarationContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token, 'VARIABLE_DECL')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#variableDeclaration.
    def exitVariableDeclaration(
            self, ctx: Dart2Parser.VariableDeclarationContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#declaredIdentifier.
    def enterDeclaredIdentifier(
            self, ctx: Dart2Parser.DeclaredIdentifierContext):
        pass

    # Exit a parse tree produced by Dart2Parser#declaredIdentifier.
    def exitDeclaredIdentifier(
            self, ctx: Dart2Parser.DeclaredIdentifierContext):
        pass

    # Enter a parse tree produced by Dart2Parser#finalConstVarOrType.
    def enterFinalConstVarOrType(
            self, ctx: Dart2Parser.FinalConstVarOrTypeContext):
        # define final or const
        pass

    # Exit a parse tree produced by Dart2Parser#finalConstVarOrType.
    def exitFinalConstVarOrType(
            self, ctx: Dart2Parser.FinalConstVarOrTypeContext):
        pass

    # Enter a parse tree produced by Dart2Parser#varOrType.
    def enterVarOrType(self, ctx: Dart2Parser.VarOrTypeContext):
        pass

    # Exit a parse tree produced by Dart2Parser#varOrType.
    def exitVarOrType(self, ctx: Dart2Parser.VarOrTypeContext):
        pass

    # Enter a parse tree produced by Dart2Parser#initializedVariableDeclaration
    def enterInitializedVariableDeclaration(
            self, ctx: Dart2Parser.InitializedVariableDeclarationContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'ASSIGNMENT_OPERATOR')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#initializedVariableDeclaration.
    def exitInitializedVariableDeclaration(
            self, ctx: Dart2Parser.InitializedVariableDeclarationContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#initializedIdentifier.
    def enterInitializedIdentifier(
            self, ctx: Dart2Parser.InitializedIdentifierContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'ASSIGNMENT_OPERATOR')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#initializedIdentifier.
    def exitInitializedIdentifier(
            self, ctx: Dart2Parser.InitializedIdentifierContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#initializedIdentifierList.
    def enterInitializedIdentifierList(
            self, ctx: Dart2Parser.InitializedIdentifierListContext):
        pass

    # Exit a parse tree produced by Dart2Parser#initializedIdentifierList.
    def exitInitializedIdentifierList(
            self, ctx: Dart2Parser.InitializedIdentifierListContext):
        pass

    # Enter a parse tree produced by Dart2Parser#functionSignature.
    def enterFunctionSignature(
            self, ctx: Dart2Parser.FunctionSignatureContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'FUNCTION_DECL')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#functionSignature.
    def exitFunctionSignature(self, ctx: Dart2Parser.FunctionSignatureContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#formalParameterPart.
    def enterFormalParameterPart(
            self, ctx: Dart2Parser.FormalParameterPartContext):
        pass

    # Exit a parse tree produced by Dart2Parser#formalParameterPart.
    def exitFormalParameterPart(
            self, ctx: Dart2Parser.FormalParameterPartContext):
        pass

    # Enter a parse tree produced by Dart2Parser#returnType.
    def enterReturnType(self, ctx: Dart2Parser.ReturnTypeContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'TYPE')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#returnType.
    def exitReturnType(self, ctx: Dart2Parser.ReturnTypeContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#functionBody.
    def enterFunctionBody(self, ctx: Dart2Parser.FunctionBodyContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'FUNCTION_BODY')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#functionBody.
    def exitFunctionBody(self, ctx: Dart2Parser.FunctionBodyContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#block.
    def enterBlock(self, ctx: Dart2Parser.BlockContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'BODY')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#block.
    def exitBlock(self, ctx: Dart2Parser.BlockContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#formalParameterList.
    def enterFormalParameterList(
            self, ctx: Dart2Parser.FormalParameterListContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'VALUE_ARGUMENT_LIST')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#formalParameterList.
    def exitFormalParameterList(
            self, ctx: Dart2Parser.FormalParameterListContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#normalFormalParameters.
    def enterNormalFormalParameters(
            self, ctx: Dart2Parser.NormalFormalParametersContext):
        pass

    # Exit a parse tree produced by Dart2Parser#normalFormalParameters.
    def exitNormalFormalParameters(
            self, ctx: Dart2Parser.NormalFormalParametersContext):
        pass

    # Enter a parse tree produced by Dart2Parser#optionalFormalParameters.
    def enterOptionalFormalParameters(
            self, ctx: Dart2Parser.OptionalFormalParametersContext):
        pass

    # Exit a parse tree produced by Dart2Parser#optionalFormalParameters.
    def exitOptionalFormalParameters(
            self, ctx: Dart2Parser.OptionalFormalParametersContext):
        pass

    # Enter a parse tree produced by
    # Dart2Parser#optionalPositionalFormalParameters.
    def enterOptionalPositionalFormalParameters(
            self, ctx: Dart2Parser.OptionalPositionalFormalParametersContext):
        pass

    # Exit a parse tree produced by
    # Dart2Parser#optionalPositionalFormalParameters.
    def exitOptionalPositionalFormalParameters(
            self, ctx: Dart2Parser.OptionalPositionalFormalParametersContext):
        pass

    # Enter a parse tree produced by Dart2Parser#namedFormalParameters.
    def enterNamedFormalParameters(
            self, ctx: Dart2Parser.NamedFormalParametersContext):
        pass

    # Exit a parse tree produced by Dart2Parser#namedFormalParameters.
    def exitNamedFormalParameters(
            self, ctx: Dart2Parser.NamedFormalParametersContext):
        pass

    # Enter a parse tree produced by Dart2Parser#normalFormalParameter.
    def enterNormalFormalParameter(
            self, ctx: Dart2Parser.NormalFormalParameterContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'VALUE_ARGUMENT')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#normalFormalParameter.
    def exitNormalFormalParameter(
            self, ctx: Dart2Parser.NormalFormalParameterContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#functionFormalParameter.
    def enterFunctionFormalParameter(
            self, ctx: Dart2Parser.FunctionFormalParameterContext):
        pass

    # Exit a parse tree produced by Dart2Parser#functionFormalParameter.
    def exitFunctionFormalParameter(
            self, ctx: Dart2Parser.FunctionFormalParameterContext):
        pass

    # Enter a parse tree produced by Dart2Parser#simpleFormalParameter.
    def enterSimpleFormalParameter(
            self, ctx: Dart2Parser.SimpleFormalParameterContext):
        pass

    # Exit a parse tree produced by Dart2Parser#simpleFormalParameter.
    def exitSimpleFormalParameter(
            self, ctx: Dart2Parser.SimpleFormalParameterContext):
        pass

    # Enter a parse tree produced by Dart2Parser#fieldFormalParameter.
    def enterFieldFormalParameter(
            self, ctx: Dart2Parser.FieldFormalParameterContext):
        pass

    # Exit a parse tree produced by Dart2Parser#fieldFormalParameter.
    def exitFieldFormalParameter(
            self, ctx: Dart2Parser.FieldFormalParameterContext):
        pass

    # Enter a parse tree produced by Dart2Parser#defaultFormalParameter.
    def enterDefaultFormalParameter(
            self, ctx: Dart2Parser.DefaultFormalParameterContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'VALUE_ARGUMENT')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#defaultFormalParameter.
    def exitDefaultFormalParameter(
            self, ctx: Dart2Parser.DefaultFormalParameterContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#defaultNamedParameter.
    def enterDefaultNamedParameter(
            self, ctx: Dart2Parser.DefaultNamedParameterContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'VALUE_ARGUMENT')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#defaultNamedParameter.
    def exitDefaultNamedParameter(
            self, ctx: Dart2Parser.DefaultNamedParameterContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#classDefinition.
    def enterClassDefinition(self, ctx: Dart2Parser.ClassDefinitionContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'CLASS_DECL')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#classDefinition.
    def exitClassDefinition(self, ctx: Dart2Parser.ClassDefinitionContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#mixins.
    def enterMixins(self, ctx: Dart2Parser.MixinsContext):
        pass

    # Exit a parse tree produced by Dart2Parser#mixins.
    def exitMixins(self, ctx: Dart2Parser.MixinsContext):
        pass

    # Enter a parse tree produced by Dart2Parser#classMemberDefinition.
    def enterClassMemberDefinition(
            self, ctx: Dart2Parser.ClassMemberDefinitionContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'CLASS_DECL')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#classMemberDefinition.
    def exitClassMemberDefinition(
            self, ctx: Dart2Parser.ClassMemberDefinitionContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#methodSignature.
    def enterMethodSignature(self, ctx: Dart2Parser.MethodSignatureContext):
        pass

    # Exit a parse tree produced by Dart2Parser#methodSignature.
    def exitMethodSignature(self, ctx: Dart2Parser.MethodSignatureContext):
        pass

    # Enter a parse tree produced by Dart2Parser#declaration.
    def enterDeclaration(self, ctx: Dart2Parser.DeclarationContext):
        pass

    # Exit a parse tree produced by Dart2Parser#declaration.
    def exitDeclaration(self, ctx: Dart2Parser.DeclarationContext):
        pass

    # Enter a parse tree produced by Dart2Parser#staticFinalDeclarationList.
    def enterStaticFinalDeclarationList(
            self, ctx: Dart2Parser.StaticFinalDeclarationListContext):
        pass

    # Exit a parse tree produced by Dart2Parser#staticFinalDeclarationList.
    def exitStaticFinalDeclarationList(
            self, ctx: Dart2Parser.StaticFinalDeclarationListContext):
        pass

    # Enter a parse tree produced by Dart2Parser#staticFinalDeclaration.
    def enterStaticFinalDeclaration(
            self, ctx: Dart2Parser.StaticFinalDeclarationContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'ASSIGNMENT_OPERATOR')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#staticFinalDeclaration.
    def exitStaticFinalDeclaration(
            self, ctx: Dart2Parser.StaticFinalDeclarationContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#operatorSignature.
    def enterOperatorSignature(
            self, ctx: Dart2Parser.OperatorSignatureContext):
        pass

    # Exit a parse tree produced by Dart2Parser#operatorSignature.
    def exitOperatorSignature(
            self, ctx: Dart2Parser.OperatorSignatureContext):
        pass

    # Enter a parse tree produced by Dart2Parser#operator.
    def enterOperator(self, ctx: Dart2Parser.OperatorContext):
        pass

    # Exit a parse tree produced by Dart2Parser#operator.
    def exitOperator(self, ctx: Dart2Parser.OperatorContext):
        pass

    # Enter a parse tree produced by Dart2Parser#binaryOperator.
    def enterBinaryOperator(self, ctx: Dart2Parser.BinaryOperatorContext):
        pass

    # Exit a parse tree produced by Dart2Parser#binaryOperator.
    def exitBinaryOperator(self, ctx: Dart2Parser.BinaryOperatorContext):
        pass

    # Enter a parse tree produced by Dart2Parser#getterSignature.
    def enterGetterSignature(self, ctx: Dart2Parser.GetterSignatureContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'GETTER')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#getterSignature.
    def exitGetterSignature(self, ctx: Dart2Parser.GetterSignatureContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#setterSignature.
    def enterSetterSignature(self, ctx: Dart2Parser.SetterSignatureContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'SETTER')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#setterSignature.
    def exitSetterSignature(self, ctx: Dart2Parser.SetterSignatureContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#constructorSignature.
    def enterConstructorSignature(
            self, ctx: Dart2Parser.ConstructorSignatureContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'CONSTRUCTOR_DECL')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#constructorSignature.
    def exitConstructorSignature(
            self, ctx: Dart2Parser.ConstructorSignatureContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#redirection.
    def enterRedirection(self, ctx: Dart2Parser.RedirectionContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'CONSTRUCTOR_DECL')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#redirection.
    def exitRedirection(self, ctx: Dart2Parser.RedirectionContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#initializers.
    def enterInitializers(self, ctx: Dart2Parser.InitializersContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'CONSTRUCTOR_CALL')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#initializers.
    def exitInitializers(self, ctx: Dart2Parser.InitializersContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#initializerListEntry.
    def enterInitializerListEntry(
            self, ctx: Dart2Parser.InitializerListEntryContext):
        pass

    # Exit a parse tree produced by Dart2Parser#initializerListEntry.
    def exitInitializerListEntry(
            self, ctx: Dart2Parser.InitializerListEntryContext):
        pass

    # Enter a parse tree produced by Dart2Parser#fieldInitializer.
    def enterFieldInitializer(self, ctx: Dart2Parser.FieldInitializerContext):
        pass

    # Exit a parse tree produced by Dart2Parser#fieldInitializer.
    def exitFieldInitializer(self, ctx: Dart2Parser.FieldInitializerContext):
        pass

    # Enter a parse tree produced by Dart2Parser#factoryConstructorSignature.
    def enterFactoryConstructorSignature(
            self, ctx: Dart2Parser.FactoryConstructorSignatureContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'CONSTRUCTOR_DECL')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#factoryConstructorSignature.
    def exitFactoryConstructorSignature(
            self, ctx: Dart2Parser.FactoryConstructorSignatureContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by
    # Dart2Parser#redirectingFactoryConstructorSignature.
    def enterRedirectingFactoryConstructorSignature(
            self,
            ctx: Dart2Parser.RedirectingFactoryConstructorSignatureContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'CONSTRUCTOR_DECL')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by
    # Dart2Parser#redirectingFactoryConstructorSignature.
    def exitRedirectingFactoryConstructorSignature(
            self,
            ctx: Dart2Parser.RedirectingFactoryConstructorSignatureContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#constantConstructorSignature.
    def enterConstantConstructorSignature(
            self, ctx: Dart2Parser.ConstantConstructorSignatureContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'CONSTRUCTOR_DECL')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#constantConstructorSignature.
    def exitConstantConstructorSignature(
            self, ctx: Dart2Parser.ConstantConstructorSignatureContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#superclass.
    def enterSuperclass(self, ctx: Dart2Parser.SuperclassContext):
        pass

    # Exit a parse tree produced by Dart2Parser#superclass.
    def exitSuperclass(self, ctx: Dart2Parser.SuperclassContext):
        pass

    # Enter a parse tree produced by Dart2Parser#interfaces.
    def enterInterfaces(self, ctx: Dart2Parser.InterfacesContext):
        pass

    # Exit a parse tree produced by Dart2Parser#interfaces.
    def exitInterfaces(self, ctx: Dart2Parser.InterfacesContext):
        pass

    # Enter a parse tree produced by Dart2Parser#mixinApplicationClass.
    def enterMixinApplicationClass(
            self, ctx: Dart2Parser.MixinApplicationClassContext):
        pass

    # Exit a parse tree produced by Dart2Parser#mixinApplicationClass.
    def exitMixinApplicationClass(
            self, ctx: Dart2Parser.MixinApplicationClassContext):
        pass

    # Enter a parse tree produced by Dart2Parser#mixinApplication.
    def enterMixinApplication(
            self, ctx: Dart2Parser.MixinApplicationContext):
        pass

    # Exit a parse tree produced by Dart2Parser#mixinApplication.
    def exitMixinApplication(
            self, ctx: Dart2Parser.MixinApplicationContext):
        pass

    # Enter a parse tree produced by Dart2Parser#enumType.
    def enterEnumType(self, ctx: Dart2Parser.EnumTypeContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'ENUM_DECL')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#enumType.
    def exitEnumType(self, ctx: Dart2Parser.EnumTypeContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#enumEntry.
    def enterEnumEntry(self, ctx: Dart2Parser.EnumEntryContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'ENUM_BODY')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#enumEntry.
    def exitEnumEntry(self, ctx: Dart2Parser.EnumEntryContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#typeParameter.
    def enterTypeParameter(self, ctx: Dart2Parser.TypeParameterContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'TYPE_ARGUMENT')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#typeParameter.
    def exitTypeParameter(self, ctx: Dart2Parser.TypeParameterContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#typeParameters.
    def enterTypeParameters(self, ctx: Dart2Parser.TypeParametersContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'TYPE_ARGUMENT_LIST')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#typeParameters.
    def exitTypeParameters(self, ctx: Dart2Parser.TypeParametersContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#metadata.
    def enterMetadata(self, ctx: Dart2Parser.MetadataContext):
        pass

    # Exit a parse tree produced by Dart2Parser#metadata.
    def exitMetadata(self, ctx: Dart2Parser.MetadataContext):
        pass

    # Enter a parse tree produced by Dart2Parser#expression.
    def enterExpression(self, ctx: Dart2Parser.ExpressionContext):
        pass

    # Exit a parse tree produced by Dart2Parser#expression.
    def exitExpression(self, ctx: Dart2Parser.ExpressionContext):
        pass

    # Enter a parse tree produced by Dart2Parser#expressionWithoutCascade.
    def enterExpressionWithoutCascade(
            self, ctx: Dart2Parser.ExpressionWithoutCascadeContext):
        pass

    # Exit a parse tree produced by Dart2Parser#expressionWithoutCascade.
    def exitExpressionWithoutCascade(
            self, ctx: Dart2Parser.ExpressionWithoutCascadeContext):
        pass

    # Enter a parse tree produced by Dart2Parser#expressionList.
    def enterExpressionList(self, ctx: Dart2Parser.ExpressionListContext):
        pass

    # Exit a parse tree produced by Dart2Parser#expressionList.
    def exitExpressionList(self, ctx: Dart2Parser.ExpressionListContext):
        pass

    # Enter a parse tree produced by Dart2Parser#primary.
    def enterPrimary(self, ctx: Dart2Parser.PrimaryContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'ACCESS_OPERATOR')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#primary.
    def exitPrimary(self, ctx: Dart2Parser.PrimaryContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#literal.
    def enterLiteral(self, ctx: Dart2Parser.LiteralContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'LITERAL')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#literal.
    def exitLiteral(self, ctx: Dart2Parser.LiteralContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#nullLiteral.
    def enterNullLiteral(self, ctx: Dart2Parser.NullLiteralContext):
        pass

    # Exit a parse tree produced by Dart2Parser#nullLiteral.
    def exitNullLiteral(self, ctx: Dart2Parser.NullLiteralContext):
        pass

    # Enter a parse tree produced by Dart2Parser#numericLiteral.
    def enterNumericLiteral(self, ctx: Dart2Parser.NumericLiteralContext):
        pass

    # Exit a parse tree produced by Dart2Parser#numericLiteral.
    def exitNumericLiteral(self, ctx: Dart2Parser.NumericLiteralContext):
        pass

    # Enter a parse tree produced by Dart2Parser#booleanLiteral.
    def enterBooleanLiteral(self, ctx: Dart2Parser.BooleanLiteralContext):
        pass

    # Exit a parse tree produced by Dart2Parser#booleanLiteral.
    def exitBooleanLiteral(self, ctx: Dart2Parser.BooleanLiteralContext):
        pass

    # Enter a parse tree produced by Dart2Parser#stringLiteral.
    def enterStringLiteral(self, ctx: Dart2Parser.StringLiteralContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'STRING')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#stringLiteral.
    def exitStringLiteral(self, ctx: Dart2Parser.StringLiteralContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#stringInterpolation.
    def enterStringInterpolation(
            self, ctx: Dart2Parser.StringInterpolationContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'STRING')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#stringInterpolation.
    def exitStringInterpolation(
            self, ctx: Dart2Parser.StringInterpolationContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#symbolLiteral.
    def enterSymbolLiteral(self, ctx: Dart2Parser.SymbolLiteralContext):
        pass

    # Exit a parse tree produced by Dart2Parser#symbolLiteral.
    def exitSymbolLiteral(self, ctx: Dart2Parser.SymbolLiteralContext):
        pass

    # Enter a parse tree produced by Dart2Parser#listLiteral.
    def enterListLiteral(self, ctx: Dart2Parser.ListLiteralContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'COLLECTION')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#listLiteral.
    def exitListLiteral(self, ctx: Dart2Parser.ListLiteralContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#mapLiteral.
    def enterMapLiteral(self, ctx: Dart2Parser.MapLiteralContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'COLLECTION')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#mapLiteral.
    def exitMapLiteral(self, ctx: Dart2Parser.MapLiteralContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#mapLiteralEntry.
    def enterMapLiteralEntry(self, ctx: Dart2Parser.MapLiteralEntryContext):
        pass

    # Exit a parse tree produced by Dart2Parser#mapLiteralEntry.
    def exitMapLiteralEntry(self, ctx: Dart2Parser.MapLiteralEntryContext):
        pass

    # Enter a parse tree produced by Dart2Parser#throwExpression.
    def enterThrowExpression(self, ctx: Dart2Parser.ThrowExpressionContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'THROW')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#throwExpression.
    def exitThrowExpression(self, ctx: Dart2Parser.ThrowExpressionContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#throwExpressionWithoutCascade.
    def enterThrowExpressionWithoutCascade(
            self, ctx: Dart2Parser.ThrowExpressionWithoutCascadeContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'THROW')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#throwExpressionWithoutCascade.
    def exitThrowExpressionWithoutCascade(
            self, ctx: Dart2Parser.ThrowExpressionWithoutCascadeContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#functionExpression.
    def enterFunctionExpression(
            self, ctx: Dart2Parser.FunctionExpressionContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'FUNCTION_DECL')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#functionExpression.
    def exitFunctionExpression(
            self, ctx: Dart2Parser.FunctionExpressionContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#thisExpression.
    def enterThisExpression(self, ctx: Dart2Parser.ThisExpressionContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'THIS')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#thisExpression.
    def exitThisExpression(self, ctx: Dart2Parser.ThisExpressionContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#nayaExpression.
    def enterNayaExpression(self, ctx: Dart2Parser.NayaExpressionContext):
        pass

    # Exit a parse tree produced by Dart2Parser#nayaExpression.
    def exitNayaExpression(self, ctx: Dart2Parser.NayaExpressionContext):
        pass

    # Enter a parse tree produced by Dart2Parser#constObjectExpression.
    def enterConstObjectExpression(
            self, ctx: Dart2Parser.ConstObjectExpressionContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'CONSTRUCTOR_CALL')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#constObjectExpression.
    def exitConstObjectExpression(
            self, ctx: Dart2Parser.ConstObjectExpressionContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#arguments.
    def enterArguments(self, ctx: Dart2Parser.ArgumentsContext):
        pass

    # Exit a parse tree produced by Dart2Parser#arguments.
    def exitArguments(self, ctx: Dart2Parser.ArgumentsContext):
        pass

    # Enter a parse tree produced by Dart2Parser#argumentList.
    def enterArgumentList(self, ctx: Dart2Parser.ArgumentListContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'VALUE_ARGUMENT_LIST')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#argumentList.
    def exitArgumentList(self, ctx: Dart2Parser.ArgumentListContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#namedArgument.
    def enterNamedArgument(self, ctx: Dart2Parser.NamedArgumentContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'VALUE_ARGUMENT')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#namedArgument.
    def exitNamedArgument(self, ctx: Dart2Parser.NamedArgumentContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#cascadeSection.
    def enterCascadeSection(self, ctx: Dart2Parser.CascadeSectionContext):
        pass

    # Exit a parse tree produced by Dart2Parser#cascadeSection.
    def exitCascadeSection(self, ctx: Dart2Parser.CascadeSectionContext):
        pass

    # Enter a parse tree produced by Dart2Parser#cascadeSelector.
    def enterCascadeSelector(self, ctx: Dart2Parser.CascadeSelectorContext):
        pass

    # Exit a parse tree produced by Dart2Parser#cascadeSelector.
    def exitCascadeSelector(self, ctx: Dart2Parser.CascadeSelectorContext):
        pass

    # Enter a parse tree produced by Dart2Parser#argumentPart.
    def enterArgumentPart(self, ctx: Dart2Parser.ArgumentPartContext):
        pass

    # Exit a parse tree produced by Dart2Parser#argumentPart.
    def exitArgumentPart(self, ctx: Dart2Parser.ArgumentPartContext):
        pass

    # Enter a parse tree produced by Dart2Parser#assignmentOperator.
    def enterAssignmentOperator(
            self, ctx: Dart2Parser.AssignmentOperatorContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'ASSIGNMENT_OPERATOR')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#assignmentOperator.
    def exitAssignmentOperator(
            self, ctx: Dart2Parser.AssignmentOperatorContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#compoundAssignmentOperator.
    def enterCompoundAssignmentOperator(
            self, ctx: Dart2Parser.CompoundAssignmentOperatorContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'PREFIX')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#compoundAssignmentOperator.
    def exitCompoundAssignmentOperator(
            self, ctx: Dart2Parser.CompoundAssignmentOperatorContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#conditionalExpression.
    def enterConditionalExpression(
            self, ctx: Dart2Parser.ConditionalExpressionContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'TERNARY')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#conditionalExpression.
    def exitConditionalExpression(
            self, ctx: Dart2Parser.ConditionalExpressionContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#ifNullExpression.
    def enterIfNullExpression(self, ctx: Dart2Parser.IfNullExpressionContext):
        pass

    # Exit a parse tree produced by Dart2Parser#ifNullExpression.
    def exitIfNullExpression(self, ctx: Dart2Parser.IfNullExpressionContext):
        pass

    # Enter a parse tree produced by Dart2Parser#logicalOrExpression.
    def enterLogicalOrExpression(
            self, ctx: Dart2Parser.LogicalOrExpressionContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'OR')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#logicalOrExpression.
    def exitLogicalOrExpression(
            self, ctx: Dart2Parser.LogicalOrExpressionContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#logicalAndExpression.
    def enterLogicalAndExpression(
            self, ctx: Dart2Parser.LogicalAndExpressionContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'AND')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#logicalAndExpression.
    def exitLogicalAndExpression(
            self, ctx: Dart2Parser.LogicalAndExpressionContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#equalityExpression.
    def enterEqualityExpression(
            self, ctx: Dart2Parser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by Dart2Parser#equalityExpression.
    def exitEqualityExpression(
            self, ctx: Dart2Parser.EqualityExpressionContext):
        pass

    # Enter a parse tree produced by Dart2Parser#equalityOperator.
    def enterEqualityOperator(self, ctx: Dart2Parser.EqualityOperatorContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'EQUALITY_OPERATOR')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#equalityOperator.
    def exitEqualityOperator(self, ctx: Dart2Parser.EqualityOperatorContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#relationalExpression.
    def enterRelationalExpression(
            self, ctx: Dart2Parser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by Dart2Parser#relationalExpression.
    def exitRelationalExpression(
            self, ctx: Dart2Parser.RelationalExpressionContext):
        pass

    # Enter a parse tree produced by Dart2Parser#relationalOperator.
    def enterRelationalOperator(
            self, ctx: Dart2Parser.RelationalOperatorContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'COMPARISON_OPERATOR')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#relationalOperator.
    def exitRelationalOperator(
            self, ctx: Dart2Parser.RelationalOperatorContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#bitwiseOrExpression.
    def enterBitwiseOrExpression(
            self, ctx: Dart2Parser.BitwiseOrExpressionContext):
        pass

    # Exit a parse tree produced by Dart2Parser#bitwiseOrExpression.
    def exitBitwiseOrExpression(
            self, ctx: Dart2Parser.BitwiseOrExpressionContext):
        pass

    # Enter a parse tree produced by Dart2Parser#bitwiseXorExpression.
    def enterBitwiseXorExpression(
            self, ctx: Dart2Parser.BitwiseXorExpressionContext):
        pass

    # Exit a parse tree produced by Dart2Parser#bitwiseXorExpression.
    def exitBitwiseXorExpression(
            self, ctx: Dart2Parser.BitwiseXorExpressionContext):
        pass

    # Enter a parse tree produced by Dart2Parser#bitwiseAndExpression.
    def enterBitwiseAndExpression(
            self, ctx: Dart2Parser.BitwiseAndExpressionContext):
        pass

    # Exit a parse tree produced by Dart2Parser#bitwiseAndExpression.
    def exitBitwiseAndExpression(
            self, ctx: Dart2Parser.BitwiseAndExpressionContext):
        pass

    # Enter a parse tree produced by Dart2Parser#bitwiseOperator.
    def enterBitwiseOperator(self, ctx: Dart2Parser.BitwiseOperatorContext):
        pass

    # Exit a parse tree produced by Dart2Parser#bitwiseOperator.
    def exitBitwiseOperator(self, ctx: Dart2Parser.BitwiseOperatorContext):
        pass

    # Enter a parse tree produced by Dart2Parser#shiftExpression.
    def enterShiftExpression(self, ctx: Dart2Parser.ShiftExpressionContext):
        pass

    # Exit a parse tree produced by Dart2Parser#shiftExpression.
    def exitShiftExpression(self, ctx: Dart2Parser.ShiftExpressionContext):
        pass

    # Enter a parse tree produced by Dart2Parser#shiftOperator.
    def enterShiftOperator(self, ctx: Dart2Parser.ShiftOperatorContext):
        pass

    # Exit a parse tree produced by Dart2Parser#shiftOperator.
    def exitShiftOperator(self, ctx: Dart2Parser.ShiftOperatorContext):
        pass

    # Enter a parse tree produced by Dart2Parser#additiveExpression.
    def enterAdditiveExpression(
            self, ctx: Dart2Parser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by Dart2Parser#additiveExpression.
    def exitAdditiveExpression(
            self, ctx: Dart2Parser.AdditiveExpressionContext):
        pass

    # Enter a parse tree produced by Dart2Parser#additiveOperator.
    def enterAdditiveOperator(self, ctx: Dart2Parser.AdditiveOperatorContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'ADDITIVE_OPERATOR')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#additiveOperator.
    def exitAdditiveOperator(self, ctx: Dart2Parser.AdditiveOperatorContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#multiplicativeExpression.
    def enterMultiplicativeExpression(
            self, ctx: Dart2Parser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by Dart2Parser#multiplicativeExpression.
    def exitMultiplicativeExpression(
            self, ctx: Dart2Parser.MultiplicativeExpressionContext):
        pass

    # Enter a parse tree produced by Dart2Parser#multiplicativeOperator.
    def enterMultiplicativeOperator(
            self, ctx: Dart2Parser.MultiplicativeOperatorContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'MULTIPLICATIVE_OPERATOR')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#multiplicativeOperator.
    def exitMultiplicativeOperator(
            self, ctx: Dart2Parser.MultiplicativeOperatorContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#unaryExpression.
    def enterUnaryExpression(self, ctx: Dart2Parser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by Dart2Parser#unaryExpression.
    def exitUnaryExpression(self, ctx: Dart2Parser.UnaryExpressionContext):
        pass

    # Enter a parse tree produced by Dart2Parser#prefixOperator.
    def enterPrefixOperator(self, ctx: Dart2Parser.PrefixOperatorContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'PREFIX')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#prefixOperator.
    def exitPrefixOperator(self, ctx: Dart2Parser.PrefixOperatorContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#minusOperator.
    def enterMinusOperator(self, ctx: Dart2Parser.MinusOperatorContext):
        # TODO: add minus operator to the tree
        pass

    # Exit a parse tree produced by Dart2Parser#minusOperator.
    def exitMinusOperator(self, ctx: Dart2Parser.MinusOperatorContext):
        pass

    # Enter a parse tree produced by Dart2Parser#negationOperator.
    def enterNegationOperator(self, ctx: Dart2Parser.NegationOperatorContext):
        # TODO: add negation operator to the tree
        pass

    # Exit a parse tree produced by Dart2Parser#negationOperator.
    def exitNegationOperator(self, ctx: Dart2Parser.NegationOperatorContext):
        pass

    # Enter a parse tree produced by Dart2Parser#tildeOperator.
    def enterTildeOperator(self, ctx: Dart2Parser.TildeOperatorContext):
        # TODO: add tilde operator to the tree
        pass

    # Exit a parse tree produced by Dart2Parser#tildeOperator.
    def exitTildeOperator(self, ctx: Dart2Parser.TildeOperatorContext):
        pass

    # Enter a parse tree produced by Dart2Parser#awaitExpression.
    def enterAwaitExpression(self, ctx: Dart2Parser.AwaitExpressionContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'AWAIT_EXPRESSION')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#awaitExpression.
    def exitAwaitExpression(self, ctx: Dart2Parser.AwaitExpressionContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#postfixExpression.
    def enterPostfixExpression(
            self, ctx: Dart2Parser.PostfixExpressionContext):
        pass

    # Exit a parse tree produced by Dart2Parser#postfixExpression.
    def exitPostfixExpression(self, ctx: Dart2Parser.PostfixExpressionContext):
        pass

    # Enter a parse tree produced by Dart2Parser#postfixOperator.
    def enterPostfixOperator(self, ctx: Dart2Parser.PostfixOperatorContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'POSFIX')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#postfixOperator.
    def exitPostfixOperator(self, ctx: Dart2Parser.PostfixOperatorContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#selector.
    def enterSelector(self, ctx: Dart2Parser.SelectorContext):
        pass

    # Exit a parse tree produced by Dart2Parser#selector.
    def exitSelector(self, ctx: Dart2Parser.SelectorContext):
        pass

    # Enter a parse tree produced by Dart2Parser#incrementOperator.
    def enterIncrementOperator(
            self, ctx: Dart2Parser.IncrementOperatorContext):
        # TODO: add increment operator ++, --
        pass

    # Exit a parse tree produced by Dart2Parser#incrementOperator.
    def exitIncrementOperator(self, ctx: Dart2Parser.IncrementOperatorContext):
        pass

    # Enter a parse tree produced by Dart2Parser#assignableExpression.
    def enterAssignableExpression(
            self, ctx: Dart2Parser.AssignableExpressionContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'ASSIGNMENT_OPERATOR')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#assignableExpression.
    def exitAssignableExpression(
            self, ctx: Dart2Parser.AssignableExpressionContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by
    # Dart2Parser#unconditionalAssignableSelector.
    def enterUnconditionalAssignableSelector(
            self, ctx: Dart2Parser.UnconditionalAssignableSelectorContext):
        pass

    # Exit a parse tree produced by
    # Dart2Parser#unconditionalAssignableSelector.
    def exitUnconditionalAssignableSelector(
            self, ctx: Dart2Parser.UnconditionalAssignableSelectorContext):
        pass

    # Enter a parse tree produced by Dart2Parser#assignableSelector.
    def enterAssignableSelector(
            self, ctx: Dart2Parser.AssignableSelectorContext):
        pass

    # Exit a parse tree produced by Dart2Parser#assignableSelector.
    def exitAssignableSelector(
            self, ctx: Dart2Parser.AssignableSelectorContext):
        pass

    # Enter a parse tree produced by Dart2Parser#identifier.
    def enterIdentifier(self, ctx: Dart2Parser.IdentifierContext):
        token = ctx.IDENTIFIER().symbol
        act_token = ShortToken(token.text, token.line, token.column)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'LITERAL')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#identifier.
    def exitIdentifier(self, ctx: Dart2Parser.IdentifierContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#qualified.
    def enterQualified(self, ctx: Dart2Parser.QualifiedContext):
        pass

    # Exit a parse tree produced by Dart2Parser#qualified.
    def exitQualified(self, ctx: Dart2Parser.QualifiedContext):
        pass

    # Enter a parse tree produced by Dart2Parser#typeTest.
    def enterTypeTest(self, ctx: Dart2Parser.TypeTestContext):
        pass

    # Exit a parse tree produced by Dart2Parser#typeTest.
    def exitTypeTest(self, ctx: Dart2Parser.TypeTestContext):
        pass

    # Enter a parse tree produced by Dart2Parser#isOperator.
    def enterIsOperator(self, ctx: Dart2Parser.IsOperatorContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'IS_TYPE')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#isOperator.
    def exitIsOperator(self, ctx: Dart2Parser.IsOperatorContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#typeCast.
    def enterTypeCast(self, ctx: Dart2Parser.TypeCastContext):
        pass

    # Exit a parse tree produced by Dart2Parser#typeCast.
    def exitTypeCast(self, ctx: Dart2Parser.TypeCastContext):
        pass

    # Enter a parse tree produced by Dart2Parser#asOperator.
    def enterAsOperator(self, ctx: Dart2Parser.AsOperatorContext):
        pass

    # Exit a parse tree produced by Dart2Parser#asOperator.
    def exitAsOperator(self, ctx: Dart2Parser.AsOperatorContext):
        pass

    # Enter a parse tree produced by Dart2Parser#statements.
    def enterStatements(self, ctx: Dart2Parser.StatementsContext):
        pass

    # Exit a parse tree produced by Dart2Parser#statements.
    def exitStatements(self, ctx: Dart2Parser.StatementsContext):
        pass

    # Enter a parse tree produced by Dart2Parser#statement.
    def enterStatement(self, ctx: Dart2Parser.StatementContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'EXPRESSION')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#statement.
    def exitStatement(self, ctx: Dart2Parser.StatementContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#nonLabledStatment.
    def enterNonLabledStatment(
            self, ctx: Dart2Parser.NonLabledStatmentContext):
        pass

    # Exit a parse tree produced by Dart2Parser#nonLabledStatment.
    def exitNonLabledStatment(
            self, ctx: Dart2Parser.NonLabledStatmentContext):
        pass

    # Enter a parse tree produced by Dart2Parser#expressionStatement.
    def enterExpressionStatement(
            self, ctx: Dart2Parser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by Dart2Parser#expressionStatement.
    def exitExpressionStatement(
            self, ctx: Dart2Parser.ExpressionStatementContext):
        pass

    # Enter a parse tree produced by Dart2Parser#localVariableDeclaration.
    def enterLocalVariableDeclaration(
            self, ctx: Dart2Parser.LocalVariableDeclarationContext):
        pass

    # Exit a parse tree produced by Dart2Parser#localVariableDeclaration.
    def exitLocalVariableDeclaration(
            self, ctx: Dart2Parser.LocalVariableDeclarationContext):
        pass

    # Enter a parse tree produced by Dart2Parser#localFunctionDeclaration.
    def enterLocalFunctionDeclaration(
            self, ctx: Dart2Parser.LocalFunctionDeclarationContext):
        pass

    # Exit a parse tree produced by Dart2Parser#localFunctionDeclaration.
    def exitLocalFunctionDeclaration(
            self, ctx: Dart2Parser.LocalFunctionDeclarationContext):
        pass

    # Enter a parse tree produced by Dart2Parser#ifStatement.
    def enterIfStatement(self, ctx: Dart2Parser.IfStatementContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'CONDITION')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#ifStatement.
    def exitIfStatement(self, ctx: Dart2Parser.IfStatementContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#forStatement.
    def enterForStatement(self, ctx: Dart2Parser.ForStatementContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'LOOP_STATEMENT')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#forStatement.
    def exitForStatement(self, ctx: Dart2Parser.ForStatementContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#forLoopParts.
    def enterForLoopParts(self, ctx: Dart2Parser.ForLoopPartsContext):
        pass

    # Exit a parse tree produced by Dart2Parser#forLoopParts.
    def exitForLoopParts(self, ctx: Dart2Parser.ForLoopPartsContext):
        pass

    # Enter a parse tree produced by Dart2Parser#forInitializerStatement.
    def enterForInitializerStatement(
            self, ctx: Dart2Parser.ForInitializerStatementContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'VARIABLE_DECL')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#forInitializerStatement.
    def exitForInitializerStatement(
            self, ctx: Dart2Parser.ForInitializerStatementContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#whileStatement.
    def enterWhileStatement(self, ctx: Dart2Parser.WhileStatementContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'LOOP_STATEMENT')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#whileStatement.
    def exitWhileStatement(self, ctx: Dart2Parser.WhileStatementContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#doStatement.
    def enterDoStatement(self, ctx: Dart2Parser.DoStatementContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'LOOP_STATEMENT')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#doStatement.
    def exitDoStatement(self, ctx: Dart2Parser.DoStatementContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#switchStatement.
    def enterSwitchStatement(self, ctx: Dart2Parser.SwitchStatementContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'CONDITION')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#switchStatement.
    def exitSwitchStatement(self, ctx: Dart2Parser.SwitchStatementContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#switchCase.
    def enterSwitchCase(self, ctx: Dart2Parser.SwitchCaseContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'BODY')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#switchCase.
    def exitSwitchCase(self, ctx: Dart2Parser.SwitchCaseContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#defaultCase.
    def enterDefaultCase(self, ctx: Dart2Parser.DefaultCaseContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'BODY')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#defaultCase.
    def exitDefaultCase(self, ctx: Dart2Parser.DefaultCaseContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#rethrowStatment.
    def enterRethrowStatment(self, ctx: Dart2Parser.RethrowStatmentContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'THROW')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#rethrowStatment.
    def exitRethrowStatment(self, ctx: Dart2Parser.RethrowStatmentContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#tryStatement.
    def enterTryStatement(self, ctx: Dart2Parser.TryStatementContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'TRY')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#tryStatement.
    def exitTryStatement(self, ctx: Dart2Parser.TryStatementContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#onPart.
    def enterOnPart(self, ctx: Dart2Parser.OnPartContext):
        pass

    # Exit a parse tree produced by Dart2Parser#onPart.
    def exitOnPart(self, ctx: Dart2Parser.OnPartContext):
        pass

    # Enter a parse tree produced by Dart2Parser#catchPart.
    def enterCatchPart(self, ctx: Dart2Parser.CatchPartContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'CATCH')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#catchPart.
    def exitCatchPart(self, ctx: Dart2Parser.CatchPartContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#finallyPart.
    def enterFinallyPart(self, ctx: Dart2Parser.FinallyPartContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'FINALLY')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#finallyPart.
    def exitFinallyPart(self, ctx: Dart2Parser.FinallyPartContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#returnStatement.
    def enterReturnStatement(self, ctx: Dart2Parser.ReturnStatementContext):
        act_token = ShortToken('return', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'JUMP_STATEMENT')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#returnStatement.
    def exitReturnStatement(self, ctx: Dart2Parser.ReturnStatementContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#label.
    def enterLabel(self, ctx: Dart2Parser.LabelContext):
        pass

    # Exit a parse tree produced by Dart2Parser#label.
    def exitLabel(self, ctx: Dart2Parser.LabelContext):
        pass

    # Enter a parse tree produced by Dart2Parser#breakStatement.
    def enterBreakStatement(self, ctx: Dart2Parser.BreakStatementContext):
        act_token = ShortToken('break', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'JUMP_STATEMENT')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#breakStatement.
    def exitBreakStatement(self, ctx: Dart2Parser.BreakStatementContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#continueStatement.
    def enterContinueStatement(
            self, ctx: Dart2Parser.ContinueStatementContext):
        act_token = ShortToken('continue', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'JUMP_STATEMENT')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#continueStatement.
    def exitContinueStatement(self, ctx: Dart2Parser.ContinueStatementContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#yieldStatement.
    def enterYieldStatement(self, ctx: Dart2Parser.YieldStatementContext):
        pass

    # Exit a parse tree produced by Dart2Parser#yieldStatement.
    def exitYieldStatement(self, ctx: Dart2Parser.YieldStatementContext):
        pass

    # Enter a parse tree produced by Dart2Parser#yieldEachStatement.
    def enterYieldEachStatement(
            self, ctx: Dart2Parser.YieldEachStatementContext):
        pass

    # Exit a parse tree produced by Dart2Parser#yieldEachStatement.
    def exitYieldEachStatement(
            self, ctx: Dart2Parser.YieldEachStatementContext):
        pass

    # Enter a parse tree produced by Dart2Parser#assertStatement.
    def enterAssertStatement(self, ctx: Dart2Parser.AssertStatementContext):
        pass

    # Exit a parse tree produced by Dart2Parser#assertStatement.
    def exitAssertStatement(self, ctx: Dart2Parser.AssertStatementContext):
        pass

    # Enter a parse tree produced by Dart2Parser#assertion.
    def enterAssertion(self, ctx: Dart2Parser.AssertionContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'ASSERT')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#assertion.
    def exitAssertion(self, ctx: Dart2Parser.AssertionContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#topLevelDefinition.
    def enterTopLevelDefinition(
            self, ctx: Dart2Parser.TopLevelDefinitionContext):
        pass

    # Exit a parse tree produced by Dart2Parser#topLevelDefinition.
    def exitTopLevelDefinition(
            self, ctx: Dart2Parser.TopLevelDefinitionContext):
        pass

    # Enter a parse tree produced by Dart2Parser#getOrSet.
    def enterGetOrSet(self, ctx: Dart2Parser.GetOrSetContext):
        pass

    # Exit a parse tree produced by Dart2Parser#getOrSet.
    def exitGetOrSet(self, ctx: Dart2Parser.GetOrSetContext):
        pass

    # Enter a parse tree produced by Dart2Parser#libraryDefinition.
    def enterLibraryDefinition(
            self, ctx: Dart2Parser.LibraryDefinitionContext):
        pass

    # Exit a parse tree produced by Dart2Parser#libraryDefinition.
    def exitLibraryDefinition(self, ctx: Dart2Parser.LibraryDefinitionContext):
        pass

    # Enter a parse tree produced by Dart2Parser#scriptTag.
    def enterScriptTag(self, ctx: Dart2Parser.ScriptTagContext):
        pass

    # Exit a parse tree produced by Dart2Parser#scriptTag.
    def exitScriptTag(self, ctx: Dart2Parser.ScriptTagContext):
        pass

    # Enter a parse tree produced by Dart2Parser#libraryName.
    def enterLibraryName(self, ctx: Dart2Parser.LibraryNameContext):
        pass

    # Exit a parse tree produced by Dart2Parser#libraryName.
    def exitLibraryName(self, ctx: Dart2Parser.LibraryNameContext):
        pass

    # Enter a parse tree produced by Dart2Parser#importOrExport.
    def enterImportOrExport(self, ctx: Dart2Parser.ImportOrExportContext):
        pass

    # Exit a parse tree produced by Dart2Parser#importOrExport.
    def exitImportOrExport(self, ctx: Dart2Parser.ImportOrExportContext):
        pass

    # Enter a parse tree produced by Dart2Parser#dottedIdentifierList.
    def enterDottedIdentifierList(
            self, ctx: Dart2Parser.DottedIdentifierListContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'ACCESS_OPERATOR')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#dottedIdentifierList.
    def exitDottedIdentifierList(
            self, ctx: Dart2Parser.DottedIdentifierListContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#libraryimport.
    def enterLibraryimport(self, ctx: Dart2Parser.LibraryimportContext):
        pass

    # Exit a parse tree produced by Dart2Parser#libraryimport.
    def exitLibraryimport(self, ctx: Dart2Parser.LibraryimportContext):
        pass

    # Enter a parse tree produced by Dart2Parser#importSpecification.
    def enterImportSpecification(
            self, ctx: Dart2Parser.ImportSpecificationContext):
        pass

    # Exit a parse tree produced by Dart2Parser#importSpecification.
    def exitImportSpecification(
            self, ctx: Dart2Parser.ImportSpecificationContext):
        pass

    # Enter a parse tree produced by Dart2Parser#combinator.
    def enterCombinator(self, ctx: Dart2Parser.CombinatorContext):
        pass

    # Exit a parse tree produced by Dart2Parser#combinator.
    def exitCombinator(self, ctx: Dart2Parser.CombinatorContext):
        pass

    # Enter a parse tree produced by Dart2Parser#identifierList.
    def enterIdentifierList(self, ctx: Dart2Parser.IdentifierListContext):
        pass

    # Exit a parse tree produced by Dart2Parser#identifierList.
    def exitIdentifierList(self, ctx: Dart2Parser.IdentifierListContext):
        pass

    # Enter a parse tree produced by Dart2Parser#libraryExport.
    def enterLibraryExport(self, ctx: Dart2Parser.LibraryExportContext):
        pass

    # Exit a parse tree produced by Dart2Parser#libraryExport.
    def exitLibraryExport(self, ctx: Dart2Parser.LibraryExportContext):
        pass

    # Enter a parse tree produced by Dart2Parser#partDirective.
    def enterPartDirective(self, ctx: Dart2Parser.PartDirectiveContext):
        pass

    # Exit a parse tree produced by Dart2Parser#partDirective.
    def exitPartDirective(self, ctx: Dart2Parser.PartDirectiveContext):
        pass

    # Enter a parse tree produced by Dart2Parser#partHeader.
    def enterPartHeader(self, ctx: Dart2Parser.PartHeaderContext):
        pass

    # Exit a parse tree produced by Dart2Parser#partHeader.
    def exitPartHeader(self, ctx: Dart2Parser.PartHeaderContext):
        pass

    # Enter a parse tree produced by Dart2Parser#partDeclaration.
    def enterPartDeclaration(self, ctx: Dart2Parser.PartDeclarationContext):
        pass

    # Exit a parse tree produced by Dart2Parser#partDeclaration.
    def exitPartDeclaration(self, ctx: Dart2Parser.PartDeclarationContext):
        pass

    # Enter a parse tree produced by Dart2Parser#uri.
    def enterUri(self, ctx: Dart2Parser.UriContext):
        pass

    # Exit a parse tree produced by Dart2Parser#uri.
    def exitUri(self, ctx: Dart2Parser.UriContext):
        pass

    # Enter a parse tree produced by Dart2Parser#configurableUri.
    def enterConfigurableUri(self, ctx: Dart2Parser.ConfigurableUriContext):
        pass

    # Exit a parse tree produced by Dart2Parser#configurableUri.
    def exitConfigurableUri(self, ctx: Dart2Parser.ConfigurableUriContext):
        pass

    # Enter a parse tree produced by Dart2Parser#configurationUri.
    def enterConfigurationUri(self, ctx: Dart2Parser.ConfigurationUriContext):
        pass

    # Exit a parse tree produced by Dart2Parser#configurationUri.
    def exitConfigurationUri(self, ctx: Dart2Parser.ConfigurationUriContext):
        pass

    # Enter a parse tree produced by Dart2Parser#uriTest.
    def enterUriTest(self, ctx: Dart2Parser.UriTestContext):
        pass

    # Exit a parse tree produced by Dart2Parser#uriTest.
    def exitUriTest(self, ctx: Dart2Parser.UriTestContext):
        pass

    # Enter a parse tree produced by Dart2Parser#dtype.
    def enterDtype(self, ctx: Dart2Parser.DtypeContext):
        pass

    # Exit a parse tree produced by Dart2Parser#dtype.
    def exitDtype(self, ctx: Dart2Parser.DtypeContext):
        pass

    # Enter a parse tree produced by Dart2Parser#typeName.
    def enterTypeName(self, ctx: Dart2Parser.TypeNameContext):
        pass

    # Exit a parse tree produced by Dart2Parser#typeName.
    def exitTypeName(self, ctx: Dart2Parser.TypeNameContext):
        pass

    # Enter a parse tree produced by Dart2Parser#typeArguments.
    def enterTypeArguments(self, ctx: Dart2Parser.TypeArgumentsContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'TYPE_ARGUMENT_LIST')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#typeArguments.
    def exitTypeArguments(self, ctx: Dart2Parser.TypeArgumentsContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#typeList.
    def enterTypeList(self, ctx: Dart2Parser.TypeListContext):
        pass

    # Exit a parse tree produced by Dart2Parser#typeList.
    def exitTypeList(self, ctx: Dart2Parser.TypeListContext):
        pass

    # Enter a parse tree produced by Dart2Parser#typeAlias.
    def enterTypeAlias(self, ctx: Dart2Parser.TypeAliasContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'TYPE_ALIAS')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#typeAlias.
    def exitTypeAlias(self, ctx: Dart2Parser.TypeAliasContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#typeAliasBody.
    def enterTypeAliasBody(self, ctx: Dart2Parser.TypeAliasBodyContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'BODY')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by Dart2Parser#typeAliasBody.
    def exitTypeAliasBody(self, ctx: Dart2Parser.TypeAliasBodyContext):
        self.current_node = self.current_node.parent

    # Enter a parse tree produced by Dart2Parser#functionTypeAlias.
    def enterFunctionTypeAlias(self, ctx: Dart2Parser.FunctionTypeAliasContext):
        pass

    # Exit a parse tree produced by Dart2Parser#functionTypeAlias.
    def exitFunctionTypeAlias(self, ctx: Dart2Parser.FunctionTypeAliasContext):
        pass

    # Enter a parse tree produced by Dart2Parser#functionPrefix.
    def enterFunctionPrefix(self, ctx: Dart2Parser.FunctionPrefixContext):
        pass

    # Exit a parse tree produced by Dart2Parser#functionPrefix.
    def exitFunctionPrefix(self, ctx: Dart2Parser.FunctionPrefixContext):
        pass
