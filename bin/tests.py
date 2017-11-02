import unittest

from data_structures.binary_tree import BinaryTree
from data_structures import linked_list


class LinkedListTests(unittest.TestCase):

    def test_empty_list(self):
        ll = linked_list.LinkedList()
        self.assertEquals(ll.to_list(), list())

    def test_single_element_list(self):

        ll = linked_list.LinkedList()
        test_list = ['First']

        for element in test_list:
            ll.add(element)
        self.assertEquals(ll.to_list(), test_list)

    def test_triple_element_list(self):

        ll = linked_list.LinkedList()
        test_list = ['First', 'Second', 'Third']

        for element in test_list:
            ll.add(element)

        self.assertEquals(ll.to_list(), test_list)

    def test_last_list(self):
        ll = linked_list.LinkedList()
        test_list = ['First', 'Second', 'Third']

        for element in test_list:
            ll.add(element)

        self.assertEquals(ll.to_list()[-1], ll.last.load)

    def test_remove_first_single(self):
        ll = linked_list.LinkedList()
        test_list = ['First']

        for element in test_list:
            ll.add(element)

        self.assertEquals(ll.remove_first(), test_list[0])
        self.assertEquals(ll.last, None)
        self.assertEquals(ll.to_list(), test_list[1:])


    def test_remove_first_multiple(self):
        ll = linked_list.LinkedList()
        test_list = ['First', 'Second', 'Third']

        for element in test_list:
            ll.add(element)

        self.assertEquals(ll.remove_first(), test_list[0])
        self.assertEquals(ll.to_list(), test_list[1:])

    def test_remove_last_single(self):
        ll = linked_list.LinkedList()
        test_list = ['First']

        for element in test_list:
            ll.add(element)

        self.assertEquals(ll.remove_last(), test_list[-1])
        self.assertEquals(ll.last, None)
        self.assertEquals(ll.to_list(), test_list[:-1])

    def test_remove_last_multiple(self):
        ll = linked_list.LinkedList()
        test_list = ['First', 'Second', 'Third']

        for element in test_list:
            ll.add(element)
        last = ll.remove_last()
        self.assertEquals(last, test_list[-1])
        self.assertEquals(ll.to_list(), test_list[:-1])

class BinaryTreeTests(unittest.TestCase):

    @staticmethod
    def generate_no_element_tree():
        tree = BinaryTree()
        return tree

    @staticmethod
    def generate_one_element_tree():
        tree = BinaryTree()
        tree.add('banana')
        return tree

    @staticmethod
    def generate_two_element_tree():
        tree = BinaryTree()
        tree.add('apple')
        tree.add('banana')
        return tree

    @staticmethod
    def generate_five_element_tree():
        tree = BinaryTree()
        tree.add('apple')
        tree.add('banana')
        tree.add('chocolate')
        tree.add('durian')
        tree.add('eclair')
        return tree


    def test_no_element(self):
        tree = self.generate_no_element_tree()

        self.assertItemsEqual(tree.to_list(), list())
        self.assertFalse(tree.contains('flour'))


    def test_one_element(self):
        tree = self.generate_one_element_tree()

        self.assertItemsEqual(tree.to_list(), ['banana'])
        self.assertTrue(tree.contains('banana'))
        self.assertFalse(tree.contains('flour'))

    def test_two_element_tree(self):
        tree = self.generate_two_element_tree()
        self.assertItemsEqual(tree.to_list(), ['apple', 'banana'])
        self.assertTrue(tree.contains('apple'))
        self.assertTrue(tree.contains('banana'))
        self.assertFalse(tree.contains('flour'))

    def test_five_element_tree(self):

        tree = self.generate_five_element_tree()
        self.assertItemsEqual(tree.to_list(), ['apple', 'banana', 'chocolate', 'durian', 'eclair'])
        self.assertTrue(tree.contains('apple'))
        self.assertTrue(tree.contains('banana'))
        self.assertTrue(tree.contains('chocolate'))
        self.assertTrue(tree.contains('durian'))
        self.assertTrue(tree.contains('eclair'))
        self.assertFalse(tree.contains('flour'))


    def test_no_element_remove(self):
        tree = self.generate_no_element_tree()
        with self.assertRaises(Exception) as context:
            tree.remove('flour')

        self.assertTrue('cannot remove' in str(context.exception))

    def test_one_element_remove(self):
        tree = self.generate_one_element_tree()
        with self.assertRaises(Exception) as context:
            tree.remove('flour')

        self.assertTrue('cannot remove' in str(context.exception))

        self.assertTrue(tree.contains('banana'))
        tree.remove('banana')
        self.assertFalse(tree.contains('banana'))

    def test_two_element_remove(self):
        tree = self.generate_two_element_tree()

        with self.assertRaises(Exception) as context:
            tree.remove('flour')

        self.assertTrue('cannot remove' in str(context.exception))

        self.assertTrue(tree.contains('banana'))
        tree.remove('banana')
        self.assertFalse(tree.contains('banana'))

        self.assertItemsEqual(tree.to_list(), ['apple'])

    def test_five_element_remove(self):
        tree = self.generate_five_element_tree()

        with self.assertRaises(Exception) as context:
            tree.remove('flour')

        self.assertTrue('cannot remove' in str(context.exception))

        self.assertTrue(tree.contains('banana'))
        tree.remove('banana')
        self.assertFalse(tree.contains('banana'))
        self.assertItemsEqual(tree.to_list(), ['apple', 'chocolate', 'durian', 'eclair'])


if __name__ == '__main__':
    unittest.main()