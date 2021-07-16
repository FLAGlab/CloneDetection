import uuid
from clone_detection.ecst.ecst_tree import ECSTree
from clone_detection.ecst.ecst_node import ECSTNode, ShortToken
from .Swift5ParserListener import SwiftParserListener
from .Swift5Parser import SwiftParser
from clone_detection.grammars.grammars_registry import LISTENERS


@LISTENERS.register('swift')
class SwiftECSTListener(SwiftParserListener):
    def __init__(self):
        self.tree = ECSTree()
        self.current_node = self.tree

    # Enter a parse tree produced by Swift5Parser#top_level.
    def enterTop_level(self, ctx:Swift5Parser.Top_levelContext):
        act_token = ShortToken('', 0, 0)
        top_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token, 'TOP')
        self.current_node.add_child(top_node)
        self.current_node = top_node

    # Exit a parse tree produced by Swift5Parser#top_level.
    def exitTop_level(self, ctx:Swift5Parser.Top_levelContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by Swift5Parser#statement.
    def enterStatement(self, ctx:Swift5Parser.StatementContext):
        pass

    # Exit a parse tree produced by Swift5Parser#statement.
    def exitStatement(self, ctx:Swift5Parser.StatementContext):
        pass


    # Enter a parse tree produced by Swift5Parser#statements.
    def enterStatements(self, ctx:Swift5Parser.StatementsContext):
        pass

    # Exit a parse tree produced by Swift5Parser#statements.
    def exitStatements(self, ctx:Swift5Parser.StatementsContext):
        pass


    # Enter a parse tree produced by Swift5Parser#loop_statement.
    def enterLoop_statement(self, ctx:Swift5Parser.Loop_statementContext):
        pass

    # Exit a parse tree produced by Swift5Parser#loop_statement.
    def exitLoop_statement(self, ctx:Swift5Parser.Loop_statementContext):
        pass


    # Enter a parse tree produced by Swift5Parser#for_in_statement.
    def enterFor_in_statement(self, ctx:Swift5Parser.For_in_statementContext):
        pass

    # Exit a parse tree produced by Swift5Parser#for_in_statement.
    def exitFor_in_statement(self, ctx:Swift5Parser.For_in_statementContext):
        pass


    # Enter a parse tree produced by Swift5Parser#while_statement.
    def enterWhile_statement(self, ctx:Swift5Parser.While_statementContext):
        pass

    # Exit a parse tree produced by Swift5Parser#while_statement.
    def exitWhile_statement(self, ctx:Swift5Parser.While_statementContext):
        pass


    # Enter a parse tree produced by Swift5Parser#condition_list.
    def enterCondition_list(self, ctx:Swift5Parser.Condition_listContext):
        pass

    # Exit a parse tree produced by Swift5Parser#condition_list.
    def exitCondition_list(self, ctx:Swift5Parser.Condition_listContext):
        pass


    # Enter a parse tree produced by Swift5Parser#condition.
    def enterCondition(self, ctx:Swift5Parser.ConditionContext):
        pass

    # Exit a parse tree produced by Swift5Parser#condition.
    def exitCondition(self, ctx:Swift5Parser.ConditionContext):
        pass


    # Enter a parse tree produced by Swift5Parser#case_condition.
    def enterCase_condition(self, ctx:Swift5Parser.Case_conditionContext):
        pass

    # Exit a parse tree produced by Swift5Parser#case_condition.
    def exitCase_condition(self, ctx:Swift5Parser.Case_conditionContext):
        pass


    # Enter a parse tree produced by Swift5Parser#optional_binding_condition.
    def enterOptional_binding_condition(self, ctx:Swift5Parser.Optional_binding_conditionContext):
        pass

    # Exit a parse tree produced by Swift5Parser#optional_binding_condition.
    def exitOptional_binding_condition(self, ctx:Swift5Parser.Optional_binding_conditionContext):
        pass


    # Enter a parse tree produced by Swift5Parser#repeat_while_statement.
    def enterRepeat_while_statement(self, ctx:Swift5Parser.Repeat_while_statementContext):
        pass

    # Exit a parse tree produced by Swift5Parser#repeat_while_statement.
    def exitRepeat_while_statement(self, ctx:Swift5Parser.Repeat_while_statementContext):
        pass


    # Enter a parse tree produced by Swift5Parser#branch_statement.
    def enterBranch_statement(self, ctx:Swift5Parser.Branch_statementContext):
        pass

    # Exit a parse tree produced by Swift5Parser#branch_statement.
    def exitBranch_statement(self, ctx:Swift5Parser.Branch_statementContext):
        pass


    # Enter a parse tree produced by Swift5Parser#if_statement.
    def enterIf_statement(self, ctx:Swift5Parser.If_statementContext):
        pass

    # Exit a parse tree produced by Swift5Parser#if_statement.
    def exitIf_statement(self, ctx:Swift5Parser.If_statementContext):
        pass


    # Enter a parse tree produced by Swift5Parser#else_clause.
    def enterElse_clause(self, ctx:Swift5Parser.Else_clauseContext):
        pass

    # Exit a parse tree produced by Swift5Parser#else_clause.
    def exitElse_clause(self, ctx:Swift5Parser.Else_clauseContext):
        pass


    # Enter a parse tree produced by Swift5Parser#guard_statement.
    def enterGuard_statement(self, ctx:Swift5Parser.Guard_statementContext):
        pass

    # Exit a parse tree produced by Swift5Parser#guard_statement.
    def exitGuard_statement(self, ctx:Swift5Parser.Guard_statementContext):
        pass


    # Enter a parse tree produced by Swift5Parser#switch_statement.
    def enterSwitch_statement(self, ctx:Swift5Parser.Switch_statementContext):
        pass

    # Exit a parse tree produced by Swift5Parser#switch_statement.
    def exitSwitch_statement(self, ctx:Swift5Parser.Switch_statementContext):
        pass


    # Enter a parse tree produced by Swift5Parser#switch_cases.
    def enterSwitch_cases(self, ctx:Swift5Parser.Switch_casesContext):
        pass

    # Exit a parse tree produced by Swift5Parser#switch_cases.
    def exitSwitch_cases(self, ctx:Swift5Parser.Switch_casesContext):
        pass


    # Enter a parse tree produced by Swift5Parser#switch_case.
    def enterSwitch_case(self, ctx:Swift5Parser.Switch_caseContext):
        pass

    # Exit a parse tree produced by Swift5Parser#switch_case.
    def exitSwitch_case(self, ctx:Swift5Parser.Switch_caseContext):
        pass


    # Enter a parse tree produced by Swift5Parser#case_label.
    def enterCase_label(self, ctx:Swift5Parser.Case_labelContext):
        pass

    # Exit a parse tree produced by Swift5Parser#case_label.
    def exitCase_label(self, ctx:Swift5Parser.Case_labelContext):
        pass


    # Enter a parse tree produced by Swift5Parser#case_item_list.
    def enterCase_item_list(self, ctx:Swift5Parser.Case_item_listContext):
        pass

    # Exit a parse tree produced by Swift5Parser#case_item_list.
    def exitCase_item_list(self, ctx:Swift5Parser.Case_item_listContext):
        pass


    # Enter a parse tree produced by Swift5Parser#default_label.
    def enterDefault_label(self, ctx:Swift5Parser.Default_labelContext):
        pass

    # Exit a parse tree produced by Swift5Parser#default_label.
    def exitDefault_label(self, ctx:Swift5Parser.Default_labelContext):
        pass


    # Enter a parse tree produced by Swift5Parser#where_clause.
    def enterWhere_clause(self, ctx:Swift5Parser.Where_clauseContext):
        pass

    # Exit a parse tree produced by Swift5Parser#where_clause.
    def exitWhere_clause(self, ctx:Swift5Parser.Where_clauseContext):
        pass


    # Enter a parse tree produced by Swift5Parser#where_expression.
    def enterWhere_expression(self, ctx:Swift5Parser.Where_expressionContext):
        pass

    # Exit a parse tree produced by Swift5Parser#where_expression.
    def exitWhere_expression(self, ctx:Swift5Parser.Where_expressionContext):
        pass


    # Enter a parse tree produced by Swift5Parser#conditional_switch_case.
    def enterConditional_switch_case(self, ctx:Swift5Parser.Conditional_switch_caseContext):
        pass

    # Exit a parse tree produced by Swift5Parser#conditional_switch_case.
    def exitConditional_switch_case(self, ctx:Swift5Parser.Conditional_switch_caseContext):
        pass


    # Enter a parse tree produced by Swift5Parser#switch_if_directive_clause.
    def enterSwitch_if_directive_clause(self, ctx:Swift5Parser.Switch_if_directive_clauseContext):
        pass

    # Exit a parse tree produced by Swift5Parser#switch_if_directive_clause.
    def exitSwitch_if_directive_clause(self, ctx:Swift5Parser.Switch_if_directive_clauseContext):
        pass


    # Enter a parse tree produced by Swift5Parser#switch_elseif_directive_clauses.
    def enterSwitch_elseif_directive_clauses(self, ctx:Swift5Parser.Switch_elseif_directive_clausesContext):
        pass

    # Exit a parse tree produced by Swift5Parser#switch_elseif_directive_clauses.
    def exitSwitch_elseif_directive_clauses(self, ctx:Swift5Parser.Switch_elseif_directive_clausesContext):
        pass


    # Enter a parse tree produced by Swift5Parser#switch_elseif_directive_clause.
    def enterSwitch_elseif_directive_clause(self, ctx:Swift5Parser.Switch_elseif_directive_clauseContext):
        pass

    # Exit a parse tree produced by Swift5Parser#switch_elseif_directive_clause.
    def exitSwitch_elseif_directive_clause(self, ctx:Swift5Parser.Switch_elseif_directive_clauseContext):
        pass


    # Enter a parse tree produced by Swift5Parser#switch_else_directive_clause.
    def enterSwitch_else_directive_clause(self, ctx:Swift5Parser.Switch_else_directive_clauseContext):
        pass

    # Exit a parse tree produced by Swift5Parser#switch_else_directive_clause.
    def exitSwitch_else_directive_clause(self, ctx:Swift5Parser.Switch_else_directive_clauseContext):
        pass


    # Enter a parse tree produced by Swift5Parser#labeled_statement.
    def enterLabeled_statement(self, ctx:Swift5Parser.Labeled_statementContext):
        pass

    # Exit a parse tree produced by Swift5Parser#labeled_statement.
    def exitLabeled_statement(self, ctx:Swift5Parser.Labeled_statementContext):
        pass


    # Enter a parse tree produced by Swift5Parser#statement_label.
    def enterStatement_label(self, ctx:Swift5Parser.Statement_labelContext):
        pass

    # Exit a parse tree produced by Swift5Parser#statement_label.
    def exitStatement_label(self, ctx:Swift5Parser.Statement_labelContext):
        pass


    # Enter a parse tree produced by Swift5Parser#label_name.
    def enterLabel_name(self, ctx:Swift5Parser.Label_nameContext):
        pass

    # Exit a parse tree produced by Swift5Parser#label_name.
    def exitLabel_name(self, ctx:Swift5Parser.Label_nameContext):
        pass


    # Enter a parse tree produced by Swift5Parser#control_transfer_statement.
    def enterControl_transfer_statement(self, ctx:Swift5Parser.Control_transfer_statementContext):
        pass

    # Exit a parse tree produced by Swift5Parser#control_transfer_statement.
    def exitControl_transfer_statement(self, ctx:Swift5Parser.Control_transfer_statementContext):
        pass


    # Enter a parse tree produced by Swift5Parser#break_statement.
    def enterBreak_statement(self, ctx:Swift5Parser.Break_statementContext):
        pass

    # Exit a parse tree produced by Swift5Parser#break_statement.
    def exitBreak_statement(self, ctx:Swift5Parser.Break_statementContext):
        pass


    # Enter a parse tree produced by Swift5Parser#continue_statement.
    def enterContinue_statement(self, ctx:Swift5Parser.Continue_statementContext):
        pass

    # Exit a parse tree produced by Swift5Parser#continue_statement.
    def exitContinue_statement(self, ctx:Swift5Parser.Continue_statementContext):
        pass


    # Enter a parse tree produced by Swift5Parser#fallthrough_statement.
    def enterFallthrough_statement(self, ctx:Swift5Parser.Fallthrough_statementContext):
        pass

    # Exit a parse tree produced by Swift5Parser#fallthrough_statement.
    def exitFallthrough_statement(self, ctx:Swift5Parser.Fallthrough_statementContext):
        pass


    # Enter a parse tree produced by Swift5Parser#return_statement.
    def enterReturn_statement(self, ctx:Swift5Parser.Return_statementContext):
        pass

    # Exit a parse tree produced by Swift5Parser#return_statement.
    def exitReturn_statement(self, ctx:Swift5Parser.Return_statementContext):
        pass


    # Enter a parse tree produced by Swift5Parser#throw_statement.
    def enterThrow_statement(self, ctx:Swift5Parser.Throw_statementContext):
        pass

    # Exit a parse tree produced by Swift5Parser#throw_statement.
    def exitThrow_statement(self, ctx:Swift5Parser.Throw_statementContext):
        pass


    # Enter a parse tree produced by Swift5Parser#defer_statement.
    def enterDefer_statement(self, ctx:Swift5Parser.Defer_statementContext):
        pass

    # Exit a parse tree produced by Swift5Parser#defer_statement.
    def exitDefer_statement(self, ctx:Swift5Parser.Defer_statementContext):
        pass


    # Enter a parse tree produced by Swift5Parser#do_statement.
    def enterDo_statement(self, ctx:Swift5Parser.Do_statementContext):
        pass

    # Exit a parse tree produced by Swift5Parser#do_statement.
    def exitDo_statement(self, ctx:Swift5Parser.Do_statementContext):
        pass


    # Enter a parse tree produced by Swift5Parser#catch_clauses.
    def enterCatch_clauses(self, ctx:Swift5Parser.Catch_clausesContext):
        pass

    # Exit a parse tree produced by Swift5Parser#catch_clauses.
    def exitCatch_clauses(self, ctx:Swift5Parser.Catch_clausesContext):
        pass


    # Enter a parse tree produced by Swift5Parser#catch_clause.
    def enterCatch_clause(self, ctx:Swift5Parser.Catch_clauseContext):
        pass

    # Exit a parse tree produced by Swift5Parser#catch_clause.
    def exitCatch_clause(self, ctx:Swift5Parser.Catch_clauseContext):
        pass


    # Enter a parse tree produced by Swift5Parser#catch_pattern_list.
    def enterCatch_pattern_list(self, ctx:Swift5Parser.Catch_pattern_listContext):
        pass

    # Exit a parse tree produced by Swift5Parser#catch_pattern_list.
    def exitCatch_pattern_list(self, ctx:Swift5Parser.Catch_pattern_listContext):
        pass


    # Enter a parse tree produced by Swift5Parser#catch_pattern.
    def enterCatch_pattern(self, ctx:Swift5Parser.Catch_patternContext):
        pass

    # Exit a parse tree produced by Swift5Parser#catch_pattern.
    def exitCatch_pattern(self, ctx:Swift5Parser.Catch_patternContext):
        pass


    # Enter a parse tree produced by Swift5Parser#compiler_control_statement.
    def enterCompiler_control_statement(self, ctx:Swift5Parser.Compiler_control_statementContext):
        pass

    # Exit a parse tree produced by Swift5Parser#compiler_control_statement.
    def exitCompiler_control_statement(self, ctx:Swift5Parser.Compiler_control_statementContext):
        pass


    # Enter a parse tree produced by Swift5Parser#conditional_compilation_block.
    def enterConditional_compilation_block(self, ctx:Swift5Parser.Conditional_compilation_blockContext):
        pass

    # Exit a parse tree produced by Swift5Parser#conditional_compilation_block.
    def exitConditional_compilation_block(self, ctx:Swift5Parser.Conditional_compilation_blockContext):
        pass


    # Enter a parse tree produced by Swift5Parser#if_directive_clause.
    def enterIf_directive_clause(self, ctx:Swift5Parser.If_directive_clauseContext):
        pass

    # Exit a parse tree produced by Swift5Parser#if_directive_clause.
    def exitIf_directive_clause(self, ctx:Swift5Parser.If_directive_clauseContext):
        pass


    # Enter a parse tree produced by Swift5Parser#elseif_directive_clauses.
    def enterElseif_directive_clauses(self, ctx:Swift5Parser.Elseif_directive_clausesContext):
        pass

    # Exit a parse tree produced by Swift5Parser#elseif_directive_clauses.
    def exitElseif_directive_clauses(self, ctx:Swift5Parser.Elseif_directive_clausesContext):
        pass


    # Enter a parse tree produced by Swift5Parser#elseif_directive_clause.
    def enterElseif_directive_clause(self, ctx:Swift5Parser.Elseif_directive_clauseContext):
        pass

    # Exit a parse tree produced by Swift5Parser#elseif_directive_clause.
    def exitElseif_directive_clause(self, ctx:Swift5Parser.Elseif_directive_clauseContext):
        pass


    # Enter a parse tree produced by Swift5Parser#else_directive_clause.
    def enterElse_directive_clause(self, ctx:Swift5Parser.Else_directive_clauseContext):
        pass

    # Exit a parse tree produced by Swift5Parser#else_directive_clause.
    def exitElse_directive_clause(self, ctx:Swift5Parser.Else_directive_clauseContext):
        pass


    # Enter a parse tree produced by Swift5Parser#compilation_condition.
    def enterCompilation_condition(self, ctx:Swift5Parser.Compilation_conditionContext):
        pass

    # Exit a parse tree produced by Swift5Parser#compilation_condition.
    def exitCompilation_condition(self, ctx:Swift5Parser.Compilation_conditionContext):
        pass


    # Enter a parse tree produced by Swift5Parser#platform_condition.
    def enterPlatform_condition(self, ctx:Swift5Parser.Platform_conditionContext):
        pass

    # Exit a parse tree produced by Swift5Parser#platform_condition.
    def exitPlatform_condition(self, ctx:Swift5Parser.Platform_conditionContext):
        pass


    # Enter a parse tree produced by Swift5Parser#swift_version.
    def enterSwift_version(self, ctx:Swift5Parser.Swift_versionContext):
        pass

    # Exit a parse tree produced by Swift5Parser#swift_version.
    def exitSwift_version(self, ctx:Swift5Parser.Swift_versionContext):
        pass


    # Enter a parse tree produced by Swift5Parser#swift_version_continuation.
    def enterSwift_version_continuation(self, ctx:Swift5Parser.Swift_version_continuationContext):
        pass

    # Exit a parse tree produced by Swift5Parser#swift_version_continuation.
    def exitSwift_version_continuation(self, ctx:Swift5Parser.Swift_version_continuationContext):
        pass


    # Enter a parse tree produced by Swift5Parser#operating_system.
    def enterOperating_system(self, ctx:Swift5Parser.Operating_systemContext):
        pass

    # Exit a parse tree produced by Swift5Parser#operating_system.
    def exitOperating_system(self, ctx:Swift5Parser.Operating_systemContext):
        pass


    # Enter a parse tree produced by Swift5Parser#architecture.
    def enterArchitecture(self, ctx:Swift5Parser.ArchitectureContext):
        pass

    # Exit a parse tree produced by Swift5Parser#architecture.
    def exitArchitecture(self, ctx:Swift5Parser.ArchitectureContext):
        pass


    # Enter a parse tree produced by Swift5Parser#module_name.
    def enterModule_name(self, ctx:Swift5Parser.Module_nameContext):
        pass

    # Exit a parse tree produced by Swift5Parser#module_name.
    def exitModule_name(self, ctx:Swift5Parser.Module_nameContext):
        pass


    # Enter a parse tree produced by Swift5Parser#environment.
    def enterEnvironment(self, ctx:Swift5Parser.EnvironmentContext):
        pass

    # Exit a parse tree produced by Swift5Parser#environment.
    def exitEnvironment(self, ctx:Swift5Parser.EnvironmentContext):
        pass


    # Enter a parse tree produced by Swift5Parser#line_control_statement.
    def enterLine_control_statement(self, ctx:Swift5Parser.Line_control_statementContext):
        pass

    # Exit a parse tree produced by Swift5Parser#line_control_statement.
    def exitLine_control_statement(self, ctx:Swift5Parser.Line_control_statementContext):
        pass


    # Enter a parse tree produced by Swift5Parser#line_number.
    def enterLine_number(self, ctx:Swift5Parser.Line_numberContext):
        pass

    # Exit a parse tree produced by Swift5Parser#line_number.
    def exitLine_number(self, ctx:Swift5Parser.Line_numberContext):
        pass


    # Enter a parse tree produced by Swift5Parser#file_name.
    def enterFile_name(self, ctx:Swift5Parser.File_nameContext):
        pass

    # Exit a parse tree produced by Swift5Parser#file_name.
    def exitFile_name(self, ctx:Swift5Parser.File_nameContext):
        pass


    # Enter a parse tree produced by Swift5Parser#diagnostic_statement.
    def enterDiagnostic_statement(self, ctx:Swift5Parser.Diagnostic_statementContext):
        pass

    # Exit a parse tree produced by Swift5Parser#diagnostic_statement.
    def exitDiagnostic_statement(self, ctx:Swift5Parser.Diagnostic_statementContext):
        pass


    # Enter a parse tree produced by Swift5Parser#diagnostic_message.
    def enterDiagnostic_message(self, ctx:Swift5Parser.Diagnostic_messageContext):
        pass

    # Exit a parse tree produced by Swift5Parser#diagnostic_message.
    def exitDiagnostic_message(self, ctx:Swift5Parser.Diagnostic_messageContext):
        pass


    # Enter a parse tree produced by Swift5Parser#availability_condition.
    def enterAvailability_condition(self, ctx:Swift5Parser.Availability_conditionContext):
        pass

    # Exit a parse tree produced by Swift5Parser#availability_condition.
    def exitAvailability_condition(self, ctx:Swift5Parser.Availability_conditionContext):
        pass


    # Enter a parse tree produced by Swift5Parser#availability_arguments.
    def enterAvailability_arguments(self, ctx:Swift5Parser.Availability_argumentsContext):
        pass

    # Exit a parse tree produced by Swift5Parser#availability_arguments.
    def exitAvailability_arguments(self, ctx:Swift5Parser.Availability_argumentsContext):
        pass


    # Enter a parse tree produced by Swift5Parser#availability_argument.
    def enterAvailability_argument(self, ctx:Swift5Parser.Availability_argumentContext):
        pass

    # Exit a parse tree produced by Swift5Parser#availability_argument.
    def exitAvailability_argument(self, ctx:Swift5Parser.Availability_argumentContext):
        pass


    # Enter a parse tree produced by Swift5Parser#platform_name.
    def enterPlatform_name(self, ctx:Swift5Parser.Platform_nameContext):
        pass

    # Exit a parse tree produced by Swift5Parser#platform_name.
    def exitPlatform_name(self, ctx:Swift5Parser.Platform_nameContext):
        pass


    # Enter a parse tree produced by Swift5Parser#platform_version.
    def enterPlatform_version(self, ctx:Swift5Parser.Platform_versionContext):
        pass

    # Exit a parse tree produced by Swift5Parser#platform_version.
    def exitPlatform_version(self, ctx:Swift5Parser.Platform_versionContext):
        pass


    # Enter a parse tree produced by Swift5Parser#generic_parameter_clause.
    def enterGeneric_parameter_clause(self, ctx:Swift5Parser.Generic_parameter_clauseContext):
        pass

    # Exit a parse tree produced by Swift5Parser#generic_parameter_clause.
    def exitGeneric_parameter_clause(self, ctx:Swift5Parser.Generic_parameter_clauseContext):
        pass


    # Enter a parse tree produced by Swift5Parser#generic_parameter_list.
    def enterGeneric_parameter_list(self, ctx:Swift5Parser.Generic_parameter_listContext):
        pass

    # Exit a parse tree produced by Swift5Parser#generic_parameter_list.
    def exitGeneric_parameter_list(self, ctx:Swift5Parser.Generic_parameter_listContext):
        pass


    # Enter a parse tree produced by Swift5Parser#generic_parameter.
    def enterGeneric_parameter(self, ctx:Swift5Parser.Generic_parameterContext):
        pass

    # Exit a parse tree produced by Swift5Parser#generic_parameter.
    def exitGeneric_parameter(self, ctx:Swift5Parser.Generic_parameterContext):
        pass


    # Enter a parse tree produced by Swift5Parser#generic_where_clause.
    def enterGeneric_where_clause(self, ctx:Swift5Parser.Generic_where_clauseContext):
        pass

    # Exit a parse tree produced by Swift5Parser#generic_where_clause.
    def exitGeneric_where_clause(self, ctx:Swift5Parser.Generic_where_clauseContext):
        pass


    # Enter a parse tree produced by Swift5Parser#requirement_list.
    def enterRequirement_list(self, ctx:Swift5Parser.Requirement_listContext):
        pass

    # Exit a parse tree produced by Swift5Parser#requirement_list.
    def exitRequirement_list(self, ctx:Swift5Parser.Requirement_listContext):
        pass


    # Enter a parse tree produced by Swift5Parser#requirement.
    def enterRequirement(self, ctx:Swift5Parser.RequirementContext):
        pass

    # Exit a parse tree produced by Swift5Parser#requirement.
    def exitRequirement(self, ctx:Swift5Parser.RequirementContext):
        pass


    # Enter a parse tree produced by Swift5Parser#conformance_requirement.
    def enterConformance_requirement(self, ctx:Swift5Parser.Conformance_requirementContext):
        pass

    # Exit a parse tree produced by Swift5Parser#conformance_requirement.
    def exitConformance_requirement(self, ctx:Swift5Parser.Conformance_requirementContext):
        pass


    # Enter a parse tree produced by Swift5Parser#same_type_requirement.
    def enterSame_type_requirement(self, ctx:Swift5Parser.Same_type_requirementContext):
        pass

    # Exit a parse tree produced by Swift5Parser#same_type_requirement.
    def exitSame_type_requirement(self, ctx:Swift5Parser.Same_type_requirementContext):
        pass


    # Enter a parse tree produced by Swift5Parser#generic_argument_clause.
    def enterGeneric_argument_clause(self, ctx:Swift5Parser.Generic_argument_clauseContext):
        pass

    # Exit a parse tree produced by Swift5Parser#generic_argument_clause.
    def exitGeneric_argument_clause(self, ctx:Swift5Parser.Generic_argument_clauseContext):
        pass


    # Enter a parse tree produced by Swift5Parser#generic_argument_list.
    def enterGeneric_argument_list(self, ctx:Swift5Parser.Generic_argument_listContext):
        pass

    # Exit a parse tree produced by Swift5Parser#generic_argument_list.
    def exitGeneric_argument_list(self, ctx:Swift5Parser.Generic_argument_listContext):
        pass


    # Enter a parse tree produced by Swift5Parser#generic_argument.
    def enterGeneric_argument(self, ctx:Swift5Parser.Generic_argumentContext):
        pass

    # Exit a parse tree produced by Swift5Parser#generic_argument.
    def exitGeneric_argument(self, ctx:Swift5Parser.Generic_argumentContext):
        pass


    # Enter a parse tree produced by Swift5Parser#declaration.
    def enterDeclaration(self, ctx:Swift5Parser.DeclarationContext):
        pass

    # Exit a parse tree produced by Swift5Parser#declaration.
    def exitDeclaration(self, ctx:Swift5Parser.DeclarationContext):
        pass


    # Enter a parse tree produced by Swift5Parser#declarations.
    def enterDeclarations(self, ctx:Swift5Parser.DeclarationsContext):
        pass

    # Exit a parse tree produced by Swift5Parser#declarations.
    def exitDeclarations(self, ctx:Swift5Parser.DeclarationsContext):
        pass


    # Enter a parse tree produced by Swift5Parser#top_level_declaration.
    def enterTop_level_declaration(self, ctx:Swift5Parser.Top_level_declarationContext):
        pass

    # Exit a parse tree produced by Swift5Parser#top_level_declaration.
    def exitTop_level_declaration(self, ctx:Swift5Parser.Top_level_declarationContext):
        pass


    # Enter a parse tree produced by Swift5Parser#code_block.
    def enterCode_block(self, ctx:Swift5Parser.Code_blockContext):
        pass

    # Exit a parse tree produced by Swift5Parser#code_block.
    def exitCode_block(self, ctx:Swift5Parser.Code_blockContext):
        pass


    # Enter a parse tree produced by Swift5Parser#import_declaration.
    def enterImport_declaration(self, ctx:Swift5Parser.Import_declarationContext):
        pass

    # Exit a parse tree produced by Swift5Parser#import_declaration.
    def exitImport_declaration(self, ctx:Swift5Parser.Import_declarationContext):
        pass


    # Enter a parse tree produced by Swift5Parser#import_kind.
    def enterImport_kind(self, ctx:Swift5Parser.Import_kindContext):
        pass

    # Exit a parse tree produced by Swift5Parser#import_kind.
    def exitImport_kind(self, ctx:Swift5Parser.Import_kindContext):
        pass


    # Enter a parse tree produced by Swift5Parser#import_path.
    def enterImport_path(self, ctx:Swift5Parser.Import_pathContext):
        pass

    # Exit a parse tree produced by Swift5Parser#import_path.
    def exitImport_path(self, ctx:Swift5Parser.Import_pathContext):
        pass


    # Enter a parse tree produced by Swift5Parser#import_path_identifier.
    def enterImport_path_identifier(self, ctx:Swift5Parser.Import_path_identifierContext):
        pass

    # Exit a parse tree produced by Swift5Parser#import_path_identifier.
    def exitImport_path_identifier(self, ctx:Swift5Parser.Import_path_identifierContext):
        pass


    # Enter a parse tree produced by Swift5Parser#constant_declaration.
    def enterConstant_declaration(self, ctx:Swift5Parser.Constant_declarationContext):
        pass

    # Exit a parse tree produced by Swift5Parser#constant_declaration.
    def exitConstant_declaration(self, ctx:Swift5Parser.Constant_declarationContext):
        pass


    # Enter a parse tree produced by Swift5Parser#pattern_initializer_list.
    def enterPattern_initializer_list(self, ctx:Swift5Parser.Pattern_initializer_listContext):
        pass

    # Exit a parse tree produced by Swift5Parser#pattern_initializer_list.
    def exitPattern_initializer_list(self, ctx:Swift5Parser.Pattern_initializer_listContext):
        pass


    # Enter a parse tree produced by Swift5Parser#pattern_initializer.
    def enterPattern_initializer(self, ctx:Swift5Parser.Pattern_initializerContext):
        pass

    # Exit a parse tree produced by Swift5Parser#pattern_initializer.
    def exitPattern_initializer(self, ctx:Swift5Parser.Pattern_initializerContext):
        pass


    # Enter a parse tree produced by Swift5Parser#initializer.
    def enterInitializer(self, ctx:Swift5Parser.InitializerContext):
        pass

    # Exit a parse tree produced by Swift5Parser#initializer.
    def exitInitializer(self, ctx:Swift5Parser.InitializerContext):
        pass


    # Enter a parse tree produced by Swift5Parser#variable_declaration.
    def enterVariable_declaration(self, ctx:Swift5Parser.Variable_declarationContext):
        pass

    # Exit a parse tree produced by Swift5Parser#variable_declaration.
    def exitVariable_declaration(self, ctx:Swift5Parser.Variable_declarationContext):
        pass


    # Enter a parse tree produced by Swift5Parser#variable_declaration_head.
    def enterVariable_declaration_head(self, ctx:Swift5Parser.Variable_declaration_headContext):
        pass

    # Exit a parse tree produced by Swift5Parser#variable_declaration_head.
    def exitVariable_declaration_head(self, ctx:Swift5Parser.Variable_declaration_headContext):
        pass


    # Enter a parse tree produced by Swift5Parser#variable_name.
    def enterVariable_name(self, ctx:Swift5Parser.Variable_nameContext):
        pass

    # Exit a parse tree produced by Swift5Parser#variable_name.
    def exitVariable_name(self, ctx:Swift5Parser.Variable_nameContext):
        pass


    # Enter a parse tree produced by Swift5Parser#getter_setter_block.
    def enterGetter_setter_block(self, ctx:Swift5Parser.Getter_setter_blockContext):
        pass

    # Exit a parse tree produced by Swift5Parser#getter_setter_block.
    def exitGetter_setter_block(self, ctx:Swift5Parser.Getter_setter_blockContext):
        pass


    # Enter a parse tree produced by Swift5Parser#getter_clause.
    def enterGetter_clause(self, ctx:Swift5Parser.Getter_clauseContext):
        pass

    # Exit a parse tree produced by Swift5Parser#getter_clause.
    def exitGetter_clause(self, ctx:Swift5Parser.Getter_clauseContext):
        pass


    # Enter a parse tree produced by Swift5Parser#setter_clause.
    def enterSetter_clause(self, ctx:Swift5Parser.Setter_clauseContext):
        pass

    # Exit a parse tree produced by Swift5Parser#setter_clause.
    def exitSetter_clause(self, ctx:Swift5Parser.Setter_clauseContext):
        pass


    # Enter a parse tree produced by Swift5Parser#setter_name.
    def enterSetter_name(self, ctx:Swift5Parser.Setter_nameContext):
        pass

    # Exit a parse tree produced by Swift5Parser#setter_name.
    def exitSetter_name(self, ctx:Swift5Parser.Setter_nameContext):
        pass


    # Enter a parse tree produced by Swift5Parser#getter_setter_keyword_block.
    def enterGetter_setter_keyword_block(self, ctx:Swift5Parser.Getter_setter_keyword_blockContext):
        pass

    # Exit a parse tree produced by Swift5Parser#getter_setter_keyword_block.
    def exitGetter_setter_keyword_block(self, ctx:Swift5Parser.Getter_setter_keyword_blockContext):
        pass


    # Enter a parse tree produced by Swift5Parser#getter_keyword_clause.
    def enterGetter_keyword_clause(self, ctx:Swift5Parser.Getter_keyword_clauseContext):
        pass

    # Exit a parse tree produced by Swift5Parser#getter_keyword_clause.
    def exitGetter_keyword_clause(self, ctx:Swift5Parser.Getter_keyword_clauseContext):
        pass


    # Enter a parse tree produced by Swift5Parser#setter_keyword_clause.
    def enterSetter_keyword_clause(self, ctx:Swift5Parser.Setter_keyword_clauseContext):
        pass

    # Exit a parse tree produced by Swift5Parser#setter_keyword_clause.
    def exitSetter_keyword_clause(self, ctx:Swift5Parser.Setter_keyword_clauseContext):
        pass


    # Enter a parse tree produced by Swift5Parser#willSet_didSet_block.
    def enterWillSet_didSet_block(self, ctx:Swift5Parser.WillSet_didSet_blockContext):
        pass

    # Exit a parse tree produced by Swift5Parser#willSet_didSet_block.
    def exitWillSet_didSet_block(self, ctx:Swift5Parser.WillSet_didSet_blockContext):
        pass


    # Enter a parse tree produced by Swift5Parser#willSet_clause.
    def enterWillSet_clause(self, ctx:Swift5Parser.WillSet_clauseContext):
        pass

    # Exit a parse tree produced by Swift5Parser#willSet_clause.
    def exitWillSet_clause(self, ctx:Swift5Parser.WillSet_clauseContext):
        pass


    # Enter a parse tree produced by Swift5Parser#didSet_clause.
    def enterDidSet_clause(self, ctx:Swift5Parser.DidSet_clauseContext):
        pass

    # Exit a parse tree produced by Swift5Parser#didSet_clause.
    def exitDidSet_clause(self, ctx:Swift5Parser.DidSet_clauseContext):
        pass


    # Enter a parse tree produced by Swift5Parser#typealias_declaration.
    def enterTypealias_declaration(self, ctx:Swift5Parser.Typealias_declarationContext):
        pass

    # Exit a parse tree produced by Swift5Parser#typealias_declaration.
    def exitTypealias_declaration(self, ctx:Swift5Parser.Typealias_declarationContext):
        pass


    # Enter a parse tree produced by Swift5Parser#typealias_name.
    def enterTypealias_name(self, ctx:Swift5Parser.Typealias_nameContext):
        pass

    # Exit a parse tree produced by Swift5Parser#typealias_name.
    def exitTypealias_name(self, ctx:Swift5Parser.Typealias_nameContext):
        pass


    # Enter a parse tree produced by Swift5Parser#typealias_assignment.
    def enterTypealias_assignment(self, ctx:Swift5Parser.Typealias_assignmentContext):
        pass

    # Exit a parse tree produced by Swift5Parser#typealias_assignment.
    def exitTypealias_assignment(self, ctx:Swift5Parser.Typealias_assignmentContext):
        pass


    # Enter a parse tree produced by Swift5Parser#function_declaration.
    def enterFunction_declaration(self, ctx:Swift5Parser.Function_declarationContext):
        pass

    # Exit a parse tree produced by Swift5Parser#function_declaration.
    def exitFunction_declaration(self, ctx:Swift5Parser.Function_declarationContext):
        pass


    # Enter a parse tree produced by Swift5Parser#function_head.
    def enterFunction_head(self, ctx:Swift5Parser.Function_headContext):
        pass

    # Exit a parse tree produced by Swift5Parser#function_head.
    def exitFunction_head(self, ctx:Swift5Parser.Function_headContext):
        pass


    # Enter a parse tree produced by Swift5Parser#function_name.
    def enterFunction_name(self, ctx:Swift5Parser.Function_nameContext):
        pass

    # Exit a parse tree produced by Swift5Parser#function_name.
    def exitFunction_name(self, ctx:Swift5Parser.Function_nameContext):
        pass


    # Enter a parse tree produced by Swift5Parser#function_signature.
    def enterFunction_signature(self, ctx:Swift5Parser.Function_signatureContext):
        pass

    # Exit a parse tree produced by Swift5Parser#function_signature.
    def exitFunction_signature(self, ctx:Swift5Parser.Function_signatureContext):
        pass


    # Enter a parse tree produced by Swift5Parser#function_result.
    def enterFunction_result(self, ctx:Swift5Parser.Function_resultContext):
        pass

    # Exit a parse tree produced by Swift5Parser#function_result.
    def exitFunction_result(self, ctx:Swift5Parser.Function_resultContext):
        pass


    # Enter a parse tree produced by Swift5Parser#function_body.
    def enterFunction_body(self, ctx:Swift5Parser.Function_bodyContext):
        pass

    # Exit a parse tree produced by Swift5Parser#function_body.
    def exitFunction_body(self, ctx:Swift5Parser.Function_bodyContext):
        pass


    # Enter a parse tree produced by Swift5Parser#parameter_clause.
    def enterParameter_clause(self, ctx:Swift5Parser.Parameter_clauseContext):
        pass

    # Exit a parse tree produced by Swift5Parser#parameter_clause.
    def exitParameter_clause(self, ctx:Swift5Parser.Parameter_clauseContext):
        pass


    # Enter a parse tree produced by Swift5Parser#parameter_list.
    def enterParameter_list(self, ctx:Swift5Parser.Parameter_listContext):
        pass

    # Exit a parse tree produced by Swift5Parser#parameter_list.
    def exitParameter_list(self, ctx:Swift5Parser.Parameter_listContext):
        pass


    # Enter a parse tree produced by Swift5Parser#parameter.
    def enterParameter(self, ctx:Swift5Parser.ParameterContext):
        pass

    # Exit a parse tree produced by Swift5Parser#parameter.
    def exitParameter(self, ctx:Swift5Parser.ParameterContext):
        pass


    # Enter a parse tree produced by Swift5Parser#external_parameter_name.
    def enterExternal_parameter_name(self, ctx:Swift5Parser.External_parameter_nameContext):
        pass

    # Exit a parse tree produced by Swift5Parser#external_parameter_name.
    def exitExternal_parameter_name(self, ctx:Swift5Parser.External_parameter_nameContext):
        pass


    # Enter a parse tree produced by Swift5Parser#local_parameter_name.
    def enterLocal_parameter_name(self, ctx:Swift5Parser.Local_parameter_nameContext):
        pass

    # Exit a parse tree produced by Swift5Parser#local_parameter_name.
    def exitLocal_parameter_name(self, ctx:Swift5Parser.Local_parameter_nameContext):
        pass


    # Enter a parse tree produced by Swift5Parser#default_argument_clause.
    def enterDefault_argument_clause(self, ctx:Swift5Parser.Default_argument_clauseContext):
        pass

    # Exit a parse tree produced by Swift5Parser#default_argument_clause.
    def exitDefault_argument_clause(self, ctx:Swift5Parser.Default_argument_clauseContext):
        pass


    # Enter a parse tree produced by Swift5Parser#enum_declaration.
    def enterEnum_declaration(self, ctx:Swift5Parser.Enum_declarationContext):
        pass

    # Exit a parse tree produced by Swift5Parser#enum_declaration.
    def exitEnum_declaration(self, ctx:Swift5Parser.Enum_declarationContext):
        pass


    # Enter a parse tree produced by Swift5Parser#union_style_enum.
    def enterUnion_style_enum(self, ctx:Swift5Parser.Union_style_enumContext):
        pass

    # Exit a parse tree produced by Swift5Parser#union_style_enum.
    def exitUnion_style_enum(self, ctx:Swift5Parser.Union_style_enumContext):
        pass


    # Enter a parse tree produced by Swift5Parser#union_style_enum_members.
    def enterUnion_style_enum_members(self, ctx:Swift5Parser.Union_style_enum_membersContext):
        pass

    # Exit a parse tree produced by Swift5Parser#union_style_enum_members.
    def exitUnion_style_enum_members(self, ctx:Swift5Parser.Union_style_enum_membersContext):
        pass


    # Enter a parse tree produced by Swift5Parser#union_style_enum_member.
    def enterUnion_style_enum_member(self, ctx:Swift5Parser.Union_style_enum_memberContext):
        pass

    # Exit a parse tree produced by Swift5Parser#union_style_enum_member.
    def exitUnion_style_enum_member(self, ctx:Swift5Parser.Union_style_enum_memberContext):
        pass


    # Enter a parse tree produced by Swift5Parser#union_style_enum_case_clause.
    def enterUnion_style_enum_case_clause(self, ctx:Swift5Parser.Union_style_enum_case_clauseContext):
        pass

    # Exit a parse tree produced by Swift5Parser#union_style_enum_case_clause.
    def exitUnion_style_enum_case_clause(self, ctx:Swift5Parser.Union_style_enum_case_clauseContext):
        pass


    # Enter a parse tree produced by Swift5Parser#union_style_enum_case_list.
    def enterUnion_style_enum_case_list(self, ctx:Swift5Parser.Union_style_enum_case_listContext):
        pass

    # Exit a parse tree produced by Swift5Parser#union_style_enum_case_list.
    def exitUnion_style_enum_case_list(self, ctx:Swift5Parser.Union_style_enum_case_listContext):
        pass


    # Enter a parse tree produced by Swift5Parser#union_style_enum_case.
    def enterUnion_style_enum_case(self, ctx:Swift5Parser.Union_style_enum_caseContext):
        pass

    # Exit a parse tree produced by Swift5Parser#union_style_enum_case.
    def exitUnion_style_enum_case(self, ctx:Swift5Parser.Union_style_enum_caseContext):
        pass


    # Enter a parse tree produced by Swift5Parser#enum_name.
    def enterEnum_name(self, ctx:Swift5Parser.Enum_nameContext):
        pass

    # Exit a parse tree produced by Swift5Parser#enum_name.
    def exitEnum_name(self, ctx:Swift5Parser.Enum_nameContext):
        pass


    # Enter a parse tree produced by Swift5Parser#enum_case_name.
    def enterEnum_case_name(self, ctx:Swift5Parser.Enum_case_nameContext):
        pass

    # Exit a parse tree produced by Swift5Parser#enum_case_name.
    def exitEnum_case_name(self, ctx:Swift5Parser.Enum_case_nameContext):
        pass


    # Enter a parse tree produced by Swift5Parser#raw_value_style_enum.
    def enterRaw_value_style_enum(self, ctx:Swift5Parser.Raw_value_style_enumContext):
        pass

    # Exit a parse tree produced by Swift5Parser#raw_value_style_enum.
    def exitRaw_value_style_enum(self, ctx:Swift5Parser.Raw_value_style_enumContext):
        pass


    # Enter a parse tree produced by Swift5Parser#raw_value_style_enum_members.
    def enterRaw_value_style_enum_members(self, ctx:Swift5Parser.Raw_value_style_enum_membersContext):
        pass

    # Exit a parse tree produced by Swift5Parser#raw_value_style_enum_members.
    def exitRaw_value_style_enum_members(self, ctx:Swift5Parser.Raw_value_style_enum_membersContext):
        pass


    # Enter a parse tree produced by Swift5Parser#raw_value_style_enum_member.
    def enterRaw_value_style_enum_member(self, ctx:Swift5Parser.Raw_value_style_enum_memberContext):
        pass

    # Exit a parse tree produced by Swift5Parser#raw_value_style_enum_member.
    def exitRaw_value_style_enum_member(self, ctx:Swift5Parser.Raw_value_style_enum_memberContext):
        pass


    # Enter a parse tree produced by Swift5Parser#raw_value_style_enum_case_clause.
    def enterRaw_value_style_enum_case_clause(self, ctx:Swift5Parser.Raw_value_style_enum_case_clauseContext):
        pass

    # Exit a parse tree produced by Swift5Parser#raw_value_style_enum_case_clause.
    def exitRaw_value_style_enum_case_clause(self, ctx:Swift5Parser.Raw_value_style_enum_case_clauseContext):
        pass


    # Enter a parse tree produced by Swift5Parser#raw_value_style_enum_case_list.
    def enterRaw_value_style_enum_case_list(self, ctx:Swift5Parser.Raw_value_style_enum_case_listContext):
        pass

    # Exit a parse tree produced by Swift5Parser#raw_value_style_enum_case_list.
    def exitRaw_value_style_enum_case_list(self, ctx:Swift5Parser.Raw_value_style_enum_case_listContext):
        pass


    # Enter a parse tree produced by Swift5Parser#raw_value_style_enum_case.
    def enterRaw_value_style_enum_case(self, ctx:Swift5Parser.Raw_value_style_enum_caseContext):
        pass

    # Exit a parse tree produced by Swift5Parser#raw_value_style_enum_case.
    def exitRaw_value_style_enum_case(self, ctx:Swift5Parser.Raw_value_style_enum_caseContext):
        pass


    # Enter a parse tree produced by Swift5Parser#raw_value_assignment.
    def enterRaw_value_assignment(self, ctx:Swift5Parser.Raw_value_assignmentContext):
        pass

    # Exit a parse tree produced by Swift5Parser#raw_value_assignment.
    def exitRaw_value_assignment(self, ctx:Swift5Parser.Raw_value_assignmentContext):
        pass


    # Enter a parse tree produced by Swift5Parser#raw_value_literal.
    def enterRaw_value_literal(self, ctx:Swift5Parser.Raw_value_literalContext):
        pass

    # Exit a parse tree produced by Swift5Parser#raw_value_literal.
    def exitRaw_value_literal(self, ctx:Swift5Parser.Raw_value_literalContext):
        pass


    # Enter a parse tree produced by Swift5Parser#struct_declaration.
    def enterStruct_declaration(self, ctx:Swift5Parser.Struct_declarationContext):
        pass

    # Exit a parse tree produced by Swift5Parser#struct_declaration.
    def exitStruct_declaration(self, ctx:Swift5Parser.Struct_declarationContext):
        pass


    # Enter a parse tree produced by Swift5Parser#struct_name.
    def enterStruct_name(self, ctx:Swift5Parser.Struct_nameContext):
        pass

    # Exit a parse tree produced by Swift5Parser#struct_name.
    def exitStruct_name(self, ctx:Swift5Parser.Struct_nameContext):
        pass


    # Enter a parse tree produced by Swift5Parser#struct_body.
    def enterStruct_body(self, ctx:Swift5Parser.Struct_bodyContext):
        pass

    # Exit a parse tree produced by Swift5Parser#struct_body.
    def exitStruct_body(self, ctx:Swift5Parser.Struct_bodyContext):
        pass


    # Enter a parse tree produced by Swift5Parser#struct_members.
    def enterStruct_members(self, ctx:Swift5Parser.Struct_membersContext):
        pass

    # Exit a parse tree produced by Swift5Parser#struct_members.
    def exitStruct_members(self, ctx:Swift5Parser.Struct_membersContext):
        pass


    # Enter a parse tree produced by Swift5Parser#struct_member.
    def enterStruct_member(self, ctx:Swift5Parser.Struct_memberContext):
        pass

    # Exit a parse tree produced by Swift5Parser#struct_member.
    def exitStruct_member(self, ctx:Swift5Parser.Struct_memberContext):
        pass


    # Enter a parse tree produced by Swift5Parser#class_declaration.
    def enterClass_declaration(self, ctx:Swift5Parser.Class_declarationContext):
        pass

    # Exit a parse tree produced by Swift5Parser#class_declaration.
    def exitClass_declaration(self, ctx:Swift5Parser.Class_declarationContext):
        pass


    # Enter a parse tree produced by Swift5Parser#class_name.
    def enterClass_name(self, ctx:Swift5Parser.Class_nameContext):
        pass

    # Exit a parse tree produced by Swift5Parser#class_name.
    def exitClass_name(self, ctx:Swift5Parser.Class_nameContext):
        pass


    # Enter a parse tree produced by Swift5Parser#class_body.
    def enterClass_body(self, ctx:Swift5Parser.Class_bodyContext):
        pass

    # Exit a parse tree produced by Swift5Parser#class_body.
    def exitClass_body(self, ctx:Swift5Parser.Class_bodyContext):
        pass


    # Enter a parse tree produced by Swift5Parser#class_members.
    def enterClass_members(self, ctx:Swift5Parser.Class_membersContext):
        pass

    # Exit a parse tree produced by Swift5Parser#class_members.
    def exitClass_members(self, ctx:Swift5Parser.Class_membersContext):
        pass


    # Enter a parse tree produced by Swift5Parser#class_member.
    def enterClass_member(self, ctx:Swift5Parser.Class_memberContext):
        pass

    # Exit a parse tree produced by Swift5Parser#class_member.
    def exitClass_member(self, ctx:Swift5Parser.Class_memberContext):
        pass


    # Enter a parse tree produced by Swift5Parser#protocol_declaration.
    def enterProtocol_declaration(self, ctx:Swift5Parser.Protocol_declarationContext):
        pass

    # Exit a parse tree produced by Swift5Parser#protocol_declaration.
    def exitProtocol_declaration(self, ctx:Swift5Parser.Protocol_declarationContext):
        pass


    # Enter a parse tree produced by Swift5Parser#protocol_name.
    def enterProtocol_name(self, ctx:Swift5Parser.Protocol_nameContext):
        pass

    # Exit a parse tree produced by Swift5Parser#protocol_name.
    def exitProtocol_name(self, ctx:Swift5Parser.Protocol_nameContext):
        pass


    # Enter a parse tree produced by Swift5Parser#protocol_body.
    def enterProtocol_body(self, ctx:Swift5Parser.Protocol_bodyContext):
        pass

    # Exit a parse tree produced by Swift5Parser#protocol_body.
    def exitProtocol_body(self, ctx:Swift5Parser.Protocol_bodyContext):
        pass


    # Enter a parse tree produced by Swift5Parser#protocol_members.
    def enterProtocol_members(self, ctx:Swift5Parser.Protocol_membersContext):
        pass

    # Exit a parse tree produced by Swift5Parser#protocol_members.
    def exitProtocol_members(self, ctx:Swift5Parser.Protocol_membersContext):
        pass


    # Enter a parse tree produced by Swift5Parser#protocol_member.
    def enterProtocol_member(self, ctx:Swift5Parser.Protocol_memberContext):
        pass

    # Exit a parse tree produced by Swift5Parser#protocol_member.
    def exitProtocol_member(self, ctx:Swift5Parser.Protocol_memberContext):
        pass


    # Enter a parse tree produced by Swift5Parser#protocol_member_declaration.
    def enterProtocol_member_declaration(self, ctx:Swift5Parser.Protocol_member_declarationContext):
        pass

    # Exit a parse tree produced by Swift5Parser#protocol_member_declaration.
    def exitProtocol_member_declaration(self, ctx:Swift5Parser.Protocol_member_declarationContext):
        pass


    # Enter a parse tree produced by Swift5Parser#protocol_property_declaration.
    def enterProtocol_property_declaration(self, ctx:Swift5Parser.Protocol_property_declarationContext):
        pass

    # Exit a parse tree produced by Swift5Parser#protocol_property_declaration.
    def exitProtocol_property_declaration(self, ctx:Swift5Parser.Protocol_property_declarationContext):
        pass


    # Enter a parse tree produced by Swift5Parser#protocol_method_declaration.
    def enterProtocol_method_declaration(self, ctx:Swift5Parser.Protocol_method_declarationContext):
        pass

    # Exit a parse tree produced by Swift5Parser#protocol_method_declaration.
    def exitProtocol_method_declaration(self, ctx:Swift5Parser.Protocol_method_declarationContext):
        pass


    # Enter a parse tree produced by Swift5Parser#protocol_initializer_declaration.
    def enterProtocol_initializer_declaration(self, ctx:Swift5Parser.Protocol_initializer_declarationContext):
        pass

    # Exit a parse tree produced by Swift5Parser#protocol_initializer_declaration.
    def exitProtocol_initializer_declaration(self, ctx:Swift5Parser.Protocol_initializer_declarationContext):
        pass


    # Enter a parse tree produced by Swift5Parser#protocol_subscript_declaration.
    def enterProtocol_subscript_declaration(self, ctx:Swift5Parser.Protocol_subscript_declarationContext):
        pass

    # Exit a parse tree produced by Swift5Parser#protocol_subscript_declaration.
    def exitProtocol_subscript_declaration(self, ctx:Swift5Parser.Protocol_subscript_declarationContext):
        pass


    # Enter a parse tree produced by Swift5Parser#protocol_associated_type_declaration.
    def enterProtocol_associated_type_declaration(self, ctx:Swift5Parser.Protocol_associated_type_declarationContext):
        pass

    # Exit a parse tree produced by Swift5Parser#protocol_associated_type_declaration.
    def exitProtocol_associated_type_declaration(self, ctx:Swift5Parser.Protocol_associated_type_declarationContext):
        pass


    # Enter a parse tree produced by Swift5Parser#initializer_declaration.
    def enterInitializer_declaration(self, ctx:Swift5Parser.Initializer_declarationContext):
        pass

    # Exit a parse tree produced by Swift5Parser#initializer_declaration.
    def exitInitializer_declaration(self, ctx:Swift5Parser.Initializer_declarationContext):
        pass


    # Enter a parse tree produced by Swift5Parser#initializer_head.
    def enterInitializer_head(self, ctx:Swift5Parser.Initializer_headContext):
        pass

    # Exit a parse tree produced by Swift5Parser#initializer_head.
    def exitInitializer_head(self, ctx:Swift5Parser.Initializer_headContext):
        pass


    # Enter a parse tree produced by Swift5Parser#initializer_body.
    def enterInitializer_body(self, ctx:Swift5Parser.Initializer_bodyContext):
        pass

    # Exit a parse tree produced by Swift5Parser#initializer_body.
    def exitInitializer_body(self, ctx:Swift5Parser.Initializer_bodyContext):
        pass


    # Enter a parse tree produced by Swift5Parser#deinitializer_declaration.
    def enterDeinitializer_declaration(self, ctx:Swift5Parser.Deinitializer_declarationContext):
        pass

    # Exit a parse tree produced by Swift5Parser#deinitializer_declaration.
    def exitDeinitializer_declaration(self, ctx:Swift5Parser.Deinitializer_declarationContext):
        pass


    # Enter a parse tree produced by Swift5Parser#extension_declaration.
    def enterExtension_declaration(self, ctx:Swift5Parser.Extension_declarationContext):
        pass

    # Exit a parse tree produced by Swift5Parser#extension_declaration.
    def exitExtension_declaration(self, ctx:Swift5Parser.Extension_declarationContext):
        pass


    # Enter a parse tree produced by Swift5Parser#extension_body.
    def enterExtension_body(self, ctx:Swift5Parser.Extension_bodyContext):
        pass

    # Exit a parse tree produced by Swift5Parser#extension_body.
    def exitExtension_body(self, ctx:Swift5Parser.Extension_bodyContext):
        pass


    # Enter a parse tree produced by Swift5Parser#extension_members.
    def enterExtension_members(self, ctx:Swift5Parser.Extension_membersContext):
        pass

    # Exit a parse tree produced by Swift5Parser#extension_members.
    def exitExtension_members(self, ctx:Swift5Parser.Extension_membersContext):
        pass


    # Enter a parse tree produced by Swift5Parser#extension_member.
    def enterExtension_member(self, ctx:Swift5Parser.Extension_memberContext):
        pass

    # Exit a parse tree produced by Swift5Parser#extension_member.
    def exitExtension_member(self, ctx:Swift5Parser.Extension_memberContext):
        pass


    # Enter a parse tree produced by Swift5Parser#subscript_declaration.
    def enterSubscript_declaration(self, ctx:Swift5Parser.Subscript_declarationContext):
        pass

    # Exit a parse tree produced by Swift5Parser#subscript_declaration.
    def exitSubscript_declaration(self, ctx:Swift5Parser.Subscript_declarationContext):
        pass


    # Enter a parse tree produced by Swift5Parser#subscript_head.
    def enterSubscript_head(self, ctx:Swift5Parser.Subscript_headContext):
        pass

    # Exit a parse tree produced by Swift5Parser#subscript_head.
    def exitSubscript_head(self, ctx:Swift5Parser.Subscript_headContext):
        pass


    # Enter a parse tree produced by Swift5Parser#subscript_result.
    def enterSubscript_result(self, ctx:Swift5Parser.Subscript_resultContext):
        pass

    # Exit a parse tree produced by Swift5Parser#subscript_result.
    def exitSubscript_result(self, ctx:Swift5Parser.Subscript_resultContext):
        pass


    # Enter a parse tree produced by Swift5Parser#operator_declaration.
    def enterOperator_declaration(self, ctx:Swift5Parser.Operator_declarationContext):
        pass

    # Exit a parse tree produced by Swift5Parser#operator_declaration.
    def exitOperator_declaration(self, ctx:Swift5Parser.Operator_declarationContext):
        pass


    # Enter a parse tree produced by Swift5Parser#prefix_operator_declaration.
    def enterPrefix_operator_declaration(self, ctx:Swift5Parser.Prefix_operator_declarationContext):
        pass

    # Exit a parse tree produced by Swift5Parser#prefix_operator_declaration.
    def exitPrefix_operator_declaration(self, ctx:Swift5Parser.Prefix_operator_declarationContext):
        pass


    # Enter a parse tree produced by Swift5Parser#postfix_operator_declaration.
    def enterPostfix_operator_declaration(self, ctx:Swift5Parser.Postfix_operator_declarationContext):
        pass

    # Exit a parse tree produced by Swift5Parser#postfix_operator_declaration.
    def exitPostfix_operator_declaration(self, ctx:Swift5Parser.Postfix_operator_declarationContext):
        pass


    # Enter a parse tree produced by Swift5Parser#infix_operator_declaration.
    def enterInfix_operator_declaration(self, ctx:Swift5Parser.Infix_operator_declarationContext):
        pass

    # Exit a parse tree produced by Swift5Parser#infix_operator_declaration.
    def exitInfix_operator_declaration(self, ctx:Swift5Parser.Infix_operator_declarationContext):
        pass


    # Enter a parse tree produced by Swift5Parser#infix_operator_group.
    def enterInfix_operator_group(self, ctx:Swift5Parser.Infix_operator_groupContext):
        pass

    # Exit a parse tree produced by Swift5Parser#infix_operator_group.
    def exitInfix_operator_group(self, ctx:Swift5Parser.Infix_operator_groupContext):
        pass


    # Enter a parse tree produced by Swift5Parser#precedence_group_declaration.
    def enterPrecedence_group_declaration(self, ctx:Swift5Parser.Precedence_group_declarationContext):
        pass

    # Exit a parse tree produced by Swift5Parser#precedence_group_declaration.
    def exitPrecedence_group_declaration(self, ctx:Swift5Parser.Precedence_group_declarationContext):
        pass


    # Enter a parse tree produced by Swift5Parser#precedence_group_attributes.
    def enterPrecedence_group_attributes(self, ctx:Swift5Parser.Precedence_group_attributesContext):
        pass

    # Exit a parse tree produced by Swift5Parser#precedence_group_attributes.
    def exitPrecedence_group_attributes(self, ctx:Swift5Parser.Precedence_group_attributesContext):
        pass


    # Enter a parse tree produced by Swift5Parser#precedence_group_attribute.
    def enterPrecedence_group_attribute(self, ctx:Swift5Parser.Precedence_group_attributeContext):
        pass

    # Exit a parse tree produced by Swift5Parser#precedence_group_attribute.
    def exitPrecedence_group_attribute(self, ctx:Swift5Parser.Precedence_group_attributeContext):
        pass


    # Enter a parse tree produced by Swift5Parser#precedence_group_relation.
    def enterPrecedence_group_relation(self, ctx:Swift5Parser.Precedence_group_relationContext):
        pass

    # Exit a parse tree produced by Swift5Parser#precedence_group_relation.
    def exitPrecedence_group_relation(self, ctx:Swift5Parser.Precedence_group_relationContext):
        pass


    # Enter a parse tree produced by Swift5Parser#precedence_group_assignment.
    def enterPrecedence_group_assignment(self, ctx:Swift5Parser.Precedence_group_assignmentContext):
        pass

    # Exit a parse tree produced by Swift5Parser#precedence_group_assignment.
    def exitPrecedence_group_assignment(self, ctx:Swift5Parser.Precedence_group_assignmentContext):
        pass


    # Enter a parse tree produced by Swift5Parser#precedence_group_associativity.
    def enterPrecedence_group_associativity(self, ctx:Swift5Parser.Precedence_group_associativityContext):
        pass

    # Exit a parse tree produced by Swift5Parser#precedence_group_associativity.
    def exitPrecedence_group_associativity(self, ctx:Swift5Parser.Precedence_group_associativityContext):
        pass


    # Enter a parse tree produced by Swift5Parser#precedence_group_names.
    def enterPrecedence_group_names(self, ctx:Swift5Parser.Precedence_group_namesContext):
        pass

    # Exit a parse tree produced by Swift5Parser#precedence_group_names.
    def exitPrecedence_group_names(self, ctx:Swift5Parser.Precedence_group_namesContext):
        pass


    # Enter a parse tree produced by Swift5Parser#precedence_group_name.
    def enterPrecedence_group_name(self, ctx:Swift5Parser.Precedence_group_nameContext):
        pass

    # Exit a parse tree produced by Swift5Parser#precedence_group_name.
    def exitPrecedence_group_name(self, ctx:Swift5Parser.Precedence_group_nameContext):
        pass


    # Enter a parse tree produced by Swift5Parser#declaration_modifier.
    def enterDeclaration_modifier(self, ctx:Swift5Parser.Declaration_modifierContext):
        pass

    # Exit a parse tree produced by Swift5Parser#declaration_modifier.
    def exitDeclaration_modifier(self, ctx:Swift5Parser.Declaration_modifierContext):
        pass


    # Enter a parse tree produced by Swift5Parser#declaration_modifiers.
    def enterDeclaration_modifiers(self, ctx:Swift5Parser.Declaration_modifiersContext):
        pass

    # Exit a parse tree produced by Swift5Parser#declaration_modifiers.
    def exitDeclaration_modifiers(self, ctx:Swift5Parser.Declaration_modifiersContext):
        pass


    # Enter a parse tree produced by Swift5Parser#access_level_modifier.
    def enterAccess_level_modifier(self, ctx:Swift5Parser.Access_level_modifierContext):
        pass

    # Exit a parse tree produced by Swift5Parser#access_level_modifier.
    def exitAccess_level_modifier(self, ctx:Swift5Parser.Access_level_modifierContext):
        pass


    # Enter a parse tree produced by Swift5Parser#mutation_modifier.
    def enterMutation_modifier(self, ctx:Swift5Parser.Mutation_modifierContext):
        pass

    # Exit a parse tree produced by Swift5Parser#mutation_modifier.
    def exitMutation_modifier(self, ctx:Swift5Parser.Mutation_modifierContext):
        pass


    # Enter a parse tree produced by Swift5Parser#pattern.
    def enterPattern(self, ctx:Swift5Parser.PatternContext):
        pass

    # Exit a parse tree produced by Swift5Parser#pattern.
    def exitPattern(self, ctx:Swift5Parser.PatternContext):
        pass


    # Enter a parse tree produced by Swift5Parser#wildcard_pattern.
    def enterWildcard_pattern(self, ctx:Swift5Parser.Wildcard_patternContext):
        pass

    # Exit a parse tree produced by Swift5Parser#wildcard_pattern.
    def exitWildcard_pattern(self, ctx:Swift5Parser.Wildcard_patternContext):
        pass


    # Enter a parse tree produced by Swift5Parser#identifier_pattern.
    def enterIdentifier_pattern(self, ctx:Swift5Parser.Identifier_patternContext):
        pass

    # Exit a parse tree produced by Swift5Parser#identifier_pattern.
    def exitIdentifier_pattern(self, ctx:Swift5Parser.Identifier_patternContext):
        pass


    # Enter a parse tree produced by Swift5Parser#value_binding_pattern.
    def enterValue_binding_pattern(self, ctx:Swift5Parser.Value_binding_patternContext):
        pass

    # Exit a parse tree produced by Swift5Parser#value_binding_pattern.
    def exitValue_binding_pattern(self, ctx:Swift5Parser.Value_binding_patternContext):
        pass


    # Enter a parse tree produced by Swift5Parser#tuple_pattern.
    def enterTuple_pattern(self, ctx:Swift5Parser.Tuple_patternContext):
        pass

    # Exit a parse tree produced by Swift5Parser#tuple_pattern.
    def exitTuple_pattern(self, ctx:Swift5Parser.Tuple_patternContext):
        pass


    # Enter a parse tree produced by Swift5Parser#tuple_pattern_element_list.
    def enterTuple_pattern_element_list(self, ctx:Swift5Parser.Tuple_pattern_element_listContext):
        pass

    # Exit a parse tree produced by Swift5Parser#tuple_pattern_element_list.
    def exitTuple_pattern_element_list(self, ctx:Swift5Parser.Tuple_pattern_element_listContext):
        pass


    # Enter a parse tree produced by Swift5Parser#tuple_pattern_element.
    def enterTuple_pattern_element(self, ctx:Swift5Parser.Tuple_pattern_elementContext):
        pass

    # Exit a parse tree produced by Swift5Parser#tuple_pattern_element.
    def exitTuple_pattern_element(self, ctx:Swift5Parser.Tuple_pattern_elementContext):
        pass


    # Enter a parse tree produced by Swift5Parser#enum_case_pattern.
    def enterEnum_case_pattern(self, ctx:Swift5Parser.Enum_case_patternContext):
        pass

    # Exit a parse tree produced by Swift5Parser#enum_case_pattern.
    def exitEnum_case_pattern(self, ctx:Swift5Parser.Enum_case_patternContext):
        pass


    # Enter a parse tree produced by Swift5Parser#optional_pattern.
    def enterOptional_pattern(self, ctx:Swift5Parser.Optional_patternContext):
        pass

    # Exit a parse tree produced by Swift5Parser#optional_pattern.
    def exitOptional_pattern(self, ctx:Swift5Parser.Optional_patternContext):
        pass


    # Enter a parse tree produced by Swift5Parser#expression_pattern.
    def enterExpression_pattern(self, ctx:Swift5Parser.Expression_patternContext):
        pass

    # Exit a parse tree produced by Swift5Parser#expression_pattern.
    def exitExpression_pattern(self, ctx:Swift5Parser.Expression_patternContext):
        pass


    # Enter a parse tree produced by Swift5Parser#attribute.
    def enterAttribute(self, ctx:Swift5Parser.AttributeContext):
        pass

    # Exit a parse tree produced by Swift5Parser#attribute.
    def exitAttribute(self, ctx:Swift5Parser.AttributeContext):
        pass


    # Enter a parse tree produced by Swift5Parser#attribute_name.
    def enterAttribute_name(self, ctx:Swift5Parser.Attribute_nameContext):
        pass

    # Exit a parse tree produced by Swift5Parser#attribute_name.
    def exitAttribute_name(self, ctx:Swift5Parser.Attribute_nameContext):
        pass


    # Enter a parse tree produced by Swift5Parser#attribute_argument_clause.
    def enterAttribute_argument_clause(self, ctx:Swift5Parser.Attribute_argument_clauseContext):
        pass

    # Exit a parse tree produced by Swift5Parser#attribute_argument_clause.
    def exitAttribute_argument_clause(self, ctx:Swift5Parser.Attribute_argument_clauseContext):
        pass


    # Enter a parse tree produced by Swift5Parser#attributes.
    def enterAttributes(self, ctx:Swift5Parser.AttributesContext):
        pass

    # Exit a parse tree produced by Swift5Parser#attributes.
    def exitAttributes(self, ctx:Swift5Parser.AttributesContext):
        pass


    # Enter a parse tree produced by Swift5Parser#balanced_tokens.
    def enterBalanced_tokens(self, ctx:Swift5Parser.Balanced_tokensContext):
        pass

    # Exit a parse tree produced by Swift5Parser#balanced_tokens.
    def exitBalanced_tokens(self, ctx:Swift5Parser.Balanced_tokensContext):
        pass


    # Enter a parse tree produced by Swift5Parser#balanced_token.
    def enterBalanced_token(self, ctx:Swift5Parser.Balanced_tokenContext):
        pass

    # Exit a parse tree produced by Swift5Parser#balanced_token.
    def exitBalanced_token(self, ctx:Swift5Parser.Balanced_tokenContext):
        pass


    # Enter a parse tree produced by Swift5Parser#balanced_token_punctuation.
    def enterBalanced_token_punctuation(self, ctx:Swift5Parser.Balanced_token_punctuationContext):
        pass

    # Exit a parse tree produced by Swift5Parser#balanced_token_punctuation.
    def exitBalanced_token_punctuation(self, ctx:Swift5Parser.Balanced_token_punctuationContext):
        pass


    # Enter a parse tree produced by Swift5Parser#expression.
    def enterExpression(self, ctx:Swift5Parser.ExpressionContext):
        pass

    # Exit a parse tree produced by Swift5Parser#expression.
    def exitExpression(self, ctx:Swift5Parser.ExpressionContext):
        pass


    # Enter a parse tree produced by Swift5Parser#expression_list.
    def enterExpression_list(self, ctx:Swift5Parser.Expression_listContext):
        pass

    # Exit a parse tree produced by Swift5Parser#expression_list.
    def exitExpression_list(self, ctx:Swift5Parser.Expression_listContext):
        pass


    # Enter a parse tree produced by Swift5Parser#prefix_expression.
    def enterPrefix_expression(self, ctx:Swift5Parser.Prefix_expressionContext):
        pass

    # Exit a parse tree produced by Swift5Parser#prefix_expression.
    def exitPrefix_expression(self, ctx:Swift5Parser.Prefix_expressionContext):
        pass


    # Enter a parse tree produced by Swift5Parser#in_out_expression.
    def enterIn_out_expression(self, ctx:Swift5Parser.In_out_expressionContext):
        pass

    # Exit a parse tree produced by Swift5Parser#in_out_expression.
    def exitIn_out_expression(self, ctx:Swift5Parser.In_out_expressionContext):
        pass


    # Enter a parse tree produced by Swift5Parser#try_operator.
    def enterTry_operator(self, ctx:Swift5Parser.Try_operatorContext):
        pass

    # Exit a parse tree produced by Swift5Parser#try_operator.
    def exitTry_operator(self, ctx:Swift5Parser.Try_operatorContext):
        pass


    # Enter a parse tree produced by Swift5Parser#binary_expression.
    def enterBinary_expression(self, ctx:Swift5Parser.Binary_expressionContext):
        pass

    # Exit a parse tree produced by Swift5Parser#binary_expression.
    def exitBinary_expression(self, ctx:Swift5Parser.Binary_expressionContext):
        pass


    # Enter a parse tree produced by Swift5Parser#binary_expressions.
    def enterBinary_expressions(self, ctx:Swift5Parser.Binary_expressionsContext):
        pass

    # Exit a parse tree produced by Swift5Parser#binary_expressions.
    def exitBinary_expressions(self, ctx:Swift5Parser.Binary_expressionsContext):
        pass


    # Enter a parse tree produced by Swift5Parser#conditional_operator.
    def enterConditional_operator(self, ctx:Swift5Parser.Conditional_operatorContext):
        pass

    # Exit a parse tree produced by Swift5Parser#conditional_operator.
    def exitConditional_operator(self, ctx:Swift5Parser.Conditional_operatorContext):
        pass


    # Enter a parse tree produced by Swift5Parser#type_casting_operator.
    def enterType_casting_operator(self, ctx:Swift5Parser.Type_casting_operatorContext):
        pass

    # Exit a parse tree produced by Swift5Parser#type_casting_operator.
    def exitType_casting_operator(self, ctx:Swift5Parser.Type_casting_operatorContext):
        pass


    # Enter a parse tree produced by Swift5Parser#primary_expression.
    def enterPrimary_expression(self, ctx:Swift5Parser.Primary_expressionContext):
        pass

    # Exit a parse tree produced by Swift5Parser#primary_expression.
    def exitPrimary_expression(self, ctx:Swift5Parser.Primary_expressionContext):
        pass


    # Enter a parse tree produced by Swift5Parser#unqualified_name.
    def enterUnqualified_name(self, ctx:Swift5Parser.Unqualified_nameContext):
        pass

    # Exit a parse tree produced by Swift5Parser#unqualified_name.
    def exitUnqualified_name(self, ctx:Swift5Parser.Unqualified_nameContext):
        pass


    # Enter a parse tree produced by Swift5Parser#literal_expression.
    def enterLiteral_expression(self, ctx:Swift5Parser.Literal_expressionContext):
        pass

    # Exit a parse tree produced by Swift5Parser#literal_expression.
    def exitLiteral_expression(self, ctx:Swift5Parser.Literal_expressionContext):
        pass


    # Enter a parse tree produced by Swift5Parser#array_literal.
    def enterArray_literal(self, ctx:Swift5Parser.Array_literalContext):
        pass

    # Exit a parse tree produced by Swift5Parser#array_literal.
    def exitArray_literal(self, ctx:Swift5Parser.Array_literalContext):
        pass


    # Enter a parse tree produced by Swift5Parser#array_literal_items.
    def enterArray_literal_items(self, ctx:Swift5Parser.Array_literal_itemsContext):
        pass

    # Exit a parse tree produced by Swift5Parser#array_literal_items.
    def exitArray_literal_items(self, ctx:Swift5Parser.Array_literal_itemsContext):
        pass


    # Enter a parse tree produced by Swift5Parser#array_literal_item.
    def enterArray_literal_item(self, ctx:Swift5Parser.Array_literal_itemContext):
        pass

    # Exit a parse tree produced by Swift5Parser#array_literal_item.
    def exitArray_literal_item(self, ctx:Swift5Parser.Array_literal_itemContext):
        pass


    # Enter a parse tree produced by Swift5Parser#dictionary_literal.
    def enterDictionary_literal(self, ctx:Swift5Parser.Dictionary_literalContext):
        pass

    # Exit a parse tree produced by Swift5Parser#dictionary_literal.
    def exitDictionary_literal(self, ctx:Swift5Parser.Dictionary_literalContext):
        pass


    # Enter a parse tree produced by Swift5Parser#dictionary_literal_items.
    def enterDictionary_literal_items(self, ctx:Swift5Parser.Dictionary_literal_itemsContext):
        pass

    # Exit a parse tree produced by Swift5Parser#dictionary_literal_items.
    def exitDictionary_literal_items(self, ctx:Swift5Parser.Dictionary_literal_itemsContext):
        pass


    # Enter a parse tree produced by Swift5Parser#dictionary_literal_item.
    def enterDictionary_literal_item(self, ctx:Swift5Parser.Dictionary_literal_itemContext):
        pass

    # Exit a parse tree produced by Swift5Parser#dictionary_literal_item.
    def exitDictionary_literal_item(self, ctx:Swift5Parser.Dictionary_literal_itemContext):
        pass


    # Enter a parse tree produced by Swift5Parser#playground_literal.
    def enterPlayground_literal(self, ctx:Swift5Parser.Playground_literalContext):
        pass

    # Exit a parse tree produced by Swift5Parser#playground_literal.
    def exitPlayground_literal(self, ctx:Swift5Parser.Playground_literalContext):
        pass


    # Enter a parse tree produced by Swift5Parser#self_pure_expression.
    def enterSelf_pure_expression(self, ctx:Swift5Parser.Self_pure_expressionContext):
        pass

    # Exit a parse tree produced by Swift5Parser#self_pure_expression.
    def exitSelf_pure_expression(self, ctx:Swift5Parser.Self_pure_expressionContext):
        pass


    # Enter a parse tree produced by Swift5Parser#self_method_expression.
    def enterSelf_method_expression(self, ctx:Swift5Parser.Self_method_expressionContext):
        pass

    # Exit a parse tree produced by Swift5Parser#self_method_expression.
    def exitSelf_method_expression(self, ctx:Swift5Parser.Self_method_expressionContext):
        pass


    # Enter a parse tree produced by Swift5Parser#self_subscript_expression.
    def enterSelf_subscript_expression(self, ctx:Swift5Parser.Self_subscript_expressionContext):
        pass

    # Exit a parse tree produced by Swift5Parser#self_subscript_expression.
    def exitSelf_subscript_expression(self, ctx:Swift5Parser.Self_subscript_expressionContext):
        pass


    # Enter a parse tree produced by Swift5Parser#self_initializer_expression.
    def enterSelf_initializer_expression(self, ctx:Swift5Parser.Self_initializer_expressionContext):
        pass

    # Exit a parse tree produced by Swift5Parser#self_initializer_expression.
    def exitSelf_initializer_expression(self, ctx:Swift5Parser.Self_initializer_expressionContext):
        pass


    # Enter a parse tree produced by Swift5Parser#superclass_method_expression.
    def enterSuperclass_method_expression(self, ctx:Swift5Parser.Superclass_method_expressionContext):
        pass

    # Exit a parse tree produced by Swift5Parser#superclass_method_expression.
    def exitSuperclass_method_expression(self, ctx:Swift5Parser.Superclass_method_expressionContext):
        pass


    # Enter a parse tree produced by Swift5Parser#superclass_subscript_expression.
    def enterSuperclass_subscript_expression(self, ctx:Swift5Parser.Superclass_subscript_expressionContext):
        pass

    # Exit a parse tree produced by Swift5Parser#superclass_subscript_expression.
    def exitSuperclass_subscript_expression(self, ctx:Swift5Parser.Superclass_subscript_expressionContext):
        pass


    # Enter a parse tree produced by Swift5Parser#superclass_initializer_expression.
    def enterSuperclass_initializer_expression(self, ctx:Swift5Parser.Superclass_initializer_expressionContext):
        pass

    # Exit a parse tree produced by Swift5Parser#superclass_initializer_expression.
    def exitSuperclass_initializer_expression(self, ctx:Swift5Parser.Superclass_initializer_expressionContext):
        pass


    # Enter a parse tree produced by Swift5Parser#closure_expression.
    def enterClosure_expression(self, ctx:Swift5Parser.Closure_expressionContext):
        pass

    # Exit a parse tree produced by Swift5Parser#closure_expression.
    def exitClosure_expression(self, ctx:Swift5Parser.Closure_expressionContext):
        pass


    # Enter a parse tree produced by Swift5Parser#closure_signature.
    def enterClosure_signature(self, ctx:Swift5Parser.Closure_signatureContext):
        pass

    # Exit a parse tree produced by Swift5Parser#closure_signature.
    def exitClosure_signature(self, ctx:Swift5Parser.Closure_signatureContext):
        pass


    # Enter a parse tree produced by Swift5Parser#closure_parameter_clause.
    def enterClosure_parameter_clause(self, ctx:Swift5Parser.Closure_parameter_clauseContext):
        pass

    # Exit a parse tree produced by Swift5Parser#closure_parameter_clause.
    def exitClosure_parameter_clause(self, ctx:Swift5Parser.Closure_parameter_clauseContext):
        pass


    # Enter a parse tree produced by Swift5Parser#closure_parameter_list.
    def enterClosure_parameter_list(self, ctx:Swift5Parser.Closure_parameter_listContext):
        pass

    # Exit a parse tree produced by Swift5Parser#closure_parameter_list.
    def exitClosure_parameter_list(self, ctx:Swift5Parser.Closure_parameter_listContext):
        pass


    # Enter a parse tree produced by Swift5Parser#closure_parameter.
    def enterClosure_parameter(self, ctx:Swift5Parser.Closure_parameterContext):
        pass

    # Exit a parse tree produced by Swift5Parser#closure_parameter.
    def exitClosure_parameter(self, ctx:Swift5Parser.Closure_parameterContext):
        pass


    # Enter a parse tree produced by Swift5Parser#capture_list.
    def enterCapture_list(self, ctx:Swift5Parser.Capture_listContext):
        pass

    # Exit a parse tree produced by Swift5Parser#capture_list.
    def exitCapture_list(self, ctx:Swift5Parser.Capture_listContext):
        pass


    # Enter a parse tree produced by Swift5Parser#capture_list_items.
    def enterCapture_list_items(self, ctx:Swift5Parser.Capture_list_itemsContext):
        pass

    # Exit a parse tree produced by Swift5Parser#capture_list_items.
    def exitCapture_list_items(self, ctx:Swift5Parser.Capture_list_itemsContext):
        pass


    # Enter a parse tree produced by Swift5Parser#capture_list_item.
    def enterCapture_list_item(self, ctx:Swift5Parser.Capture_list_itemContext):
        pass

    # Exit a parse tree produced by Swift5Parser#capture_list_item.
    def exitCapture_list_item(self, ctx:Swift5Parser.Capture_list_itemContext):
        pass


    # Enter a parse tree produced by Swift5Parser#capture_specifier.
    def enterCapture_specifier(self, ctx:Swift5Parser.Capture_specifierContext):
        pass

    # Exit a parse tree produced by Swift5Parser#capture_specifier.
    def exitCapture_specifier(self, ctx:Swift5Parser.Capture_specifierContext):
        pass


    # Enter a parse tree produced by Swift5Parser#implicit_member_expression.
    def enterImplicit_member_expression(self, ctx:Swift5Parser.Implicit_member_expressionContext):
        pass

    # Exit a parse tree produced by Swift5Parser#implicit_member_expression.
    def exitImplicit_member_expression(self, ctx:Swift5Parser.Implicit_member_expressionContext):
        pass


    # Enter a parse tree produced by Swift5Parser#parenthesized_operator.
    def enterParenthesized_operator(self, ctx:Swift5Parser.Parenthesized_operatorContext):
        pass

    # Exit a parse tree produced by Swift5Parser#parenthesized_operator.
    def exitParenthesized_operator(self, ctx:Swift5Parser.Parenthesized_operatorContext):
        pass


    # Enter a parse tree produced by Swift5Parser#parenthesized_expression.
    def enterParenthesized_expression(self, ctx:Swift5Parser.Parenthesized_expressionContext):
        pass

    # Exit a parse tree produced by Swift5Parser#parenthesized_expression.
    def exitParenthesized_expression(self, ctx:Swift5Parser.Parenthesized_expressionContext):
        pass


    # Enter a parse tree produced by Swift5Parser#tuple_expression.
    def enterTuple_expression(self, ctx:Swift5Parser.Tuple_expressionContext):
        pass

    # Exit a parse tree produced by Swift5Parser#tuple_expression.
    def exitTuple_expression(self, ctx:Swift5Parser.Tuple_expressionContext):
        pass


    # Enter a parse tree produced by Swift5Parser#tuple_element_list.
    def enterTuple_element_list(self, ctx:Swift5Parser.Tuple_element_listContext):
        pass

    # Exit a parse tree produced by Swift5Parser#tuple_element_list.
    def exitTuple_element_list(self, ctx:Swift5Parser.Tuple_element_listContext):
        pass


    # Enter a parse tree produced by Swift5Parser#tuple_element.
    def enterTuple_element(self, ctx:Swift5Parser.Tuple_elementContext):
        pass

    # Exit a parse tree produced by Swift5Parser#tuple_element.
    def exitTuple_element(self, ctx:Swift5Parser.Tuple_elementContext):
        pass


    # Enter a parse tree produced by Swift5Parser#wildcard_expression.
    def enterWildcard_expression(self, ctx:Swift5Parser.Wildcard_expressionContext):
        pass

    # Exit a parse tree produced by Swift5Parser#wildcard_expression.
    def exitWildcard_expression(self, ctx:Swift5Parser.Wildcard_expressionContext):
        pass


    # Enter a parse tree produced by Swift5Parser#key_path_expression.
    def enterKey_path_expression(self, ctx:Swift5Parser.Key_path_expressionContext):
        pass

    # Exit a parse tree produced by Swift5Parser#key_path_expression.
    def exitKey_path_expression(self, ctx:Swift5Parser.Key_path_expressionContext):
        pass


    # Enter a parse tree produced by Swift5Parser#key_path_components.
    def enterKey_path_components(self, ctx:Swift5Parser.Key_path_componentsContext):
        pass

    # Exit a parse tree produced by Swift5Parser#key_path_components.
    def exitKey_path_components(self, ctx:Swift5Parser.Key_path_componentsContext):
        pass


    # Enter a parse tree produced by Swift5Parser#key_path_component.
    def enterKey_path_component(self, ctx:Swift5Parser.Key_path_componentContext):
        pass

    # Exit a parse tree produced by Swift5Parser#key_path_component.
    def exitKey_path_component(self, ctx:Swift5Parser.Key_path_componentContext):
        pass


    # Enter a parse tree produced by Swift5Parser#key_path_postfixes.
    def enterKey_path_postfixes(self, ctx:Swift5Parser.Key_path_postfixesContext):
        pass

    # Exit a parse tree produced by Swift5Parser#key_path_postfixes.
    def exitKey_path_postfixes(self, ctx:Swift5Parser.Key_path_postfixesContext):
        pass


    # Enter a parse tree produced by Swift5Parser#key_path_postfix.
    def enterKey_path_postfix(self, ctx:Swift5Parser.Key_path_postfixContext):
        pass

    # Exit a parse tree produced by Swift5Parser#key_path_postfix.
    def exitKey_path_postfix(self, ctx:Swift5Parser.Key_path_postfixContext):
        pass


    # Enter a parse tree produced by Swift5Parser#selector_expression.
    def enterSelector_expression(self, ctx:Swift5Parser.Selector_expressionContext):
        pass

    # Exit a parse tree produced by Swift5Parser#selector_expression.
    def exitSelector_expression(self, ctx:Swift5Parser.Selector_expressionContext):
        pass


    # Enter a parse tree produced by Swift5Parser#key_path_string_expression.
    def enterKey_path_string_expression(self, ctx:Swift5Parser.Key_path_string_expressionContext):
        pass

    # Exit a parse tree produced by Swift5Parser#key_path_string_expression.
    def exitKey_path_string_expression(self, ctx:Swift5Parser.Key_path_string_expressionContext):
        pass


    # Enter a parse tree produced by Swift5Parser#postfix_expression.
    def enterPostfix_expression(self, ctx:Swift5Parser.Postfix_expressionContext):
        pass

    # Exit a parse tree produced by Swift5Parser#postfix_expression.
    def exitPostfix_expression(self, ctx:Swift5Parser.Postfix_expressionContext):
        pass


    # Enter a parse tree produced by Swift5Parser#function_call_suffix.
    def enterFunction_call_suffix(self, ctx:Swift5Parser.Function_call_suffixContext):
        pass

    # Exit a parse tree produced by Swift5Parser#function_call_suffix.
    def exitFunction_call_suffix(self, ctx:Swift5Parser.Function_call_suffixContext):
        pass


    # Enter a parse tree produced by Swift5Parser#initializer_suffix.
    def enterInitializer_suffix(self, ctx:Swift5Parser.Initializer_suffixContext):
        pass

    # Exit a parse tree produced by Swift5Parser#initializer_suffix.
    def exitInitializer_suffix(self, ctx:Swift5Parser.Initializer_suffixContext):
        pass


    # Enter a parse tree produced by Swift5Parser#explicit_member_suffix.
    def enterExplicit_member_suffix(self, ctx:Swift5Parser.Explicit_member_suffixContext):
        pass

    # Exit a parse tree produced by Swift5Parser#explicit_member_suffix.
    def exitExplicit_member_suffix(self, ctx:Swift5Parser.Explicit_member_suffixContext):
        pass


    # Enter a parse tree produced by Swift5Parser#postfix_self_suffix.
    def enterPostfix_self_suffix(self, ctx:Swift5Parser.Postfix_self_suffixContext):
        pass

    # Exit a parse tree produced by Swift5Parser#postfix_self_suffix.
    def exitPostfix_self_suffix(self, ctx:Swift5Parser.Postfix_self_suffixContext):
        pass


    # Enter a parse tree produced by Swift5Parser#subscript_suffix.
    def enterSubscript_suffix(self, ctx:Swift5Parser.Subscript_suffixContext):
        pass

    # Exit a parse tree produced by Swift5Parser#subscript_suffix.
    def exitSubscript_suffix(self, ctx:Swift5Parser.Subscript_suffixContext):
        pass


    # Enter a parse tree produced by Swift5Parser#forced_value_suffix.
    def enterForced_value_suffix(self, ctx:Swift5Parser.Forced_value_suffixContext):
        pass

    # Exit a parse tree produced by Swift5Parser#forced_value_suffix.
    def exitForced_value_suffix(self, ctx:Swift5Parser.Forced_value_suffixContext):
        pass


    # Enter a parse tree produced by Swift5Parser#optional_chaining_suffix.
    def enterOptional_chaining_suffix(self, ctx:Swift5Parser.Optional_chaining_suffixContext):
        pass

    # Exit a parse tree produced by Swift5Parser#optional_chaining_suffix.
    def exitOptional_chaining_suffix(self, ctx:Swift5Parser.Optional_chaining_suffixContext):
        pass


    # Enter a parse tree produced by Swift5Parser#function_call_argument_clause.
    def enterFunction_call_argument_clause(self, ctx:Swift5Parser.Function_call_argument_clauseContext):
        pass

    # Exit a parse tree produced by Swift5Parser#function_call_argument_clause.
    def exitFunction_call_argument_clause(self, ctx:Swift5Parser.Function_call_argument_clauseContext):
        pass


    # Enter a parse tree produced by Swift5Parser#function_call_argument_list.
    def enterFunction_call_argument_list(self, ctx:Swift5Parser.Function_call_argument_listContext):
        pass

    # Exit a parse tree produced by Swift5Parser#function_call_argument_list.
    def exitFunction_call_argument_list(self, ctx:Swift5Parser.Function_call_argument_listContext):
        pass


    # Enter a parse tree produced by Swift5Parser#function_call_argument.
    def enterFunction_call_argument(self, ctx:Swift5Parser.Function_call_argumentContext):
        pass

    # Exit a parse tree produced by Swift5Parser#function_call_argument.
    def exitFunction_call_argument(self, ctx:Swift5Parser.Function_call_argumentContext):
        pass


    # Enter a parse tree produced by Swift5Parser#trailing_closures.
    def enterTrailing_closures(self, ctx:Swift5Parser.Trailing_closuresContext):
        pass

    # Exit a parse tree produced by Swift5Parser#trailing_closures.
    def exitTrailing_closures(self, ctx:Swift5Parser.Trailing_closuresContext):
        pass


    # Enter a parse tree produced by Swift5Parser#labeled_trailing_closures.
    def enterLabeled_trailing_closures(self, ctx:Swift5Parser.Labeled_trailing_closuresContext):
        pass

    # Exit a parse tree produced by Swift5Parser#labeled_trailing_closures.
    def exitLabeled_trailing_closures(self, ctx:Swift5Parser.Labeled_trailing_closuresContext):
        pass


    # Enter a parse tree produced by Swift5Parser#labeled_trailing_closure.
    def enterLabeled_trailing_closure(self, ctx:Swift5Parser.Labeled_trailing_closureContext):
        pass

    # Exit a parse tree produced by Swift5Parser#labeled_trailing_closure.
    def exitLabeled_trailing_closure(self, ctx:Swift5Parser.Labeled_trailing_closureContext):
        pass


    # Enter a parse tree produced by Swift5Parser#argument_names.
    def enterArgument_names(self, ctx:Swift5Parser.Argument_namesContext):
        pass

    # Exit a parse tree produced by Swift5Parser#argument_names.
    def exitArgument_names(self, ctx:Swift5Parser.Argument_namesContext):
        pass


    # Enter a parse tree produced by Swift5Parser#argument_name.
    def enterArgument_name(self, ctx:Swift5Parser.Argument_nameContext):
        pass

    # Exit a parse tree produced by Swift5Parser#argument_name.
    def exitArgument_name(self, ctx:Swift5Parser.Argument_nameContext):
        pass


    # Enter a parse tree produced by Swift5Parser#type.
    def enterType(self, ctx:Swift5Parser.TypeContext):
        pass

    # Exit a parse tree produced by Swift5Parser#type.
    def exitType(self, ctx:Swift5Parser.TypeContext):
        pass


    # Enter a parse tree produced by Swift5Parser#type_annotation.
    def enterType_annotation(self, ctx:Swift5Parser.Type_annotationContext):
        pass

    # Exit a parse tree produced by Swift5Parser#type_annotation.
    def exitType_annotation(self, ctx:Swift5Parser.Type_annotationContext):
        pass


    # Enter a parse tree produced by Swift5Parser#type_identifier.
    def enterType_identifier(self, ctx:Swift5Parser.Type_identifierContext):
        pass

    # Exit a parse tree produced by Swift5Parser#type_identifier.
    def exitType_identifier(self, ctx:Swift5Parser.Type_identifierContext):
        pass


    # Enter a parse tree produced by Swift5Parser#type_name.
    def enterType_name(self, ctx:Swift5Parser.Type_nameContext):
        pass

    # Exit a parse tree produced by Swift5Parser#type_name.
    def exitType_name(self, ctx:Swift5Parser.Type_nameContext):
        pass


    # Enter a parse tree produced by Swift5Parser#tuple_type.
    def enterTuple_type(self, ctx:Swift5Parser.Tuple_typeContext):
        pass

    # Exit a parse tree produced by Swift5Parser#tuple_type.
    def exitTuple_type(self, ctx:Swift5Parser.Tuple_typeContext):
        pass


    # Enter a parse tree produced by Swift5Parser#tuple_type_element_list.
    def enterTuple_type_element_list(self, ctx:Swift5Parser.Tuple_type_element_listContext):
        pass

    # Exit a parse tree produced by Swift5Parser#tuple_type_element_list.
    def exitTuple_type_element_list(self, ctx:Swift5Parser.Tuple_type_element_listContext):
        pass


    # Enter a parse tree produced by Swift5Parser#tuple_type_element.
    def enterTuple_type_element(self, ctx:Swift5Parser.Tuple_type_elementContext):
        pass

    # Exit a parse tree produced by Swift5Parser#tuple_type_element.
    def exitTuple_type_element(self, ctx:Swift5Parser.Tuple_type_elementContext):
        pass


    # Enter a parse tree produced by Swift5Parser#element_name.
    def enterElement_name(self, ctx:Swift5Parser.Element_nameContext):
        pass

    # Exit a parse tree produced by Swift5Parser#element_name.
    def exitElement_name(self, ctx:Swift5Parser.Element_nameContext):
        pass


    # Enter a parse tree produced by Swift5Parser#function_type.
    def enterFunction_type(self, ctx:Swift5Parser.Function_typeContext):
        pass

    # Exit a parse tree produced by Swift5Parser#function_type.
    def exitFunction_type(self, ctx:Swift5Parser.Function_typeContext):
        pass


    # Enter a parse tree produced by Swift5Parser#function_type_argument_clause.
    def enterFunction_type_argument_clause(self, ctx:Swift5Parser.Function_type_argument_clauseContext):
        pass

    # Exit a parse tree produced by Swift5Parser#function_type_argument_clause.
    def exitFunction_type_argument_clause(self, ctx:Swift5Parser.Function_type_argument_clauseContext):
        pass


    # Enter a parse tree produced by Swift5Parser#function_type_argument_list.
    def enterFunction_type_argument_list(self, ctx:Swift5Parser.Function_type_argument_listContext):
        pass

    # Exit a parse tree produced by Swift5Parser#function_type_argument_list.
    def exitFunction_type_argument_list(self, ctx:Swift5Parser.Function_type_argument_listContext):
        pass


    # Enter a parse tree produced by Swift5Parser#function_type_argument.
    def enterFunction_type_argument(self, ctx:Swift5Parser.Function_type_argumentContext):
        pass

    # Exit a parse tree produced by Swift5Parser#function_type_argument.
    def exitFunction_type_argument(self, ctx:Swift5Parser.Function_type_argumentContext):
        pass


    # Enter a parse tree produced by Swift5Parser#argument_label.
    def enterArgument_label(self, ctx:Swift5Parser.Argument_labelContext):
        pass

    # Exit a parse tree produced by Swift5Parser#argument_label.
    def exitArgument_label(self, ctx:Swift5Parser.Argument_labelContext):
        pass


    # Enter a parse tree produced by Swift5Parser#array_type.
    def enterArray_type(self, ctx:Swift5Parser.Array_typeContext):
        pass

    # Exit a parse tree produced by Swift5Parser#array_type.
    def exitArray_type(self, ctx:Swift5Parser.Array_typeContext):
        pass


    # Enter a parse tree produced by Swift5Parser#dictionary_type.
    def enterDictionary_type(self, ctx:Swift5Parser.Dictionary_typeContext):
        pass

    # Exit a parse tree produced by Swift5Parser#dictionary_type.
    def exitDictionary_type(self, ctx:Swift5Parser.Dictionary_typeContext):
        pass


    # Enter a parse tree produced by Swift5Parser#protocol_composition_type.
    def enterProtocol_composition_type(self, ctx:Swift5Parser.Protocol_composition_typeContext):
        pass

    # Exit a parse tree produced by Swift5Parser#protocol_composition_type.
    def exitProtocol_composition_type(self, ctx:Swift5Parser.Protocol_composition_typeContext):
        pass


    # Enter a parse tree produced by Swift5Parser#trailing_composition_and.
    def enterTrailing_composition_and(self, ctx:Swift5Parser.Trailing_composition_andContext):
        pass

    # Exit a parse tree produced by Swift5Parser#trailing_composition_and.
    def exitTrailing_composition_and(self, ctx:Swift5Parser.Trailing_composition_andContext):
        pass


    # Enter a parse tree produced by Swift5Parser#opaque_type.
    def enterOpaque_type(self, ctx:Swift5Parser.Opaque_typeContext):
        pass

    # Exit a parse tree produced by Swift5Parser#opaque_type.
    def exitOpaque_type(self, ctx:Swift5Parser.Opaque_typeContext):
        pass


    # Enter a parse tree produced by Swift5Parser#any_type.
    def enterAny_type(self, ctx:Swift5Parser.Any_typeContext):
        pass

    # Exit a parse tree produced by Swift5Parser#any_type.
    def exitAny_type(self, ctx:Swift5Parser.Any_typeContext):
        pass


    # Enter a parse tree produced by Swift5Parser#self_type.
    def enterSelf_type(self, ctx:Swift5Parser.Self_typeContext):
        pass

    # Exit a parse tree produced by Swift5Parser#self_type.
    def exitSelf_type(self, ctx:Swift5Parser.Self_typeContext):
        pass


    # Enter a parse tree produced by Swift5Parser#type_inheritance_clause.
    def enterType_inheritance_clause(self, ctx:Swift5Parser.Type_inheritance_clauseContext):
        pass

    # Exit a parse tree produced by Swift5Parser#type_inheritance_clause.
    def exitType_inheritance_clause(self, ctx:Swift5Parser.Type_inheritance_clauseContext):
        pass


    # Enter a parse tree produced by Swift5Parser#type_inheritance_list.
    def enterType_inheritance_list(self, ctx:Swift5Parser.Type_inheritance_listContext):
        pass

    # Exit a parse tree produced by Swift5Parser#type_inheritance_list.
    def exitType_inheritance_list(self, ctx:Swift5Parser.Type_inheritance_listContext):
        pass


    # Enter a parse tree produced by Swift5Parser#identifier.
    def enterIdentifier(self, ctx:Swift5Parser.IdentifierContext):
        pass

    # Exit a parse tree produced by Swift5Parser#identifier.
    def exitIdentifier(self, ctx:Swift5Parser.IdentifierContext):
        pass


    # Enter a parse tree produced by Swift5Parser#identifier_list.
    def enterIdentifier_list(self, ctx:Swift5Parser.Identifier_listContext):
        pass

    # Exit a parse tree produced by Swift5Parser#identifier_list.
    def exitIdentifier_list(self, ctx:Swift5Parser.Identifier_listContext):
        pass


    # Enter a parse tree produced by Swift5Parser#keyword.
    def enterKeyword(self, ctx:Swift5Parser.KeywordContext):
        pass

    # Exit a parse tree produced by Swift5Parser#keyword.
    def exitKeyword(self, ctx:Swift5Parser.KeywordContext):
        pass


    # Enter a parse tree produced by Swift5Parser#assignment_operator.
    def enterAssignment_operator(self, ctx:Swift5Parser.Assignment_operatorContext):
        pass

    # Exit a parse tree produced by Swift5Parser#assignment_operator.
    def exitAssignment_operator(self, ctx:Swift5Parser.Assignment_operatorContext):
        pass


    # Enter a parse tree produced by Swift5Parser#negate_prefix_operator.
    def enterNegate_prefix_operator(self, ctx:Swift5Parser.Negate_prefix_operatorContext):
        pass

    # Exit a parse tree produced by Swift5Parser#negate_prefix_operator.
    def exitNegate_prefix_operator(self, ctx:Swift5Parser.Negate_prefix_operatorContext):
        pass


    # Enter a parse tree produced by Swift5Parser#compilation_condition_AND.
    def enterCompilation_condition_AND(self, ctx:Swift5Parser.Compilation_condition_ANDContext):
        pass

    # Exit a parse tree produced by Swift5Parser#compilation_condition_AND.
    def exitCompilation_condition_AND(self, ctx:Swift5Parser.Compilation_condition_ANDContext):
        pass


    # Enter a parse tree produced by Swift5Parser#compilation_condition_OR.
    def enterCompilation_condition_OR(self, ctx:Swift5Parser.Compilation_condition_ORContext):
        pass

    # Exit a parse tree produced by Swift5Parser#compilation_condition_OR.
    def exitCompilation_condition_OR(self, ctx:Swift5Parser.Compilation_condition_ORContext):
        pass


    # Enter a parse tree produced by Swift5Parser#compilation_condition_GE.
    def enterCompilation_condition_GE(self, ctx:Swift5Parser.Compilation_condition_GEContext):
        pass

    # Exit a parse tree produced by Swift5Parser#compilation_condition_GE.
    def exitCompilation_condition_GE(self, ctx:Swift5Parser.Compilation_condition_GEContext):
        pass


    # Enter a parse tree produced by Swift5Parser#compilation_condition_L.
    def enterCompilation_condition_L(self, ctx:Swift5Parser.Compilation_condition_LContext):
        pass

    # Exit a parse tree produced by Swift5Parser#compilation_condition_L.
    def exitCompilation_condition_L(self, ctx:Swift5Parser.Compilation_condition_LContext):
        pass


    # Enter a parse tree produced by Swift5Parser#arrow_operator.
    def enterArrow_operator(self, ctx:Swift5Parser.Arrow_operatorContext):
        pass

    # Exit a parse tree produced by Swift5Parser#arrow_operator.
    def exitArrow_operator(self, ctx:Swift5Parser.Arrow_operatorContext):
        pass


    # Enter a parse tree produced by Swift5Parser#range_operator.
    def enterRange_operator(self, ctx:Swift5Parser.Range_operatorContext):
        pass

    # Exit a parse tree produced by Swift5Parser#range_operator.
    def exitRange_operator(self, ctx:Swift5Parser.Range_operatorContext):
        pass


    # Enter a parse tree produced by Swift5Parser#same_type_equals.
    def enterSame_type_equals(self, ctx:Swift5Parser.Same_type_equalsContext):
        pass

    # Exit a parse tree produced by Swift5Parser#same_type_equals.
    def exitSame_type_equals(self, ctx:Swift5Parser.Same_type_equalsContext):
        pass


    # Enter a parse tree produced by Swift5Parser#binary_operator.
    def enterBinary_operator(self, ctx:Swift5Parser.Binary_operatorContext):
        pass

    # Exit a parse tree produced by Swift5Parser#binary_operator.
    def exitBinary_operator(self, ctx:Swift5Parser.Binary_operatorContext):
        pass


    # Enter a parse tree produced by Swift5Parser#prefix_operator.
    def enterPrefix_operator(self, ctx:Swift5Parser.Prefix_operatorContext):
        pass

    # Exit a parse tree produced by Swift5Parser#prefix_operator.
    def exitPrefix_operator(self, ctx:Swift5Parser.Prefix_operatorContext):
        pass


    # Enter a parse tree produced by Swift5Parser#postfix_operator.
    def enterPostfix_operator(self, ctx:Swift5Parser.Postfix_operatorContext):
        pass

    # Exit a parse tree produced by Swift5Parser#postfix_operator.
    def exitPostfix_operator(self, ctx:Swift5Parser.Postfix_operatorContext):
        pass


    # Enter a parse tree produced by Swift5Parser#operator.
    def enterOperator(self, ctx:Swift5Parser.OperatorContext):
        pass

    # Exit a parse tree produced by Swift5Parser#operator.
    def exitOperator(self, ctx:Swift5Parser.OperatorContext):
        pass


    # Enter a parse tree produced by Swift5Parser#operator_head.
    def enterOperator_head(self, ctx:Swift5Parser.Operator_headContext):
        pass

    # Exit a parse tree produced by Swift5Parser#operator_head.
    def exitOperator_head(self, ctx:Swift5Parser.Operator_headContext):
        pass


    # Enter a parse tree produced by Swift5Parser#operator_character.
    def enterOperator_character(self, ctx:Swift5Parser.Operator_characterContext):
        pass

    # Exit a parse tree produced by Swift5Parser#operator_character.
    def exitOperator_character(self, ctx:Swift5Parser.Operator_characterContext):
        pass


    # Enter a parse tree produced by Swift5Parser#operator_characters.
    def enterOperator_characters(self, ctx:Swift5Parser.Operator_charactersContext):
        pass

    # Exit a parse tree produced by Swift5Parser#operator_characters.
    def exitOperator_characters(self, ctx:Swift5Parser.Operator_charactersContext):
        pass


    # Enter a parse tree produced by Swift5Parser#dot_operator_head.
    def enterDot_operator_head(self, ctx:Swift5Parser.Dot_operator_headContext):
        pass

    # Exit a parse tree produced by Swift5Parser#dot_operator_head.
    def exitDot_operator_head(self, ctx:Swift5Parser.Dot_operator_headContext):
        pass


    # Enter a parse tree produced by Swift5Parser#dot_operator_character.
    def enterDot_operator_character(self, ctx:Swift5Parser.Dot_operator_characterContext):
        pass

    # Exit a parse tree produced by Swift5Parser#dot_operator_character.
    def exitDot_operator_character(self, ctx:Swift5Parser.Dot_operator_characterContext):
        pass


    # Enter a parse tree produced by Swift5Parser#dot_operator_characters.
    def enterDot_operator_characters(self, ctx:Swift5Parser.Dot_operator_charactersContext):
        pass

    # Exit a parse tree produced by Swift5Parser#dot_operator_characters.
    def exitDot_operator_characters(self, ctx:Swift5Parser.Dot_operator_charactersContext):
        pass


    # Enter a parse tree produced by Swift5Parser#literal.
    def enterLiteral(self, ctx:Swift5Parser.LiteralContext):
        pass

    # Exit a parse tree produced by Swift5Parser#literal.
    def exitLiteral(self, ctx:Swift5Parser.LiteralContext):
        pass


    # Enter a parse tree produced by Swift5Parser#numeric_literal.
    def enterNumeric_literal(self, ctx:Swift5Parser.Numeric_literalContext):
        pass

    # Exit a parse tree produced by Swift5Parser#numeric_literal.
    def exitNumeric_literal(self, ctx:Swift5Parser.Numeric_literalContext):
        pass


    # Enter a parse tree produced by Swift5Parser#boolean_literal.
    def enterBoolean_literal(self, ctx:Swift5Parser.Boolean_literalContext):
        pass

    # Exit a parse tree produced by Swift5Parser#boolean_literal.
    def exitBoolean_literal(self, ctx:Swift5Parser.Boolean_literalContext):
        pass


    # Enter a parse tree produced by Swift5Parser#nil_literal.
    def enterNil_literal(self, ctx:Swift5Parser.Nil_literalContext):
        pass

    # Exit a parse tree produced by Swift5Parser#nil_literal.
    def exitNil_literal(self, ctx:Swift5Parser.Nil_literalContext):
        pass


    # Enter a parse tree produced by Swift5Parser#integer_literal.
    def enterInteger_literal(self, ctx:Swift5Parser.Integer_literalContext):
        pass

    # Exit a parse tree produced by Swift5Parser#integer_literal.
    def exitInteger_literal(self, ctx:Swift5Parser.Integer_literalContext):
        pass


    # Enter a parse tree produced by Swift5Parser#string_literal.
    def enterString_literal(self, ctx:Swift5Parser.String_literalContext):
        pass

    # Exit a parse tree produced by Swift5Parser#string_literal.
    def exitString_literal(self, ctx:Swift5Parser.String_literalContext):
        pass


    # Enter a parse tree produced by Swift5Parser#extended_string_literal.
    def enterExtended_string_literal(self, ctx:Swift5Parser.Extended_string_literalContext):
        pass

    # Exit a parse tree produced by Swift5Parser#extended_string_literal.
    def exitExtended_string_literal(self, ctx:Swift5Parser.Extended_string_literalContext):
        pass


    # Enter a parse tree produced by Swift5Parser#static_string_literal.
    def enterStatic_string_literal(self, ctx:Swift5Parser.Static_string_literalContext):
        pass

    # Exit a parse tree produced by Swift5Parser#static_string_literal.
    def exitStatic_string_literal(self, ctx:Swift5Parser.Static_string_literalContext):
        pass


    # Enter a parse tree produced by Swift5Parser#interpolated_string_literal.
    def enterInterpolated_string_literal(self, ctx:Swift5Parser.Interpolated_string_literalContext):
        pass

    # Exit a parse tree produced by Swift5Parser#interpolated_string_literal.
    def exitInterpolated_string_literal(self, ctx:Swift5Parser.Interpolated_string_literalContext):
        pass
