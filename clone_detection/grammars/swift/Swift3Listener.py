# Generated from ../clone_detection/grammars/swift/Swift3.g4 by ANTLR 4.7.1
from antlr4 import *
from .Swift3Parser import Swift3Parser

from clone_detection.grammars.grammars_registry import LISTENERS


# This class defines a complete listener for a parse tree produced by Swift3Parser.
@LISTENERS.register('swift')
class Swift3Listener(ParseTreeListener):

    # Enter a parse tree produced by Swift3Parser#top_level.
    def enterTop_level(self, ctx:Swift3Parser.Top_levelContext):
        pass

    # Exit a parse tree produced by Swift3Parser#top_level.
    def exitTop_level(self, ctx:Swift3Parser.Top_levelContext):
        pass


    # Enter a parse tree produced by Swift3Parser#statement.
    def enterStatement(self, ctx:Swift3Parser.StatementContext):
        pass

    # Exit a parse tree produced by Swift3Parser#statement.
    def exitStatement(self, ctx:Swift3Parser.StatementContext):
        pass


    # Enter a parse tree produced by Swift3Parser#statements.
    def enterStatements(self, ctx:Swift3Parser.StatementsContext):
        pass

    # Exit a parse tree produced by Swift3Parser#statements.
    def exitStatements(self, ctx:Swift3Parser.StatementsContext):
        pass


    # Enter a parse tree produced by Swift3Parser#statements_impl.
    def enterStatements_impl(self, ctx:Swift3Parser.Statements_implContext):
        pass

    # Exit a parse tree produced by Swift3Parser#statements_impl.
    def exitStatements_impl(self, ctx:Swift3Parser.Statements_implContext):
        pass


    # Enter a parse tree produced by Swift3Parser#loop_statement.
    def enterLoop_statement(self, ctx:Swift3Parser.Loop_statementContext):
        pass

    # Exit a parse tree produced by Swift3Parser#loop_statement.
    def exitLoop_statement(self, ctx:Swift3Parser.Loop_statementContext):
        pass


    # Enter a parse tree produced by Swift3Parser#for_statement.
    def enterFor_statement(self, ctx:Swift3Parser.For_statementContext):
        pass

    # Exit a parse tree produced by Swift3Parser#for_statement.
    def exitFor_statement(self, ctx:Swift3Parser.For_statementContext):
        pass


    # Enter a parse tree produced by Swift3Parser#for_init.
    def enterFor_init(self, ctx:Swift3Parser.For_initContext):
        pass

    # Exit a parse tree produced by Swift3Parser#for_init.
    def exitFor_init(self, ctx:Swift3Parser.For_initContext):
        pass


    # Enter a parse tree produced by Swift3Parser#for_in_statement.
    def enterFor_in_statement(self, ctx:Swift3Parser.For_in_statementContext):
        pass

    # Exit a parse tree produced by Swift3Parser#for_in_statement.
    def exitFor_in_statement(self, ctx:Swift3Parser.For_in_statementContext):
        pass


    # Enter a parse tree produced by Swift3Parser#while_statement.
    def enterWhile_statement(self, ctx:Swift3Parser.While_statementContext):
        pass

    # Exit a parse tree produced by Swift3Parser#while_statement.
    def exitWhile_statement(self, ctx:Swift3Parser.While_statementContext):
        pass


    # Enter a parse tree produced by Swift3Parser#condition_list.
    def enterCondition_list(self, ctx:Swift3Parser.Condition_listContext):
        pass

    # Exit a parse tree produced by Swift3Parser#condition_list.
    def exitCondition_list(self, ctx:Swift3Parser.Condition_listContext):
        pass


    # Enter a parse tree produced by Swift3Parser#condition.
    def enterCondition(self, ctx:Swift3Parser.ConditionContext):
        pass

    # Exit a parse tree produced by Swift3Parser#condition.
    def exitCondition(self, ctx:Swift3Parser.ConditionContext):
        pass


    # Enter a parse tree produced by Swift3Parser#case_condition.
    def enterCase_condition(self, ctx:Swift3Parser.Case_conditionContext):
        pass

    # Exit a parse tree produced by Swift3Parser#case_condition.
    def exitCase_condition(self, ctx:Swift3Parser.Case_conditionContext):
        pass


    # Enter a parse tree produced by Swift3Parser#optional_binding_condition.
    def enterOptional_binding_condition(self, ctx:Swift3Parser.Optional_binding_conditionContext):
        pass

    # Exit a parse tree produced by Swift3Parser#optional_binding_condition.
    def exitOptional_binding_condition(self, ctx:Swift3Parser.Optional_binding_conditionContext):
        pass


    # Enter a parse tree produced by Swift3Parser#repeat_while_statement.
    def enterRepeat_while_statement(self, ctx:Swift3Parser.Repeat_while_statementContext):
        pass

    # Exit a parse tree produced by Swift3Parser#repeat_while_statement.
    def exitRepeat_while_statement(self, ctx:Swift3Parser.Repeat_while_statementContext):
        pass


    # Enter a parse tree produced by Swift3Parser#branch_statement.
    def enterBranch_statement(self, ctx:Swift3Parser.Branch_statementContext):
        pass

    # Exit a parse tree produced by Swift3Parser#branch_statement.
    def exitBranch_statement(self, ctx:Swift3Parser.Branch_statementContext):
        pass


    # Enter a parse tree produced by Swift3Parser#if_statement.
    def enterIf_statement(self, ctx:Swift3Parser.If_statementContext):
        pass

    # Exit a parse tree produced by Swift3Parser#if_statement.
    def exitIf_statement(self, ctx:Swift3Parser.If_statementContext):
        pass


    # Enter a parse tree produced by Swift3Parser#else_clause.
    def enterElse_clause(self, ctx:Swift3Parser.Else_clauseContext):
        pass

    # Exit a parse tree produced by Swift3Parser#else_clause.
    def exitElse_clause(self, ctx:Swift3Parser.Else_clauseContext):
        pass


    # Enter a parse tree produced by Swift3Parser#guard_statement.
    def enterGuard_statement(self, ctx:Swift3Parser.Guard_statementContext):
        pass

    # Exit a parse tree produced by Swift3Parser#guard_statement.
    def exitGuard_statement(self, ctx:Swift3Parser.Guard_statementContext):
        pass


    # Enter a parse tree produced by Swift3Parser#switch_statement.
    def enterSwitch_statement(self, ctx:Swift3Parser.Switch_statementContext):
        pass

    # Exit a parse tree produced by Swift3Parser#switch_statement.
    def exitSwitch_statement(self, ctx:Swift3Parser.Switch_statementContext):
        pass


    # Enter a parse tree produced by Swift3Parser#switch_cases.
    def enterSwitch_cases(self, ctx:Swift3Parser.Switch_casesContext):
        pass

    # Exit a parse tree produced by Swift3Parser#switch_cases.
    def exitSwitch_cases(self, ctx:Swift3Parser.Switch_casesContext):
        pass


    # Enter a parse tree produced by Swift3Parser#switch_case.
    def enterSwitch_case(self, ctx:Swift3Parser.Switch_caseContext):
        pass

    # Exit a parse tree produced by Swift3Parser#switch_case.
    def exitSwitch_case(self, ctx:Swift3Parser.Switch_caseContext):
        pass


    # Enter a parse tree produced by Swift3Parser#case_label.
    def enterCase_label(self, ctx:Swift3Parser.Case_labelContext):
        pass

    # Exit a parse tree produced by Swift3Parser#case_label.
    def exitCase_label(self, ctx:Swift3Parser.Case_labelContext):
        pass


    # Enter a parse tree produced by Swift3Parser#case_item_list.
    def enterCase_item_list(self, ctx:Swift3Parser.Case_item_listContext):
        pass

    # Exit a parse tree produced by Swift3Parser#case_item_list.
    def exitCase_item_list(self, ctx:Swift3Parser.Case_item_listContext):
        pass


    # Enter a parse tree produced by Swift3Parser#default_label.
    def enterDefault_label(self, ctx:Swift3Parser.Default_labelContext):
        pass

    # Exit a parse tree produced by Swift3Parser#default_label.
    def exitDefault_label(self, ctx:Swift3Parser.Default_labelContext):
        pass


    # Enter a parse tree produced by Swift3Parser#where_clause.
    def enterWhere_clause(self, ctx:Swift3Parser.Where_clauseContext):
        pass

    # Exit a parse tree produced by Swift3Parser#where_clause.
    def exitWhere_clause(self, ctx:Swift3Parser.Where_clauseContext):
        pass


    # Enter a parse tree produced by Swift3Parser#where_expression.
    def enterWhere_expression(self, ctx:Swift3Parser.Where_expressionContext):
        pass

    # Exit a parse tree produced by Swift3Parser#where_expression.
    def exitWhere_expression(self, ctx:Swift3Parser.Where_expressionContext):
        pass


    # Enter a parse tree produced by Swift3Parser#labeled_statement.
    def enterLabeled_statement(self, ctx:Swift3Parser.Labeled_statementContext):
        pass

    # Exit a parse tree produced by Swift3Parser#labeled_statement.
    def exitLabeled_statement(self, ctx:Swift3Parser.Labeled_statementContext):
        pass


    # Enter a parse tree produced by Swift3Parser#statement_label.
    def enterStatement_label(self, ctx:Swift3Parser.Statement_labelContext):
        pass

    # Exit a parse tree produced by Swift3Parser#statement_label.
    def exitStatement_label(self, ctx:Swift3Parser.Statement_labelContext):
        pass


    # Enter a parse tree produced by Swift3Parser#label_name.
    def enterLabel_name(self, ctx:Swift3Parser.Label_nameContext):
        pass

    # Exit a parse tree produced by Swift3Parser#label_name.
    def exitLabel_name(self, ctx:Swift3Parser.Label_nameContext):
        pass


    # Enter a parse tree produced by Swift3Parser#control_transfer_statement.
    def enterControl_transfer_statement(self, ctx:Swift3Parser.Control_transfer_statementContext):
        pass

    # Exit a parse tree produced by Swift3Parser#control_transfer_statement.
    def exitControl_transfer_statement(self, ctx:Swift3Parser.Control_transfer_statementContext):
        pass


    # Enter a parse tree produced by Swift3Parser#break_statement.
    def enterBreak_statement(self, ctx:Swift3Parser.Break_statementContext):
        pass

    # Exit a parse tree produced by Swift3Parser#break_statement.
    def exitBreak_statement(self, ctx:Swift3Parser.Break_statementContext):
        pass


    # Enter a parse tree produced by Swift3Parser#continue_statement.
    def enterContinue_statement(self, ctx:Swift3Parser.Continue_statementContext):
        pass

    # Exit a parse tree produced by Swift3Parser#continue_statement.
    def exitContinue_statement(self, ctx:Swift3Parser.Continue_statementContext):
        pass


    # Enter a parse tree produced by Swift3Parser#fallthrough_statement.
    def enterFallthrough_statement(self, ctx:Swift3Parser.Fallthrough_statementContext):
        pass

    # Exit a parse tree produced by Swift3Parser#fallthrough_statement.
    def exitFallthrough_statement(self, ctx:Swift3Parser.Fallthrough_statementContext):
        pass


    # Enter a parse tree produced by Swift3Parser#return_statement.
    def enterReturn_statement(self, ctx:Swift3Parser.Return_statementContext):
        pass

    # Exit a parse tree produced by Swift3Parser#return_statement.
    def exitReturn_statement(self, ctx:Swift3Parser.Return_statementContext):
        pass


    # Enter a parse tree produced by Swift3Parser#throw_statement.
    def enterThrow_statement(self, ctx:Swift3Parser.Throw_statementContext):
        pass

    # Exit a parse tree produced by Swift3Parser#throw_statement.
    def exitThrow_statement(self, ctx:Swift3Parser.Throw_statementContext):
        pass


    # Enter a parse tree produced by Swift3Parser#defer_statement.
    def enterDefer_statement(self, ctx:Swift3Parser.Defer_statementContext):
        pass

    # Exit a parse tree produced by Swift3Parser#defer_statement.
    def exitDefer_statement(self, ctx:Swift3Parser.Defer_statementContext):
        pass


    # Enter a parse tree produced by Swift3Parser#do_statement.
    def enterDo_statement(self, ctx:Swift3Parser.Do_statementContext):
        pass

    # Exit a parse tree produced by Swift3Parser#do_statement.
    def exitDo_statement(self, ctx:Swift3Parser.Do_statementContext):
        pass


    # Enter a parse tree produced by Swift3Parser#catch_clauses.
    def enterCatch_clauses(self, ctx:Swift3Parser.Catch_clausesContext):
        pass

    # Exit a parse tree produced by Swift3Parser#catch_clauses.
    def exitCatch_clauses(self, ctx:Swift3Parser.Catch_clausesContext):
        pass


    # Enter a parse tree produced by Swift3Parser#catch_clause.
    def enterCatch_clause(self, ctx:Swift3Parser.Catch_clauseContext):
        pass

    # Exit a parse tree produced by Swift3Parser#catch_clause.
    def exitCatch_clause(self, ctx:Swift3Parser.Catch_clauseContext):
        pass


    # Enter a parse tree produced by Swift3Parser#compiler_control_statement.
    def enterCompiler_control_statement(self, ctx:Swift3Parser.Compiler_control_statementContext):
        pass

    # Exit a parse tree produced by Swift3Parser#compiler_control_statement.
    def exitCompiler_control_statement(self, ctx:Swift3Parser.Compiler_control_statementContext):
        pass


    # Enter a parse tree produced by Swift3Parser#conditional_compilation_block.
    def enterConditional_compilation_block(self, ctx:Swift3Parser.Conditional_compilation_blockContext):
        pass

    # Exit a parse tree produced by Swift3Parser#conditional_compilation_block.
    def exitConditional_compilation_block(self, ctx:Swift3Parser.Conditional_compilation_blockContext):
        pass


    # Enter a parse tree produced by Swift3Parser#if_directive_clause.
    def enterIf_directive_clause(self, ctx:Swift3Parser.If_directive_clauseContext):
        pass

    # Exit a parse tree produced by Swift3Parser#if_directive_clause.
    def exitIf_directive_clause(self, ctx:Swift3Parser.If_directive_clauseContext):
        pass


    # Enter a parse tree produced by Swift3Parser#elseif_directive_clauses.
    def enterElseif_directive_clauses(self, ctx:Swift3Parser.Elseif_directive_clausesContext):
        pass

    # Exit a parse tree produced by Swift3Parser#elseif_directive_clauses.
    def exitElseif_directive_clauses(self, ctx:Swift3Parser.Elseif_directive_clausesContext):
        pass


    # Enter a parse tree produced by Swift3Parser#elseif_directive_clause.
    def enterElseif_directive_clause(self, ctx:Swift3Parser.Elseif_directive_clauseContext):
        pass

    # Exit a parse tree produced by Swift3Parser#elseif_directive_clause.
    def exitElseif_directive_clause(self, ctx:Swift3Parser.Elseif_directive_clauseContext):
        pass


    # Enter a parse tree produced by Swift3Parser#else_directive_clause.
    def enterElse_directive_clause(self, ctx:Swift3Parser.Else_directive_clauseContext):
        pass

    # Exit a parse tree produced by Swift3Parser#else_directive_clause.
    def exitElse_directive_clause(self, ctx:Swift3Parser.Else_directive_clauseContext):
        pass


    # Enter a parse tree produced by Swift3Parser#if_directive.
    def enterIf_directive(self, ctx:Swift3Parser.If_directiveContext):
        pass

    # Exit a parse tree produced by Swift3Parser#if_directive.
    def exitIf_directive(self, ctx:Swift3Parser.If_directiveContext):
        pass


    # Enter a parse tree produced by Swift3Parser#elseif_directive.
    def enterElseif_directive(self, ctx:Swift3Parser.Elseif_directiveContext):
        pass

    # Exit a parse tree produced by Swift3Parser#elseif_directive.
    def exitElseif_directive(self, ctx:Swift3Parser.Elseif_directiveContext):
        pass


    # Enter a parse tree produced by Swift3Parser#else_directive.
    def enterElse_directive(self, ctx:Swift3Parser.Else_directiveContext):
        pass

    # Exit a parse tree produced by Swift3Parser#else_directive.
    def exitElse_directive(self, ctx:Swift3Parser.Else_directiveContext):
        pass


    # Enter a parse tree produced by Swift3Parser#endif_directive.
    def enterEndif_directive(self, ctx:Swift3Parser.Endif_directiveContext):
        pass

    # Exit a parse tree produced by Swift3Parser#endif_directive.
    def exitEndif_directive(self, ctx:Swift3Parser.Endif_directiveContext):
        pass


    # Enter a parse tree produced by Swift3Parser#compilation_condition.
    def enterCompilation_condition(self, ctx:Swift3Parser.Compilation_conditionContext):
        pass

    # Exit a parse tree produced by Swift3Parser#compilation_condition.
    def exitCompilation_condition(self, ctx:Swift3Parser.Compilation_conditionContext):
        pass


    # Enter a parse tree produced by Swift3Parser#platform_condition.
    def enterPlatform_condition(self, ctx:Swift3Parser.Platform_conditionContext):
        pass

    # Exit a parse tree produced by Swift3Parser#platform_condition.
    def exitPlatform_condition(self, ctx:Swift3Parser.Platform_conditionContext):
        pass


    # Enter a parse tree produced by Swift3Parser#swift_version.
    def enterSwift_version(self, ctx:Swift3Parser.Swift_versionContext):
        pass

    # Exit a parse tree produced by Swift3Parser#swift_version.
    def exitSwift_version(self, ctx:Swift3Parser.Swift_versionContext):
        pass


    # Enter a parse tree produced by Swift3Parser#operating_system.
    def enterOperating_system(self, ctx:Swift3Parser.Operating_systemContext):
        pass

    # Exit a parse tree produced by Swift3Parser#operating_system.
    def exitOperating_system(self, ctx:Swift3Parser.Operating_systemContext):
        pass


    # Enter a parse tree produced by Swift3Parser#architecture.
    def enterArchitecture(self, ctx:Swift3Parser.ArchitectureContext):
        pass

    # Exit a parse tree produced by Swift3Parser#architecture.
    def exitArchitecture(self, ctx:Swift3Parser.ArchitectureContext):
        pass


    # Enter a parse tree produced by Swift3Parser#line_control_statement.
    def enterLine_control_statement(self, ctx:Swift3Parser.Line_control_statementContext):
        pass

    # Exit a parse tree produced by Swift3Parser#line_control_statement.
    def exitLine_control_statement(self, ctx:Swift3Parser.Line_control_statementContext):
        pass


    # Enter a parse tree produced by Swift3Parser#line_number.
    def enterLine_number(self, ctx:Swift3Parser.Line_numberContext):
        pass

    # Exit a parse tree produced by Swift3Parser#line_number.
    def exitLine_number(self, ctx:Swift3Parser.Line_numberContext):
        pass


    # Enter a parse tree produced by Swift3Parser#file_name.
    def enterFile_name(self, ctx:Swift3Parser.File_nameContext):
        pass

    # Exit a parse tree produced by Swift3Parser#file_name.
    def exitFile_name(self, ctx:Swift3Parser.File_nameContext):
        pass


    # Enter a parse tree produced by Swift3Parser#availability_condition.
    def enterAvailability_condition(self, ctx:Swift3Parser.Availability_conditionContext):
        pass

    # Exit a parse tree produced by Swift3Parser#availability_condition.
    def exitAvailability_condition(self, ctx:Swift3Parser.Availability_conditionContext):
        pass


    # Enter a parse tree produced by Swift3Parser#availability_arguments.
    def enterAvailability_arguments(self, ctx:Swift3Parser.Availability_argumentsContext):
        pass

    # Exit a parse tree produced by Swift3Parser#availability_arguments.
    def exitAvailability_arguments(self, ctx:Swift3Parser.Availability_argumentsContext):
        pass


    # Enter a parse tree produced by Swift3Parser#availability_argument.
    def enterAvailability_argument(self, ctx:Swift3Parser.Availability_argumentContext):
        pass

    # Exit a parse tree produced by Swift3Parser#availability_argument.
    def exitAvailability_argument(self, ctx:Swift3Parser.Availability_argumentContext):
        pass


    # Enter a parse tree produced by Swift3Parser#generic_parameter_clause.
    def enterGeneric_parameter_clause(self, ctx:Swift3Parser.Generic_parameter_clauseContext):
        pass

    # Exit a parse tree produced by Swift3Parser#generic_parameter_clause.
    def exitGeneric_parameter_clause(self, ctx:Swift3Parser.Generic_parameter_clauseContext):
        pass


    # Enter a parse tree produced by Swift3Parser#generic_parameter_list.
    def enterGeneric_parameter_list(self, ctx:Swift3Parser.Generic_parameter_listContext):
        pass

    # Exit a parse tree produced by Swift3Parser#generic_parameter_list.
    def exitGeneric_parameter_list(self, ctx:Swift3Parser.Generic_parameter_listContext):
        pass


    # Enter a parse tree produced by Swift3Parser#generic_parameter.
    def enterGeneric_parameter(self, ctx:Swift3Parser.Generic_parameterContext):
        pass

    # Exit a parse tree produced by Swift3Parser#generic_parameter.
    def exitGeneric_parameter(self, ctx:Swift3Parser.Generic_parameterContext):
        pass


    # Enter a parse tree produced by Swift3Parser#generic_where_clause.
    def enterGeneric_where_clause(self, ctx:Swift3Parser.Generic_where_clauseContext):
        pass

    # Exit a parse tree produced by Swift3Parser#generic_where_clause.
    def exitGeneric_where_clause(self, ctx:Swift3Parser.Generic_where_clauseContext):
        pass


    # Enter a parse tree produced by Swift3Parser#requirement_list.
    def enterRequirement_list(self, ctx:Swift3Parser.Requirement_listContext):
        pass

    # Exit a parse tree produced by Swift3Parser#requirement_list.
    def exitRequirement_list(self, ctx:Swift3Parser.Requirement_listContext):
        pass


    # Enter a parse tree produced by Swift3Parser#requirement.
    def enterRequirement(self, ctx:Swift3Parser.RequirementContext):
        pass

    # Exit a parse tree produced by Swift3Parser#requirement.
    def exitRequirement(self, ctx:Swift3Parser.RequirementContext):
        pass


    # Enter a parse tree produced by Swift3Parser#conformance_requirement.
    def enterConformance_requirement(self, ctx:Swift3Parser.Conformance_requirementContext):
        pass

    # Exit a parse tree produced by Swift3Parser#conformance_requirement.
    def exitConformance_requirement(self, ctx:Swift3Parser.Conformance_requirementContext):
        pass


    # Enter a parse tree produced by Swift3Parser#same_type_requirement.
    def enterSame_type_requirement(self, ctx:Swift3Parser.Same_type_requirementContext):
        pass

    # Exit a parse tree produced by Swift3Parser#same_type_requirement.
    def exitSame_type_requirement(self, ctx:Swift3Parser.Same_type_requirementContext):
        pass


    # Enter a parse tree produced by Swift3Parser#generic_argument_clause.
    def enterGeneric_argument_clause(self, ctx:Swift3Parser.Generic_argument_clauseContext):
        pass

    # Exit a parse tree produced by Swift3Parser#generic_argument_clause.
    def exitGeneric_argument_clause(self, ctx:Swift3Parser.Generic_argument_clauseContext):
        pass


    # Enter a parse tree produced by Swift3Parser#generic_argument_list.
    def enterGeneric_argument_list(self, ctx:Swift3Parser.Generic_argument_listContext):
        pass

    # Exit a parse tree produced by Swift3Parser#generic_argument_list.
    def exitGeneric_argument_list(self, ctx:Swift3Parser.Generic_argument_listContext):
        pass


    # Enter a parse tree produced by Swift3Parser#generic_argument.
    def enterGeneric_argument(self, ctx:Swift3Parser.Generic_argumentContext):
        pass

    # Exit a parse tree produced by Swift3Parser#generic_argument.
    def exitGeneric_argument(self, ctx:Swift3Parser.Generic_argumentContext):
        pass


    # Enter a parse tree produced by Swift3Parser#declaration.
    def enterDeclaration(self, ctx:Swift3Parser.DeclarationContext):
        pass

    # Exit a parse tree produced by Swift3Parser#declaration.
    def exitDeclaration(self, ctx:Swift3Parser.DeclarationContext):
        pass


    # Enter a parse tree produced by Swift3Parser#declarations.
    def enterDeclarations(self, ctx:Swift3Parser.DeclarationsContext):
        pass

    # Exit a parse tree produced by Swift3Parser#declarations.
    def exitDeclarations(self, ctx:Swift3Parser.DeclarationsContext):
        pass


    # Enter a parse tree produced by Swift3Parser#top_level_declaration.
    def enterTop_level_declaration(self, ctx:Swift3Parser.Top_level_declarationContext):
        pass

    # Exit a parse tree produced by Swift3Parser#top_level_declaration.
    def exitTop_level_declaration(self, ctx:Swift3Parser.Top_level_declarationContext):
        pass


    # Enter a parse tree produced by Swift3Parser#code_block.
    def enterCode_block(self, ctx:Swift3Parser.Code_blockContext):
        pass

    # Exit a parse tree produced by Swift3Parser#code_block.
    def exitCode_block(self, ctx:Swift3Parser.Code_blockContext):
        pass


    # Enter a parse tree produced by Swift3Parser#import_declaration.
    def enterImport_declaration(self, ctx:Swift3Parser.Import_declarationContext):
        pass

    # Exit a parse tree produced by Swift3Parser#import_declaration.
    def exitImport_declaration(self, ctx:Swift3Parser.Import_declarationContext):
        pass


    # Enter a parse tree produced by Swift3Parser#import_kind.
    def enterImport_kind(self, ctx:Swift3Parser.Import_kindContext):
        pass

    # Exit a parse tree produced by Swift3Parser#import_kind.
    def exitImport_kind(self, ctx:Swift3Parser.Import_kindContext):
        pass


    # Enter a parse tree produced by Swift3Parser#import_path.
    def enterImport_path(self, ctx:Swift3Parser.Import_pathContext):
        pass

    # Exit a parse tree produced by Swift3Parser#import_path.
    def exitImport_path(self, ctx:Swift3Parser.Import_pathContext):
        pass


    # Enter a parse tree produced by Swift3Parser#import_path_identifier.
    def enterImport_path_identifier(self, ctx:Swift3Parser.Import_path_identifierContext):
        pass

    # Exit a parse tree produced by Swift3Parser#import_path_identifier.
    def exitImport_path_identifier(self, ctx:Swift3Parser.Import_path_identifierContext):
        pass


    # Enter a parse tree produced by Swift3Parser#constant_declaration.
    def enterConstant_declaration(self, ctx:Swift3Parser.Constant_declarationContext):
        pass

    # Exit a parse tree produced by Swift3Parser#constant_declaration.
    def exitConstant_declaration(self, ctx:Swift3Parser.Constant_declarationContext):
        pass


    # Enter a parse tree produced by Swift3Parser#pattern_initializer_list.
    def enterPattern_initializer_list(self, ctx:Swift3Parser.Pattern_initializer_listContext):
        pass

    # Exit a parse tree produced by Swift3Parser#pattern_initializer_list.
    def exitPattern_initializer_list(self, ctx:Swift3Parser.Pattern_initializer_listContext):
        pass


    # Enter a parse tree produced by Swift3Parser#pattern_initializer.
    def enterPattern_initializer(self, ctx:Swift3Parser.Pattern_initializerContext):
        pass

    # Exit a parse tree produced by Swift3Parser#pattern_initializer.
    def exitPattern_initializer(self, ctx:Swift3Parser.Pattern_initializerContext):
        pass


    # Enter a parse tree produced by Swift3Parser#initializer.
    def enterInitializer(self, ctx:Swift3Parser.InitializerContext):
        pass

    # Exit a parse tree produced by Swift3Parser#initializer.
    def exitInitializer(self, ctx:Swift3Parser.InitializerContext):
        pass


    # Enter a parse tree produced by Swift3Parser#variable_declaration.
    def enterVariable_declaration(self, ctx:Swift3Parser.Variable_declarationContext):
        pass

    # Exit a parse tree produced by Swift3Parser#variable_declaration.
    def exitVariable_declaration(self, ctx:Swift3Parser.Variable_declarationContext):
        pass


    # Enter a parse tree produced by Swift3Parser#variable_declaration_head.
    def enterVariable_declaration_head(self, ctx:Swift3Parser.Variable_declaration_headContext):
        pass

    # Exit a parse tree produced by Swift3Parser#variable_declaration_head.
    def exitVariable_declaration_head(self, ctx:Swift3Parser.Variable_declaration_headContext):
        pass


    # Enter a parse tree produced by Swift3Parser#variable_name.
    def enterVariable_name(self, ctx:Swift3Parser.Variable_nameContext):
        pass

    # Exit a parse tree produced by Swift3Parser#variable_name.
    def exitVariable_name(self, ctx:Swift3Parser.Variable_nameContext):
        pass


    # Enter a parse tree produced by Swift3Parser#getter_setter_block.
    def enterGetter_setter_block(self, ctx:Swift3Parser.Getter_setter_blockContext):
        pass

    # Exit a parse tree produced by Swift3Parser#getter_setter_block.
    def exitGetter_setter_block(self, ctx:Swift3Parser.Getter_setter_blockContext):
        pass


    # Enter a parse tree produced by Swift3Parser#getter_clause.
    def enterGetter_clause(self, ctx:Swift3Parser.Getter_clauseContext):
        pass

    # Exit a parse tree produced by Swift3Parser#getter_clause.
    def exitGetter_clause(self, ctx:Swift3Parser.Getter_clauseContext):
        pass


    # Enter a parse tree produced by Swift3Parser#setter_clause.
    def enterSetter_clause(self, ctx:Swift3Parser.Setter_clauseContext):
        pass

    # Exit a parse tree produced by Swift3Parser#setter_clause.
    def exitSetter_clause(self, ctx:Swift3Parser.Setter_clauseContext):
        pass


    # Enter a parse tree produced by Swift3Parser#setter_name.
    def enterSetter_name(self, ctx:Swift3Parser.Setter_nameContext):
        pass

    # Exit a parse tree produced by Swift3Parser#setter_name.
    def exitSetter_name(self, ctx:Swift3Parser.Setter_nameContext):
        pass


    # Enter a parse tree produced by Swift3Parser#getter_setter_keyword_block.
    def enterGetter_setter_keyword_block(self, ctx:Swift3Parser.Getter_setter_keyword_blockContext):
        pass

    # Exit a parse tree produced by Swift3Parser#getter_setter_keyword_block.
    def exitGetter_setter_keyword_block(self, ctx:Swift3Parser.Getter_setter_keyword_blockContext):
        pass


    # Enter a parse tree produced by Swift3Parser#getter_keyword_clause.
    def enterGetter_keyword_clause(self, ctx:Swift3Parser.Getter_keyword_clauseContext):
        pass

    # Exit a parse tree produced by Swift3Parser#getter_keyword_clause.
    def exitGetter_keyword_clause(self, ctx:Swift3Parser.Getter_keyword_clauseContext):
        pass


    # Enter a parse tree produced by Swift3Parser#setter_keyword_clause.
    def enterSetter_keyword_clause(self, ctx:Swift3Parser.Setter_keyword_clauseContext):
        pass

    # Exit a parse tree produced by Swift3Parser#setter_keyword_clause.
    def exitSetter_keyword_clause(self, ctx:Swift3Parser.Setter_keyword_clauseContext):
        pass


    # Enter a parse tree produced by Swift3Parser#willSet_didSet_block.
    def enterWillSet_didSet_block(self, ctx:Swift3Parser.WillSet_didSet_blockContext):
        pass

    # Exit a parse tree produced by Swift3Parser#willSet_didSet_block.
    def exitWillSet_didSet_block(self, ctx:Swift3Parser.WillSet_didSet_blockContext):
        pass


    # Enter a parse tree produced by Swift3Parser#willSet_clause.
    def enterWillSet_clause(self, ctx:Swift3Parser.WillSet_clauseContext):
        pass

    # Exit a parse tree produced by Swift3Parser#willSet_clause.
    def exitWillSet_clause(self, ctx:Swift3Parser.WillSet_clauseContext):
        pass


    # Enter a parse tree produced by Swift3Parser#didSet_clause.
    def enterDidSet_clause(self, ctx:Swift3Parser.DidSet_clauseContext):
        pass

    # Exit a parse tree produced by Swift3Parser#didSet_clause.
    def exitDidSet_clause(self, ctx:Swift3Parser.DidSet_clauseContext):
        pass


    # Enter a parse tree produced by Swift3Parser#typealias_declaration.
    def enterTypealias_declaration(self, ctx:Swift3Parser.Typealias_declarationContext):
        pass

    # Exit a parse tree produced by Swift3Parser#typealias_declaration.
    def exitTypealias_declaration(self, ctx:Swift3Parser.Typealias_declarationContext):
        pass


    # Enter a parse tree produced by Swift3Parser#typealias_name.
    def enterTypealias_name(self, ctx:Swift3Parser.Typealias_nameContext):
        pass

    # Exit a parse tree produced by Swift3Parser#typealias_name.
    def exitTypealias_name(self, ctx:Swift3Parser.Typealias_nameContext):
        pass


    # Enter a parse tree produced by Swift3Parser#typealias_assignment.
    def enterTypealias_assignment(self, ctx:Swift3Parser.Typealias_assignmentContext):
        pass

    # Exit a parse tree produced by Swift3Parser#typealias_assignment.
    def exitTypealias_assignment(self, ctx:Swift3Parser.Typealias_assignmentContext):
        pass


    # Enter a parse tree produced by Swift3Parser#function_declaration.
    def enterFunction_declaration(self, ctx:Swift3Parser.Function_declarationContext):
        pass

    # Exit a parse tree produced by Swift3Parser#function_declaration.
    def exitFunction_declaration(self, ctx:Swift3Parser.Function_declarationContext):
        pass


    # Enter a parse tree produced by Swift3Parser#function_head.
    def enterFunction_head(self, ctx:Swift3Parser.Function_headContext):
        pass

    # Exit a parse tree produced by Swift3Parser#function_head.
    def exitFunction_head(self, ctx:Swift3Parser.Function_headContext):
        pass


    # Enter a parse tree produced by Swift3Parser#function_name.
    def enterFunction_name(self, ctx:Swift3Parser.Function_nameContext):
        pass

    # Exit a parse tree produced by Swift3Parser#function_name.
    def exitFunction_name(self, ctx:Swift3Parser.Function_nameContext):
        pass


    # Enter a parse tree produced by Swift3Parser#function_signature.
    def enterFunction_signature(self, ctx:Swift3Parser.Function_signatureContext):
        pass

    # Exit a parse tree produced by Swift3Parser#function_signature.
    def exitFunction_signature(self, ctx:Swift3Parser.Function_signatureContext):
        pass


    # Enter a parse tree produced by Swift3Parser#function_result.
    def enterFunction_result(self, ctx:Swift3Parser.Function_resultContext):
        pass

    # Exit a parse tree produced by Swift3Parser#function_result.
    def exitFunction_result(self, ctx:Swift3Parser.Function_resultContext):
        pass


    # Enter a parse tree produced by Swift3Parser#function_body.
    def enterFunction_body(self, ctx:Swift3Parser.Function_bodyContext):
        pass

    # Exit a parse tree produced by Swift3Parser#function_body.
    def exitFunction_body(self, ctx:Swift3Parser.Function_bodyContext):
        pass


    # Enter a parse tree produced by Swift3Parser#parameter_clause.
    def enterParameter_clause(self, ctx:Swift3Parser.Parameter_clauseContext):
        pass

    # Exit a parse tree produced by Swift3Parser#parameter_clause.
    def exitParameter_clause(self, ctx:Swift3Parser.Parameter_clauseContext):
        pass


    # Enter a parse tree produced by Swift3Parser#parameter_list.
    def enterParameter_list(self, ctx:Swift3Parser.Parameter_listContext):
        pass

    # Exit a parse tree produced by Swift3Parser#parameter_list.
    def exitParameter_list(self, ctx:Swift3Parser.Parameter_listContext):
        pass


    # Enter a parse tree produced by Swift3Parser#parameter.
    def enterParameter(self, ctx:Swift3Parser.ParameterContext):
        pass

    # Exit a parse tree produced by Swift3Parser#parameter.
    def exitParameter(self, ctx:Swift3Parser.ParameterContext):
        pass


    # Enter a parse tree produced by Swift3Parser#external_parameter_name.
    def enterExternal_parameter_name(self, ctx:Swift3Parser.External_parameter_nameContext):
        pass

    # Exit a parse tree produced by Swift3Parser#external_parameter_name.
    def exitExternal_parameter_name(self, ctx:Swift3Parser.External_parameter_nameContext):
        pass


    # Enter a parse tree produced by Swift3Parser#local_parameter_name.
    def enterLocal_parameter_name(self, ctx:Swift3Parser.Local_parameter_nameContext):
        pass

    # Exit a parse tree produced by Swift3Parser#local_parameter_name.
    def exitLocal_parameter_name(self, ctx:Swift3Parser.Local_parameter_nameContext):
        pass


    # Enter a parse tree produced by Swift3Parser#default_argument_clause.
    def enterDefault_argument_clause(self, ctx:Swift3Parser.Default_argument_clauseContext):
        pass

    # Exit a parse tree produced by Swift3Parser#default_argument_clause.
    def exitDefault_argument_clause(self, ctx:Swift3Parser.Default_argument_clauseContext):
        pass


    # Enter a parse tree produced by Swift3Parser#enum_declaration.
    def enterEnum_declaration(self, ctx:Swift3Parser.Enum_declarationContext):
        pass

    # Exit a parse tree produced by Swift3Parser#enum_declaration.
    def exitEnum_declaration(self, ctx:Swift3Parser.Enum_declarationContext):
        pass


    # Enter a parse tree produced by Swift3Parser#union_style_enum.
    def enterUnion_style_enum(self, ctx:Swift3Parser.Union_style_enumContext):
        pass

    # Exit a parse tree produced by Swift3Parser#union_style_enum.
    def exitUnion_style_enum(self, ctx:Swift3Parser.Union_style_enumContext):
        pass


    # Enter a parse tree produced by Swift3Parser#union_style_enum_members.
    def enterUnion_style_enum_members(self, ctx:Swift3Parser.Union_style_enum_membersContext):
        pass

    # Exit a parse tree produced by Swift3Parser#union_style_enum_members.
    def exitUnion_style_enum_members(self, ctx:Swift3Parser.Union_style_enum_membersContext):
        pass


    # Enter a parse tree produced by Swift3Parser#union_style_enum_member.
    def enterUnion_style_enum_member(self, ctx:Swift3Parser.Union_style_enum_memberContext):
        pass

    # Exit a parse tree produced by Swift3Parser#union_style_enum_member.
    def exitUnion_style_enum_member(self, ctx:Swift3Parser.Union_style_enum_memberContext):
        pass


    # Enter a parse tree produced by Swift3Parser#union_style_enum_case_clause.
    def enterUnion_style_enum_case_clause(self, ctx:Swift3Parser.Union_style_enum_case_clauseContext):
        pass

    # Exit a parse tree produced by Swift3Parser#union_style_enum_case_clause.
    def exitUnion_style_enum_case_clause(self, ctx:Swift3Parser.Union_style_enum_case_clauseContext):
        pass


    # Enter a parse tree produced by Swift3Parser#union_style_enum_case_list.
    def enterUnion_style_enum_case_list(self, ctx:Swift3Parser.Union_style_enum_case_listContext):
        pass

    # Exit a parse tree produced by Swift3Parser#union_style_enum_case_list.
    def exitUnion_style_enum_case_list(self, ctx:Swift3Parser.Union_style_enum_case_listContext):
        pass


    # Enter a parse tree produced by Swift3Parser#union_style_enum_case.
    def enterUnion_style_enum_case(self, ctx:Swift3Parser.Union_style_enum_caseContext):
        pass

    # Exit a parse tree produced by Swift3Parser#union_style_enum_case.
    def exitUnion_style_enum_case(self, ctx:Swift3Parser.Union_style_enum_caseContext):
        pass


    # Enter a parse tree produced by Swift3Parser#enum_name.
    def enterEnum_name(self, ctx:Swift3Parser.Enum_nameContext):
        pass

    # Exit a parse tree produced by Swift3Parser#enum_name.
    def exitEnum_name(self, ctx:Swift3Parser.Enum_nameContext):
        pass


    # Enter a parse tree produced by Swift3Parser#enum_case_name.
    def enterEnum_case_name(self, ctx:Swift3Parser.Enum_case_nameContext):
        pass

    # Exit a parse tree produced by Swift3Parser#enum_case_name.
    def exitEnum_case_name(self, ctx:Swift3Parser.Enum_case_nameContext):
        pass


    # Enter a parse tree produced by Swift3Parser#raw_value_style_enum.
    def enterRaw_value_style_enum(self, ctx:Swift3Parser.Raw_value_style_enumContext):
        pass

    # Exit a parse tree produced by Swift3Parser#raw_value_style_enum.
    def exitRaw_value_style_enum(self, ctx:Swift3Parser.Raw_value_style_enumContext):
        pass


    # Enter a parse tree produced by Swift3Parser#raw_value_style_enum_members.
    def enterRaw_value_style_enum_members(self, ctx:Swift3Parser.Raw_value_style_enum_membersContext):
        pass

    # Exit a parse tree produced by Swift3Parser#raw_value_style_enum_members.
    def exitRaw_value_style_enum_members(self, ctx:Swift3Parser.Raw_value_style_enum_membersContext):
        pass


    # Enter a parse tree produced by Swift3Parser#raw_value_style_enum_member.
    def enterRaw_value_style_enum_member(self, ctx:Swift3Parser.Raw_value_style_enum_memberContext):
        pass

    # Exit a parse tree produced by Swift3Parser#raw_value_style_enum_member.
    def exitRaw_value_style_enum_member(self, ctx:Swift3Parser.Raw_value_style_enum_memberContext):
        pass


    # Enter a parse tree produced by Swift3Parser#raw_value_style_enum_case_clause.
    def enterRaw_value_style_enum_case_clause(self, ctx:Swift3Parser.Raw_value_style_enum_case_clauseContext):
        pass

    # Exit a parse tree produced by Swift3Parser#raw_value_style_enum_case_clause.
    def exitRaw_value_style_enum_case_clause(self, ctx:Swift3Parser.Raw_value_style_enum_case_clauseContext):
        pass


    # Enter a parse tree produced by Swift3Parser#raw_value_style_enum_case_list.
    def enterRaw_value_style_enum_case_list(self, ctx:Swift3Parser.Raw_value_style_enum_case_listContext):
        pass

    # Exit a parse tree produced by Swift3Parser#raw_value_style_enum_case_list.
    def exitRaw_value_style_enum_case_list(self, ctx:Swift3Parser.Raw_value_style_enum_case_listContext):
        pass


    # Enter a parse tree produced by Swift3Parser#raw_value_style_enum_case.
    def enterRaw_value_style_enum_case(self, ctx:Swift3Parser.Raw_value_style_enum_caseContext):
        pass

    # Exit a parse tree produced by Swift3Parser#raw_value_style_enum_case.
    def exitRaw_value_style_enum_case(self, ctx:Swift3Parser.Raw_value_style_enum_caseContext):
        pass


    # Enter a parse tree produced by Swift3Parser#raw_value_assignment.
    def enterRaw_value_assignment(self, ctx:Swift3Parser.Raw_value_assignmentContext):
        pass

    # Exit a parse tree produced by Swift3Parser#raw_value_assignment.
    def exitRaw_value_assignment(self, ctx:Swift3Parser.Raw_value_assignmentContext):
        pass


    # Enter a parse tree produced by Swift3Parser#raw_value_literal.
    def enterRaw_value_literal(self, ctx:Swift3Parser.Raw_value_literalContext):
        pass

    # Exit a parse tree produced by Swift3Parser#raw_value_literal.
    def exitRaw_value_literal(self, ctx:Swift3Parser.Raw_value_literalContext):
        pass


    # Enter a parse tree produced by Swift3Parser#struct_declaration.
    def enterStruct_declaration(self, ctx:Swift3Parser.Struct_declarationContext):
        pass

    # Exit a parse tree produced by Swift3Parser#struct_declaration.
    def exitStruct_declaration(self, ctx:Swift3Parser.Struct_declarationContext):
        pass


    # Enter a parse tree produced by Swift3Parser#struct_name.
    def enterStruct_name(self, ctx:Swift3Parser.Struct_nameContext):
        pass

    # Exit a parse tree produced by Swift3Parser#struct_name.
    def exitStruct_name(self, ctx:Swift3Parser.Struct_nameContext):
        pass


    # Enter a parse tree produced by Swift3Parser#struct_body.
    def enterStruct_body(self, ctx:Swift3Parser.Struct_bodyContext):
        pass

    # Exit a parse tree produced by Swift3Parser#struct_body.
    def exitStruct_body(self, ctx:Swift3Parser.Struct_bodyContext):
        pass


    # Enter a parse tree produced by Swift3Parser#struct_member.
    def enterStruct_member(self, ctx:Swift3Parser.Struct_memberContext):
        pass

    # Exit a parse tree produced by Swift3Parser#struct_member.
    def exitStruct_member(self, ctx:Swift3Parser.Struct_memberContext):
        pass


    # Enter a parse tree produced by Swift3Parser#class_declaration.
    def enterClass_declaration(self, ctx:Swift3Parser.Class_declarationContext):
        pass

    # Exit a parse tree produced by Swift3Parser#class_declaration.
    def exitClass_declaration(self, ctx:Swift3Parser.Class_declarationContext):
        pass


    # Enter a parse tree produced by Swift3Parser#class_name.
    def enterClass_name(self, ctx:Swift3Parser.Class_nameContext):
        pass

    # Exit a parse tree produced by Swift3Parser#class_name.
    def exitClass_name(self, ctx:Swift3Parser.Class_nameContext):
        pass


    # Enter a parse tree produced by Swift3Parser#class_body.
    def enterClass_body(self, ctx:Swift3Parser.Class_bodyContext):
        pass

    # Exit a parse tree produced by Swift3Parser#class_body.
    def exitClass_body(self, ctx:Swift3Parser.Class_bodyContext):
        pass


    # Enter a parse tree produced by Swift3Parser#class_member.
    def enterClass_member(self, ctx:Swift3Parser.Class_memberContext):
        pass

    # Exit a parse tree produced by Swift3Parser#class_member.
    def exitClass_member(self, ctx:Swift3Parser.Class_memberContext):
        pass


    # Enter a parse tree produced by Swift3Parser#protocol_declaration.
    def enterProtocol_declaration(self, ctx:Swift3Parser.Protocol_declarationContext):
        pass

    # Exit a parse tree produced by Swift3Parser#protocol_declaration.
    def exitProtocol_declaration(self, ctx:Swift3Parser.Protocol_declarationContext):
        pass


    # Enter a parse tree produced by Swift3Parser#protocol_name.
    def enterProtocol_name(self, ctx:Swift3Parser.Protocol_nameContext):
        pass

    # Exit a parse tree produced by Swift3Parser#protocol_name.
    def exitProtocol_name(self, ctx:Swift3Parser.Protocol_nameContext):
        pass


    # Enter a parse tree produced by Swift3Parser#protocol_body.
    def enterProtocol_body(self, ctx:Swift3Parser.Protocol_bodyContext):
        pass

    # Exit a parse tree produced by Swift3Parser#protocol_body.
    def exitProtocol_body(self, ctx:Swift3Parser.Protocol_bodyContext):
        pass


    # Enter a parse tree produced by Swift3Parser#protocol_member.
    def enterProtocol_member(self, ctx:Swift3Parser.Protocol_memberContext):
        pass

    # Exit a parse tree produced by Swift3Parser#protocol_member.
    def exitProtocol_member(self, ctx:Swift3Parser.Protocol_memberContext):
        pass


    # Enter a parse tree produced by Swift3Parser#protocol_member_declaration.
    def enterProtocol_member_declaration(self, ctx:Swift3Parser.Protocol_member_declarationContext):
        pass

    # Exit a parse tree produced by Swift3Parser#protocol_member_declaration.
    def exitProtocol_member_declaration(self, ctx:Swift3Parser.Protocol_member_declarationContext):
        pass


    # Enter a parse tree produced by Swift3Parser#protocol_property_declaration.
    def enterProtocol_property_declaration(self, ctx:Swift3Parser.Protocol_property_declarationContext):
        pass

    # Exit a parse tree produced by Swift3Parser#protocol_property_declaration.
    def exitProtocol_property_declaration(self, ctx:Swift3Parser.Protocol_property_declarationContext):
        pass


    # Enter a parse tree produced by Swift3Parser#protocol_method_declaration.
    def enterProtocol_method_declaration(self, ctx:Swift3Parser.Protocol_method_declarationContext):
        pass

    # Exit a parse tree produced by Swift3Parser#protocol_method_declaration.
    def exitProtocol_method_declaration(self, ctx:Swift3Parser.Protocol_method_declarationContext):
        pass


    # Enter a parse tree produced by Swift3Parser#protocol_initializer_declaration.
    def enterProtocol_initializer_declaration(self, ctx:Swift3Parser.Protocol_initializer_declarationContext):
        pass

    # Exit a parse tree produced by Swift3Parser#protocol_initializer_declaration.
    def exitProtocol_initializer_declaration(self, ctx:Swift3Parser.Protocol_initializer_declarationContext):
        pass


    # Enter a parse tree produced by Swift3Parser#protocol_subscript_declaration.
    def enterProtocol_subscript_declaration(self, ctx:Swift3Parser.Protocol_subscript_declarationContext):
        pass

    # Exit a parse tree produced by Swift3Parser#protocol_subscript_declaration.
    def exitProtocol_subscript_declaration(self, ctx:Swift3Parser.Protocol_subscript_declarationContext):
        pass


    # Enter a parse tree produced by Swift3Parser#protocol_associated_type_declaration.
    def enterProtocol_associated_type_declaration(self, ctx:Swift3Parser.Protocol_associated_type_declarationContext):
        pass

    # Exit a parse tree produced by Swift3Parser#protocol_associated_type_declaration.
    def exitProtocol_associated_type_declaration(self, ctx:Swift3Parser.Protocol_associated_type_declarationContext):
        pass


    # Enter a parse tree produced by Swift3Parser#initializer_declaration.
    def enterInitializer_declaration(self, ctx:Swift3Parser.Initializer_declarationContext):
        pass

    # Exit a parse tree produced by Swift3Parser#initializer_declaration.
    def exitInitializer_declaration(self, ctx:Swift3Parser.Initializer_declarationContext):
        pass


    # Enter a parse tree produced by Swift3Parser#initializer_head.
    def enterInitializer_head(self, ctx:Swift3Parser.Initializer_headContext):
        pass

    # Exit a parse tree produced by Swift3Parser#initializer_head.
    def exitInitializer_head(self, ctx:Swift3Parser.Initializer_headContext):
        pass


    # Enter a parse tree produced by Swift3Parser#initializer_body.
    def enterInitializer_body(self, ctx:Swift3Parser.Initializer_bodyContext):
        pass

    # Exit a parse tree produced by Swift3Parser#initializer_body.
    def exitInitializer_body(self, ctx:Swift3Parser.Initializer_bodyContext):
        pass


    # Enter a parse tree produced by Swift3Parser#deinitializer_declaration.
    def enterDeinitializer_declaration(self, ctx:Swift3Parser.Deinitializer_declarationContext):
        pass

    # Exit a parse tree produced by Swift3Parser#deinitializer_declaration.
    def exitDeinitializer_declaration(self, ctx:Swift3Parser.Deinitializer_declarationContext):
        pass


    # Enter a parse tree produced by Swift3Parser#extension_declaration.
    def enterExtension_declaration(self, ctx:Swift3Parser.Extension_declarationContext):
        pass

    # Exit a parse tree produced by Swift3Parser#extension_declaration.
    def exitExtension_declaration(self, ctx:Swift3Parser.Extension_declarationContext):
        pass


    # Enter a parse tree produced by Swift3Parser#extension_body.
    def enterExtension_body(self, ctx:Swift3Parser.Extension_bodyContext):
        pass

    # Exit a parse tree produced by Swift3Parser#extension_body.
    def exitExtension_body(self, ctx:Swift3Parser.Extension_bodyContext):
        pass


    # Enter a parse tree produced by Swift3Parser#extension_member.
    def enterExtension_member(self, ctx:Swift3Parser.Extension_memberContext):
        pass

    # Exit a parse tree produced by Swift3Parser#extension_member.
    def exitExtension_member(self, ctx:Swift3Parser.Extension_memberContext):
        pass


    # Enter a parse tree produced by Swift3Parser#subscript_declaration.
    def enterSubscript_declaration(self, ctx:Swift3Parser.Subscript_declarationContext):
        pass

    # Exit a parse tree produced by Swift3Parser#subscript_declaration.
    def exitSubscript_declaration(self, ctx:Swift3Parser.Subscript_declarationContext):
        pass


    # Enter a parse tree produced by Swift3Parser#subscript_head.
    def enterSubscript_head(self, ctx:Swift3Parser.Subscript_headContext):
        pass

    # Exit a parse tree produced by Swift3Parser#subscript_head.
    def exitSubscript_head(self, ctx:Swift3Parser.Subscript_headContext):
        pass


    # Enter a parse tree produced by Swift3Parser#subscript_result.
    def enterSubscript_result(self, ctx:Swift3Parser.Subscript_resultContext):
        pass

    # Exit a parse tree produced by Swift3Parser#subscript_result.
    def exitSubscript_result(self, ctx:Swift3Parser.Subscript_resultContext):
        pass


    # Enter a parse tree produced by Swift3Parser#operator_declaration.
    def enterOperator_declaration(self, ctx:Swift3Parser.Operator_declarationContext):
        pass

    # Exit a parse tree produced by Swift3Parser#operator_declaration.
    def exitOperator_declaration(self, ctx:Swift3Parser.Operator_declarationContext):
        pass


    # Enter a parse tree produced by Swift3Parser#prefix_operator_declaration.
    def enterPrefix_operator_declaration(self, ctx:Swift3Parser.Prefix_operator_declarationContext):
        pass

    # Exit a parse tree produced by Swift3Parser#prefix_operator_declaration.
    def exitPrefix_operator_declaration(self, ctx:Swift3Parser.Prefix_operator_declarationContext):
        pass


    # Enter a parse tree produced by Swift3Parser#postfix_operator_declaration.
    def enterPostfix_operator_declaration(self, ctx:Swift3Parser.Postfix_operator_declarationContext):
        pass

    # Exit a parse tree produced by Swift3Parser#postfix_operator_declaration.
    def exitPostfix_operator_declaration(self, ctx:Swift3Parser.Postfix_operator_declarationContext):
        pass


    # Enter a parse tree produced by Swift3Parser#infix_operator_declaration.
    def enterInfix_operator_declaration(self, ctx:Swift3Parser.Infix_operator_declarationContext):
        pass

    # Exit a parse tree produced by Swift3Parser#infix_operator_declaration.
    def exitInfix_operator_declaration(self, ctx:Swift3Parser.Infix_operator_declarationContext):
        pass


    # Enter a parse tree produced by Swift3Parser#infix_operator_group.
    def enterInfix_operator_group(self, ctx:Swift3Parser.Infix_operator_groupContext):
        pass

    # Exit a parse tree produced by Swift3Parser#infix_operator_group.
    def exitInfix_operator_group(self, ctx:Swift3Parser.Infix_operator_groupContext):
        pass


    # Enter a parse tree produced by Swift3Parser#precedence_group_declaration.
    def enterPrecedence_group_declaration(self, ctx:Swift3Parser.Precedence_group_declarationContext):
        pass

    # Exit a parse tree produced by Swift3Parser#precedence_group_declaration.
    def exitPrecedence_group_declaration(self, ctx:Swift3Parser.Precedence_group_declarationContext):
        pass


    # Enter a parse tree produced by Swift3Parser#precedence_group_attribute.
    def enterPrecedence_group_attribute(self, ctx:Swift3Parser.Precedence_group_attributeContext):
        pass

    # Exit a parse tree produced by Swift3Parser#precedence_group_attribute.
    def exitPrecedence_group_attribute(self, ctx:Swift3Parser.Precedence_group_attributeContext):
        pass


    # Enter a parse tree produced by Swift3Parser#precedence_group_relation.
    def enterPrecedence_group_relation(self, ctx:Swift3Parser.Precedence_group_relationContext):
        pass

    # Exit a parse tree produced by Swift3Parser#precedence_group_relation.
    def exitPrecedence_group_relation(self, ctx:Swift3Parser.Precedence_group_relationContext):
        pass


    # Enter a parse tree produced by Swift3Parser#precedence_group_assignment.
    def enterPrecedence_group_assignment(self, ctx:Swift3Parser.Precedence_group_assignmentContext):
        pass

    # Exit a parse tree produced by Swift3Parser#precedence_group_assignment.
    def exitPrecedence_group_assignment(self, ctx:Swift3Parser.Precedence_group_assignmentContext):
        pass


    # Enter a parse tree produced by Swift3Parser#precedence_group_associativity.
    def enterPrecedence_group_associativity(self, ctx:Swift3Parser.Precedence_group_associativityContext):
        pass

    # Exit a parse tree produced by Swift3Parser#precedence_group_associativity.
    def exitPrecedence_group_associativity(self, ctx:Swift3Parser.Precedence_group_associativityContext):
        pass


    # Enter a parse tree produced by Swift3Parser#associativity.
    def enterAssociativity(self, ctx:Swift3Parser.AssociativityContext):
        pass

    # Exit a parse tree produced by Swift3Parser#associativity.
    def exitAssociativity(self, ctx:Swift3Parser.AssociativityContext):
        pass


    # Enter a parse tree produced by Swift3Parser#precedence_group_names.
    def enterPrecedence_group_names(self, ctx:Swift3Parser.Precedence_group_namesContext):
        pass

    # Exit a parse tree produced by Swift3Parser#precedence_group_names.
    def exitPrecedence_group_names(self, ctx:Swift3Parser.Precedence_group_namesContext):
        pass


    # Enter a parse tree produced by Swift3Parser#precedence_group_name.
    def enterPrecedence_group_name(self, ctx:Swift3Parser.Precedence_group_nameContext):
        pass

    # Exit a parse tree produced by Swift3Parser#precedence_group_name.
    def exitPrecedence_group_name(self, ctx:Swift3Parser.Precedence_group_nameContext):
        pass


    # Enter a parse tree produced by Swift3Parser#declaration_modifier.
    def enterDeclaration_modifier(self, ctx:Swift3Parser.Declaration_modifierContext):
        pass

    # Exit a parse tree produced by Swift3Parser#declaration_modifier.
    def exitDeclaration_modifier(self, ctx:Swift3Parser.Declaration_modifierContext):
        pass


    # Enter a parse tree produced by Swift3Parser#declaration_modifiers.
    def enterDeclaration_modifiers(self, ctx:Swift3Parser.Declaration_modifiersContext):
        pass

    # Exit a parse tree produced by Swift3Parser#declaration_modifiers.
    def exitDeclaration_modifiers(self, ctx:Swift3Parser.Declaration_modifiersContext):
        pass


    # Enter a parse tree produced by Swift3Parser#access_level_modifier.
    def enterAccess_level_modifier(self, ctx:Swift3Parser.Access_level_modifierContext):
        pass

    # Exit a parse tree produced by Swift3Parser#access_level_modifier.
    def exitAccess_level_modifier(self, ctx:Swift3Parser.Access_level_modifierContext):
        pass


    # Enter a parse tree produced by Swift3Parser#mutation_modifier.
    def enterMutation_modifier(self, ctx:Swift3Parser.Mutation_modifierContext):
        pass

    # Exit a parse tree produced by Swift3Parser#mutation_modifier.
    def exitMutation_modifier(self, ctx:Swift3Parser.Mutation_modifierContext):
        pass


    # Enter a parse tree produced by Swift3Parser#pattern.
    def enterPattern(self, ctx:Swift3Parser.PatternContext):
        pass

    # Exit a parse tree produced by Swift3Parser#pattern.
    def exitPattern(self, ctx:Swift3Parser.PatternContext):
        pass


    # Enter a parse tree produced by Swift3Parser#wildcard_pattern.
    def enterWildcard_pattern(self, ctx:Swift3Parser.Wildcard_patternContext):
        pass

    # Exit a parse tree produced by Swift3Parser#wildcard_pattern.
    def exitWildcard_pattern(self, ctx:Swift3Parser.Wildcard_patternContext):
        pass


    # Enter a parse tree produced by Swift3Parser#identifier_pattern.
    def enterIdentifier_pattern(self, ctx:Swift3Parser.Identifier_patternContext):
        pass

    # Exit a parse tree produced by Swift3Parser#identifier_pattern.
    def exitIdentifier_pattern(self, ctx:Swift3Parser.Identifier_patternContext):
        pass


    # Enter a parse tree produced by Swift3Parser#value_binding_pattern.
    def enterValue_binding_pattern(self, ctx:Swift3Parser.Value_binding_patternContext):
        pass

    # Exit a parse tree produced by Swift3Parser#value_binding_pattern.
    def exitValue_binding_pattern(self, ctx:Swift3Parser.Value_binding_patternContext):
        pass


    # Enter a parse tree produced by Swift3Parser#tuple_pattern.
    def enterTuple_pattern(self, ctx:Swift3Parser.Tuple_patternContext):
        pass

    # Exit a parse tree produced by Swift3Parser#tuple_pattern.
    def exitTuple_pattern(self, ctx:Swift3Parser.Tuple_patternContext):
        pass


    # Enter a parse tree produced by Swift3Parser#tuple_pattern_element_list.
    def enterTuple_pattern_element_list(self, ctx:Swift3Parser.Tuple_pattern_element_listContext):
        pass

    # Exit a parse tree produced by Swift3Parser#tuple_pattern_element_list.
    def exitTuple_pattern_element_list(self, ctx:Swift3Parser.Tuple_pattern_element_listContext):
        pass


    # Enter a parse tree produced by Swift3Parser#tuple_pattern_element.
    def enterTuple_pattern_element(self, ctx:Swift3Parser.Tuple_pattern_elementContext):
        pass

    # Exit a parse tree produced by Swift3Parser#tuple_pattern_element.
    def exitTuple_pattern_element(self, ctx:Swift3Parser.Tuple_pattern_elementContext):
        pass


    # Enter a parse tree produced by Swift3Parser#enum_case_pattern.
    def enterEnum_case_pattern(self, ctx:Swift3Parser.Enum_case_patternContext):
        pass

    # Exit a parse tree produced by Swift3Parser#enum_case_pattern.
    def exitEnum_case_pattern(self, ctx:Swift3Parser.Enum_case_patternContext):
        pass


    # Enter a parse tree produced by Swift3Parser#optional_pattern.
    def enterOptional_pattern(self, ctx:Swift3Parser.Optional_patternContext):
        pass

    # Exit a parse tree produced by Swift3Parser#optional_pattern.
    def exitOptional_pattern(self, ctx:Swift3Parser.Optional_patternContext):
        pass


    # Enter a parse tree produced by Swift3Parser#expression_pattern.
    def enterExpression_pattern(self, ctx:Swift3Parser.Expression_patternContext):
        pass

    # Exit a parse tree produced by Swift3Parser#expression_pattern.
    def exitExpression_pattern(self, ctx:Swift3Parser.Expression_patternContext):
        pass


    # Enter a parse tree produced by Swift3Parser#attribute.
    def enterAttribute(self, ctx:Swift3Parser.AttributeContext):
        pass

    # Exit a parse tree produced by Swift3Parser#attribute.
    def exitAttribute(self, ctx:Swift3Parser.AttributeContext):
        pass


    # Enter a parse tree produced by Swift3Parser#attribute_name.
    def enterAttribute_name(self, ctx:Swift3Parser.Attribute_nameContext):
        pass

    # Exit a parse tree produced by Swift3Parser#attribute_name.
    def exitAttribute_name(self, ctx:Swift3Parser.Attribute_nameContext):
        pass


    # Enter a parse tree produced by Swift3Parser#attribute_argument_clause.
    def enterAttribute_argument_clause(self, ctx:Swift3Parser.Attribute_argument_clauseContext):
        pass

    # Exit a parse tree produced by Swift3Parser#attribute_argument_clause.
    def exitAttribute_argument_clause(self, ctx:Swift3Parser.Attribute_argument_clauseContext):
        pass


    # Enter a parse tree produced by Swift3Parser#attributes.
    def enterAttributes(self, ctx:Swift3Parser.AttributesContext):
        pass

    # Exit a parse tree produced by Swift3Parser#attributes.
    def exitAttributes(self, ctx:Swift3Parser.AttributesContext):
        pass


    # Enter a parse tree produced by Swift3Parser#balanced_tokens.
    def enterBalanced_tokens(self, ctx:Swift3Parser.Balanced_tokensContext):
        pass

    # Exit a parse tree produced by Swift3Parser#balanced_tokens.
    def exitBalanced_tokens(self, ctx:Swift3Parser.Balanced_tokensContext):
        pass


    # Enter a parse tree produced by Swift3Parser#balanced_token.
    def enterBalanced_token(self, ctx:Swift3Parser.Balanced_tokenContext):
        pass

    # Exit a parse tree produced by Swift3Parser#balanced_token.
    def exitBalanced_token(self, ctx:Swift3Parser.Balanced_tokenContext):
        pass


    # Enter a parse tree produced by Swift3Parser#any_punctuation_for_balanced_token.
    def enterAny_punctuation_for_balanced_token(self, ctx:Swift3Parser.Any_punctuation_for_balanced_tokenContext):
        pass

    # Exit a parse tree produced by Swift3Parser#any_punctuation_for_balanced_token.
    def exitAny_punctuation_for_balanced_token(self, ctx:Swift3Parser.Any_punctuation_for_balanced_tokenContext):
        pass


    # Enter a parse tree produced by Swift3Parser#expression.
    def enterExpression(self, ctx:Swift3Parser.ExpressionContext):
        pass

    # Exit a parse tree produced by Swift3Parser#expression.
    def exitExpression(self, ctx:Swift3Parser.ExpressionContext):
        pass


    # Enter a parse tree produced by Swift3Parser#expression_list.
    def enterExpression_list(self, ctx:Swift3Parser.Expression_listContext):
        pass

    # Exit a parse tree produced by Swift3Parser#expression_list.
    def exitExpression_list(self, ctx:Swift3Parser.Expression_listContext):
        pass


    # Enter a parse tree produced by Swift3Parser#prefix_expression.
    def enterPrefix_expression(self, ctx:Swift3Parser.Prefix_expressionContext):
        pass

    # Exit a parse tree produced by Swift3Parser#prefix_expression.
    def exitPrefix_expression(self, ctx:Swift3Parser.Prefix_expressionContext):
        pass


    # Enter a parse tree produced by Swift3Parser#in_out_expression.
    def enterIn_out_expression(self, ctx:Swift3Parser.In_out_expressionContext):
        pass

    # Exit a parse tree produced by Swift3Parser#in_out_expression.
    def exitIn_out_expression(self, ctx:Swift3Parser.In_out_expressionContext):
        pass


    # Enter a parse tree produced by Swift3Parser#try_operator.
    def enterTry_operator(self, ctx:Swift3Parser.Try_operatorContext):
        pass

    # Exit a parse tree produced by Swift3Parser#try_operator.
    def exitTry_operator(self, ctx:Swift3Parser.Try_operatorContext):
        pass


    # Enter a parse tree produced by Swift3Parser#binary_expression.
    def enterBinary_expression(self, ctx:Swift3Parser.Binary_expressionContext):
        pass

    # Exit a parse tree produced by Swift3Parser#binary_expression.
    def exitBinary_expression(self, ctx:Swift3Parser.Binary_expressionContext):
        pass


    # Enter a parse tree produced by Swift3Parser#binary_expressions.
    def enterBinary_expressions(self, ctx:Swift3Parser.Binary_expressionsContext):
        pass

    # Exit a parse tree produced by Swift3Parser#binary_expressions.
    def exitBinary_expressions(self, ctx:Swift3Parser.Binary_expressionsContext):
        pass


    # Enter a parse tree produced by Swift3Parser#conditional_operator.
    def enterConditional_operator(self, ctx:Swift3Parser.Conditional_operatorContext):
        pass

    # Exit a parse tree produced by Swift3Parser#conditional_operator.
    def exitConditional_operator(self, ctx:Swift3Parser.Conditional_operatorContext):
        pass


    # Enter a parse tree produced by Swift3Parser#type_casting_operator.
    def enterType_casting_operator(self, ctx:Swift3Parser.Type_casting_operatorContext):
        pass

    # Exit a parse tree produced by Swift3Parser#type_casting_operator.
    def exitType_casting_operator(self, ctx:Swift3Parser.Type_casting_operatorContext):
        pass


    # Enter a parse tree produced by Swift3Parser#primary_expression.
    def enterPrimary_expression(self, ctx:Swift3Parser.Primary_expressionContext):
        pass

    # Exit a parse tree produced by Swift3Parser#primary_expression.
    def exitPrimary_expression(self, ctx:Swift3Parser.Primary_expressionContext):
        pass


    # Enter a parse tree produced by Swift3Parser#literal_expression.
    def enterLiteral_expression(self, ctx:Swift3Parser.Literal_expressionContext):
        pass

    # Exit a parse tree produced by Swift3Parser#literal_expression.
    def exitLiteral_expression(self, ctx:Swift3Parser.Literal_expressionContext):
        pass


    # Enter a parse tree produced by Swift3Parser#array_literal.
    def enterArray_literal(self, ctx:Swift3Parser.Array_literalContext):
        pass

    # Exit a parse tree produced by Swift3Parser#array_literal.
    def exitArray_literal(self, ctx:Swift3Parser.Array_literalContext):
        pass


    # Enter a parse tree produced by Swift3Parser#array_literal_items.
    def enterArray_literal_items(self, ctx:Swift3Parser.Array_literal_itemsContext):
        pass

    # Exit a parse tree produced by Swift3Parser#array_literal_items.
    def exitArray_literal_items(self, ctx:Swift3Parser.Array_literal_itemsContext):
        pass


    # Enter a parse tree produced by Swift3Parser#array_literal_item.
    def enterArray_literal_item(self, ctx:Swift3Parser.Array_literal_itemContext):
        pass

    # Exit a parse tree produced by Swift3Parser#array_literal_item.
    def exitArray_literal_item(self, ctx:Swift3Parser.Array_literal_itemContext):
        pass


    # Enter a parse tree produced by Swift3Parser#dictionary_literal.
    def enterDictionary_literal(self, ctx:Swift3Parser.Dictionary_literalContext):
        pass

    # Exit a parse tree produced by Swift3Parser#dictionary_literal.
    def exitDictionary_literal(self, ctx:Swift3Parser.Dictionary_literalContext):
        pass


    # Enter a parse tree produced by Swift3Parser#dictionary_literal_items.
    def enterDictionary_literal_items(self, ctx:Swift3Parser.Dictionary_literal_itemsContext):
        pass

    # Exit a parse tree produced by Swift3Parser#dictionary_literal_items.
    def exitDictionary_literal_items(self, ctx:Swift3Parser.Dictionary_literal_itemsContext):
        pass


    # Enter a parse tree produced by Swift3Parser#dictionary_literal_item.
    def enterDictionary_literal_item(self, ctx:Swift3Parser.Dictionary_literal_itemContext):
        pass

    # Exit a parse tree produced by Swift3Parser#dictionary_literal_item.
    def exitDictionary_literal_item(self, ctx:Swift3Parser.Dictionary_literal_itemContext):
        pass


    # Enter a parse tree produced by Swift3Parser#playground_literal.
    def enterPlayground_literal(self, ctx:Swift3Parser.Playground_literalContext):
        pass

    # Exit a parse tree produced by Swift3Parser#playground_literal.
    def exitPlayground_literal(self, ctx:Swift3Parser.Playground_literalContext):
        pass


    # Enter a parse tree produced by Swift3Parser#self_expression.
    def enterSelf_expression(self, ctx:Swift3Parser.Self_expressionContext):
        pass

    # Exit a parse tree produced by Swift3Parser#self_expression.
    def exitSelf_expression(self, ctx:Swift3Parser.Self_expressionContext):
        pass


    # Enter a parse tree produced by Swift3Parser#superclass_expression.
    def enterSuperclass_expression(self, ctx:Swift3Parser.Superclass_expressionContext):
        pass

    # Exit a parse tree produced by Swift3Parser#superclass_expression.
    def exitSuperclass_expression(self, ctx:Swift3Parser.Superclass_expressionContext):
        pass


    # Enter a parse tree produced by Swift3Parser#superclass_method_expression.
    def enterSuperclass_method_expression(self, ctx:Swift3Parser.Superclass_method_expressionContext):
        pass

    # Exit a parse tree produced by Swift3Parser#superclass_method_expression.
    def exitSuperclass_method_expression(self, ctx:Swift3Parser.Superclass_method_expressionContext):
        pass


    # Enter a parse tree produced by Swift3Parser#superclass_subscript_expression.
    def enterSuperclass_subscript_expression(self, ctx:Swift3Parser.Superclass_subscript_expressionContext):
        pass

    # Exit a parse tree produced by Swift3Parser#superclass_subscript_expression.
    def exitSuperclass_subscript_expression(self, ctx:Swift3Parser.Superclass_subscript_expressionContext):
        pass


    # Enter a parse tree produced by Swift3Parser#superclass_initializer_expression.
    def enterSuperclass_initializer_expression(self, ctx:Swift3Parser.Superclass_initializer_expressionContext):
        pass

    # Exit a parse tree produced by Swift3Parser#superclass_initializer_expression.
    def exitSuperclass_initializer_expression(self, ctx:Swift3Parser.Superclass_initializer_expressionContext):
        pass


    # Enter a parse tree produced by Swift3Parser#closure_expression.
    def enterClosure_expression(self, ctx:Swift3Parser.Closure_expressionContext):
        pass

    # Exit a parse tree produced by Swift3Parser#closure_expression.
    def exitClosure_expression(self, ctx:Swift3Parser.Closure_expressionContext):
        pass


    # Enter a parse tree produced by Swift3Parser#closure_signature.
    def enterClosure_signature(self, ctx:Swift3Parser.Closure_signatureContext):
        pass

    # Exit a parse tree produced by Swift3Parser#closure_signature.
    def exitClosure_signature(self, ctx:Swift3Parser.Closure_signatureContext):
        pass


    # Enter a parse tree produced by Swift3Parser#closure_parameter_clause.
    def enterClosure_parameter_clause(self, ctx:Swift3Parser.Closure_parameter_clauseContext):
        pass

    # Exit a parse tree produced by Swift3Parser#closure_parameter_clause.
    def exitClosure_parameter_clause(self, ctx:Swift3Parser.Closure_parameter_clauseContext):
        pass


    # Enter a parse tree produced by Swift3Parser#closure_parameter_clause_identifier_list.
    def enterClosure_parameter_clause_identifier_list(self, ctx:Swift3Parser.Closure_parameter_clause_identifier_listContext):
        pass

    # Exit a parse tree produced by Swift3Parser#closure_parameter_clause_identifier_list.
    def exitClosure_parameter_clause_identifier_list(self, ctx:Swift3Parser.Closure_parameter_clause_identifier_listContext):
        pass


    # Enter a parse tree produced by Swift3Parser#closure_parameter_list.
    def enterClosure_parameter_list(self, ctx:Swift3Parser.Closure_parameter_listContext):
        pass

    # Exit a parse tree produced by Swift3Parser#closure_parameter_list.
    def exitClosure_parameter_list(self, ctx:Swift3Parser.Closure_parameter_listContext):
        pass


    # Enter a parse tree produced by Swift3Parser#closure_parameter.
    def enterClosure_parameter(self, ctx:Swift3Parser.Closure_parameterContext):
        pass

    # Exit a parse tree produced by Swift3Parser#closure_parameter.
    def exitClosure_parameter(self, ctx:Swift3Parser.Closure_parameterContext):
        pass


    # Enter a parse tree produced by Swift3Parser#closure_parameter_name.
    def enterClosure_parameter_name(self, ctx:Swift3Parser.Closure_parameter_nameContext):
        pass

    # Exit a parse tree produced by Swift3Parser#closure_parameter_name.
    def exitClosure_parameter_name(self, ctx:Swift3Parser.Closure_parameter_nameContext):
        pass


    # Enter a parse tree produced by Swift3Parser#capture_list.
    def enterCapture_list(self, ctx:Swift3Parser.Capture_listContext):
        pass

    # Exit a parse tree produced by Swift3Parser#capture_list.
    def exitCapture_list(self, ctx:Swift3Parser.Capture_listContext):
        pass


    # Enter a parse tree produced by Swift3Parser#capture_list_items.
    def enterCapture_list_items(self, ctx:Swift3Parser.Capture_list_itemsContext):
        pass

    # Exit a parse tree produced by Swift3Parser#capture_list_items.
    def exitCapture_list_items(self, ctx:Swift3Parser.Capture_list_itemsContext):
        pass


    # Enter a parse tree produced by Swift3Parser#capture_list_item.
    def enterCapture_list_item(self, ctx:Swift3Parser.Capture_list_itemContext):
        pass

    # Exit a parse tree produced by Swift3Parser#capture_list_item.
    def exitCapture_list_item(self, ctx:Swift3Parser.Capture_list_itemContext):
        pass


    # Enter a parse tree produced by Swift3Parser#capture_specifier.
    def enterCapture_specifier(self, ctx:Swift3Parser.Capture_specifierContext):
        pass

    # Exit a parse tree produced by Swift3Parser#capture_specifier.
    def exitCapture_specifier(self, ctx:Swift3Parser.Capture_specifierContext):
        pass


    # Enter a parse tree produced by Swift3Parser#implicit_member_expression.
    def enterImplicit_member_expression(self, ctx:Swift3Parser.Implicit_member_expressionContext):
        pass

    # Exit a parse tree produced by Swift3Parser#implicit_member_expression.
    def exitImplicit_member_expression(self, ctx:Swift3Parser.Implicit_member_expressionContext):
        pass


    # Enter a parse tree produced by Swift3Parser#parenthesized_expression.
    def enterParenthesized_expression(self, ctx:Swift3Parser.Parenthesized_expressionContext):
        pass

    # Exit a parse tree produced by Swift3Parser#parenthesized_expression.
    def exitParenthesized_expression(self, ctx:Swift3Parser.Parenthesized_expressionContext):
        pass


    # Enter a parse tree produced by Swift3Parser#tuple_expression.
    def enterTuple_expression(self, ctx:Swift3Parser.Tuple_expressionContext):
        pass

    # Exit a parse tree produced by Swift3Parser#tuple_expression.
    def exitTuple_expression(self, ctx:Swift3Parser.Tuple_expressionContext):
        pass


    # Enter a parse tree produced by Swift3Parser#tuple_element.
    def enterTuple_element(self, ctx:Swift3Parser.Tuple_elementContext):
        pass

    # Exit a parse tree produced by Swift3Parser#tuple_element.
    def exitTuple_element(self, ctx:Swift3Parser.Tuple_elementContext):
        pass


    # Enter a parse tree produced by Swift3Parser#wildcard_expression.
    def enterWildcard_expression(self, ctx:Swift3Parser.Wildcard_expressionContext):
        pass

    # Exit a parse tree produced by Swift3Parser#wildcard_expression.
    def exitWildcard_expression(self, ctx:Swift3Parser.Wildcard_expressionContext):
        pass


    # Enter a parse tree produced by Swift3Parser#selector_expression.
    def enterSelector_expression(self, ctx:Swift3Parser.Selector_expressionContext):
        pass

    # Exit a parse tree produced by Swift3Parser#selector_expression.
    def exitSelector_expression(self, ctx:Swift3Parser.Selector_expressionContext):
        pass


    # Enter a parse tree produced by Swift3Parser#key_path_expression.
    def enterKey_path_expression(self, ctx:Swift3Parser.Key_path_expressionContext):
        pass

    # Exit a parse tree produced by Swift3Parser#key_path_expression.
    def exitKey_path_expression(self, ctx:Swift3Parser.Key_path_expressionContext):
        pass


    # Enter a parse tree produced by Swift3Parser#function_call_expression_with_closure.
    def enterFunction_call_expression_with_closure(self, ctx:Swift3Parser.Function_call_expression_with_closureContext):
        pass

    # Exit a parse tree produced by Swift3Parser#function_call_expression_with_closure.
    def exitFunction_call_expression_with_closure(self, ctx:Swift3Parser.Function_call_expression_with_closureContext):
        pass


    # Enter a parse tree produced by Swift3Parser#function_call_expression.
    def enterFunction_call_expression(self, ctx:Swift3Parser.Function_call_expressionContext):
        pass

    # Exit a parse tree produced by Swift3Parser#function_call_expression.
    def exitFunction_call_expression(self, ctx:Swift3Parser.Function_call_expressionContext):
        pass


    # Enter a parse tree produced by Swift3Parser#explicit_member_expression1.
    def enterExplicit_member_expression1(self, ctx:Swift3Parser.Explicit_member_expression1Context):
        pass

    # Exit a parse tree produced by Swift3Parser#explicit_member_expression1.
    def exitExplicit_member_expression1(self, ctx:Swift3Parser.Explicit_member_expression1Context):
        pass


    # Enter a parse tree produced by Swift3Parser#initializer_expression.
    def enterInitializer_expression(self, ctx:Swift3Parser.Initializer_expressionContext):
        pass

    # Exit a parse tree produced by Swift3Parser#initializer_expression.
    def exitInitializer_expression(self, ctx:Swift3Parser.Initializer_expressionContext):
        pass


    # Enter a parse tree produced by Swift3Parser#postfix_self_expression.
    def enterPostfix_self_expression(self, ctx:Swift3Parser.Postfix_self_expressionContext):
        pass

    # Exit a parse tree produced by Swift3Parser#postfix_self_expression.
    def exitPostfix_self_expression(self, ctx:Swift3Parser.Postfix_self_expressionContext):
        pass


    # Enter a parse tree produced by Swift3Parser#initializer_expression_with_args.
    def enterInitializer_expression_with_args(self, ctx:Swift3Parser.Initializer_expression_with_argsContext):
        pass

    # Exit a parse tree produced by Swift3Parser#initializer_expression_with_args.
    def exitInitializer_expression_with_args(self, ctx:Swift3Parser.Initializer_expression_with_argsContext):
        pass


    # Enter a parse tree produced by Swift3Parser#dynamic_type.
    def enterDynamic_type(self, ctx:Swift3Parser.Dynamic_typeContext):
        pass

    # Exit a parse tree produced by Swift3Parser#dynamic_type.
    def exitDynamic_type(self, ctx:Swift3Parser.Dynamic_typeContext):
        pass


    # Enter a parse tree produced by Swift3Parser#subscript_expression.
    def enterSubscript_expression(self, ctx:Swift3Parser.Subscript_expressionContext):
        pass

    # Exit a parse tree produced by Swift3Parser#subscript_expression.
    def exitSubscript_expression(self, ctx:Swift3Parser.Subscript_expressionContext):
        pass


    # Enter a parse tree produced by Swift3Parser#explicit_member_expression2.
    def enterExplicit_member_expression2(self, ctx:Swift3Parser.Explicit_member_expression2Context):
        pass

    # Exit a parse tree produced by Swift3Parser#explicit_member_expression2.
    def exitExplicit_member_expression2(self, ctx:Swift3Parser.Explicit_member_expression2Context):
        pass


    # Enter a parse tree produced by Swift3Parser#explicit_member_expression3.
    def enterExplicit_member_expression3(self, ctx:Swift3Parser.Explicit_member_expression3Context):
        pass

    # Exit a parse tree produced by Swift3Parser#explicit_member_expression3.
    def exitExplicit_member_expression3(self, ctx:Swift3Parser.Explicit_member_expression3Context):
        pass


    # Enter a parse tree produced by Swift3Parser#explicit_member_expression4.
    def enterExplicit_member_expression4(self, ctx:Swift3Parser.Explicit_member_expression4Context):
        pass

    # Exit a parse tree produced by Swift3Parser#explicit_member_expression4.
    def exitExplicit_member_expression4(self, ctx:Swift3Parser.Explicit_member_expression4Context):
        pass


    # Enter a parse tree produced by Swift3Parser#postfix_operation.
    def enterPostfix_operation(self, ctx:Swift3Parser.Postfix_operationContext):
        pass

    # Exit a parse tree produced by Swift3Parser#postfix_operation.
    def exitPostfix_operation(self, ctx:Swift3Parser.Postfix_operationContext):
        pass


    # Enter a parse tree produced by Swift3Parser#primary.
    def enterPrimary(self, ctx:Swift3Parser.PrimaryContext):
        pass

    # Exit a parse tree produced by Swift3Parser#primary.
    def exitPrimary(self, ctx:Swift3Parser.PrimaryContext):
        pass


    # Enter a parse tree produced by Swift3Parser#function_call_argument_clause.
    def enterFunction_call_argument_clause(self, ctx:Swift3Parser.Function_call_argument_clauseContext):
        pass

    # Exit a parse tree produced by Swift3Parser#function_call_argument_clause.
    def exitFunction_call_argument_clause(self, ctx:Swift3Parser.Function_call_argument_clauseContext):
        pass


    # Enter a parse tree produced by Swift3Parser#function_call_argument_list.
    def enterFunction_call_argument_list(self, ctx:Swift3Parser.Function_call_argument_listContext):
        pass

    # Exit a parse tree produced by Swift3Parser#function_call_argument_list.
    def exitFunction_call_argument_list(self, ctx:Swift3Parser.Function_call_argument_listContext):
        pass


    # Enter a parse tree produced by Swift3Parser#function_call_argument.
    def enterFunction_call_argument(self, ctx:Swift3Parser.Function_call_argumentContext):
        pass

    # Exit a parse tree produced by Swift3Parser#function_call_argument.
    def exitFunction_call_argument(self, ctx:Swift3Parser.Function_call_argumentContext):
        pass


    # Enter a parse tree produced by Swift3Parser#trailing_closure.
    def enterTrailing_closure(self, ctx:Swift3Parser.Trailing_closureContext):
        pass

    # Exit a parse tree produced by Swift3Parser#trailing_closure.
    def exitTrailing_closure(self, ctx:Swift3Parser.Trailing_closureContext):
        pass


    # Enter a parse tree produced by Swift3Parser#argument_names.
    def enterArgument_names(self, ctx:Swift3Parser.Argument_namesContext):
        pass

    # Exit a parse tree produced by Swift3Parser#argument_names.
    def exitArgument_names(self, ctx:Swift3Parser.Argument_namesContext):
        pass


    # Enter a parse tree produced by Swift3Parser#argument_name.
    def enterArgument_name(self, ctx:Swift3Parser.Argument_nameContext):
        pass

    # Exit a parse tree produced by Swift3Parser#argument_name.
    def exitArgument_name(self, ctx:Swift3Parser.Argument_nameContext):
        pass


    # Enter a parse tree produced by Swift3Parser#dynamic_type_expression.
    def enterDynamic_type_expression(self, ctx:Swift3Parser.Dynamic_type_expressionContext):
        pass

    # Exit a parse tree produced by Swift3Parser#dynamic_type_expression.
    def exitDynamic_type_expression(self, ctx:Swift3Parser.Dynamic_type_expressionContext):
        pass


    # Enter a parse tree produced by Swift3Parser#the_metatype_protocol_type.
    def enterThe_metatype_protocol_type(self, ctx:Swift3Parser.The_metatype_protocol_typeContext):
        pass

    # Exit a parse tree produced by Swift3Parser#the_metatype_protocol_type.
    def exitThe_metatype_protocol_type(self, ctx:Swift3Parser.The_metatype_protocol_typeContext):
        pass


    # Enter a parse tree produced by Swift3Parser#the_function_type.
    def enterThe_function_type(self, ctx:Swift3Parser.The_function_typeContext):
        pass

    # Exit a parse tree produced by Swift3Parser#the_function_type.
    def exitThe_function_type(self, ctx:Swift3Parser.The_function_typeContext):
        pass


    # Enter a parse tree produced by Swift3Parser#the_implicitly_unwrapped_optional_type.
    def enterThe_implicitly_unwrapped_optional_type(self, ctx:Swift3Parser.The_implicitly_unwrapped_optional_typeContext):
        pass

    # Exit a parse tree produced by Swift3Parser#the_implicitly_unwrapped_optional_type.
    def exitThe_implicitly_unwrapped_optional_type(self, ctx:Swift3Parser.The_implicitly_unwrapped_optional_typeContext):
        pass


    # Enter a parse tree produced by Swift3Parser#the_dictionary_type.
    def enterThe_dictionary_type(self, ctx:Swift3Parser.The_dictionary_typeContext):
        pass

    # Exit a parse tree produced by Swift3Parser#the_dictionary_type.
    def exitThe_dictionary_type(self, ctx:Swift3Parser.The_dictionary_typeContext):
        pass


    # Enter a parse tree produced by Swift3Parser#the_optional_type.
    def enterThe_optional_type(self, ctx:Swift3Parser.The_optional_typeContext):
        pass

    # Exit a parse tree produced by Swift3Parser#the_optional_type.
    def exitThe_optional_type(self, ctx:Swift3Parser.The_optional_typeContext):
        pass


    # Enter a parse tree produced by Swift3Parser#the_tuple_type.
    def enterThe_tuple_type(self, ctx:Swift3Parser.The_tuple_typeContext):
        pass

    # Exit a parse tree produced by Swift3Parser#the_tuple_type.
    def exitThe_tuple_type(self, ctx:Swift3Parser.The_tuple_typeContext):
        pass


    # Enter a parse tree produced by Swift3Parser#the_self_type.
    def enterThe_self_type(self, ctx:Swift3Parser.The_self_typeContext):
        pass

    # Exit a parse tree produced by Swift3Parser#the_self_type.
    def exitThe_self_type(self, ctx:Swift3Parser.The_self_typeContext):
        pass


    # Enter a parse tree produced by Swift3Parser#the_array_type.
    def enterThe_array_type(self, ctx:Swift3Parser.The_array_typeContext):
        pass

    # Exit a parse tree produced by Swift3Parser#the_array_type.
    def exitThe_array_type(self, ctx:Swift3Parser.The_array_typeContext):
        pass


    # Enter a parse tree produced by Swift3Parser#the_metatype_type_type.
    def enterThe_metatype_type_type(self, ctx:Swift3Parser.The_metatype_type_typeContext):
        pass

    # Exit a parse tree produced by Swift3Parser#the_metatype_type_type.
    def exitThe_metatype_type_type(self, ctx:Swift3Parser.The_metatype_type_typeContext):
        pass


    # Enter a parse tree produced by Swift3Parser#the_protocol_composition_type.
    def enterThe_protocol_composition_type(self, ctx:Swift3Parser.The_protocol_composition_typeContext):
        pass

    # Exit a parse tree produced by Swift3Parser#the_protocol_composition_type.
    def exitThe_protocol_composition_type(self, ctx:Swift3Parser.The_protocol_composition_typeContext):
        pass


    # Enter a parse tree produced by Swift3Parser#the_any_type.
    def enterThe_any_type(self, ctx:Swift3Parser.The_any_typeContext):
        pass

    # Exit a parse tree produced by Swift3Parser#the_any_type.
    def exitThe_any_type(self, ctx:Swift3Parser.The_any_typeContext):
        pass


    # Enter a parse tree produced by Swift3Parser#the_type_identifier.
    def enterThe_type_identifier(self, ctx:Swift3Parser.The_type_identifierContext):
        pass

    # Exit a parse tree produced by Swift3Parser#the_type_identifier.
    def exitThe_type_identifier(self, ctx:Swift3Parser.The_type_identifierContext):
        pass


    # Enter a parse tree produced by Swift3Parser#type_annotation.
    def enterType_annotation(self, ctx:Swift3Parser.Type_annotationContext):
        pass

    # Exit a parse tree produced by Swift3Parser#type_annotation.
    def exitType_annotation(self, ctx:Swift3Parser.Type_annotationContext):
        pass


    # Enter a parse tree produced by Swift3Parser#type_identifier.
    def enterType_identifier(self, ctx:Swift3Parser.Type_identifierContext):
        pass

    # Exit a parse tree produced by Swift3Parser#type_identifier.
    def exitType_identifier(self, ctx:Swift3Parser.Type_identifierContext):
        pass


    # Enter a parse tree produced by Swift3Parser#type_name.
    def enterType_name(self, ctx:Swift3Parser.Type_nameContext):
        pass

    # Exit a parse tree produced by Swift3Parser#type_name.
    def exitType_name(self, ctx:Swift3Parser.Type_nameContext):
        pass


    # Enter a parse tree produced by Swift3Parser#tuple_type.
    def enterTuple_type(self, ctx:Swift3Parser.Tuple_typeContext):
        pass

    # Exit a parse tree produced by Swift3Parser#tuple_type.
    def exitTuple_type(self, ctx:Swift3Parser.Tuple_typeContext):
        pass


    # Enter a parse tree produced by Swift3Parser#tuple_type_element_list.
    def enterTuple_type_element_list(self, ctx:Swift3Parser.Tuple_type_element_listContext):
        pass

    # Exit a parse tree produced by Swift3Parser#tuple_type_element_list.
    def exitTuple_type_element_list(self, ctx:Swift3Parser.Tuple_type_element_listContext):
        pass


    # Enter a parse tree produced by Swift3Parser#tuple_type_element.
    def enterTuple_type_element(self, ctx:Swift3Parser.Tuple_type_elementContext):
        pass

    # Exit a parse tree produced by Swift3Parser#tuple_type_element.
    def exitTuple_type_element(self, ctx:Swift3Parser.Tuple_type_elementContext):
        pass


    # Enter a parse tree produced by Swift3Parser#element_name.
    def enterElement_name(self, ctx:Swift3Parser.Element_nameContext):
        pass

    # Exit a parse tree produced by Swift3Parser#element_name.
    def exitElement_name(self, ctx:Swift3Parser.Element_nameContext):
        pass


    # Enter a parse tree produced by Swift3Parser#function_type.
    def enterFunction_type(self, ctx:Swift3Parser.Function_typeContext):
        pass

    # Exit a parse tree produced by Swift3Parser#function_type.
    def exitFunction_type(self, ctx:Swift3Parser.Function_typeContext):
        pass


    # Enter a parse tree produced by Swift3Parser#function_type_argument_clause.
    def enterFunction_type_argument_clause(self, ctx:Swift3Parser.Function_type_argument_clauseContext):
        pass

    # Exit a parse tree produced by Swift3Parser#function_type_argument_clause.
    def exitFunction_type_argument_clause(self, ctx:Swift3Parser.Function_type_argument_clauseContext):
        pass


    # Enter a parse tree produced by Swift3Parser#function_type_argument_list.
    def enterFunction_type_argument_list(self, ctx:Swift3Parser.Function_type_argument_listContext):
        pass

    # Exit a parse tree produced by Swift3Parser#function_type_argument_list.
    def exitFunction_type_argument_list(self, ctx:Swift3Parser.Function_type_argument_listContext):
        pass


    # Enter a parse tree produced by Swift3Parser#function_type_argument.
    def enterFunction_type_argument(self, ctx:Swift3Parser.Function_type_argumentContext):
        pass

    # Exit a parse tree produced by Swift3Parser#function_type_argument.
    def exitFunction_type_argument(self, ctx:Swift3Parser.Function_type_argumentContext):
        pass


    # Enter a parse tree produced by Swift3Parser#argument_label.
    def enterArgument_label(self, ctx:Swift3Parser.Argument_labelContext):
        pass

    # Exit a parse tree produced by Swift3Parser#argument_label.
    def exitArgument_label(self, ctx:Swift3Parser.Argument_labelContext):
        pass


    # Enter a parse tree produced by Swift3Parser#array_type.
    def enterArray_type(self, ctx:Swift3Parser.Array_typeContext):
        pass

    # Exit a parse tree produced by Swift3Parser#array_type.
    def exitArray_type(self, ctx:Swift3Parser.Array_typeContext):
        pass


    # Enter a parse tree produced by Swift3Parser#dictionary_type.
    def enterDictionary_type(self, ctx:Swift3Parser.Dictionary_typeContext):
        pass

    # Exit a parse tree produced by Swift3Parser#dictionary_type.
    def exitDictionary_type(self, ctx:Swift3Parser.Dictionary_typeContext):
        pass


    # Enter a parse tree produced by Swift3Parser#protocol_composition_type.
    def enterProtocol_composition_type(self, ctx:Swift3Parser.Protocol_composition_typeContext):
        pass

    # Exit a parse tree produced by Swift3Parser#protocol_composition_type.
    def exitProtocol_composition_type(self, ctx:Swift3Parser.Protocol_composition_typeContext):
        pass


    # Enter a parse tree produced by Swift3Parser#protocol_identifier.
    def enterProtocol_identifier(self, ctx:Swift3Parser.Protocol_identifierContext):
        pass

    # Exit a parse tree produced by Swift3Parser#protocol_identifier.
    def exitProtocol_identifier(self, ctx:Swift3Parser.Protocol_identifierContext):
        pass


    # Enter a parse tree produced by Swift3Parser#type_inheritance_clause.
    def enterType_inheritance_clause(self, ctx:Swift3Parser.Type_inheritance_clauseContext):
        pass

    # Exit a parse tree produced by Swift3Parser#type_inheritance_clause.
    def exitType_inheritance_clause(self, ctx:Swift3Parser.Type_inheritance_clauseContext):
        pass


    # Enter a parse tree produced by Swift3Parser#type_inheritance_list.
    def enterType_inheritance_list(self, ctx:Swift3Parser.Type_inheritance_listContext):
        pass

    # Exit a parse tree produced by Swift3Parser#type_inheritance_list.
    def exitType_inheritance_list(self, ctx:Swift3Parser.Type_inheritance_listContext):
        pass


    # Enter a parse tree produced by Swift3Parser#class_requirement.
    def enterClass_requirement(self, ctx:Swift3Parser.Class_requirementContext):
        pass

    # Exit a parse tree produced by Swift3Parser#class_requirement.
    def exitClass_requirement(self, ctx:Swift3Parser.Class_requirementContext):
        pass


    # Enter a parse tree produced by Swift3Parser#declaration_identifier.
    def enterDeclaration_identifier(self, ctx:Swift3Parser.Declaration_identifierContext):
        pass

    # Exit a parse tree produced by Swift3Parser#declaration_identifier.
    def exitDeclaration_identifier(self, ctx:Swift3Parser.Declaration_identifierContext):
        pass


    # Enter a parse tree produced by Swift3Parser#label_identifier.
    def enterLabel_identifier(self, ctx:Swift3Parser.Label_identifierContext):
        pass

    # Exit a parse tree produced by Swift3Parser#label_identifier.
    def exitLabel_identifier(self, ctx:Swift3Parser.Label_identifierContext):
        pass


    # Enter a parse tree produced by Swift3Parser#keyword_as_identifier_in_declarations.
    def enterKeyword_as_identifier_in_declarations(self, ctx:Swift3Parser.Keyword_as_identifier_in_declarationsContext):
        pass

    # Exit a parse tree produced by Swift3Parser#keyword_as_identifier_in_declarations.
    def exitKeyword_as_identifier_in_declarations(self, ctx:Swift3Parser.Keyword_as_identifier_in_declarationsContext):
        pass


    # Enter a parse tree produced by Swift3Parser#keyword_as_identifier_in_labels.
    def enterKeyword_as_identifier_in_labels(self, ctx:Swift3Parser.Keyword_as_identifier_in_labelsContext):
        pass

    # Exit a parse tree produced by Swift3Parser#keyword_as_identifier_in_labels.
    def exitKeyword_as_identifier_in_labels(self, ctx:Swift3Parser.Keyword_as_identifier_in_labelsContext):
        pass


    # Enter a parse tree produced by Swift3Parser#assignment_operator.
    def enterAssignment_operator(self, ctx:Swift3Parser.Assignment_operatorContext):
        pass

    # Exit a parse tree produced by Swift3Parser#assignment_operator.
    def exitAssignment_operator(self, ctx:Swift3Parser.Assignment_operatorContext):
        pass


    # Enter a parse tree produced by Swift3Parser#negate_prefix_operator.
    def enterNegate_prefix_operator(self, ctx:Swift3Parser.Negate_prefix_operatorContext):
        pass

    # Exit a parse tree produced by Swift3Parser#negate_prefix_operator.
    def exitNegate_prefix_operator(self, ctx:Swift3Parser.Negate_prefix_operatorContext):
        pass


    # Enter a parse tree produced by Swift3Parser#compilation_condition_AND.
    def enterCompilation_condition_AND(self, ctx:Swift3Parser.Compilation_condition_ANDContext):
        pass

    # Exit a parse tree produced by Swift3Parser#compilation_condition_AND.
    def exitCompilation_condition_AND(self, ctx:Swift3Parser.Compilation_condition_ANDContext):
        pass


    # Enter a parse tree produced by Swift3Parser#compilation_condition_OR.
    def enterCompilation_condition_OR(self, ctx:Swift3Parser.Compilation_condition_ORContext):
        pass

    # Exit a parse tree produced by Swift3Parser#compilation_condition_OR.
    def exitCompilation_condition_OR(self, ctx:Swift3Parser.Compilation_condition_ORContext):
        pass


    # Enter a parse tree produced by Swift3Parser#compilation_condition_GE.
    def enterCompilation_condition_GE(self, ctx:Swift3Parser.Compilation_condition_GEContext):
        pass

    # Exit a parse tree produced by Swift3Parser#compilation_condition_GE.
    def exitCompilation_condition_GE(self, ctx:Swift3Parser.Compilation_condition_GEContext):
        pass


    # Enter a parse tree produced by Swift3Parser#arrow_operator.
    def enterArrow_operator(self, ctx:Swift3Parser.Arrow_operatorContext):
        pass

    # Exit a parse tree produced by Swift3Parser#arrow_operator.
    def exitArrow_operator(self, ctx:Swift3Parser.Arrow_operatorContext):
        pass


    # Enter a parse tree produced by Swift3Parser#range_operator.
    def enterRange_operator(self, ctx:Swift3Parser.Range_operatorContext):
        pass

    # Exit a parse tree produced by Swift3Parser#range_operator.
    def exitRange_operator(self, ctx:Swift3Parser.Range_operatorContext):
        pass


    # Enter a parse tree produced by Swift3Parser#same_type_equals.
    def enterSame_type_equals(self, ctx:Swift3Parser.Same_type_equalsContext):
        pass

    # Exit a parse tree produced by Swift3Parser#same_type_equals.
    def exitSame_type_equals(self, ctx:Swift3Parser.Same_type_equalsContext):
        pass


    # Enter a parse tree produced by Swift3Parser#binary_operator.
    def enterBinary_operator(self, ctx:Swift3Parser.Binary_operatorContext):
        pass

    # Exit a parse tree produced by Swift3Parser#binary_operator.
    def exitBinary_operator(self, ctx:Swift3Parser.Binary_operatorContext):
        pass


    # Enter a parse tree produced by Swift3Parser#prefix_operator.
    def enterPrefix_operator(self, ctx:Swift3Parser.Prefix_operatorContext):
        pass

    # Exit a parse tree produced by Swift3Parser#prefix_operator.
    def exitPrefix_operator(self, ctx:Swift3Parser.Prefix_operatorContext):
        pass


    # Enter a parse tree produced by Swift3Parser#postfix_operator.
    def enterPostfix_operator(self, ctx:Swift3Parser.Postfix_operatorContext):
        pass

    # Exit a parse tree produced by Swift3Parser#postfix_operator.
    def exitPostfix_operator(self, ctx:Swift3Parser.Postfix_operatorContext):
        pass


    # Enter a parse tree produced by Swift3Parser#operator.
    def enterOperator(self, ctx:Swift3Parser.OperatorContext):
        pass

    # Exit a parse tree produced by Swift3Parser#operator.
    def exitOperator(self, ctx:Swift3Parser.OperatorContext):
        pass


    # Enter a parse tree produced by Swift3Parser#operator_character.
    def enterOperator_character(self, ctx:Swift3Parser.Operator_characterContext):
        pass

    # Exit a parse tree produced by Swift3Parser#operator_character.
    def exitOperator_character(self, ctx:Swift3Parser.Operator_characterContext):
        pass


    # Enter a parse tree produced by Swift3Parser#operator_head.
    def enterOperator_head(self, ctx:Swift3Parser.Operator_headContext):
        pass

    # Exit a parse tree produced by Swift3Parser#operator_head.
    def exitOperator_head(self, ctx:Swift3Parser.Operator_headContext):
        pass


    # Enter a parse tree produced by Swift3Parser#dot_operator_head.
    def enterDot_operator_head(self, ctx:Swift3Parser.Dot_operator_headContext):
        pass

    # Exit a parse tree produced by Swift3Parser#dot_operator_head.
    def exitDot_operator_head(self, ctx:Swift3Parser.Dot_operator_headContext):
        pass


    # Enter a parse tree produced by Swift3Parser#dot_operator_character.
    def enterDot_operator_character(self, ctx:Swift3Parser.Dot_operator_characterContext):
        pass

    # Exit a parse tree produced by Swift3Parser#dot_operator_character.
    def exitDot_operator_character(self, ctx:Swift3Parser.Dot_operator_characterContext):
        pass


    # Enter a parse tree produced by Swift3Parser#literal.
    def enterLiteral(self, ctx:Swift3Parser.LiteralContext):
        pass

    # Exit a parse tree produced by Swift3Parser#literal.
    def exitLiteral(self, ctx:Swift3Parser.LiteralContext):
        pass


    # Enter a parse tree produced by Swift3Parser#numeric_literal.
    def enterNumeric_literal(self, ctx:Swift3Parser.Numeric_literalContext):
        pass

    # Exit a parse tree produced by Swift3Parser#numeric_literal.
    def exitNumeric_literal(self, ctx:Swift3Parser.Numeric_literalContext):
        pass


    # Enter a parse tree produced by Swift3Parser#boolean_literal.
    def enterBoolean_literal(self, ctx:Swift3Parser.Boolean_literalContext):
        pass

    # Exit a parse tree produced by Swift3Parser#boolean_literal.
    def exitBoolean_literal(self, ctx:Swift3Parser.Boolean_literalContext):
        pass


    # Enter a parse tree produced by Swift3Parser#nil_literal.
    def enterNil_literal(self, ctx:Swift3Parser.Nil_literalContext):
        pass

    # Exit a parse tree produced by Swift3Parser#nil_literal.
    def exitNil_literal(self, ctx:Swift3Parser.Nil_literalContext):
        pass


    # Enter a parse tree produced by Swift3Parser#integer_literal.
    def enterInteger_literal(self, ctx:Swift3Parser.Integer_literalContext):
        pass

    # Exit a parse tree produced by Swift3Parser#integer_literal.
    def exitInteger_literal(self, ctx:Swift3Parser.Integer_literalContext):
        pass


    # Enter a parse tree produced by Swift3Parser#string_literal.
    def enterString_literal(self, ctx:Swift3Parser.String_literalContext):
        pass

    # Exit a parse tree produced by Swift3Parser#string_literal.
    def exitString_literal(self, ctx:Swift3Parser.String_literalContext):
        pass


