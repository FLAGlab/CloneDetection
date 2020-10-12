# Generated from ../clone_detection/grammars/swift/Swift3.g4 by ANTLR 4.7.1
from antlr4 import *
from .Swift3Parser import Swift3Parser

from clone_detection.grammars.grammars_registry import VISITORS


# This class defines a complete generic visitor for a parse tree produced by Swift3Parser.
@VISITORS.register('swift')
class Swift3Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by Swift3Parser#top_level.
    def visitTop_level(self, ctx:Swift3Parser.Top_levelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#statement.
    def visitStatement(self, ctx:Swift3Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#statements.
    def visitStatements(self, ctx:Swift3Parser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#statements_impl.
    def visitStatements_impl(self, ctx:Swift3Parser.Statements_implContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#loop_statement.
    def visitLoop_statement(self, ctx:Swift3Parser.Loop_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#for_statement.
    def visitFor_statement(self, ctx:Swift3Parser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#for_init.
    def visitFor_init(self, ctx:Swift3Parser.For_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#for_in_statement.
    def visitFor_in_statement(self, ctx:Swift3Parser.For_in_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#while_statement.
    def visitWhile_statement(self, ctx:Swift3Parser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#condition_list.
    def visitCondition_list(self, ctx:Swift3Parser.Condition_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#condition.
    def visitCondition(self, ctx:Swift3Parser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#case_condition.
    def visitCase_condition(self, ctx:Swift3Parser.Case_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#optional_binding_condition.
    def visitOptional_binding_condition(self, ctx:Swift3Parser.Optional_binding_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#repeat_while_statement.
    def visitRepeat_while_statement(self, ctx:Swift3Parser.Repeat_while_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#branch_statement.
    def visitBranch_statement(self, ctx:Swift3Parser.Branch_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#if_statement.
    def visitIf_statement(self, ctx:Swift3Parser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#else_clause.
    def visitElse_clause(self, ctx:Swift3Parser.Else_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#guard_statement.
    def visitGuard_statement(self, ctx:Swift3Parser.Guard_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#switch_statement.
    def visitSwitch_statement(self, ctx:Swift3Parser.Switch_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#switch_cases.
    def visitSwitch_cases(self, ctx:Swift3Parser.Switch_casesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#switch_case.
    def visitSwitch_case(self, ctx:Swift3Parser.Switch_caseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#case_label.
    def visitCase_label(self, ctx:Swift3Parser.Case_labelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#case_item_list.
    def visitCase_item_list(self, ctx:Swift3Parser.Case_item_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#default_label.
    def visitDefault_label(self, ctx:Swift3Parser.Default_labelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#where_clause.
    def visitWhere_clause(self, ctx:Swift3Parser.Where_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#where_expression.
    def visitWhere_expression(self, ctx:Swift3Parser.Where_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#labeled_statement.
    def visitLabeled_statement(self, ctx:Swift3Parser.Labeled_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#statement_label.
    def visitStatement_label(self, ctx:Swift3Parser.Statement_labelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#label_name.
    def visitLabel_name(self, ctx:Swift3Parser.Label_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#control_transfer_statement.
    def visitControl_transfer_statement(self, ctx:Swift3Parser.Control_transfer_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#break_statement.
    def visitBreak_statement(self, ctx:Swift3Parser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#continue_statement.
    def visitContinue_statement(self, ctx:Swift3Parser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#fallthrough_statement.
    def visitFallthrough_statement(self, ctx:Swift3Parser.Fallthrough_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#return_statement.
    def visitReturn_statement(self, ctx:Swift3Parser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#throw_statement.
    def visitThrow_statement(self, ctx:Swift3Parser.Throw_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#defer_statement.
    def visitDefer_statement(self, ctx:Swift3Parser.Defer_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#do_statement.
    def visitDo_statement(self, ctx:Swift3Parser.Do_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#catch_clauses.
    def visitCatch_clauses(self, ctx:Swift3Parser.Catch_clausesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#catch_clause.
    def visitCatch_clause(self, ctx:Swift3Parser.Catch_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#compiler_control_statement.
    def visitCompiler_control_statement(self, ctx:Swift3Parser.Compiler_control_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#conditional_compilation_block.
    def visitConditional_compilation_block(self, ctx:Swift3Parser.Conditional_compilation_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#if_directive_clause.
    def visitIf_directive_clause(self, ctx:Swift3Parser.If_directive_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#elseif_directive_clauses.
    def visitElseif_directive_clauses(self, ctx:Swift3Parser.Elseif_directive_clausesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#elseif_directive_clause.
    def visitElseif_directive_clause(self, ctx:Swift3Parser.Elseif_directive_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#else_directive_clause.
    def visitElse_directive_clause(self, ctx:Swift3Parser.Else_directive_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#if_directive.
    def visitIf_directive(self, ctx:Swift3Parser.If_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#elseif_directive.
    def visitElseif_directive(self, ctx:Swift3Parser.Elseif_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#else_directive.
    def visitElse_directive(self, ctx:Swift3Parser.Else_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#endif_directive.
    def visitEndif_directive(self, ctx:Swift3Parser.Endif_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#compilation_condition.
    def visitCompilation_condition(self, ctx:Swift3Parser.Compilation_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#platform_condition.
    def visitPlatform_condition(self, ctx:Swift3Parser.Platform_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#swift_version.
    def visitSwift_version(self, ctx:Swift3Parser.Swift_versionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#operating_system.
    def visitOperating_system(self, ctx:Swift3Parser.Operating_systemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#architecture.
    def visitArchitecture(self, ctx:Swift3Parser.ArchitectureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#line_control_statement.
    def visitLine_control_statement(self, ctx:Swift3Parser.Line_control_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#line_number.
    def visitLine_number(self, ctx:Swift3Parser.Line_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#file_name.
    def visitFile_name(self, ctx:Swift3Parser.File_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#availability_condition.
    def visitAvailability_condition(self, ctx:Swift3Parser.Availability_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#availability_arguments.
    def visitAvailability_arguments(self, ctx:Swift3Parser.Availability_argumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#availability_argument.
    def visitAvailability_argument(self, ctx:Swift3Parser.Availability_argumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#generic_parameter_clause.
    def visitGeneric_parameter_clause(self, ctx:Swift3Parser.Generic_parameter_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#generic_parameter_list.
    def visitGeneric_parameter_list(self, ctx:Swift3Parser.Generic_parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#generic_parameter.
    def visitGeneric_parameter(self, ctx:Swift3Parser.Generic_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#generic_where_clause.
    def visitGeneric_where_clause(self, ctx:Swift3Parser.Generic_where_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#requirement_list.
    def visitRequirement_list(self, ctx:Swift3Parser.Requirement_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#requirement.
    def visitRequirement(self, ctx:Swift3Parser.RequirementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#conformance_requirement.
    def visitConformance_requirement(self, ctx:Swift3Parser.Conformance_requirementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#same_type_requirement.
    def visitSame_type_requirement(self, ctx:Swift3Parser.Same_type_requirementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#generic_argument_clause.
    def visitGeneric_argument_clause(self, ctx:Swift3Parser.Generic_argument_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#generic_argument_list.
    def visitGeneric_argument_list(self, ctx:Swift3Parser.Generic_argument_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#generic_argument.
    def visitGeneric_argument(self, ctx:Swift3Parser.Generic_argumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#declaration.
    def visitDeclaration(self, ctx:Swift3Parser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#declarations.
    def visitDeclarations(self, ctx:Swift3Parser.DeclarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#top_level_declaration.
    def visitTop_level_declaration(self, ctx:Swift3Parser.Top_level_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#code_block.
    def visitCode_block(self, ctx:Swift3Parser.Code_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#import_declaration.
    def visitImport_declaration(self, ctx:Swift3Parser.Import_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#import_kind.
    def visitImport_kind(self, ctx:Swift3Parser.Import_kindContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#import_path.
    def visitImport_path(self, ctx:Swift3Parser.Import_pathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#import_path_identifier.
    def visitImport_path_identifier(self, ctx:Swift3Parser.Import_path_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#constant_declaration.
    def visitConstant_declaration(self, ctx:Swift3Parser.Constant_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#pattern_initializer_list.
    def visitPattern_initializer_list(self, ctx:Swift3Parser.Pattern_initializer_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#pattern_initializer.
    def visitPattern_initializer(self, ctx:Swift3Parser.Pattern_initializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#initializer.
    def visitInitializer(self, ctx:Swift3Parser.InitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#variable_declaration.
    def visitVariable_declaration(self, ctx:Swift3Parser.Variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#variable_declaration_head.
    def visitVariable_declaration_head(self, ctx:Swift3Parser.Variable_declaration_headContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#variable_name.
    def visitVariable_name(self, ctx:Swift3Parser.Variable_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#getter_setter_block.
    def visitGetter_setter_block(self, ctx:Swift3Parser.Getter_setter_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#getter_clause.
    def visitGetter_clause(self, ctx:Swift3Parser.Getter_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#setter_clause.
    def visitSetter_clause(self, ctx:Swift3Parser.Setter_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#setter_name.
    def visitSetter_name(self, ctx:Swift3Parser.Setter_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#getter_setter_keyword_block.
    def visitGetter_setter_keyword_block(self, ctx:Swift3Parser.Getter_setter_keyword_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#getter_keyword_clause.
    def visitGetter_keyword_clause(self, ctx:Swift3Parser.Getter_keyword_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#setter_keyword_clause.
    def visitSetter_keyword_clause(self, ctx:Swift3Parser.Setter_keyword_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#willSet_didSet_block.
    def visitWillSet_didSet_block(self, ctx:Swift3Parser.WillSet_didSet_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#willSet_clause.
    def visitWillSet_clause(self, ctx:Swift3Parser.WillSet_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#didSet_clause.
    def visitDidSet_clause(self, ctx:Swift3Parser.DidSet_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#typealias_declaration.
    def visitTypealias_declaration(self, ctx:Swift3Parser.Typealias_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#typealias_name.
    def visitTypealias_name(self, ctx:Swift3Parser.Typealias_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#typealias_assignment.
    def visitTypealias_assignment(self, ctx:Swift3Parser.Typealias_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#function_declaration.
    def visitFunction_declaration(self, ctx:Swift3Parser.Function_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#function_head.
    def visitFunction_head(self, ctx:Swift3Parser.Function_headContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#function_name.
    def visitFunction_name(self, ctx:Swift3Parser.Function_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#function_signature.
    def visitFunction_signature(self, ctx:Swift3Parser.Function_signatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#function_result.
    def visitFunction_result(self, ctx:Swift3Parser.Function_resultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#function_body.
    def visitFunction_body(self, ctx:Swift3Parser.Function_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#parameter_clause.
    def visitParameter_clause(self, ctx:Swift3Parser.Parameter_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#parameter_list.
    def visitParameter_list(self, ctx:Swift3Parser.Parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#parameter.
    def visitParameter(self, ctx:Swift3Parser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#external_parameter_name.
    def visitExternal_parameter_name(self, ctx:Swift3Parser.External_parameter_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#local_parameter_name.
    def visitLocal_parameter_name(self, ctx:Swift3Parser.Local_parameter_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#default_argument_clause.
    def visitDefault_argument_clause(self, ctx:Swift3Parser.Default_argument_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#enum_declaration.
    def visitEnum_declaration(self, ctx:Swift3Parser.Enum_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#union_style_enum.
    def visitUnion_style_enum(self, ctx:Swift3Parser.Union_style_enumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#union_style_enum_members.
    def visitUnion_style_enum_members(self, ctx:Swift3Parser.Union_style_enum_membersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#union_style_enum_member.
    def visitUnion_style_enum_member(self, ctx:Swift3Parser.Union_style_enum_memberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#union_style_enum_case_clause.
    def visitUnion_style_enum_case_clause(self, ctx:Swift3Parser.Union_style_enum_case_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#union_style_enum_case_list.
    def visitUnion_style_enum_case_list(self, ctx:Swift3Parser.Union_style_enum_case_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#union_style_enum_case.
    def visitUnion_style_enum_case(self, ctx:Swift3Parser.Union_style_enum_caseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#enum_name.
    def visitEnum_name(self, ctx:Swift3Parser.Enum_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#enum_case_name.
    def visitEnum_case_name(self, ctx:Swift3Parser.Enum_case_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#raw_value_style_enum.
    def visitRaw_value_style_enum(self, ctx:Swift3Parser.Raw_value_style_enumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#raw_value_style_enum_members.
    def visitRaw_value_style_enum_members(self, ctx:Swift3Parser.Raw_value_style_enum_membersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#raw_value_style_enum_member.
    def visitRaw_value_style_enum_member(self, ctx:Swift3Parser.Raw_value_style_enum_memberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#raw_value_style_enum_case_clause.
    def visitRaw_value_style_enum_case_clause(self, ctx:Swift3Parser.Raw_value_style_enum_case_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#raw_value_style_enum_case_list.
    def visitRaw_value_style_enum_case_list(self, ctx:Swift3Parser.Raw_value_style_enum_case_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#raw_value_style_enum_case.
    def visitRaw_value_style_enum_case(self, ctx:Swift3Parser.Raw_value_style_enum_caseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#raw_value_assignment.
    def visitRaw_value_assignment(self, ctx:Swift3Parser.Raw_value_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#raw_value_literal.
    def visitRaw_value_literal(self, ctx:Swift3Parser.Raw_value_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#struct_declaration.
    def visitStruct_declaration(self, ctx:Swift3Parser.Struct_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#struct_name.
    def visitStruct_name(self, ctx:Swift3Parser.Struct_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#struct_body.
    def visitStruct_body(self, ctx:Swift3Parser.Struct_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#struct_member.
    def visitStruct_member(self, ctx:Swift3Parser.Struct_memberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#class_declaration.
    def visitClass_declaration(self, ctx:Swift3Parser.Class_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#class_name.
    def visitClass_name(self, ctx:Swift3Parser.Class_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#class_body.
    def visitClass_body(self, ctx:Swift3Parser.Class_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#class_member.
    def visitClass_member(self, ctx:Swift3Parser.Class_memberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#protocol_declaration.
    def visitProtocol_declaration(self, ctx:Swift3Parser.Protocol_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#protocol_name.
    def visitProtocol_name(self, ctx:Swift3Parser.Protocol_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#protocol_body.
    def visitProtocol_body(self, ctx:Swift3Parser.Protocol_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#protocol_member.
    def visitProtocol_member(self, ctx:Swift3Parser.Protocol_memberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#protocol_member_declaration.
    def visitProtocol_member_declaration(self, ctx:Swift3Parser.Protocol_member_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#protocol_property_declaration.
    def visitProtocol_property_declaration(self, ctx:Swift3Parser.Protocol_property_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#protocol_method_declaration.
    def visitProtocol_method_declaration(self, ctx:Swift3Parser.Protocol_method_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#protocol_initializer_declaration.
    def visitProtocol_initializer_declaration(self, ctx:Swift3Parser.Protocol_initializer_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#protocol_subscript_declaration.
    def visitProtocol_subscript_declaration(self, ctx:Swift3Parser.Protocol_subscript_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#protocol_associated_type_declaration.
    def visitProtocol_associated_type_declaration(self, ctx:Swift3Parser.Protocol_associated_type_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#initializer_declaration.
    def visitInitializer_declaration(self, ctx:Swift3Parser.Initializer_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#initializer_head.
    def visitInitializer_head(self, ctx:Swift3Parser.Initializer_headContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#initializer_body.
    def visitInitializer_body(self, ctx:Swift3Parser.Initializer_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#deinitializer_declaration.
    def visitDeinitializer_declaration(self, ctx:Swift3Parser.Deinitializer_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#extension_declaration.
    def visitExtension_declaration(self, ctx:Swift3Parser.Extension_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#extension_body.
    def visitExtension_body(self, ctx:Swift3Parser.Extension_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#extension_member.
    def visitExtension_member(self, ctx:Swift3Parser.Extension_memberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#subscript_declaration.
    def visitSubscript_declaration(self, ctx:Swift3Parser.Subscript_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#subscript_head.
    def visitSubscript_head(self, ctx:Swift3Parser.Subscript_headContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#subscript_result.
    def visitSubscript_result(self, ctx:Swift3Parser.Subscript_resultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#operator_declaration.
    def visitOperator_declaration(self, ctx:Swift3Parser.Operator_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#prefix_operator_declaration.
    def visitPrefix_operator_declaration(self, ctx:Swift3Parser.Prefix_operator_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#postfix_operator_declaration.
    def visitPostfix_operator_declaration(self, ctx:Swift3Parser.Postfix_operator_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#infix_operator_declaration.
    def visitInfix_operator_declaration(self, ctx:Swift3Parser.Infix_operator_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#infix_operator_group.
    def visitInfix_operator_group(self, ctx:Swift3Parser.Infix_operator_groupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#precedence_group_declaration.
    def visitPrecedence_group_declaration(self, ctx:Swift3Parser.Precedence_group_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#precedence_group_attribute.
    def visitPrecedence_group_attribute(self, ctx:Swift3Parser.Precedence_group_attributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#precedence_group_relation.
    def visitPrecedence_group_relation(self, ctx:Swift3Parser.Precedence_group_relationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#precedence_group_assignment.
    def visitPrecedence_group_assignment(self, ctx:Swift3Parser.Precedence_group_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#precedence_group_associativity.
    def visitPrecedence_group_associativity(self, ctx:Swift3Parser.Precedence_group_associativityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#associativity.
    def visitAssociativity(self, ctx:Swift3Parser.AssociativityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#precedence_group_names.
    def visitPrecedence_group_names(self, ctx:Swift3Parser.Precedence_group_namesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#precedence_group_name.
    def visitPrecedence_group_name(self, ctx:Swift3Parser.Precedence_group_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#declaration_modifier.
    def visitDeclaration_modifier(self, ctx:Swift3Parser.Declaration_modifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#declaration_modifiers.
    def visitDeclaration_modifiers(self, ctx:Swift3Parser.Declaration_modifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#access_level_modifier.
    def visitAccess_level_modifier(self, ctx:Swift3Parser.Access_level_modifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#mutation_modifier.
    def visitMutation_modifier(self, ctx:Swift3Parser.Mutation_modifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#pattern.
    def visitPattern(self, ctx:Swift3Parser.PatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#wildcard_pattern.
    def visitWildcard_pattern(self, ctx:Swift3Parser.Wildcard_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#identifier_pattern.
    def visitIdentifier_pattern(self, ctx:Swift3Parser.Identifier_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#value_binding_pattern.
    def visitValue_binding_pattern(self, ctx:Swift3Parser.Value_binding_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#tuple_pattern.
    def visitTuple_pattern(self, ctx:Swift3Parser.Tuple_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#tuple_pattern_element_list.
    def visitTuple_pattern_element_list(self, ctx:Swift3Parser.Tuple_pattern_element_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#tuple_pattern_element.
    def visitTuple_pattern_element(self, ctx:Swift3Parser.Tuple_pattern_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#enum_case_pattern.
    def visitEnum_case_pattern(self, ctx:Swift3Parser.Enum_case_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#optional_pattern.
    def visitOptional_pattern(self, ctx:Swift3Parser.Optional_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#expression_pattern.
    def visitExpression_pattern(self, ctx:Swift3Parser.Expression_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#attribute.
    def visitAttribute(self, ctx:Swift3Parser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#attribute_name.
    def visitAttribute_name(self, ctx:Swift3Parser.Attribute_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#attribute_argument_clause.
    def visitAttribute_argument_clause(self, ctx:Swift3Parser.Attribute_argument_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#attributes.
    def visitAttributes(self, ctx:Swift3Parser.AttributesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#balanced_tokens.
    def visitBalanced_tokens(self, ctx:Swift3Parser.Balanced_tokensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#balanced_token.
    def visitBalanced_token(self, ctx:Swift3Parser.Balanced_tokenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#any_punctuation_for_balanced_token.
    def visitAny_punctuation_for_balanced_token(self, ctx:Swift3Parser.Any_punctuation_for_balanced_tokenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#expression.
    def visitExpression(self, ctx:Swift3Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#expression_list.
    def visitExpression_list(self, ctx:Swift3Parser.Expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#prefix_expression.
    def visitPrefix_expression(self, ctx:Swift3Parser.Prefix_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#in_out_expression.
    def visitIn_out_expression(self, ctx:Swift3Parser.In_out_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#try_operator.
    def visitTry_operator(self, ctx:Swift3Parser.Try_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#binary_expression.
    def visitBinary_expression(self, ctx:Swift3Parser.Binary_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#binary_expressions.
    def visitBinary_expressions(self, ctx:Swift3Parser.Binary_expressionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#conditional_operator.
    def visitConditional_operator(self, ctx:Swift3Parser.Conditional_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#type_casting_operator.
    def visitType_casting_operator(self, ctx:Swift3Parser.Type_casting_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#primary_expression.
    def visitPrimary_expression(self, ctx:Swift3Parser.Primary_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#literal_expression.
    def visitLiteral_expression(self, ctx:Swift3Parser.Literal_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#array_literal.
    def visitArray_literal(self, ctx:Swift3Parser.Array_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#array_literal_items.
    def visitArray_literal_items(self, ctx:Swift3Parser.Array_literal_itemsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#array_literal_item.
    def visitArray_literal_item(self, ctx:Swift3Parser.Array_literal_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#dictionary_literal.
    def visitDictionary_literal(self, ctx:Swift3Parser.Dictionary_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#dictionary_literal_items.
    def visitDictionary_literal_items(self, ctx:Swift3Parser.Dictionary_literal_itemsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#dictionary_literal_item.
    def visitDictionary_literal_item(self, ctx:Swift3Parser.Dictionary_literal_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#playground_literal.
    def visitPlayground_literal(self, ctx:Swift3Parser.Playground_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#self_expression.
    def visitSelf_expression(self, ctx:Swift3Parser.Self_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#superclass_expression.
    def visitSuperclass_expression(self, ctx:Swift3Parser.Superclass_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#superclass_method_expression.
    def visitSuperclass_method_expression(self, ctx:Swift3Parser.Superclass_method_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#superclass_subscript_expression.
    def visitSuperclass_subscript_expression(self, ctx:Swift3Parser.Superclass_subscript_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#superclass_initializer_expression.
    def visitSuperclass_initializer_expression(self, ctx:Swift3Parser.Superclass_initializer_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#closure_expression.
    def visitClosure_expression(self, ctx:Swift3Parser.Closure_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#closure_signature.
    def visitClosure_signature(self, ctx:Swift3Parser.Closure_signatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#closure_parameter_clause.
    def visitClosure_parameter_clause(self, ctx:Swift3Parser.Closure_parameter_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#closure_parameter_clause_identifier_list.
    def visitClosure_parameter_clause_identifier_list(self, ctx:Swift3Parser.Closure_parameter_clause_identifier_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#closure_parameter_list.
    def visitClosure_parameter_list(self, ctx:Swift3Parser.Closure_parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#closure_parameter.
    def visitClosure_parameter(self, ctx:Swift3Parser.Closure_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#closure_parameter_name.
    def visitClosure_parameter_name(self, ctx:Swift3Parser.Closure_parameter_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#capture_list.
    def visitCapture_list(self, ctx:Swift3Parser.Capture_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#capture_list_items.
    def visitCapture_list_items(self, ctx:Swift3Parser.Capture_list_itemsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#capture_list_item.
    def visitCapture_list_item(self, ctx:Swift3Parser.Capture_list_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#capture_specifier.
    def visitCapture_specifier(self, ctx:Swift3Parser.Capture_specifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#implicit_member_expression.
    def visitImplicit_member_expression(self, ctx:Swift3Parser.Implicit_member_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#parenthesized_expression.
    def visitParenthesized_expression(self, ctx:Swift3Parser.Parenthesized_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#tuple_expression.
    def visitTuple_expression(self, ctx:Swift3Parser.Tuple_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#tuple_element.
    def visitTuple_element(self, ctx:Swift3Parser.Tuple_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#wildcard_expression.
    def visitWildcard_expression(self, ctx:Swift3Parser.Wildcard_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#selector_expression.
    def visitSelector_expression(self, ctx:Swift3Parser.Selector_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#key_path_expression.
    def visitKey_path_expression(self, ctx:Swift3Parser.Key_path_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#function_call_expression_with_closure.
    def visitFunction_call_expression_with_closure(self, ctx:Swift3Parser.Function_call_expression_with_closureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#function_call_expression.
    def visitFunction_call_expression(self, ctx:Swift3Parser.Function_call_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#explicit_member_expression1.
    def visitExplicit_member_expression1(self, ctx:Swift3Parser.Explicit_member_expression1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#initializer_expression.
    def visitInitializer_expression(self, ctx:Swift3Parser.Initializer_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#postfix_self_expression.
    def visitPostfix_self_expression(self, ctx:Swift3Parser.Postfix_self_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#initializer_expression_with_args.
    def visitInitializer_expression_with_args(self, ctx:Swift3Parser.Initializer_expression_with_argsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#dynamic_type.
    def visitDynamic_type(self, ctx:Swift3Parser.Dynamic_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#subscript_expression.
    def visitSubscript_expression(self, ctx:Swift3Parser.Subscript_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#explicit_member_expression2.
    def visitExplicit_member_expression2(self, ctx:Swift3Parser.Explicit_member_expression2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#explicit_member_expression3.
    def visitExplicit_member_expression3(self, ctx:Swift3Parser.Explicit_member_expression3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#explicit_member_expression4.
    def visitExplicit_member_expression4(self, ctx:Swift3Parser.Explicit_member_expression4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#postfix_operation.
    def visitPostfix_operation(self, ctx:Swift3Parser.Postfix_operationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#primary.
    def visitPrimary(self, ctx:Swift3Parser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#function_call_argument_clause.
    def visitFunction_call_argument_clause(self, ctx:Swift3Parser.Function_call_argument_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#function_call_argument_list.
    def visitFunction_call_argument_list(self, ctx:Swift3Parser.Function_call_argument_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#function_call_argument.
    def visitFunction_call_argument(self, ctx:Swift3Parser.Function_call_argumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#trailing_closure.
    def visitTrailing_closure(self, ctx:Swift3Parser.Trailing_closureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#argument_names.
    def visitArgument_names(self, ctx:Swift3Parser.Argument_namesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#argument_name.
    def visitArgument_name(self, ctx:Swift3Parser.Argument_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#dynamic_type_expression.
    def visitDynamic_type_expression(self, ctx:Swift3Parser.Dynamic_type_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#the_metatype_protocol_type.
    def visitThe_metatype_protocol_type(self, ctx:Swift3Parser.The_metatype_protocol_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#the_function_type.
    def visitThe_function_type(self, ctx:Swift3Parser.The_function_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#the_implicitly_unwrapped_optional_type.
    def visitThe_implicitly_unwrapped_optional_type(self, ctx:Swift3Parser.The_implicitly_unwrapped_optional_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#the_dictionary_type.
    def visitThe_dictionary_type(self, ctx:Swift3Parser.The_dictionary_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#the_optional_type.
    def visitThe_optional_type(self, ctx:Swift3Parser.The_optional_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#the_tuple_type.
    def visitThe_tuple_type(self, ctx:Swift3Parser.The_tuple_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#the_self_type.
    def visitThe_self_type(self, ctx:Swift3Parser.The_self_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#the_array_type.
    def visitThe_array_type(self, ctx:Swift3Parser.The_array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#the_metatype_type_type.
    def visitThe_metatype_type_type(self, ctx:Swift3Parser.The_metatype_type_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#the_protocol_composition_type.
    def visitThe_protocol_composition_type(self, ctx:Swift3Parser.The_protocol_composition_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#the_any_type.
    def visitThe_any_type(self, ctx:Swift3Parser.The_any_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#the_type_identifier.
    def visitThe_type_identifier(self, ctx:Swift3Parser.The_type_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#type_annotation.
    def visitType_annotation(self, ctx:Swift3Parser.Type_annotationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#type_identifier.
    def visitType_identifier(self, ctx:Swift3Parser.Type_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#type_name.
    def visitType_name(self, ctx:Swift3Parser.Type_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#tuple_type.
    def visitTuple_type(self, ctx:Swift3Parser.Tuple_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#tuple_type_element_list.
    def visitTuple_type_element_list(self, ctx:Swift3Parser.Tuple_type_element_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#tuple_type_element.
    def visitTuple_type_element(self, ctx:Swift3Parser.Tuple_type_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#element_name.
    def visitElement_name(self, ctx:Swift3Parser.Element_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#function_type.
    def visitFunction_type(self, ctx:Swift3Parser.Function_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#function_type_argument_clause.
    def visitFunction_type_argument_clause(self, ctx:Swift3Parser.Function_type_argument_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#function_type_argument_list.
    def visitFunction_type_argument_list(self, ctx:Swift3Parser.Function_type_argument_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#function_type_argument.
    def visitFunction_type_argument(self, ctx:Swift3Parser.Function_type_argumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#argument_label.
    def visitArgument_label(self, ctx:Swift3Parser.Argument_labelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#array_type.
    def visitArray_type(self, ctx:Swift3Parser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#dictionary_type.
    def visitDictionary_type(self, ctx:Swift3Parser.Dictionary_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#protocol_composition_type.
    def visitProtocol_composition_type(self, ctx:Swift3Parser.Protocol_composition_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#protocol_identifier.
    def visitProtocol_identifier(self, ctx:Swift3Parser.Protocol_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#type_inheritance_clause.
    def visitType_inheritance_clause(self, ctx:Swift3Parser.Type_inheritance_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#type_inheritance_list.
    def visitType_inheritance_list(self, ctx:Swift3Parser.Type_inheritance_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#class_requirement.
    def visitClass_requirement(self, ctx:Swift3Parser.Class_requirementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#declaration_identifier.
    def visitDeclaration_identifier(self, ctx:Swift3Parser.Declaration_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#label_identifier.
    def visitLabel_identifier(self, ctx:Swift3Parser.Label_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#keyword_as_identifier_in_declarations.
    def visitKeyword_as_identifier_in_declarations(self, ctx:Swift3Parser.Keyword_as_identifier_in_declarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#keyword_as_identifier_in_labels.
    def visitKeyword_as_identifier_in_labels(self, ctx:Swift3Parser.Keyword_as_identifier_in_labelsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#assignment_operator.
    def visitAssignment_operator(self, ctx:Swift3Parser.Assignment_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#negate_prefix_operator.
    def visitNegate_prefix_operator(self, ctx:Swift3Parser.Negate_prefix_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#compilation_condition_AND.
    def visitCompilation_condition_AND(self, ctx:Swift3Parser.Compilation_condition_ANDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#compilation_condition_OR.
    def visitCompilation_condition_OR(self, ctx:Swift3Parser.Compilation_condition_ORContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#compilation_condition_GE.
    def visitCompilation_condition_GE(self, ctx:Swift3Parser.Compilation_condition_GEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#arrow_operator.
    def visitArrow_operator(self, ctx:Swift3Parser.Arrow_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#range_operator.
    def visitRange_operator(self, ctx:Swift3Parser.Range_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#same_type_equals.
    def visitSame_type_equals(self, ctx:Swift3Parser.Same_type_equalsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#binary_operator.
    def visitBinary_operator(self, ctx:Swift3Parser.Binary_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#prefix_operator.
    def visitPrefix_operator(self, ctx:Swift3Parser.Prefix_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#postfix_operator.
    def visitPostfix_operator(self, ctx:Swift3Parser.Postfix_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#operator.
    def visitOperator(self, ctx:Swift3Parser.OperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#operator_character.
    def visitOperator_character(self, ctx:Swift3Parser.Operator_characterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#operator_head.
    def visitOperator_head(self, ctx:Swift3Parser.Operator_headContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#dot_operator_head.
    def visitDot_operator_head(self, ctx:Swift3Parser.Dot_operator_headContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#dot_operator_character.
    def visitDot_operator_character(self, ctx:Swift3Parser.Dot_operator_characterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#literal.
    def visitLiteral(self, ctx:Swift3Parser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#numeric_literal.
    def visitNumeric_literal(self, ctx:Swift3Parser.Numeric_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#boolean_literal.
    def visitBoolean_literal(self, ctx:Swift3Parser.Boolean_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#nil_literal.
    def visitNil_literal(self, ctx:Swift3Parser.Nil_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#integer_literal.
    def visitInteger_literal(self, ctx:Swift3Parser.Integer_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift3Parser#string_literal.
    def visitString_literal(self, ctx:Swift3Parser.String_literalContext):
        return self.visitChildren(ctx)



del Swift3Parser