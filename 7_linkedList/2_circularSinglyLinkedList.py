class Node():
    def __init__(self, value = None):
        self.value = value
        self.next = None

class Circular():
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head

        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break
    
    def createSll(self, value):
        node = Node(value)
        node.next = node
        self.tail = node
        self.head = node
        return 'CircularLinkedListCreated'

    def insertScll(self, value, location):
        newNode = Node(value)
        if self.head is None:
            return 'There is no value'
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
                
            elif location == 1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode

            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index+=1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
            return 'The node is created'
    def traversal(self):
        if self.head is None:
            print('There is no linked list')
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break

    def search(self, value):
        if self.head is None:
            print('There is no value')
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == value:
                    return value
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    return 'There is no such value'
    def deleteNode(self, location):
        if self.head is None:
            print('There is no linked list')
        else:
            if location == 0:
                if self.head == self.tail:
                    self.tail.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head

            elif location == 1:
                if self.head == self.tail:
                    self.tail.next = None
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = self.head
                    self.tail = node
            else:
                tempNode= self.head
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


circularScll = Circular()
circularScll.createSll(0)
circularScll.insertScll(1,1)
circularScll.insertScll(2,1)
circularScll.insertScll(3,1)

circularScll.traversal()
print(circularScll.search(3))
print([node.value for node in circularScll]) 