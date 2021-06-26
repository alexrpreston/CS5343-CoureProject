from PCBQueue import processQueue, PCB

class userInterface:
    def __init__(self):
        self.queue = processQueue()
        self.fh = fileHandler()

    def printMainMenu(self):
        print("=======================")
        print("1. Load PCB Data From File")
        print("2. Manually Input PCB's")
        print("3. Print proccess queue")
        print("4. Exit")
        print("========================")
        print("What would you like to do: ", end="")
        choice = int(input())
        if choice == 4:
            quit()
        while choice > 3 or choice < 1:
            print("Invalid Input")
            print("What would you like to do: ", end="")
            choice = int(input())
        if choice == 1:
            self.loadDataFromFile()
        elif choice == 2:
            self.inputData()
        elif choice == 3:
            self.printQueue()


    def loadDataFromFile(self):
        print("Files need to be in the format PID, arrival_time, burst_time, priority")
        print("Comma seperated for each field and newlines seperating each PCB")
        print("(Files need to be .txt)")
        print("Enter name of file: ", end="")
        fileName = input()
        pcbData = self.fh.parseInputFile(fileName)
        for row in pcbData:
            PID, arrival_time, burst_time, priority = row
            self.queue.addPCB(PCB(PID, priority))
        print(str(len(pcbData)) + " Process Control Blocks loaded and appended to the queue.")
        self.printMainMenu()

    def inputData(self):
        print("Please input data in the format PID, arrival_time, burst_time, priority")
        print("Type exit to exit")
        pass

    def printQueue(self):
        self.queue.printProcessQueue()
        self.printMainMenu()

class fileHandler:
    def __init__(self):
        pass

    def parseInputFile(self, fileName):
        pcbData = []
        inputFile = open(fileName, "r")
        for line in inputFile:
            data = self.cleanData(line.split(", "))
            pcbData.append(data)
        return pcbData

    def cleanData(self, data):
        for i in range(len(data)):
            data[i] = data[i].strip()
            data[i] = int(data[i])
        return data
