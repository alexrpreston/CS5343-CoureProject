from PCBQueue import processQueue, PCB
import os

class userInterface:
    def __init__(self):
        self.queue = processQueue()
        self.fh = fileHandler()
        print("Welcome to the PCB Queue Simulator.")

    def printMainMenu(self):
        print("=======================")
        print("1. Load PCB Data From File")
        print("2. Manually Input PCB's")
        print("3. Print proccess queue")
        print("4. Delete a PCB")
        print("5. Exit")
        print("========================")
        print("What would you like to do: ", end="")
        choice = int(input())
        if choice == 5:
            quit()
        while choice > 4 or choice < 1:
            print("Invalid Input")
            print("What would you like to do: ", end="")
            choice = int(input())
        if choice == 1:
            self.loadDataFromFile()
        elif choice == 2:
            print("Please input data in the format PID, arrival_time, burst_time, priority")
            print("An example of the required format: 2760, 1, 16, 1")
            self.inputData()
        elif choice == 3:
            self.printQueue()
        elif choice == 4:
            print("Please enter the PID of the PCB you want to delete.")
            print("If no PCB is entered the first one will be removed.")
            self.deletePCB()


    def loadDataFromFile(self):
        print("Files need to be in the format PID, arrival_time, burst_time, priority")
        print("Comma seperated for each field and newlines seperating each PCB")
        print("An example of the required format: 2760, 1, 16, 1")
        print("(Files need to be .txt)")
        print("Enter name of file: ", end="")
        fileName = input()
        while os.path.exists(fileName) is False:
            print("No such file or directory: ", fileName)
            print("Enter name of file: ", end="")
            fileName = input()
        pcbData = self.fh.parseInputFile(fileName)
        for row in pcbData:
            PID, arrival_time, burst_time, priority = row
            self.queue.addPCB(PCB(PID, priority))
        print(str(len(pcbData)) + " Process Control Blocks loaded and appended to the queue.")
        self.printMainMenu()

    def inputData(self):
        print("Enter PCB data: ", end="")
        inputs = input().split(", ")
        while len(inputs) != 4:
            print("Error. We were expecting four arguements but recieved", len(inputs), "\nTry Again: ", end="")
            inputs = input().split(", ")
        PID, arrival_time, burst_time, priority = inputs
        self.queue.addPCB(PCB(PID, priority))
        print("Would you like to add another PCB? (Y/N): ", end=" ")
        addAnotherPCB = input()
        if addAnotherPCB.lower() == "y" or addAnotherPCB.lower() == "yes":
            self.inputData()
        else:
            self.printMainMenu()
        

    def printQueue(self):
        self.queue.printProcessQueue()
        self.printMainMenu()

    def deletePCB(self):
        print("PID: ", end=" ")
        PID = input()
        if PID is None: 
            self.queue.deletePCB()
        else:
            self.queue.deletePCB(PID)
        print("Would you like to delete another PCB? (Y/N): ", end=" ")
        deleteAnotherPCB = input()
        if deleteAnotherPCB.lower() == "y" or deleteAnotherPCB.lower() == "yes":
            self.deletePCB()
        else:
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
