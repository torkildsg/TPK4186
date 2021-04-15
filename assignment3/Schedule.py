"""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """

from Plant import Plant
from Event import Event
from Buffer import Buffer
from Batch import Batch
from Task import Task
from Printer import Printer
import sys

class Schedule:
    def __init__(self, plant):
        self.plant = plant
        self.schedule = []
        self.finalSchedule = []
        self.currentDate = 1
        self.batches = []
        self.eventNumber = 0
    
    # Kan muligens slettes
    def decreaseEventNum(self):
        self.eventNumber -= int(1)
    
    #Kan muligens slettes
    def decreaseCurrentDate(self):
        self.currentDate -= int(1)
    
    def getPlant(self):
        return self.plant

    def getSchedule(self):
        return self.schedule
    
    def getFinalSchedule(self):
        return self.finalSchedule
    
    def popFirstEvent(self):
        return self.schedule.pop(0)
    
    def isScheduleEmpty(self):
        return len(self.schedule)==0
    
    def scheduleEvent(self, type, date, batch, buffer, task):
        self.eventNumber += 1
        event = Event(type, self.eventNumber, date)
        event.setBatch(batch)
        event.setBuffer(buffer)
        event.setTask(task)
        if event not in self.schedule:
            position = 0
            while position < len(self.schedule):
                otherEvent = self.schedule[position]
                if otherEvent.getDate() > event.getDate():
                    break
                position += 1
            self.schedule.insert(position, event)
            self.finalSchedule.append(event) # Kan slettes
        return event
    
    # MÅ FIKSE DETTE: If two input buffers of a machine contains
    # batches, the machine has to choose which task to perform

    def scheduleBufferToTask(self, task): # Muligens splitte opp batcher for å kjøre gjennom halve batcher
        
        if task.getName() == 'End': 
            return False
        else:
            capOutgoingBuffer = task.getFirstOfOutgoingBuffers().getAvailableCap()
            incomingBatch = task.getFirstOfIncomingBuffers().getFirstBatchInQueue()
            numOfWafersIncomingBatch = incomingBatch.getNumOfWafers()
            incomingBuffer = task.getFirstOfIncomingBuffers()
            outgoingBuffer = task.getFirstOfOutgoingBuffers()
        
            # En maskin kan bare utføre en task av gangen, må legges til
            if capOutgoingBuffer >= numOfWafersIncomingBatch:
                self.currentDate += int(1)
                return self.scheduleEvent(Event.BUFFER_TO_TASK, int(self.currentDate-1), incomingBatch, incomingBuffer, task) 
            else: return False
    
    # Finne ut om en TASK kan holde på en batch selvom output_buffer er full? Nei det kan den ikke. 
    def scheduleTaskToBuffer(self, buffer):
        sourceTask = buffer.getSourceTask()
        incomingBatch = sourceTask.getHoldingBatch()
        
        evv = False
        

        if incomingBatch != None and incomingBatch not in buffer.getHistoryQueueOfBatches(): #and buffer.getTargetTask().getName() == "Task2":
            # ----
            """
            historyList = []
            for r in buffer.getHistoryQueueOfBatches():
                    historyList.append(r.getBatchCode())
            
            print("historylist: ")
            print(historyList) 

            print("incoming batch: "+str(incomingBatch.getBatchCode()))

            listOfBatchCodesInBuffer = []
            for e in buffer.getQueueOfBatches():
                listOfBatchCodesInBuffer.append(e.getBatchCode())
            print("List of batchcodes in outbuffer: ")
            print(listOfBatchCodesInBuffer)
            print("\n NEW_Iteration \n")"""
            
            # ----

            self.currentDate += int(1)
            evv = self.scheduleEvent(Event.TASK_TO_BUFFER, int(self.currentDate-1), incomingBatch, buffer, sourceTask)
            return evv
        else: return False # Denne linjen kan kanskje slettes
    