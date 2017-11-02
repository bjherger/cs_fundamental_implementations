import unittest

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



if __name__ == '__main__':
    unittest.main()