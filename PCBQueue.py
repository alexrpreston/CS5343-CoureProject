class PCB:
    def __init__(self, proccessID, priorty):
        self.processID = proccessID
        self.priorty = priorty

    def getProcessID(self):
        return self.processID

    def getPriorty(self):
        return self.priorty

class processQueue:
    def __init__(self):
        self.queue = LinkedList()
    def addPCB(self, PCB, position=None):
        if position is None:
            self.queue.insert(PCB)
        else:
            newNode = Node(PCB)
            if position == 0:
                temp = self.queue.head
                newNode.setNext(temp)
                self.queue.head = newNode
            else:
                i = 0
                head = self.queue.head
                while head.getNext():
                    i += 1
                    if i == position:
                        temp = head
                        newNode.setNext(temp.getNext())
                        head.setNext(newNode)
                        break
                    head = head.getNext()
                raise ValueError("Insertion position is beyond length of list")

    def deletePCB(self, PID=None):
        if PID is None:
            self.queue.head = self.queue.head.getNext()
        else:
            current = self.queue.head
            previous = None
            found = False
            while current and found is False:
                if int(current.getData().getProcessID()) == int(PID):
                    found = True
                else:
                    previous = current
                    current = current.getNext()
            if current is None:
                raise ValueError("PCB with PID not in list")
            if previous is None:
                self.queue.head = current.getNext()
            else:
                previous.setNext(current.getNext())
    
    def printProcessQueue(self):
        head = self.queue.head
        print("\n\n\nProcess Queue")
        while head.getNext():
            print(("====================="))
            print("= PID: " + str(head.getData().getProcessID()))
            print("= Priority: " + str(head.getData().getPriorty()))
            print("=====================")
            print("        |")
            print("        |")
            print("        ▼")
            head = head.getNext()
            if head.getNext() is None:
                print(("====================="))
                print("= PID: " + str(head.getData().getProcessID()))
                print("= Priority: " + str(head.getData().getPriorty()))
                print("=====================")
        print("\n\n\n")


class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setNext(self, next):
        self.next = next

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            head = temp = self.head
            while head.getNext():
                head = head.getNext()
            head.setNext(newNode)
            self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.getNext()
        return count

    def printList(self):
        head = self.head
        while head.getNext():
            print((repr(head.getData()) + " --> "), end='')
            head = head.getNext()
            if head.getNext() is None:
                print(repr(head.getData()))

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return current
