class Node(object):
    def __init__(self, data, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous

    def __repr__(self):
        return "<Node {}>".format(self.data)


class DoublyLinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.tail = None

    def push(self, data):
        """Add node to front of DLL"""

        new_node = Node(data)

        if self.head is None:
            self.head = self.tail = new_node

        else:
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node
            self.head.previous = None

    def pop(self):
        """Remove node from end of DLL"""

        if self.tail:
            if self.tail.previous:
                self.tail = self.tail.previous
                if self.tail.previous is None:
                    self.head = self.tail
                self.tail.next = None

            elif not self.tail.previous:
                self.head = None
                self.tail = None

        else:
            return "No node to pop"

    def insert_before(self, node, data):
        """Insert new node with data before node"""

        new_node = Node(data)
        new_node.next = node

        if not node.previous: #if node is head
            node.previous = new_node
            self.head = new_node

        else:
            node.previous.next = new_node
            node.previous = new_node

    def insert_after(self, node, data):
        """Insert new node with data after node"""

        new_node = Node(data)
        new_node.previous = node

        if not node.next: #if node is tail
            node.next = new_node
            new_node.next = None

        else:
            new_node.next = node.next
            node.next.previous = new_node
            node.next = new_node

    def remove(self, node):
        """Remove node and connect previous and next nodes together"""

        if node.next and node.previous: #we're removing node that is not head or tail
            next_node = node.next
            previous_node = node.previous

            previous_node.next = next_node
            next_node.previous = previous_node

            node.next = node.previous = None #Make this node free standing

        elif node.next: #we're removing the current head node
            self.head = node.next

        elif node.previous: #we're removing current last node
            self.tail = node.previous
            self.tail.next = None





# Creating DLL: B -> C
b = Node('b')
c = Node('c')
b.next = c
c.previous = b
c.next = None
dll = DoublyLinkedList()

dll.head = b
dll.tail = c
dll.push('a') # Push node A to front of DLL, make it head
# DLL: A -> B -> C

dll.pop() # Pop node C
# DLL: A -> B

dll.remove(b)
# DLL: A

#dll.insert_after(dll.head, "x")
#dll.insert_before(dll.head, "y")










