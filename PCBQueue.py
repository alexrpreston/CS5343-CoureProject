class PCB:
    def __init__(self, proccessID, arrivalTime, burstTime, priorty):
        self.processID = proccessID
        self.arrivalTime = arrivalTime
        self.burstTime = burstTime
        self.priorty = priorty

    def getProcessID(self):
        return self.processID

    def getPriorty(self):
        return self.priorty

    def getBurstTime(self):
        return self.burstTime

    def getArrivalTime(self):
        return self.arrivalTime

class processQueue:
    def __init__(self):
        self.queue = LinkedList()
    def getHeadPCB(self):
        return self.queue.head
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
            print("= Arrival Time: " + str(head.getData().getArrivalTime()))
            print("= Burst Time: " + str(head.getData().getBurstTime()))
            print("= Priority: " + str(head.getData().getPriorty()))
            print("=====================")
            print("        |")
            print("        |")
            print("        ▼")
            head = head.getNext()
            if head.getNext() is None:
                print(("====================="))
                print("= PID: " + str(head.getData().getProcessID()))
                print("= Arrival Time: " + str(head.getData().getArrivalTime()))
                print("= Burst Time: " + str(head.getData().getBurstTime()))
                print("= Priority: " + str(head.getData().getPriorty()))
                print("=====================")
        print("\n\n\n")

class schedulers():
    def shortestJobFirst(self, proccessQueue):
        def arrivalTime(elem):
            return elem.getArrivalTime()
        time = 0
        waitingTime = []
        sortedQueue = []
        #sort processes according to arrival time
        head = proccessQueue.queue.head
        while head:
            sortedQueue.append(head.getData())
            head = head.getNext()
        sortedQueue.sort(key=arrivalTime)
        for pcb in sortedQueue:
            print(pcb.getPriorty(),pcb.getBurstTime(), pcb.getArrivalTime())
        #dequeue PCBs to calculate wait time for each process
        time = sortedQueue[0].getArrivalTime()
        while sortedQueue:
            shortestBurstPCB = None
            shortestBurstNum = float("inf")
            for PCB in sortedQueue:
                if PCB.getArrivalTime() <= time and PCB.getBurstTime() < shortestBurstNum:
                    shortestBurstPCB = PCB
                    shortestBurstNum = PCB.getBurstTime()
            if time < shortestBurstPCB.getArrivalTime():
                time += shortestBurstPCB.getArrivalTime()
            waitingTime.append(time)
            time += shortestBurstPCB.getBurstTime()
            del sortedQueue[sortedQueue.index(shortestBurstPCB)]
        return sum(waitingTime) / len(waitingTime)


    def nonPreemptivePriorty(self, proccessQueue):
        def arrivalTime(elem):
            return elem.getArrivalTime()
        time = 0
        waitingTime = []
        sortedQueue = []
        #sort processes according to arrival time
        head = proccessQueue.queue.head
        while head:
            sortedQueue.append(head.getData())
            head = head.getNext()
        sortedQueue.sort(key=arrivalTime)
        #dequeue PCBs to calculate wait time for each process
        for pcb in sortedQueue:
            print(pcb.getPriorty(),pcb.getBurstTime(), pcb.getArrivalTime())
        time = sortedQueue[0].getArrivalTime()
        while sortedQueue:
            highestPriortyPCB = None
            highestPriortyNum = float("inf")
            for PCB in sortedQueue:
                if PCB.getArrivalTime() <= time and PCB.getPriorty() < highestPriortyNum:
                    highestPriortyPCB = PCB
                    highestPriortyNum = PCB.getPriorty()
            if time < highestPriortyPCB.getArrivalTime():
                time += highestPriortyPCB.getArrivalTime()
            waitingTime.append(time)
            time += highestPriortyPCB.getBurstTime()
            del sortedQueue[sortedQueue.index(highestPriortyPCB)]
            for pcb in sortedQueue:
                print(pcb.getPriorty(), end = " ")
            print()
        print(waitingTime)
        return sum(waitingTime) / len(waitingTime)

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
