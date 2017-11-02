import unittest

from data_structures import linked_list


class LinkedListTests(unittest.TestCase):

    def test(self):
        ll = linked_list.LinkedList()
        self.assertEquals(ll.to_list(), list())

if __name__ == '__main__':
    unittest.main()