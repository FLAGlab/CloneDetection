import math
from antlr4 import ParserRuleContext, Token, TokenStream

DOT = 132
LCURLY = 133
LPAREN = 134
LBRACK = 135
RCURLY = 136
RPAREN = 137
RBRACK = 138
COMMA = 139
COLON = 140
SEMI = 141
WS = 169
Block_comment = 170
Line_comment = 171
operatorHead = set({})
leftWS = set({})
rightWS = set({})

operatorHead |= {ord('/')}
operatorHead |= {ord('=')}
operatorHead |= {ord('-')}
operatorHead |= {ord('+')}
operatorHead |= {ord('!')}
operatorHead |= {ord('*')}
operatorHead |= {ord('%')}
operatorHead |= {ord('<')}
operatorHead |= {ord('>')}
operatorHead |= {ord('&')}
operatorHead |= {ord('|')}
operatorHead |= {ord('^')}
operatorHead |= {ord('~')}
operatorHead |= {ord('?')}

# operator-head → U+00A1–U+00A7
operatorHead |= {x for x in range(0x00A1, 0x00A7+1)}

# operator-head → U+00A9 or U+00AB
operatorHead |= {0x00A9}
operatorHead |= {0x00AB}

# operator-head → U+00AC or U+00AE
operatorHead |= {0x00AC}
operatorHead |= {0x00AE}

# operator-head → U+00A9 or U+00AB
operatorHead |= {0x00A9}
operatorHead |= {0x00AB}

# operator-head → U+00B0–U+00B1, U+00B6, U+00BB, U+00BF, U+00D7, or U+00F7
operatorHead |= {x for x in range(0x00B0, 0x00B1+1)}
operatorHead |= {0x00B6}
operatorHead |= {0x00BB}
operatorHead |= {0x00BF}
operatorHead |= {0x00D7}
operatorHead |= {0x00F7}

# operator-head → U+2016–U+2017 or U+2020–U+2027
operatorHead |= {x for x in range(0x2016, 0x2017+1)}
operatorHead |= {x for x in range(0x2020, 0x2027+1)}

# operator-head → U+2030–U+203E
operatorHead |= {x for x in range(0x2030, 0x203E+1)}

# operator-head → U+2041–U+2053
operatorHead |= {x for x in range(0x2041, 0x2053+1)}

# operator-head → U+2055–U+205E
operatorHead |= {x for x in range(0x2055, 0x205E+1)}

# operator-head → U+2190–U+23FF
operatorHead |= {x for x in range(0x2190, 0x23FF+1)}

# operator-head → U+2500–U+2775
operatorHead |= {x for x in range(0x2500, 0x2775+1)}

# operator-head → U+2794–U+2BFF
operatorHead |= {x for x in range(0x2794, 0x2BFF+1)}

# operator-head → U+2E00–U+2E7F
operatorHead |= {x for x in range(0x2E00, 0x2E7F+1)}

# operator-head → U+3001–U+3003
operatorHead |= {x for x in range(0x3001, 0x3003+1)}

# operator-head → U+3008–U+3030
operatorHead |= {x for x in range(0x3008, 0x3030+1)}

# operator-character → operator-head­
operatorCharacter = set(operatorHead)

# operator-character → U+0300–U+036F
operatorCharacter |= {x for x in range(0x0300, 0x036F+1)}

# operator-character → U+1DC0–U+1DFF
operatorCharacter |= {x for x in range(0x1DC0, 0x1DFF+1)}

# operator-character → U+20D0–U+20FF
operatorCharacter |= {x for x in range(0x20D0, 0x20FF+1)}

# operator-character → U+FE00–U+FE0F
operatorCharacter |= {x for x in range(0xFE00, 0xFE0F+1)}

# operator-character → U+FE20–U+FE2F
operatorCharacter |= {x for x in range(0xFE20, 0xFE2F+1)}

# operator-character → U+E0100–U+E01EF
operatorCharacter |= {x for x in range(0xE0100, 0xE01EF+1)}

leftWS |= {WS}
leftWS |= {LPAREN}
leftWS |= {LBRACK}
leftWS |= {LCURLY}
leftWS |= {COMMA}
leftWS |= {COLON}
leftWS |= {SEMI}

rightWS |= {WS}
rightWS |= {RPAREN}
rightWS |= {RBRACK}
rightWS |= {RCURLY}
rightWS |= {COMMA}
rightWS |= {COLON}
rightWS |= {SEMI}
rightWS |= {Line_comment}
rightWS |= {Block_comment}


class SwiftSupport():
    '''
    There is one caveat to the rules above. If the ! or ? predefined operator
     has no whitespace on the left, it is treated as a postfix operator,
     regardless of whether it has whitespace on the right. To use the ? as
     the optional-chaining operator, it must not have whitespace on the left.
      To use it in the ternary conditional (? :) operator, it must have
      whitespace around both sides.

    operator-head : /  =  -  +  !  *  %  <  >  &  |  ^  ~  ?
      | [\u00A1-\u00A7]
      | [\u00A9\u00AB]
      | [\u00AC\u00AE]
      | [\u00B0-\u00B1\u00B6\u00BB\u00BF\u00D7\u00F7]
      | [\u2016-\u2017\u2020-\u2027]
      | [\u2030-\u203E]
      | [\u2041-\u2053]
      | [\u2055-\u205E]
      | [\u2190-\u23FF]
      | [\u2500-\u2775]
      | [\u2794-\u2BFF]
      | [\u2E00-\u2E7F]
      | [\u3001-\u3003]
      | [\u3008-\u3030]
      ;
     '''
    @staticmethod
    def isCharacterFromSet(token, charset):
        if token.type == Token.EOF:
            return False
        else:
            text = token.text
            codepoint = ord(text[0])
            return codepoint in charset

    @staticmethod
    def isOperatorHead(token):
        return SwiftSupport.isCharacterFromSet(token, operatorHead)

    @staticmethod
    def isOperatorCharacter(token):
        return SwiftSupport.isCharacterFromSet(token, operatorCharacter)

    @staticmethod
    def isOpNext(tokens):
        stop = SwiftSupport.getLastOpTokenIndex(tokens)
        if stop == -1:
            return False
        return True

    @staticmethod
    def getLastOpTokenIndex(tokens):
        """
        Find stop token index of next operator; return -1 if not operator.
        """
        currentTokenIndex = tokens.index
        currentToken = tokens.get(currentTokenIndex)
        # operator → dot-operator-head­ dot-operator-characters
        if (currentToken.type == DOT and
                tokens.get(currentTokenIndex + 1).type == DOT):
            # dot-operator
            currentTokenIndex += 2  # point at token after ".."
            currentToken = tokens.get(currentTokenIndex)

            # dot-operator-character → .­ | operator-character­
            while (currentToken.type == DOT or
                   SwiftSupport.isOperatorCharacter(currentToken)):
                currentTokenIndex += 1
                currentToken = tokens.get(currentTokenIndex)
            return currentTokenIndex - 1

        # operator → operator-head­ operator-characters­?
        if SwiftSupport.isOperatorHead(currentToken):
            currentToken = tokens.get(currentTokenIndex)
            while SwiftSupport.isOperatorCharacter(currentToken):
                currentTokenIndex += 1
                currentToken = tokens.get(currentTokenIndex)
            return currentTokenIndex - 1
        else:
            return -1

    @staticmethod
    def isBinaryOp(tokens):
        """
        If an operator has whitespace around both sides or around neither side,
        it is treated as a binary operator. As an example, the + operator in a+b
        and a + b is treated as a binary operator.
        """
        stop = SwiftSupport.getLastOpTokenIndex(tokens)
        if stop == -1:
            return False
        start = tokens.index
        prevToken = tokens.get(start - 1)
        nextToken = tokens.get(stop + 1)
        prevIsWS = SwiftSupport.isLeftOperatorWS(prevToken)
        nextIsWS = SwiftSupport.isRightOperatorWS(nextToken)
        result = prevIsWS and nextIsWS or (not prevIsWS and not nextIsWS)
        # text = tokens.getText(start, stop)
        return result

    @staticmethod
    def isPrefixOp(tokens):
        """
        If an operator has whitespace on the left side only, it is treated as a
        prefix unary operator. As an example, the ++ operator in a ++b is treated
        as a prefix unary operator."
        """
        stop = SwiftSupport.getLastOpTokenIndex(tokens)
        if stop == -1:
            return False
        start = tokens.index
        prevToken = tokens.get(start - 1)
        nextToken = tokens.get(stop + 1)
        prevIsWS = SwiftSupport.isLeftOperatorWS(prevToken)
        nextIsWS = SwiftSupport.isRightOperatorWS(nextToken)
        result = prevIsWS and not nextIsWS
        return result

    @staticmethod
    def isPostfixOp(tokens):
        """
        If an operator has whitespace on the right side only, it is treated as a
        postfix unary operator. As an example, the ++ operator in a++ b is treated
        as a postfix unary operator.

        If an operator has no whitespace on the left but is followed immediately
        by a dot (.), it is treated as a postfix unary operator. As an example,
        the ++ operator in a++.b is treated as a postfix unary operator (a++ .b
        rather than a ++ .b).
        """
        stop = SwiftSupport.getLastOpTokenIndex(tokens)
        if stop == -1:
            return False

        start = tokens.index
        prevToken = tokens.get(start - 1)
        nextToken = tokens.get(stop + 1)
        prevIsWS = SwiftSupport.isLeftOperatorWS(prevToken)
        nextIsWS = SwiftSupport.isRightOperatorWS(nextToken)
        result = (not prevIsWS and nextIsWS) or (
            not prevIsWS and nextToken.type == DOT)
        # text = tokens.getText(start, stop)
        return result

    @staticmethod
    def isOperator(tokens, op):
        stop = SwiftSupport.getLastOpTokenIndex(tokens)
        if stop == -1:
            return False
        start = tokens.index
        text = tokens.getText(start, stop)
        return text == op

    @staticmethod
    def isLeftOperatorWS(token):
        return token.type in leftWS

    @staticmethod
    def isRightOperatorWS(token):
        return (token.type in rightWS) or token.type == Token.EOF

    @staticmethod
    def isSeparatedStatement(tokens, indexOfPreviousStatement):
        indexFrom = indexOfPreviousStatement - 1
        indexTo = tokens.index - 1
        # Stupid check for new line and semicolon, can be optimized
        if indexFrom >= 0:
            while (indexFrom >= 0 and
                   tokens.get(indexFrom).channel == Token.HIDDEN_CHANNEL):
                indexFrom -= 1
            interval = tokens.getText(indexFrom, indexTo)
            if "\n" in interval or ";" in interval:
                return True
            else:
                return False
        else:
            return True
