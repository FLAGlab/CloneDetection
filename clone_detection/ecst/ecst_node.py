from .universal_nodes import UNIVERSAL_NODES


class ECSTNode():
    """"Define a ECST node."""
    def __init__(self, id, parent, token, type_):
        """Initialize the ECST Node."""
        self.id = id
        self.parent = parent
        self.token = token
        self.type = type_
        self.children = []
        self.level = 0

    def add_child(self, node):
        """Add a new children to the node."""
        node.level = self.level + 1
        self.children.append(node)

    def rewrite_token(self, new_token):
        """Change the token for a new one."""
        self.token = new_token

    def rewrite_type(self, new_type):
        """Change the type of the node."""
        self.type = type

    def dispose_children(self):
        """Clear all the children of the node."""
        self.children = []

    def __str__(self):
        """Method to convert the node to string."""
        tab_level = self.level * '\t'
        this_print = tab_level + str((self.token.text, self.type))
        l_print = [this_print]
        for child in self.children:
            l_print.append(str(child))
        open_brace = '\n' + tab_level + '[\n'
        close_brace = '\n' + tab_level + '],\n'
        return open_brace + ''.join(l_print) + close_brace

    def __repr__(self):
        return str(self)

    def tokens_match(node_1, node_2):
        """Returns if the token is the same for both nodes."""
        return node_1.token.text == node_2.token.text

    def __eq__(self, value):
        """"Compare method."""
        if self == value:
            return True
        if not value:
            return False
        value_token = value.token
        same_text = self.token.text == value_token.text
        same_line = self.token.line == value_token.line
        same_col = self.token.column == value_token.column
        return same_text and same_line and same_col

    def to_root_finger_print(self):
        """Print the parent tree."""
        res = ''
        tmp = self.parent
        while tmp:
            res.append('{} <-- '.format(tmp))
        return res

    def find_first_at_first_level(self, token):
        """Find the first children with the given token in the first level."""
        for child in self.children:
            if child.token.text == token:
                return child
        return None

    def find_all_at_first_level(self, token):
        """Find all the children with the given token in the first level."""
        res = []
        for child in self.children:
            if child.token.text == token:
                res.append(child)
        return res

    def dfs_subtree(self, exclude_universal_nodes):
        """Get the dfs subtree."""
        dfs_children_list = list(self.children)
        res = []
        while dfs_children_list != []:
            child = dfs_children_list.pop(0)
            is_universal_node = child.token in UNIVERSAL_NODES
            if ((exclude_universal_nodes and not is_universal_node) or not
                    exclude_universal_nodes):
                res.append(child)
            dfs_children_list += child.children
        return res

    def empty_subtree(self):
        """Return if the subtree is empty."""
        return len(self.children) > 0

    def replace_child(self, target, new_node):
        """Replace the target child with the new one."""
        target_index = self.children.index(target)
        self.children.pop(target_index)
        self.children.insert(target_index, new_node)


class ShortToken():
    """Define a ShortToken."""
    def __init__(self, text, line, column):
        """Initialize a token"""
        self.text = text
        self.line = line
        self.column = column
