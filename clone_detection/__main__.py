import os

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
    print(repr(listener.tree.children))
    return lexer, parser, tree


if __name__ == "__main__":
    args = get_args()
    if len(args.f) < 2:
        raise ValueError('Not enough files provided for comparison')
    for f in args.f:
        lexer, parser, tree = load_grammar(f)
