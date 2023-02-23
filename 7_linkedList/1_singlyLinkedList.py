class Node():
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    
    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
    
    def traversal(self):
        if self.head is None:
            print('There is no linked list')
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next
    
    def searchSll(self, value):
        if self.head is None:
            print('There is no linked list')
        else:
            node = self.head
            while node is not None:
                if node.value == value:
                    return node.value
                node = node.next
            return 'There is no such value'
    
    def deleteNode(self, location):
        if self.head == None:
            print('There is no linked list')
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            
            else:
                tempNode = self.head
                index = 0
                while index < location-1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next

    def deleteAll(self):
        if self.head is None:
            print('There is no linked list')
        else:
            self.head = None
            self.tail = None
            

singlyLinkedList = LinkedList()
singlyLinkedList.insertSLL(1,1)
singlyLinkedList.insertSLL(2,1)
# Node1 = Node(1)
# Node2 = Node(2)
# singlyLinkedList.deleteNode(1)
# singlyLinkedList.head = Node1
# singlyLinkedList.head.next = Node2
# singlyLinkedList.tail = Node2
print([node.value for node in singlyLinkedList])
# singlyLinkedList.traversal()
# print(singlyLinkedList.searchSll(3))
        

        