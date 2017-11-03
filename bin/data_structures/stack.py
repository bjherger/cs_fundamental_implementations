class Stack(object):

    # Simple first in, last out (FLFO) stack, based on the Java Queue API:
    # https://docs.oracle.com/javase/7/docs/api/java/util/Queue.html

    def __init__(self):
        self.head = None

    def add(self, load):
        if self.head is None:
            self.head = StackNode(load)
        else:
            parent = self.head

            while parent.next is not None:
                parent = parent.next

            parent.next = StackNode(load)

    def to_list(self):
        agg = list()
        current = self.head
        while current is not None:
            agg.append(current.load)
            current = current.next

        return agg

    def peek(self):
        if self.head is None:
            return None
        else:
            return self.head.load

    def offer(self):
        pass

    def remove(self):
        if self.head is None:
            return None
        else:
            old_head = self.head
            new_head = self.head.next
            self.head = new_head
            return old_head.load

class StackNode(object):

    def __init__(self, load):
        self.load = load
        self.next = None