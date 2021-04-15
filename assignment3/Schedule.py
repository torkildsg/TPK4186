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
        self.currentSchedule = []
        self.allScheduledEvents = []
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

    def getCurrentSchedule(self):
        return self.currentSchedule
    
    def getAllScheduledEvents(self):
        return self.allScheduledEvents
    
    def popFirstEvent(self):
        return self.currentSchedule.pop(0)
    
    def isCurrentScheduleEmpty(self):
        return len(self.currentSchedule)==0
    
    def scheduleEvent(self, type, date, batch, buffer, task):
        self.eventNumber += 1
        event = Event(type, self.eventNumber, date)
        event.setBatch(batch)
        event.setBuffer(buffer)
        event.setTask(task)
        if event not in self.currentSchedule:
            position = 0
            while position < len(self.currentSchedule):
                otherEvent = self.currentSchedule[position]
                if otherEvent.getDate() > event.getDate():
                    break
                position += 1
            self.currentSchedule.insert(position, event)
            self.allScheduledEvents.append(event) # Kan slettes
        return event
    
    # MÅ FIKSE DETTE: If two input buffers of a machine contains
    # batches, the machine has to choose which task to perform

    def scheduleBufferToTask(self, task): # Muligens splitte opp batcher for å kjøre gjennom halve batcher
        
        if task.getName() == 'End':
            return False
        else:
            incomingBuffer = task.getFirstOfIncomingBuffers() # the incoming buffer to this task
            outgoingBuffer = task.getFirstOfOutgoingBuffers() # The outgoing buffer to this task
            capOutgoingBuffer = outgoingBuffer.getAvailableCap() # Available capacity that the outgoing buffer has
            incomingBatch = incomingBuffer.getFirstBatchInQueue() # The batch coming in from the incoming buffer
            numOfWafersIncomingBatch = incomingBatch.getNumOfWafers() # Number of wafers that the incoming batch contains
        
            # En maskin kan bare utføre en task av gangen - DET ER LAGT TIL 
            if capOutgoingBuffer >= numOfWafersIncomingBatch:
                self.currentDate += int(1)
                return self.scheduleEvent(Event.BUFFER_TO_TASK, int(self.currentDate-1), incomingBatch, incomingBuffer, task) 
            else: return False
    
    # Finne ut om en TASK kan holde på en batch selvom output_buffer er full? Nei det kan den ikke. 
    def scheduleTaskToBuffer(self, buffer):
        sourceTask = buffer.getSourceTask() # The predecessor task to this buffer
        incomingBatch = sourceTask.getHoldingBatch() # The batch that the task is holding, and we want to enter the buffer
        

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
    