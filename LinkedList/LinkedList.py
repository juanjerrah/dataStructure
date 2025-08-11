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
    
    def pop_first(self):
        if self.length == 0:
            return None
        
        curr = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        self.length -= 1
        return curr.value

    def remove(self, index):
        if self.length - 1 < index:
            return None
        
        if index == 0:
            head = self.head
            self.pop_first()
            return head.value
        
        if self.length - 1 == index:
            tail = self.tail
            self.pop()
            return tail.value
        
        count = 0
        to_remove = self.head
        pre = self.head
        while to_remove:
            if count == index:
                pre.next = to_remove.next
                break
            else:
                count += 1
                pre = to_remove
                to_remove = to_remove.next
        
        self.length -= 1
        return to_remove.value
        


ll = LinkedList(1)
ll.append(2)
ll.append(6)
ll.append(3)
ll.prepend(9)

print("Before")
ll.print()
print("After remove", ll.remove(3))
ll.print()


