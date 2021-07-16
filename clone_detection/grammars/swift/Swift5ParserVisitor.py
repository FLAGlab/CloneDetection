# Generated from Swift5Parser.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .Swift5Parser import Swift5Parser
else:
    from Swift5Parser import Swift5Parser

# This class defines a complete generic visitor for a parse tree produced by Swift5Parser.

class Swift5ParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by Swift5Parser#top_level.
    def visitTop_level(self, ctx:Swift5Parser.Top_levelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#statement.
    def visitStatement(self, ctx:Swift5Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#statements.
    def visitStatements(self, ctx:Swift5Parser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#loop_statement.
    def visitLoop_statement(self, ctx:Swift5Parser.Loop_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#for_in_statement.
    def visitFor_in_statement(self, ctx:Swift5Parser.For_in_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#while_statement.
    def visitWhile_statement(self, ctx:Swift5Parser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#condition_list.
    def visitCondition_list(self, ctx:Swift5Parser.Condition_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#condition.
    def visitCondition(self, ctx:Swift5Parser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#case_condition.
    def visitCase_condition(self, ctx:Swift5Parser.Case_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#optional_binding_condition.
    def visitOptional_binding_condition(self, ctx:Swift5Parser.Optional_binding_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#repeat_while_statement.
    def visitRepeat_while_statement(self, ctx:Swift5Parser.Repeat_while_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#branch_statement.
    def visitBranch_statement(self, ctx:Swift5Parser.Branch_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#if_statement.
    def visitIf_statement(self, ctx:Swift5Parser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#else_clause.
    def visitElse_clause(self, ctx:Swift5Parser.Else_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#guard_statement.
    def visitGuard_statement(self, ctx:Swift5Parser.Guard_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#switch_statement.
    def visitSwitch_statement(self, ctx:Swift5Parser.Switch_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#switch_cases.
    def visitSwitch_cases(self, ctx:Swift5Parser.Switch_casesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#switch_case.
    def visitSwitch_case(self, ctx:Swift5Parser.Switch_caseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#case_label.
    def visitCase_label(self, ctx:Swift5Parser.Case_labelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#case_item_list.
    def visitCase_item_list(self, ctx:Swift5Parser.Case_item_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#default_label.
    def visitDefault_label(self, ctx:Swift5Parser.Default_labelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#where_clause.
    def visitWhere_clause(self, ctx:Swift5Parser.Where_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#where_expression.
    def visitWhere_expression(self, ctx:Swift5Parser.Where_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#conditional_switch_case.
    def visitConditional_switch_case(self, ctx:Swift5Parser.Conditional_switch_caseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#switch_if_directive_clause.
    def visitSwitch_if_directive_clause(self, ctx:Swift5Parser.Switch_if_directive_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#switch_elseif_directive_clauses.
    def visitSwitch_elseif_directive_clauses(self, ctx:Swift5Parser.Switch_elseif_directive_clausesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#switch_elseif_directive_clause.
    def visitSwitch_elseif_directive_clause(self, ctx:Swift5Parser.Switch_elseif_directive_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#switch_else_directive_clause.
    def visitSwitch_else_directive_clause(self, ctx:Swift5Parser.Switch_else_directive_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#labeled_statement.
    def visitLabeled_statement(self, ctx:Swift5Parser.Labeled_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#statement_label.
    def visitStatement_label(self, ctx:Swift5Parser.Statement_labelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#label_name.
    def visitLabel_name(self, ctx:Swift5Parser.Label_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#control_transfer_statement.
    def visitControl_transfer_statement(self, ctx:Swift5Parser.Control_transfer_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#break_statement.
    def visitBreak_statement(self, ctx:Swift5Parser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#continue_statement.
    def visitContinue_statement(self, ctx:Swift5Parser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#fallthrough_statement.
    def visitFallthrough_statement(self, ctx:Swift5Parser.Fallthrough_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#return_statement.
    def visitReturn_statement(self, ctx:Swift5Parser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#throw_statement.
    def visitThrow_statement(self, ctx:Swift5Parser.Throw_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#defer_statement.
    def visitDefer_statement(self, ctx:Swift5Parser.Defer_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#do_statement.
    def visitDo_statement(self, ctx:Swift5Parser.Do_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#catch_clauses.
    def visitCatch_clauses(self, ctx:Swift5Parser.Catch_clausesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#catch_clause.
    def visitCatch_clause(self, ctx:Swift5Parser.Catch_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#catch_pattern_list.
    def visitCatch_pattern_list(self, ctx:Swift5Parser.Catch_pattern_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#catch_pattern.
    def visitCatch_pattern(self, ctx:Swift5Parser.Catch_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#compiler_control_statement.
    def visitCompiler_control_statement(self, ctx:Swift5Parser.Compiler_control_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#conditional_compilation_block.
    def visitConditional_compilation_block(self, ctx:Swift5Parser.Conditional_compilation_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#if_directive_clause.
    def visitIf_directive_clause(self, ctx:Swift5Parser.If_directive_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#elseif_directive_clauses.
    def visitElseif_directive_clauses(self, ctx:Swift5Parser.Elseif_directive_clausesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#elseif_directive_clause.
    def visitElseif_directive_clause(self, ctx:Swift5Parser.Elseif_directive_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#else_directive_clause.
    def visitElse_directive_clause(self, ctx:Swift5Parser.Else_directive_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#compilation_condition.
    def visitCompilation_condition(self, ctx:Swift5Parser.Compilation_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#platform_condition.
    def visitPlatform_condition(self, ctx:Swift5Parser.Platform_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#swift_version.
    def visitSwift_version(self, ctx:Swift5Parser.Swift_versionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#swift_version_continuation.
    def visitSwift_version_continuation(self, ctx:Swift5Parser.Swift_version_continuationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#operating_system.
    def visitOperating_system(self, ctx:Swift5Parser.Operating_systemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#architecture.
    def visitArchitecture(self, ctx:Swift5Parser.ArchitectureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#module_name.
    def visitModule_name(self, ctx:Swift5Parser.Module_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#environment.
    def visitEnvironment(self, ctx:Swift5Parser.EnvironmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#line_control_statement.
    def visitLine_control_statement(self, ctx:Swift5Parser.Line_control_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#line_number.
    def visitLine_number(self, ctx:Swift5Parser.Line_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#file_name.
    def visitFile_name(self, ctx:Swift5Parser.File_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#diagnostic_statement.
    def visitDiagnostic_statement(self, ctx:Swift5Parser.Diagnostic_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#diagnostic_message.
    def visitDiagnostic_message(self, ctx:Swift5Parser.Diagnostic_messageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#availability_condition.
    def visitAvailability_condition(self, ctx:Swift5Parser.Availability_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#availability_arguments.
    def visitAvailability_arguments(self, ctx:Swift5Parser.Availability_argumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#availability_argument.
    def visitAvailability_argument(self, ctx:Swift5Parser.Availability_argumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#platform_name.
    def visitPlatform_name(self, ctx:Swift5Parser.Platform_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#platform_version.
    def visitPlatform_version(self, ctx:Swift5Parser.Platform_versionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#generic_parameter_clause.
    def visitGeneric_parameter_clause(self, ctx:Swift5Parser.Generic_parameter_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#generic_parameter_list.
    def visitGeneric_parameter_list(self, ctx:Swift5Parser.Generic_parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#generic_parameter.
    def visitGeneric_parameter(self, ctx:Swift5Parser.Generic_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#generic_where_clause.
    def visitGeneric_where_clause(self, ctx:Swift5Parser.Generic_where_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#requirement_list.
    def visitRequirement_list(self, ctx:Swift5Parser.Requirement_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#requirement.
    def visitRequirement(self, ctx:Swift5Parser.RequirementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#conformance_requirement.
    def visitConformance_requirement(self, ctx:Swift5Parser.Conformance_requirementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#same_type_requirement.
    def visitSame_type_requirement(self, ctx:Swift5Parser.Same_type_requirementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#generic_argument_clause.
    def visitGeneric_argument_clause(self, ctx:Swift5Parser.Generic_argument_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#generic_argument_list.
    def visitGeneric_argument_list(self, ctx:Swift5Parser.Generic_argument_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#generic_argument.
    def visitGeneric_argument(self, ctx:Swift5Parser.Generic_argumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#declaration.
    def visitDeclaration(self, ctx:Swift5Parser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#declarations.
    def visitDeclarations(self, ctx:Swift5Parser.DeclarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#top_level_declaration.
    def visitTop_level_declaration(self, ctx:Swift5Parser.Top_level_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#code_block.
    def visitCode_block(self, ctx:Swift5Parser.Code_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#import_declaration.
    def visitImport_declaration(self, ctx:Swift5Parser.Import_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#import_kind.
    def visitImport_kind(self, ctx:Swift5Parser.Import_kindContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#import_path.
    def visitImport_path(self, ctx:Swift5Parser.Import_pathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#import_path_identifier.
    def visitImport_path_identifier(self, ctx:Swift5Parser.Import_path_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#constant_declaration.
    def visitConstant_declaration(self, ctx:Swift5Parser.Constant_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#pattern_initializer_list.
    def visitPattern_initializer_list(self, ctx:Swift5Parser.Pattern_initializer_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#pattern_initializer.
    def visitPattern_initializer(self, ctx:Swift5Parser.Pattern_initializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#initializer.
    def visitInitializer(self, ctx:Swift5Parser.InitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#variable_declaration.
    def visitVariable_declaration(self, ctx:Swift5Parser.Variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#variable_declaration_head.
    def visitVariable_declaration_head(self, ctx:Swift5Parser.Variable_declaration_headContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#variable_name.
    def visitVariable_name(self, ctx:Swift5Parser.Variable_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#getter_setter_block.
    def visitGetter_setter_block(self, ctx:Swift5Parser.Getter_setter_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#getter_clause.
    def visitGetter_clause(self, ctx:Swift5Parser.Getter_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#setter_clause.
    def visitSetter_clause(self, ctx:Swift5Parser.Setter_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#setter_name.
    def visitSetter_name(self, ctx:Swift5Parser.Setter_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#getter_setter_keyword_block.
    def visitGetter_setter_keyword_block(self, ctx:Swift5Parser.Getter_setter_keyword_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#getter_keyword_clause.
    def visitGetter_keyword_clause(self, ctx:Swift5Parser.Getter_keyword_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#setter_keyword_clause.
    def visitSetter_keyword_clause(self, ctx:Swift5Parser.Setter_keyword_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#willSet_didSet_block.
    def visitWillSet_didSet_block(self, ctx:Swift5Parser.WillSet_didSet_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#willSet_clause.
    def visitWillSet_clause(self, ctx:Swift5Parser.WillSet_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#didSet_clause.
    def visitDidSet_clause(self, ctx:Swift5Parser.DidSet_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#typealias_declaration.
    def visitTypealias_declaration(self, ctx:Swift5Parser.Typealias_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#typealias_name.
    def visitTypealias_name(self, ctx:Swift5Parser.Typealias_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#typealias_assignment.
    def visitTypealias_assignment(self, ctx:Swift5Parser.Typealias_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#function_declaration.
    def visitFunction_declaration(self, ctx:Swift5Parser.Function_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#function_head.
    def visitFunction_head(self, ctx:Swift5Parser.Function_headContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#function_name.
    def visitFunction_name(self, ctx:Swift5Parser.Function_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#function_signature.
    def visitFunction_signature(self, ctx:Swift5Parser.Function_signatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#function_result.
    def visitFunction_result(self, ctx:Swift5Parser.Function_resultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#function_body.
    def visitFunction_body(self, ctx:Swift5Parser.Function_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#parameter_clause.
    def visitParameter_clause(self, ctx:Swift5Parser.Parameter_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#parameter_list.
    def visitParameter_list(self, ctx:Swift5Parser.Parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#parameter.
    def visitParameter(self, ctx:Swift5Parser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#external_parameter_name.
    def visitExternal_parameter_name(self, ctx:Swift5Parser.External_parameter_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#local_parameter_name.
    def visitLocal_parameter_name(self, ctx:Swift5Parser.Local_parameter_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#default_argument_clause.
    def visitDefault_argument_clause(self, ctx:Swift5Parser.Default_argument_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#enum_declaration.
    def visitEnum_declaration(self, ctx:Swift5Parser.Enum_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#union_style_enum.
    def visitUnion_style_enum(self, ctx:Swift5Parser.Union_style_enumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#union_style_enum_members.
    def visitUnion_style_enum_members(self, ctx:Swift5Parser.Union_style_enum_membersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#union_style_enum_member.
    def visitUnion_style_enum_member(self, ctx:Swift5Parser.Union_style_enum_memberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#union_style_enum_case_clause.
    def visitUnion_style_enum_case_clause(self, ctx:Swift5Parser.Union_style_enum_case_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#union_style_enum_case_list.
    def visitUnion_style_enum_case_list(self, ctx:Swift5Parser.Union_style_enum_case_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#union_style_enum_case.
    def visitUnion_style_enum_case(self, ctx:Swift5Parser.Union_style_enum_caseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#enum_name.
    def visitEnum_name(self, ctx:Swift5Parser.Enum_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#enum_case_name.
    def visitEnum_case_name(self, ctx:Swift5Parser.Enum_case_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#raw_value_style_enum.
    def visitRaw_value_style_enum(self, ctx:Swift5Parser.Raw_value_style_enumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#raw_value_style_enum_members.
    def visitRaw_value_style_enum_members(self, ctx:Swift5Parser.Raw_value_style_enum_membersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#raw_value_style_enum_member.
    def visitRaw_value_style_enum_member(self, ctx:Swift5Parser.Raw_value_style_enum_memberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#raw_value_style_enum_case_clause.
    def visitRaw_value_style_enum_case_clause(self, ctx:Swift5Parser.Raw_value_style_enum_case_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#raw_value_style_enum_case_list.
    def visitRaw_value_style_enum_case_list(self, ctx:Swift5Parser.Raw_value_style_enum_case_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#raw_value_style_enum_case.
    def visitRaw_value_style_enum_case(self, ctx:Swift5Parser.Raw_value_style_enum_caseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#raw_value_assignment.
    def visitRaw_value_assignment(self, ctx:Swift5Parser.Raw_value_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#raw_value_literal.
    def visitRaw_value_literal(self, ctx:Swift5Parser.Raw_value_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#struct_declaration.
    def visitStruct_declaration(self, ctx:Swift5Parser.Struct_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#struct_name.
    def visitStruct_name(self, ctx:Swift5Parser.Struct_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#struct_body.
    def visitStruct_body(self, ctx:Swift5Parser.Struct_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#struct_members.
    def visitStruct_members(self, ctx:Swift5Parser.Struct_membersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#struct_member.
    def visitStruct_member(self, ctx:Swift5Parser.Struct_memberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#class_declaration.
    def visitClass_declaration(self, ctx:Swift5Parser.Class_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#class_name.
    def visitClass_name(self, ctx:Swift5Parser.Class_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#class_body.
    def visitClass_body(self, ctx:Swift5Parser.Class_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#class_members.
    def visitClass_members(self, ctx:Swift5Parser.Class_membersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#class_member.
    def visitClass_member(self, ctx:Swift5Parser.Class_memberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#protocol_declaration.
    def visitProtocol_declaration(self, ctx:Swift5Parser.Protocol_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#protocol_name.
    def visitProtocol_name(self, ctx:Swift5Parser.Protocol_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#protocol_body.
    def visitProtocol_body(self, ctx:Swift5Parser.Protocol_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#protocol_members.
    def visitProtocol_members(self, ctx:Swift5Parser.Protocol_membersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#protocol_member.
    def visitProtocol_member(self, ctx:Swift5Parser.Protocol_memberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#protocol_member_declaration.
    def visitProtocol_member_declaration(self, ctx:Swift5Parser.Protocol_member_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#protocol_property_declaration.
    def visitProtocol_property_declaration(self, ctx:Swift5Parser.Protocol_property_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#protocol_method_declaration.
    def visitProtocol_method_declaration(self, ctx:Swift5Parser.Protocol_method_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#protocol_initializer_declaration.
    def visitProtocol_initializer_declaration(self, ctx:Swift5Parser.Protocol_initializer_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#protocol_subscript_declaration.
    def visitProtocol_subscript_declaration(self, ctx:Swift5Parser.Protocol_subscript_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#protocol_associated_type_declaration.
    def visitProtocol_associated_type_declaration(self, ctx:Swift5Parser.Protocol_associated_type_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#initializer_declaration.
    def visitInitializer_declaration(self, ctx:Swift5Parser.Initializer_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#initializer_head.
    def visitInitializer_head(self, ctx:Swift5Parser.Initializer_headContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#initializer_body.
    def visitInitializer_body(self, ctx:Swift5Parser.Initializer_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#deinitializer_declaration.
    def visitDeinitializer_declaration(self, ctx:Swift5Parser.Deinitializer_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#extension_declaration.
    def visitExtension_declaration(self, ctx:Swift5Parser.Extension_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#extension_body.
    def visitExtension_body(self, ctx:Swift5Parser.Extension_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#extension_members.
    def visitExtension_members(self, ctx:Swift5Parser.Extension_membersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#extension_member.
    def visitExtension_member(self, ctx:Swift5Parser.Extension_memberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#subscript_declaration.
    def visitSubscript_declaration(self, ctx:Swift5Parser.Subscript_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#subscript_head.
    def visitSubscript_head(self, ctx:Swift5Parser.Subscript_headContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#subscript_result.
    def visitSubscript_result(self, ctx:Swift5Parser.Subscript_resultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#operator_declaration.
    def visitOperator_declaration(self, ctx:Swift5Parser.Operator_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#prefix_operator_declaration.
    def visitPrefix_operator_declaration(self, ctx:Swift5Parser.Prefix_operator_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#postfix_operator_declaration.
    def visitPostfix_operator_declaration(self, ctx:Swift5Parser.Postfix_operator_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#infix_operator_declaration.
    def visitInfix_operator_declaration(self, ctx:Swift5Parser.Infix_operator_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#infix_operator_group.
    def visitInfix_operator_group(self, ctx:Swift5Parser.Infix_operator_groupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#precedence_group_declaration.
    def visitPrecedence_group_declaration(self, ctx:Swift5Parser.Precedence_group_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#precedence_group_attributes.
    def visitPrecedence_group_attributes(self, ctx:Swift5Parser.Precedence_group_attributesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#precedence_group_attribute.
    def visitPrecedence_group_attribute(self, ctx:Swift5Parser.Precedence_group_attributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#precedence_group_relation.
    def visitPrecedence_group_relation(self, ctx:Swift5Parser.Precedence_group_relationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#precedence_group_assignment.
    def visitPrecedence_group_assignment(self, ctx:Swift5Parser.Precedence_group_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#precedence_group_associativity.
    def visitPrecedence_group_associativity(self, ctx:Swift5Parser.Precedence_group_associativityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#precedence_group_names.
    def visitPrecedence_group_names(self, ctx:Swift5Parser.Precedence_group_namesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#precedence_group_name.
    def visitPrecedence_group_name(self, ctx:Swift5Parser.Precedence_group_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#declaration_modifier.
    def visitDeclaration_modifier(self, ctx:Swift5Parser.Declaration_modifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#declaration_modifiers.
    def visitDeclaration_modifiers(self, ctx:Swift5Parser.Declaration_modifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#access_level_modifier.
    def visitAccess_level_modifier(self, ctx:Swift5Parser.Access_level_modifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#mutation_modifier.
    def visitMutation_modifier(self, ctx:Swift5Parser.Mutation_modifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#pattern.
    def visitPattern(self, ctx:Swift5Parser.PatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#wildcard_pattern.
    def visitWildcard_pattern(self, ctx:Swift5Parser.Wildcard_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#identifier_pattern.
    def visitIdentifier_pattern(self, ctx:Swift5Parser.Identifier_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#value_binding_pattern.
    def visitValue_binding_pattern(self, ctx:Swift5Parser.Value_binding_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#tuple_pattern.
    def visitTuple_pattern(self, ctx:Swift5Parser.Tuple_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#tuple_pattern_element_list.
    def visitTuple_pattern_element_list(self, ctx:Swift5Parser.Tuple_pattern_element_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#tuple_pattern_element.
    def visitTuple_pattern_element(self, ctx:Swift5Parser.Tuple_pattern_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#enum_case_pattern.
    def visitEnum_case_pattern(self, ctx:Swift5Parser.Enum_case_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#optional_pattern.
    def visitOptional_pattern(self, ctx:Swift5Parser.Optional_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#expression_pattern.
    def visitExpression_pattern(self, ctx:Swift5Parser.Expression_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#attribute.
    def visitAttribute(self, ctx:Swift5Parser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#attribute_name.
    def visitAttribute_name(self, ctx:Swift5Parser.Attribute_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#attribute_argument_clause.
    def visitAttribute_argument_clause(self, ctx:Swift5Parser.Attribute_argument_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#attributes.
    def visitAttributes(self, ctx:Swift5Parser.AttributesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#balanced_tokens.
    def visitBalanced_tokens(self, ctx:Swift5Parser.Balanced_tokensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#balanced_token.
    def visitBalanced_token(self, ctx:Swift5Parser.Balanced_tokenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#balanced_token_punctuation.
    def visitBalanced_token_punctuation(self, ctx:Swift5Parser.Balanced_token_punctuationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#expression.
    def visitExpression(self, ctx:Swift5Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#expression_list.
    def visitExpression_list(self, ctx:Swift5Parser.Expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#prefix_expression.
    def visitPrefix_expression(self, ctx:Swift5Parser.Prefix_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#in_out_expression.
    def visitIn_out_expression(self, ctx:Swift5Parser.In_out_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#try_operator.
    def visitTry_operator(self, ctx:Swift5Parser.Try_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#binary_expression.
    def visitBinary_expression(self, ctx:Swift5Parser.Binary_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#binary_expressions.
    def visitBinary_expressions(self, ctx:Swift5Parser.Binary_expressionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#conditional_operator.
    def visitConditional_operator(self, ctx:Swift5Parser.Conditional_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#type_casting_operator.
    def visitType_casting_operator(self, ctx:Swift5Parser.Type_casting_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#primary_expression.
    def visitPrimary_expression(self, ctx:Swift5Parser.Primary_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#unqualified_name.
    def visitUnqualified_name(self, ctx:Swift5Parser.Unqualified_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#literal_expression.
    def visitLiteral_expression(self, ctx:Swift5Parser.Literal_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#array_literal.
    def visitArray_literal(self, ctx:Swift5Parser.Array_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#array_literal_items.
    def visitArray_literal_items(self, ctx:Swift5Parser.Array_literal_itemsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#array_literal_item.
    def visitArray_literal_item(self, ctx:Swift5Parser.Array_literal_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#dictionary_literal.
    def visitDictionary_literal(self, ctx:Swift5Parser.Dictionary_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#dictionary_literal_items.
    def visitDictionary_literal_items(self, ctx:Swift5Parser.Dictionary_literal_itemsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#dictionary_literal_item.
    def visitDictionary_literal_item(self, ctx:Swift5Parser.Dictionary_literal_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#playground_literal.
    def visitPlayground_literal(self, ctx:Swift5Parser.Playground_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#self_pure_expression.
    def visitSelf_pure_expression(self, ctx:Swift5Parser.Self_pure_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#self_method_expression.
    def visitSelf_method_expression(self, ctx:Swift5Parser.Self_method_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#self_subscript_expression.
    def visitSelf_subscript_expression(self, ctx:Swift5Parser.Self_subscript_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#self_initializer_expression.
    def visitSelf_initializer_expression(self, ctx:Swift5Parser.Self_initializer_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#superclass_method_expression.
    def visitSuperclass_method_expression(self, ctx:Swift5Parser.Superclass_method_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#superclass_subscript_expression.
    def visitSuperclass_subscript_expression(self, ctx:Swift5Parser.Superclass_subscript_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#superclass_initializer_expression.
    def visitSuperclass_initializer_expression(self, ctx:Swift5Parser.Superclass_initializer_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#closure_expression.
    def visitClosure_expression(self, ctx:Swift5Parser.Closure_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#closure_signature.
    def visitClosure_signature(self, ctx:Swift5Parser.Closure_signatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#closure_parameter_clause.
    def visitClosure_parameter_clause(self, ctx:Swift5Parser.Closure_parameter_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#closure_parameter_list.
    def visitClosure_parameter_list(self, ctx:Swift5Parser.Closure_parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#closure_parameter.
    def visitClosure_parameter(self, ctx:Swift5Parser.Closure_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#capture_list.
    def visitCapture_list(self, ctx:Swift5Parser.Capture_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#capture_list_items.
    def visitCapture_list_items(self, ctx:Swift5Parser.Capture_list_itemsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#capture_list_item.
    def visitCapture_list_item(self, ctx:Swift5Parser.Capture_list_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#capture_specifier.
    def visitCapture_specifier(self, ctx:Swift5Parser.Capture_specifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#implicit_member_expression.
    def visitImplicit_member_expression(self, ctx:Swift5Parser.Implicit_member_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#parenthesized_operator.
    def visitParenthesized_operator(self, ctx:Swift5Parser.Parenthesized_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#parenthesized_expression.
    def visitParenthesized_expression(self, ctx:Swift5Parser.Parenthesized_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#tuple_expression.
    def visitTuple_expression(self, ctx:Swift5Parser.Tuple_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#tuple_element_list.
    def visitTuple_element_list(self, ctx:Swift5Parser.Tuple_element_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#tuple_element.
    def visitTuple_element(self, ctx:Swift5Parser.Tuple_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#wildcard_expression.
    def visitWildcard_expression(self, ctx:Swift5Parser.Wildcard_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#key_path_expression.
    def visitKey_path_expression(self, ctx:Swift5Parser.Key_path_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#key_path_components.
    def visitKey_path_components(self, ctx:Swift5Parser.Key_path_componentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#key_path_component.
    def visitKey_path_component(self, ctx:Swift5Parser.Key_path_componentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#key_path_postfixes.
    def visitKey_path_postfixes(self, ctx:Swift5Parser.Key_path_postfixesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#key_path_postfix.
    def visitKey_path_postfix(self, ctx:Swift5Parser.Key_path_postfixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#selector_expression.
    def visitSelector_expression(self, ctx:Swift5Parser.Selector_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#key_path_string_expression.
    def visitKey_path_string_expression(self, ctx:Swift5Parser.Key_path_string_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#postfix_expression.
    def visitPostfix_expression(self, ctx:Swift5Parser.Postfix_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#function_call_suffix.
    def visitFunction_call_suffix(self, ctx:Swift5Parser.Function_call_suffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#initializer_suffix.
    def visitInitializer_suffix(self, ctx:Swift5Parser.Initializer_suffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#explicit_member_suffix.
    def visitExplicit_member_suffix(self, ctx:Swift5Parser.Explicit_member_suffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#postfix_self_suffix.
    def visitPostfix_self_suffix(self, ctx:Swift5Parser.Postfix_self_suffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#subscript_suffix.
    def visitSubscript_suffix(self, ctx:Swift5Parser.Subscript_suffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#forced_value_suffix.
    def visitForced_value_suffix(self, ctx:Swift5Parser.Forced_value_suffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#optional_chaining_suffix.
    def visitOptional_chaining_suffix(self, ctx:Swift5Parser.Optional_chaining_suffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#function_call_argument_clause.
    def visitFunction_call_argument_clause(self, ctx:Swift5Parser.Function_call_argument_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#function_call_argument_list.
    def visitFunction_call_argument_list(self, ctx:Swift5Parser.Function_call_argument_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#function_call_argument.
    def visitFunction_call_argument(self, ctx:Swift5Parser.Function_call_argumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#trailing_closures.
    def visitTrailing_closures(self, ctx:Swift5Parser.Trailing_closuresContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#labeled_trailing_closures.
    def visitLabeled_trailing_closures(self, ctx:Swift5Parser.Labeled_trailing_closuresContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#labeled_trailing_closure.
    def visitLabeled_trailing_closure(self, ctx:Swift5Parser.Labeled_trailing_closureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#argument_names.
    def visitArgument_names(self, ctx:Swift5Parser.Argument_namesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#argument_name.
    def visitArgument_name(self, ctx:Swift5Parser.Argument_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#type.
    def visitType(self, ctx:Swift5Parser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#type_annotation.
    def visitType_annotation(self, ctx:Swift5Parser.Type_annotationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#type_identifier.
    def visitType_identifier(self, ctx:Swift5Parser.Type_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#type_name.
    def visitType_name(self, ctx:Swift5Parser.Type_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#tuple_type.
    def visitTuple_type(self, ctx:Swift5Parser.Tuple_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#tuple_type_element_list.
    def visitTuple_type_element_list(self, ctx:Swift5Parser.Tuple_type_element_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#tuple_type_element.
    def visitTuple_type_element(self, ctx:Swift5Parser.Tuple_type_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#element_name.
    def visitElement_name(self, ctx:Swift5Parser.Element_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#function_type.
    def visitFunction_type(self, ctx:Swift5Parser.Function_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#function_type_argument_clause.
    def visitFunction_type_argument_clause(self, ctx:Swift5Parser.Function_type_argument_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#function_type_argument_list.
    def visitFunction_type_argument_list(self, ctx:Swift5Parser.Function_type_argument_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#function_type_argument.
    def visitFunction_type_argument(self, ctx:Swift5Parser.Function_type_argumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#argument_label.
    def visitArgument_label(self, ctx:Swift5Parser.Argument_labelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#array_type.
    def visitArray_type(self, ctx:Swift5Parser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#dictionary_type.
    def visitDictionary_type(self, ctx:Swift5Parser.Dictionary_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#protocol_composition_type.
    def visitProtocol_composition_type(self, ctx:Swift5Parser.Protocol_composition_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#trailing_composition_and.
    def visitTrailing_composition_and(self, ctx:Swift5Parser.Trailing_composition_andContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#opaque_type.
    def visitOpaque_type(self, ctx:Swift5Parser.Opaque_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#any_type.
    def visitAny_type(self, ctx:Swift5Parser.Any_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#self_type.
    def visitSelf_type(self, ctx:Swift5Parser.Self_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#type_inheritance_clause.
    def visitType_inheritance_clause(self, ctx:Swift5Parser.Type_inheritance_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#type_inheritance_list.
    def visitType_inheritance_list(self, ctx:Swift5Parser.Type_inheritance_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#identifier.
    def visitIdentifier(self, ctx:Swift5Parser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#identifier_list.
    def visitIdentifier_list(self, ctx:Swift5Parser.Identifier_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#keyword.
    def visitKeyword(self, ctx:Swift5Parser.KeywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#assignment_operator.
    def visitAssignment_operator(self, ctx:Swift5Parser.Assignment_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#negate_prefix_operator.
    def visitNegate_prefix_operator(self, ctx:Swift5Parser.Negate_prefix_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#compilation_condition_AND.
    def visitCompilation_condition_AND(self, ctx:Swift5Parser.Compilation_condition_ANDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#compilation_condition_OR.
    def visitCompilation_condition_OR(self, ctx:Swift5Parser.Compilation_condition_ORContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#compilation_condition_GE.
    def visitCompilation_condition_GE(self, ctx:Swift5Parser.Compilation_condition_GEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#compilation_condition_L.
    def visitCompilation_condition_L(self, ctx:Swift5Parser.Compilation_condition_LContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#arrow_operator.
    def visitArrow_operator(self, ctx:Swift5Parser.Arrow_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#range_operator.
    def visitRange_operator(self, ctx:Swift5Parser.Range_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#same_type_equals.
    def visitSame_type_equals(self, ctx:Swift5Parser.Same_type_equalsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#binary_operator.
    def visitBinary_operator(self, ctx:Swift5Parser.Binary_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#prefix_operator.
    def visitPrefix_operator(self, ctx:Swift5Parser.Prefix_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#postfix_operator.
    def visitPostfix_operator(self, ctx:Swift5Parser.Postfix_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#operator.
    def visitOperator(self, ctx:Swift5Parser.OperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#operator_head.
    def visitOperator_head(self, ctx:Swift5Parser.Operator_headContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#operator_character.
    def visitOperator_character(self, ctx:Swift5Parser.Operator_characterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#operator_characters.
    def visitOperator_characters(self, ctx:Swift5Parser.Operator_charactersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#dot_operator_head.
    def visitDot_operator_head(self, ctx:Swift5Parser.Dot_operator_headContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#dot_operator_character.
    def visitDot_operator_character(self, ctx:Swift5Parser.Dot_operator_characterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#dot_operator_characters.
    def visitDot_operator_characters(self, ctx:Swift5Parser.Dot_operator_charactersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#literal.
    def visitLiteral(self, ctx:Swift5Parser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#numeric_literal.
    def visitNumeric_literal(self, ctx:Swift5Parser.Numeric_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#boolean_literal.
    def visitBoolean_literal(self, ctx:Swift5Parser.Boolean_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#nil_literal.
    def visitNil_literal(self, ctx:Swift5Parser.Nil_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#integer_literal.
    def visitInteger_literal(self, ctx:Swift5Parser.Integer_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#string_literal.
    def visitString_literal(self, ctx:Swift5Parser.String_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#extended_string_literal.
    def visitExtended_string_literal(self, ctx:Swift5Parser.Extended_string_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#static_string_literal.
    def visitStatic_string_literal(self, ctx:Swift5Parser.Static_string_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Swift5Parser#interpolated_string_literal.
    def visitInterpolated_string_literal(self, ctx:Swift5Parser.Interpolated_string_literalContext):
        return self.visitChildren(ctx)



del Swift5Parser