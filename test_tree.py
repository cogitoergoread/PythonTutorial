from unittest import TestCase
from Tree import Tree, get_sum

class TestTree(TestCase):
    def setUp(self):
        self.tree =  Tree("+", Tree(1), Tree("*", Tree(2), Tree(3)))

    def test_str_preorder(self):
        self.assertEqual("+ 1 * 2 3", self.tree.str_preorder())

    def test_str_postorder(self):
        self.assertEqual("1 2 3 * +", self.tree.str_postorder())

    def test_str_inorder(self):
        self.assertEqual("1 + 2 * 3", self.tree.str_inorder())

    def test_str_indented(self):
        self.assertEqual("    3/n  */n    2/n+/n  1/n", self.tree.str_indented())

    def test_expr_par(self):
        token_list = [9, "*", 11, "+", 5, "*", 7, "end"]
        tree2 = get_sum(token_list)
        s2 = tree2.str_postorder()
        self.assertEqual("9 11 * 5 7 * +", s2)

    def test_expr_par(self):
        token_list = [9, "*", "(", 11, "+", 5, ")", "*", 7, "end"]
        tree2 = get_sum(token_list)
        s2 = tree2.str_postorder()
        self.assertEqual("9 11 5 + 7 * *", s2)
