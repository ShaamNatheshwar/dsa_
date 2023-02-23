class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

class Stack:
    def __init__(self):
        self.linkedList = LinkedList()
    def __str__(self):
        values = [str(x.value) for x in self.linkedList]
        return '\n'.join(values)

    def isEmpty(self):
        if self.linkedList.head is None:
            return True
        else :
            return False
    def push(self, push):
        node = Node(push)
        node.next = self.linkedList.head
        self.linkedList.head = node

    def pop(self):
        if self.isEmpty():
            return 'There is no value'
        else:
            nodeValue = self.linkedList.head.value
            self.linkedList.head = self.linkedList.head.next
            return nodeValue
    def peek(self):
        if self.isEmpty():
            return 'There is no value'
        else:
            nodeVale = self.linkedList.head.value
            return nodeVale
    def delete(self):
        self.linkedList.head = None

        
            
customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)

print(customStack.peek())