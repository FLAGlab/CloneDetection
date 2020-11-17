from .ecst_node import ECSTNode, ShortToken


class ECSTree(ECSTNode):
    def __init__(self):
        """Initialize the ECST structure."""
        root_token = ShortToken('', 0, 0)
        super().__init__(None, None, root_token, None)
