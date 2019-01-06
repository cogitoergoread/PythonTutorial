"""
http://openbookproject.net/thinkcs/python/english3e/trees.html
"""

class Tree:
    """
    The process of assembling a tree is similar to the process of assembling a linked list.
    Each constructor invocation builds a single node.
    """
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)

    def str_preorder(self):
        """
        print a tree, first print the contents of the root, then print the entire left subtree,
        and then print the entire right subtree.
        :return: Preorder representation
        :rtype: str
        """
        s: str  =""
        s += str(self.cargo)
        if self.left:
            s += " " + self.left.str_preorder()
        if self.right:
            s += " " + self.right.str_preorder()
        return s

    def str_postorder(self):
        """
        print the subtrees first and then the root node
        :return: Postorder representation
        :rtype: str
        """
        s: str  =""
        if self.left:
            s += self.left.str_postorder() + " "
        if self.right:
            s += self.right.str_postorder() + " "
        s += str(self.cargo)
        return s

    def str_inorder(self):
        """
        traverse a tree inorder, you print the left tree, then the root, and then the right tree
        :return: Inrder representation
        :rtype: str
        """
        s: str  =""
        if self.left:
            s += self.left.str_inorder() + " "
        s += str(self.cargo)
        if self.right:
            s += " " + self.right.str_inorder()
        return s

    def str_indented(self, level = 0):
        """
        generate a graphical representation of a tree
        :param level: Indentation level
        :type level: int
        :return: String representation
        :rtype: str
        """
        s: str  =""
        if self.right:
            s += self.right.str_indented(level + 1)
        s += "  " * level + str(self.cargo) + "/n"
        if self.left:
            s += self.left.str_indented(level + 1)
        return s

def get_token(token_list, expected):
    if token_list[0] == expected:
        del token_list[0]
        return True
    return False

def get_number(token_list):
    if get_token(token_list, "("):
        x = get_sum(token_list)  # Get the subexpression
        get_token(token_list, ")")  # Remove the closing parenthesis
        return x
    else:
        x = token_list[0]
        if type(x) != type(0): return None
        del token_list[0]
        return Tree(x, None, None)

def get_sum(token_list):
    a = get_product(token_list)
    if get_token(token_list, "+"):
        b = get_sum(token_list)
        return Tree("+", a, b)
    return a

def get_product(token_list):
    a = get_number(token_list)
    if get_token(token_list, "*"):
        b = get_product(token_list)       # This line changed
        return Tree("*", a, b)
    return a