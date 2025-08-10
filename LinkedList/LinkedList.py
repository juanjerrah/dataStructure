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
        return True

    def pop(self):
        if self.length == 0:
            return None
        
        curr = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            pre = None
            while curr.next is not None:
                pre = curr
                curr = curr.next
            
            self.tail = pre
            pre.next = None
        self.length -= 1
        return curr.value

    def prepend(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True


ll = LinkedList(1)
ll.append(2)
ll.append(6)
ll.append(3)
ll.prepend(9)
print("Before pop")
ll.print()
print("After pop")
print("Removido: ", ll.pop())
ll.print()


