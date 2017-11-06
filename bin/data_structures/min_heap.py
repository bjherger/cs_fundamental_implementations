class MinHeap(object):

    # Unbounded min heap, vaguely based on Java PriorityQueue API: https://docs.oracle.com/javase/7/docs/api/java/util/PriorityQueue.html
    def __init__(self):
        self.heap_list = list()
        self.last_index = -1

    def add(self, elem):
        self.heap_list.append(elem)
        self.last_index = self.last_index + 1
        self.bubble_up(self.last_index)

    def to_list(self):
        return self.heap_list

    def peek(self):
        return self.heap_list[0]

    def remove(self):

        if self.last_index <0:
            return None
        elif self.last_index == 0:
            return_element = self.heap_list[0]
            self.heap_list = list()
            self.last_index = self.last_index - 1
            return return_element
        else:
            return_element = self.heap_list[0]
            self.heap_list[0] = self.heap_list[self.last_index]
            self.bubble_down(0)
            self.heap_list = self.heap_list[:-1]
            return return_element

    def bubble_up(self, bubble_index):
        print self.heap_list
        print bubble_index, bubble_index / 2
        print self.heap_list[bubble_index], self.heap_list[bubble_index / 2]
        # TODO Could also end when parent is less than new child (?)
        while bubble_index / 2 > -1:
            print 'inside while'
            if self.heap_list[bubble_index] < self.heap_list[bubble_index / 2]:
                print 'triggered'
                self.switch_indices(bubble_index/2, bubble_index)
                bubble_index = bubble_index / 2

    def bubble_down(self, bubble_index):

        while bubble_index < self.last_index:
            if self.heap_list[bubble_index] > self.heap_list[bubble_index*2]:
                self.heap_list = self.switch_indices(bubble_index * 2, bubble_index)
                bubble_index = bubble_index * 2

    @staticmethod
    def switch_indices(input_list, index_1, index_2):

        tmp = input_list[index_1]
        input_list[index_1] = input_list[index_2]
        input_list[index_2] = tmp
        return input_list

