import os
import os.path as osp
import itertools

from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from clone_detection.utils.arguments import get_args

from clone_detection.grammars.grammars_registry import (PARSERS, LEXERS,
                                                        LISTENERS)


START_RULE = {
    'java': 'compilationUnit',
    'swift': 'top_level_declaration',
    'kt': 'kotlinFile',
    'cpp': 'translationUnit',
    'dart': 'compilationUnit',
}

SUPPORTED_LANGUAGES = {'kt', 'dart'}

SIMILAR_NODES = {
    'IDENTIFIER': ['LITERAL', 'IDENTIFIER'],
    'CLASS_DECL': ['CLASS_DECL'],
    'CONSTRUCTOR_DECL': ['CONSTRUCTOR_DECL'],
    'PARAMETER_LIST': ['PARAMETER_LIST', 'VALUE_ARGUMENT_LIST'],
    'PARAMETER': ['PARAMETER'],
    'CONSTRUCTOR_CALL': ['CONSTRUCTOR_CALL'],
    'CLASS_BODY': ['CLASS_BODY', 'BODY'],
    'CLASS_MEMBER': ['CLASS_MEMBER'],
    'ENUM_DECL': ['ENUM_DECL'],
    'ENUM_BODY': ['ENUM_BODY'],
    'FUNCTION_DECL': ['FUNCTION_DECL'],
    'FUNCTION_BODY': ['FUNCTION_BODY'],
    'FUNCION_CALL': ['FUNCION_CALL'],
    'ATTRIBUTE_DECL': ['ATTRIBUTE_DECL', 'VARIABLE_DECL'],
    'VARIABLE_DECL': ['VARIABLE_DECL', 'ATTRIBUTE_DECL'],
    'GETTER': ['GETTER'],
    'SETTER': ['SETTER'],
    'TYPE_ALIAS': ['TYPE_ALIAS'],
    'PARAMETER_TYPE': ['PARAMETER_TYPE', 'TYPE'],
    'TYPE': ['TYPE'],
    'NULLABLE_TYPE': ['NULLABLE_TYPE', 'TYPE'],
    'FUNCTION_TYPE': ['FUNCTION_TYPE', 'TYPE'],
    'USER_TYPE': ['USER_TYPE', 'TYPE'],
    'OR': ['OR'],
    'AND': ['AND'],
    'TERNARY': ['TERNARY'],
    'AS': ['AS'],
    'PREFIX': ['PREFIX'],
    'POSFIX': ['POSFIX'],
    'COLLECTION_INDEXING': ['COLLECTION_INDEXING'],
    'VALUE_ARGUMENT_LIST': ['PARAMETER_LIST'],
    'VALUE_ARGUMENT': ['VALUE_ARGUMENT'],
    'TYPE_ARGUMENT_LIST': ['TYPE_ARGUMENT_LIST'],
    'TYPE_ARGUMENT': ['TYPE_ARGUMENT'],
    'STRING': ['STRING'],
    'COLLECTION': ['COLLECTION'],
    'SUPER_CALL': ['SUPER_CALL'],
    'CONDITION': ['CONDITION'],
    'BODY': ['BODY'],
    'TRY': ['TRY'],
    'CATCH': ['CATCH'],
    'FINALLY': ['FINALLY'],
    'LOOP_STATEMENT': ['LOOP_STATEMENT'],
    'JUMP_STATEMENT': ['JUMP_STATEMENT'],
    'EQUALITY_OPERATOR': ['EQUALITY_OPERATOR'],
    'COMPARISON_OPERATOR': ['COMPARISON_OPERATOR'],
    'MEMBER_OF': ['MEMBER_OF'],
    'IS_TYPE': ['IS_TYPE'],
    'ADDITIVE_OPERATOR': ['ADDITIVE_OPERATOR'],
    'MULTIPLICATIVE_OPERATOR': ['MULTIPLICATIVE_OPERATOR'],
    'LOGICAL_OPERATOR': ['LOGICAL_OPERATOR'],
    'ACCESS_OPERATOR': ['ACCESS_OPERATOR'],
    'VISIBILITY_MODIFIER': ['VISIBILITY_MODIFIER'],
    'CONST_DECL': ['CONST_DECL'],
    'INHERITANCE_MODIFIER': ['INHERITANCE_MODIFIER'],
    'LITERAL': ['IDENTIFIER', 'LITERAL'],
    'ASSIGNMENT_OPERATOR': ['ASSIGNMENT_OPERATOR'],
    'EXPRESSION': ['EXPRESSION'],
    'THROW': ['THROW'],
    'THIS': ['THIS'],
    'AWAIT_EXPRESSION': ['AWAIT_EXPRESSION'],
    'ASSERT': ['ASSERT'],
}

ADVANCE_NODES = {
    'TYPE',
    'BODY',
    'EXPRESSION',
}

STOP_NODES = {
    'FUNCTION_DECL',
    'FUNCTION_BODY',
    'CLASS_DECL',
    'CLASS_BODY',
}


def load_grammar(f):
    """Load grammar given the file."""
    _name, ext = os.path.splitext(f)
    ext = ext[1:]
    if ext not in LISTENERS:
        raise ValueError('The program does not support the file extension')
    input_stream = FileStream(f)
    lexer = LEXERS[ext](input_stream)
    stream = CommonTokenStream(lexer)
    parser = PARSERS[ext](stream)
    tree = getattr(parser, START_RULE[ext])()
    listener = LISTENERS[ext]()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    # print(repr(listener.tree.children))
    return listener.tree


def compare_block(tree_1, tree_2):
    """Compare a function declaration statement among the given trees."""
    count_type_1 = 0
    count_type_2_3 = 0
    clones = []
    tree_1 = tree_1.dfs_subtree()
    tree_2 = tree_2.dfs_subtree()
    i, j = 0, 0
    while True:
        if i >= len(tree_1):
            break
        if j >= len(tree_2):
            break
        act_1 = tree_1[i]
        act_2 = tree_2[j]
        if act_2.type in ADVANCE_NODES:
            j += 1
            continue
        elif act_1.type in ADVANCE_NODES:
            i += 1
            continue
        elif act_1.type in STOP_NODES or act_2.type in STOP_NODES:
            break
        if (act_2.type in SIMILAR_NODES[act_1.type] or
                act_1.type in SIMILAR_NODES[act_2.type]):
            token_1 = act_1.token
            token_2 = act_2.token
            if token_1.text == token_2.text and token_1 != '':
                # Type 1 clone
                clones.append((token_1, token_2))
                count_type_1 += 1
            else:
                # Type 2/3 clone
                clones.append((token_1, token_2))
                count_type_2_3 += 1
        i += 1
        j += 1
    return clones, count_type_1, count_type_2_3


def compare_ecst(trees, return_all=False):
    """Compare the given trees to find clones."""
    blocks = {}
    block_keys = set()
    final_clones = []
    for i, tree in enumerate(trees):
        act_blocks = tree.dfs_split_blocks()
        blocks[i] = act_blocks
        block_keys |= act_blocks.keys()
    for key in block_keys:
        pairs = list(itertools.combinations(range(0, len(trees)), 2))
        act_clones = []
        max_type_1 = 0
        max_type_2_3 = 0
        for i, j in pairs:
            try:
                first_subtrees = blocks[i][key]
                second_subtrees = blocks[j][key]
                max_clones = []
                for first_tree in first_subtrees:
                    for second_tree in second_subtrees:
                        res = compare_block(first_tree, second_tree)
                        clones, count_type_1, count_type_2_3 = res
                        total = count_type_1 + count_type_2_3
                        if return_all:
                            max_clones = max_clones + clones
                        else:
                            if total > max_type_1 + max_type_2_3:
                                # Has more clones than the other blocks
                                max_type_1 += count_type_1
                                max_type_2_3 += count_type_2_3
                                max_clones = clones
                            elif total == max_type_1 + max_type_2_3:
                                if max_type_1 > max_type_2_3:
                                    max_type_1 += count_type_1
                                    max_type_2_3 += count_type_2_3
                                    max_clones = clones
                act_clones = act_clones + max_clones
            except KeyError:
                pass
        final_clones = final_clones + act_clones
    return final_clones


def discover_files(directory):
    """Discover supported files in the given directory."""
    res = []
    for root, _, files in os.walk(directory):
        for f in files:
            _, ext = osp.splitext(f)
            if ext in SUPPORTED_LANGUAGES:
                res.append(osp.join(root, f))
    return res


if __name__ == "__main__":
    args = get_args()
    if len(args.f) < 2:
        raise ValueError('Not enough files provided for comparison')

    if args.d != '':
        directory_files = discover_files(args.d)

    files = args.f + directory_files

    ecst_trees = {}
    for f in files:
        tree = load_grammar(f)
        ecst_trees.append(tree)

    clones = compare_ecst(ecst_trees, return_all=False)
    for token_1, token_2 in clones:
        if (token_1.line == 0 and token_1.column == 0 or
                token_2.line == 0 and token_2.column == 0):
            print(token_1.type, token_2.type)
        else:
            print(token_1.text, token_2.text)
            print(token_1.line, token_2.line)
            print(token_1.column, token_2.column)
