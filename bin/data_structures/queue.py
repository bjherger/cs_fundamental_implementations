class Queue(object):

    # Simple first in, first out (FIFO) stack, based on the Java Queue API:
    # https://docs.oracle.com/javase/7/docs/api/java/util/Queue.html

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, load):
        new_node = QueueNode(load)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def to_list(self):
        if self.head is None:
            return list()
        else:
            agg = list()
            current = self.head
            while current is not None:
                agg.append(current.load)

                current = current.next

            return agg

        pass

    def peek(self):
        if self.head is None:
            return None
        else:
            return self.head.load

    def remove(self):
        if self.head is None:
            return None
        else:
            old_head = self.head
            new_head = old_head.next

            self.head = new_head

            if new_head is None:
                self.tail = None

            return old_head.load

class QueueNode(object):

    def __init__(self, load):
        self.load = load
        self.next = None
