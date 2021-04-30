"""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """

from Plant import Plant
from Event import Event
from Buffer import Buffer
from Batch import Batch
from Task import Task
class Schedule:
    def __init__(self, plant):
        self.plant = plant
        self.currentSchedule = []
        self.currentDate = 0
        self.eventNumber = 0
    
    def resetSchedule(self):
        self.currentDate = 0
        self.allScheduledEvents = []
        self.currentSchedule = []
        return True

    def getPlant(self):
        return self.plant

    def getCurrentDate(self):
        return self.currentDate

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
                if otherEvent.getDate() >= event.getDate():
                    break
                position += 1
            self.currentSchedule.insert(position, event)
        return event

    def scheduleBufferToTask(self, task): 
        if task.getName() == 'End':
            return False
        else:
            incomingBuffer = task.getFirstOfIncomingBuffers() # the incoming buffer to this task
            outgoingBuffer = task.getFirstOfOutgoingBuffers() # The outgoing buffer to this task
            capOutgoingBuffer = outgoingBuffer.getAvailableCap() # Available capacity that the outgoing buffer has
            incomingBatch = incomingBuffer.getFirstBatchInQueue() # The batch coming in from the incoming buffer
            numOfWafersIncomingBatch = incomingBatch.getNumOfWafers() # Number of wafers that the incoming batch contains
         
            if capOutgoingBuffer >= numOfWafersIncomingBatch:
                date = int(self.currentDate + task.getLoadTime())
                return self.scheduleEvent(Event.BUFFER_TO_TASK, date, incomingBatch, incomingBuffer, task) 
            else: return False
    
    
    def scheduleTaskToBuffer(self, buffer):
        sourceTask = buffer.getSourceTask() # The predecessor task to this buffer
        incomingBatch = sourceTask.getHoldingBatch() # The batch that the task is holding, and we want to enter the buffer
        
        if (incomingBatch not in buffer.getHistoryQueueOfBatches()) and incomingBatch != None: 
            date = int(self.currentDate + (incomingBatch.getNumOfWafers() * sourceTask.getProcessTime()) + sourceTask.getUnloadTime())
            self.scheduleEvent(Event.TASK_TO_BUFFER, date, incomingBatch, buffer, sourceTask)
        else: return False 