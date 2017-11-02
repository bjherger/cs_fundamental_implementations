class LinkedList(object):

    def __init__(self):
        self.first = None
        self.last = None

    def to_list(self):
        # If list has no elements, return empty list
        if self.first is None:
            return list()
        else:
            next = self.first
            agg = list()
            while next is not None:
                agg.append(next.load)
                next = next.next_node
            return agg

    def add(self, E):
        new_node = Node(E)
        # If list has no elements, set first and last
        if self.first is None:
            self.first = new_node
            self.last = new_node

        # If list already has elements, link to last and update last
        else:
            self.last.set_next_node(new_node)
            self.last = new_node

    def remove_first(self):
        # If list has no elements, throw error
        if self.first is None:
            raise IndexError('Linked list has no first element to remove')

        # Else remove first element and update pointers
        else:
            old_first = self.first
            new_first = old_first.next_node
            self.first = new_first

            if new_first is None:
                self.last = None

            return old_first.load

    def remove_last(self):
        # If list has no elements, throw error
        if self.first is None:
            raise IndexError('Linked list has no first element to remove')

        # Else remove last element and update pointers
        else:

            # If there is only one element, return that
            if self.first == self.last:
                return self.remove_first()

            # If there is more than one element, find new last and update
            else:
                old_last = self.last

                new_last_found = False
                new_last = self.first
                while not new_last_found:

                    if new_last.next_node == old_last:
                        new_last_found = True
                    else:
                        new_last = new_last.next_node

                self.last = new_last
                self.last.set_next_node(None)
                return old_last.load


class Node(object):

    def __init__(self, load):

        self.load = load
        self.next_node = None

    def set_next_node(self, next_node):

        self.next_node = next_node

