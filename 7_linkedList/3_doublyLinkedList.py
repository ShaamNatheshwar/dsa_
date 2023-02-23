class Node():
    def __init__(self, value = None):
        self.next = None
        self.value = value
        self.prev = None

class CircularList():
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

    def createCll(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        node.next = None
        node.prev = None
        return 'we have created a circular list'
    
    def insert(self, location, value):
        if self.head is None:
            print ('There is no head')
        else:
            newNode = Node(value)
            if location == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.next = self.head
                self.head = newNode
            elif location == 1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                if index < location -1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                tempNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode
    
    def traverseDLL(self):
        if self.head is None:
            print("There is not any element to traverse")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                if tempNode == self.tail.next:
                    break
    
    def search(self, value):
        if self.head is None:
            print('There is no such value')
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == value:
                    return value
                tempNode = tempNode.next
            return "The node doesnot exit"
    
    def deleteNode(self, location):
        if self.head is None:
            print('There is no value')
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode + 1
                    index += 1
                tempNode.next = tempNode.next.next
                tempNode.next.prev = tempNode
            print('Deleted successfully')

    def deleteAll(self):
        if self.head is None:
            print('There is No head')
        else:
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
            print('Deleted')

double = CircularList()
double.createCll(5)
double.insert(0,0)
double.insert(2,1)
double.insert(6,2)
print(double.search(5))
# double.traverseDLL()
print([node.value for node in double]) 
