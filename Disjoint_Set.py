class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
        self.tail = None
    def display(self):
        i = self.head()
        while(i!=None):
            print(i.value)
            i = i.next

class LinkedListNode:
    def __init__(self,value):
        self.value = value
        self.list = None
        self.next = None
    

class Set(LinkedList):
    def __init__(self,identifier):
        super().__init__()
        self.identifier = identifier
    def getIdentifier(self):
        return self.identifier

def makeSet(val):
    s = Set()
    s.head = LinkedListNode(val)
    s.tail = s.head
    s.head.list = s
    s.length = 1
    s.identifier = val
    return s

def findSet(x:LinkedListNode):
    return x.list

def Union(x:LinkedListNode,y:LinkedListNode):
    base = x.list if x.list.length > y.list.length else y.list
    attatchment = x.list if base == y.list else x.list
    base.tail.next = attatchment.head
    i = attatchment.head
    while(i != None):
        i.list = base
        i = i.next
    base.length += attatchment.length
    base.tail = attatchment.tail

