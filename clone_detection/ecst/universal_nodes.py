UNIVERSAL_NODES = {
    'FILE',  # File node
    'SCRIPT',  # Script node
    'IDENTIFIER',  # Actual name for functions, classes, variables, etc
    'CLASS_DECL',  # Class declaration
    'CONSTRUCTOR_DECL',  # Constructor declaration
    'PARAMETER_LIST',  # List of parameters for everything
    'PARAMETER',  # Node that identifies a single parameter
    'CONSTRUCTOR_CALL',  # Create new object from constructor
    'CLASS_BODY',  # Defines a body for a class
    'CLASS_MEMBER',  # Define a member of a class
    'ENUM_DECL',  # Define a enumeratio
    'ENUM_BODY',  # Defines a enumeration body
    'FUNCTION_DECL',  # Function declaration
    'FUNCTION_BODY',  # Define the body function
    'FUNCION_CALL',  # Define a function call
    'ATTRIBUTE_DECL',  # Attribute declaration
    'VARIABLE_DECL',  # Variable declaration
    'GETTER',  # Getter declaration
    'SETTER',  # Setter declaration
    'TYPE_ALIAS',  # Define a type alias, shorter name type that can be created
    'PARAMETER_TYPE',  # Define the type of a parameter
    'TYPE',  # Define a type
    'NULLABLE_TYPE',  # Define a nullable type
    'FUNCTION_TYPE',  # Define a function type
    'USER_TYPE',  # Define a user type
    'OR',  # Define conjuction || conjuction
    'AND',  # Define something && something
    'TERNARY',  # Define a ternary/elvis operation
    'AS',  # Define as expression - casting
    'PREFIX',  # Define a prefix operation ++, --, +=, -=, etc.
    'POSFIX',  # Define a posfix operation ++, --, !, etc
    'COLLECTION_INDEXING',  # Index an array
    'VALUE_ARGUMENT_LIST',  # List of arguments used for a call
    'VALUE_ARGUMENT',  # Value argument ^^
    'TYPE_ARGUMENT_LIST',  # List of type arguments <Type1, Type2>
    'TYPE_ARGUMENT',  # Type Argument ^^
    'STRING',  # Define a String literal
    'COLLECTION',  # Define a collection, can be an array, etc
    'SUPER_CALL',  # Defines a call to super
    'CONDITION',  # Defines a condition, if, when, switch, etc
    'BODY',  # Defines the body of a control structure: for, while, if, etc
    'TRY',  # Defines a try block
    'CATCH',  # Defines a catch block
    'FINALLY',  # Defines a finally block
    'LOOP_STATEMENT',  # Defines loop statement for, while, dowhile
    'JUMP_STATEMENT',  # Defines jump statement break, continue, return
    'EQUALITY_OPERATOR',  # Define an equality operation == !==
    'COMPARISON_OPERATOR',  # Define a comparison operation >, <
    'MEMBER_OF',  # Define if x is IN container or NOT IN
    'IS_TYPE',  # Define if x IS of type or NOT IS
    'ADDITIVE_OPERATOR',  # Define an additive/subtraction operation
    'MULTIPLICATIVE_OPERATOR',  # Define a multiplication/division/modulus
    'LOGICAL_OPERATOR',  # Define a logical operator like not, !
    'ACCESS_OPERATOR',  # Define an access operator like '.' or '::'
    'VISIBILITY_MODIFIER',  # Define the visibility public, private, protected
    'CONST_DECL',  # Declare a constant , cons keyword
    'INHERITANCE_MODIFIER',  # Declare if the inheritance is abstract, final
    'LITERAL',  # Defines the value of a constant, integer, boolean, etc
    'ASSIGNMENT_OPERATOR',  # Give value to a variable var x = 3
    'EXPRESSION',  # Define a expression of the language, if, for, while, condition, etc
    'THROW',  # Define a throw exception expression
    'THIS',  # Define a this, self expression
    'AWAIT_EXPRESSION',  # Define an await expression
    'ASSERT',  # Define assert expression
}
