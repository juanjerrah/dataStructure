class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.node = Node(value)
        self.head = self.node
        self.tail = self.node
        self.length = 1
    
    def print(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

    def append(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1


ll = LinkedList(1)
ll.append(2)
ll.print()

