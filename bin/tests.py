import unittest

import cPickle
import pandas
from pandas.util.testing import assert_frame_equal

from algorithms.binary_search import binary_search
from data_structures.graph import NodeGraph
from ml.tf_idf import TfIdf
from data_structures.min_heap import MinHeap
from data_structures.queue import Queue
from data_structures.stack import Stack
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


class StackTests(unittest.TestCase):
    def create_no_element_stack(self):
        queue = Stack()

        return queue

    def create_one_element_stack(self):
        queue = Stack()

        queue.add('apple')

        return queue

    def create_five_element_stack(self):
        queue = Stack()

        for elem in ['apple', 'banana', 'chocolate', 'durian', 'eclair']:
            queue.add(elem)
        return queue

    def test_no_elem_stack(self):
        queue = self.create_no_element_stack()

        self.assertEquals(queue.to_list(), list())
        self.assertEquals(queue.peek(), None)

    def test_one_elem_stack(self):
        queue = self.create_one_element_stack()

        self.assertEquals(queue.to_list(), ['apple'])
        self.assertEquals(queue.peek(), 'apple')
        removed = queue.remove()
        self.assertEquals(removed, 'apple')
        self.assertEquals(queue.to_list(), list())
        self.assertEquals(queue.peek(), None)

    def test_five_elem_stack(self):
        queue = self.create_five_element_stack()

        self.assertEquals(queue.to_list(), ['apple', 'banana', 'chocolate', 'durian', 'eclair'])
        self.assertEquals(queue.peek(), 'apple')
        removed = queue.remove()
        self.assertEquals(removed, 'apple')
        self.assertEquals(queue.to_list(), ['banana', 'chocolate', 'durian', 'eclair'])
        self.assertEquals(queue.peek(), 'banana')


class QueueTests(unittest.TestCase):
    def create_no_element(self):
        queue = Queue()

        return queue

    def create_one_element(self):
        queue = Queue()

        for i in ['apple']:
            queue.add(i)

        return queue

    def create_two_element(self):
        queue = Queue()

        for i in ['apple', 'banana']:
            queue.add(i)

        return queue

    def create_five_element(self):
        queue = Queue()

        for i in ['apple', 'banana', 'chocolate', 'durian', 'eclair']:
            queue.add(i)

        return queue

    def test_no_element(self):
        queue = self.create_no_element()

        self.assertEqual(queue.to_list(), list())
        self.assertAlmostEquals(queue.remove(), None)

    def test_one_element(self):
        queue = self.create_one_element()

        self.assertEqual(queue.to_list(), ['apple'])
        self.assertEqual(queue.peek(), 'apple')
        self.assertEqual(queue.remove(), 'apple')
        self.assertEqual(queue.remove(), None)

    def test_two_elemnt(self):
        queue = self.create_two_element()

        self.assertEqual(queue.to_list(), ['apple', 'banana'])
        self.assertEqual(queue.peek(), 'apple')
        self.assertEqual(queue.remove(), 'apple')
        self.assertEqual(queue.remove(), 'banana')
        self.assertEqual(queue.remove(), None)

    def test_five_elemnt(self):
        queue = self.create_five_element()

        elements = ['apple', 'banana', 'chocolate', 'durian', 'eclair']
        self.assertEqual(queue.to_list(), elements)
        self.assertEqual(queue.peek(), 'apple')

        for i in elements:
            self.assertEqual(queue.remove(), i)

        self.assertEqual(queue.remove(), None)


class BinarySearchTest(unittest.TestCase):
    def test_no_element(self):
        a = []
        self.assertFalse(binary_search(a, 5))

    def test_one_element(self):
        a = [3]

        self.assertTrue(binary_search(a, 3))
        self.assertFalse(binary_search(a, 5))

    def test_two_element(self):
        a = [2, 3]

        self.assertTrue(binary_search(a, 2))
        self.assertTrue(binary_search(a, 3))
        self.assertFalse(binary_search(a, 5))

    def test_five_element(self):
        a = [2, 3, 13, 18, 100]

        self.assertTrue(binary_search(a, 2))
        self.assertTrue(binary_search(a, 3))
        self.assertTrue(binary_search(a, 13))
        self.assertTrue(binary_search(a, 18))
        self.assertTrue(binary_search(a, 100))
        self.assertFalse(binary_search(a, 5))

    def test_six_elements(self):
        a = [2, 3, 13, 18, 100, 1000]

        self.assertTrue(binary_search(a, 2))
        self.assertTrue(binary_search(a, 3))
        self.assertTrue(binary_search(a, 13))
        self.assertTrue(binary_search(a, 18))
        self.assertTrue(binary_search(a, 100))
        self.assertTrue(binary_search(a, 1000))
        self.assertFalse(binary_search(a, 5))


class TestMinHeap(unittest.TestCase):
    def test_switch_indices(self):
        l = [1, 2, 3, 4, 5]

        self.assertEquals(MinHeap.switch_indices(l, 2, 4), [1, 2, 5, 4, 3])

    def create_no_elements(self):

        h = MinHeap()

        return h

    def create_one_elements(self):
        h = MinHeap()

        l = [-5]

        for i in l:
            h.add(i)

        return h

    def create_two_elements(self):
        h = MinHeap()

        l = [13, -5]

        for i in l:
            h.add(i)

        return h

    def create_five_elements(self):
        h = MinHeap()

        l = [-5, 13, 22, -30, 100]

        for i in l:
            h.add(i)

        return h

    def test_no_elements(self):
        h = self.create_no_elements()

        self.assertItemsEqual(h.to_list(), list())
        self.assertEquals(h.remove(), None)

    def test_one_elements(self):
        h = self.create_one_elements()

        self.assertItemsEqual(h.to_list(), [-5])
        self.assertEquals(h.peek(), -5)
        self.assertEquals(h.remove(), -5)
        self.assertItemsEqual(h.to_list(), list())
        self.assertEquals(h.remove(), None)

    def test_two_elements(self):
        h = self.create_two_elements()
        l = sorted([13, -5])

        for (l_index, l_element) in enumerate(l):
            self.assertItemsEqual(h.to_list(), l[l_index:])
            self.assertEquals(h.peek(), l_element)
            self.assertEquals(h.remove(), l_element)

    def test_five_elements(self):
        h = self.create_five_elements()
        l = sorted([-5, 13, 22, -30, 100])

        for (l_index, l_element) in enumerate(l):
            self.assertItemsEqual(h.to_list(), l[l_index:])
            self.assertEquals(h.peek(), l_element)
            self.assertEquals(h.remove(), l_element)


class TestNodeGraph(unittest.TestCase):
    def test_no_nodes(self):
        g = NodeGraph()

        node_values = list()

        for node_value in node_values:
            g.add_node(node_value)

        self.assertItemsEqual(g.to_adjacency_list(), list())

    def test_one_nodes(self):
        g = NodeGraph()

        node_values = list('a')

        for node_value in node_values:
            g.add_node(node_value)

        self.assertItemsEqual(g.to_adjacency_list(), list())
        self.assertItemsEqual(g.to_node_list(), ['a'])

    def test_two_nodes(self):
        g = NodeGraph()

        node_values = ['a', 'b']

        for node_value in node_values:
            g.add_node(node_value)

        self.assertItemsEqual(g.to_adjacency_list(), list())

        g.add_edge('b', 'a')
        self.assertItemsEqual(g.to_adjacency_list(), [('b', 'a')])
        self.assertItemsEqual(g.to_node_list(), ['a', 'b'])

    def test_five_nodes(self):
        g = NodeGraph()

        node_values = ['a', 'b', 'c', 'd', 'e']

        for node_value in node_values:
            g.add_node(node_value)

        self.assertItemsEqual(g.to_node_list(), ['a', 'b', 'c', 'd', 'e'])

        # No edges
        self.assertItemsEqual(g.to_adjacency_list(), list())

        # One edge
        g.add_edge('b', 'a')
        self.assertItemsEqual(g.to_adjacency_list(), [('b', 'a')])

        g.add_edge('a', 'b')
        self.assertItemsEqual(g.to_adjacency_list(), [('b', 'a'), ('a', 'b')])

        g.add_edge('e', 'a')
        self.assertItemsEqual(g.to_adjacency_list(), [('b', 'a'), ('a', 'b'), ('e', 'a')])

        self.assertRaises(ValueError, g.get_node, 'k')


class TestTfidf(unittest.TestCase):
    def create_no_documents(self):
        doc_list = list()

        df = pandas.DataFrame(data=doc_list, columns=['text'])
        df['document'] = df.index

        return df

    def create_one_document(self):
        doc_list = ['This is a test document']

        df = pandas.DataFrame(data=doc_list, columns=['text'])
        df['document'] = df.index

        return df

    def create_two_documents(self):
        doc_list = ['This is a test document', 'This is another test document, which is a bit longer']

        df = pandas.DataFrame(data=doc_list, columns=['text'])
        df['document'] = df.index

        return df

    def test_no_documents(self):
        X = self.create_no_documents()
        tf = TfIdf()
        result = tf.fit_transform(X)

        gold_standard = cPickle.load(open('../resources/tfidf/no_doc.pkl'))
        assert_frame_equal(result.reset_index(drop=True), gold_standard.reset_index(drop=True))

    def test_one_documents(self):
        X = self.create_one_document()
        tf = TfIdf()
        result = tf.fit_transform(X)

        gold_standard = cPickle.load(open('../resources/tfidf/one_doc.pkl'))
        assert_frame_equal(result.reset_index(drop=True), gold_standard.reset_index(drop=True))

    def test_two_documents(self):
        X = self.create_two_documents()
        tf = TfIdf()
        result = tf.fit_transform(X)

        gold_standard = cPickle.load(open('../resources/tfidf/two_doc.pkl'))
        assert_frame_equal(result.reset_index(drop=True), gold_standard.reset_index(drop=True))


if __name__ == '__main__':
    unittest.main()
