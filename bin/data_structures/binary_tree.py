class BinaryTree(object):
    # Roughly based on http://www1.cs.columbia.edu/~bert/courses/3134/slides/Lecture7.pdf

    def __init__(self):
        self.root = None

    def to_list(self):

        elements = self.inorder(self.root)

        return elements

    def add(self, element):
        # If tree is empty, add root
        if self.root is None:
            self.root = TreeNode(element)

        # Else, find appropriate place to add new node, add it
        else:
            # Find appropriate place to add
            current = self.root
            inserted = False
            while not inserted:
                if current.load == element:
                    inserted = True
                elif current.load < element and current.right is None:
                    parent = current
                    parent.right = TreeNode(element)
                    inserted = True
                elif current.load < element and current.right is not None:
                    current = current.right
                elif current.load > element and current.left is None:
                    parent = current
                    parent.left = TreeNode(element)
                    inserted = True
                elif current.load > element and current.left is not None:
                    current = current.left
                else:
                    print 'Error adding new element'

        return

    def contains(self, element):
        # Find node containing element
        current = self.root
        subtree_root = None

        while current is not None and subtree_root is None:
            if current.load == element:
                subtree_root = current
            elif current.load < element:
                current = current.right
            else:
                current = current.left

        return subtree_root is not None

    def remove(self, element):
        if self.root is None:
            raise IndexError('Binary Tree has no elements, cannot remove')
        else:

            # Check if element is only member of tree
            if self.root.load == element:
                self.root = None

            else:
                # Find parent
                current = self.root
                parent = None
                child_location = None
                element_node = None

                while parent is None and current is not None:
                    if current.left is not None and current.left.load == element:
                        parent = current
                        child_location = 'left'
                        element_node = parent.left
                    elif current.right is not None and current.right.load == element:
                        parent = current
                        child_location = 'right'
                        element_node = parent.right
                    elif current.load < element:
                        current = current.right
                    elif current.load > element:
                        current = current.left

                    # Tree does not contain element
                    if current is None and parent is None:
                        raise IndexError('Binary Tree does not have this element, cannot remove')

                # Create list of elements to add back in
                to_add = list()
                if element_node.left is not None:
                    to_add.extend(self.subtree(element_node.left.load))
                if element_node.right is not None:
                    to_add.extend(self.subtree(element_node.right.load))

                # Remove element's node
                if child_location == 'left':
                    parent.left = None
                elif child_location == 'right':
                    parent.right = None
                # Add everything back in
                for re_add in to_add:
                    self.add(re_add)


    def subtree(self, element):

        # Find node containing element
        current = self.root
        subtree_root = None

        while current is not None and subtree_root is None:

            if current.load == element:
                subtree_root = current
                current = None
            elif current.load > element:
                current = current.left
            elif current.load < element:
                current = current.right
            else:
                print 'Issue w/ subtree'


        # Traverse subtree
        elements = self.inorder(subtree_root)
        return elements

    def inorder(self, node):
        elements = list()

        if node is not None:

            if node.left is not None:
                elements.extend(self.inorder(node.left))

            elements.append(node.load)

            if node.right is not None:
                elements.extend(self.inorder(node.right))

        return elements

    def re_balance(self):
        # TODO
        pass


class TreeNode(object):
    def __init__(self, load):
        self.load = load
        self.left = None
        self.right = None

    def set_right(self, new_right):
        pass

    def set_list(self, new_left):
        pass
