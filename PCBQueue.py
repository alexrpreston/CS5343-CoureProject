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
    def addPCB(self, PCB):
        self.queue.insert(PCB)
    def deletePCF(self, PID):
        current = self.queue.head
        previous = None
        found = False
        while current and found is False:
            if current.getData().getProcessID() == PID:
                found = True
            else:
                previous = current
                current = current.getNext()
        if current is None:
            raise ValueError("PID not in list")
        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
    
    def printProcessQueue(self):
        head = self.queue.head
        while head.getNext():
            print(("====================="))
            print("= PID: " + str(head.getData().getProcessID()))
            print("= Priority: " + str(head.getData().getPriorty()))
            print("=====================")
            print("  |")
            print("  |")
            print("  ▼")
            head = head.getNext()
            if head.getNext() is None:
                print(("====================="))
                print("= PID: " + str(head.getData().getProcessID()))
                print("= Priority: " + str(head.getData().getPriorty()))
                print("=====================")



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

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.getData() == data:
                found = True
            else:
                previous = current
                current = current.getNext()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


readyQueue = processQueue()
newPCB = PCB(8356, 1)
readyQueue.addPCB(newPCB)
newPCB = PCB(2346, 2)
readyQueue.addPCB(newPCB)
newPCB = PCB(1356, 2)
readyQueue.addPCB(newPCB)
newPCB = PCB(9776, 3)
readyQueue.addPCB(newPCB)
print("Ready Queue")
readyQueue.printProcessQueue()
readyQueue.deletePCF(1356)
readyQueue.deletePCF(9776)
print("\n\nReady Queue")
readyQueue.printProcessQueue()