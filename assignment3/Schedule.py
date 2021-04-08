"""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """

from Plant import Plant
from Event import Event
from Buffer import Buffer
from Task import Task

class Schedule:
    def __init__(self, plant):
        self.plant = plant
        self.schedule = []
        self.currentDate = 0
        self.batches = []
        self.eventNumber = 0
    
    def getSchedule(self):
        return self.schedule
    
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
        # self.printer.PrintEvent(event, sys.stdout)
        return event
    
    def scheduleBatchToTask(self, task): # Muligens splitte opp batcher for å kjøre gjennom halve batcher
        capOutgoingBuffer = task.getOutgoingBuffer().getAvailableCap()
        numOfWafersIncomingBatch = task.getIncomingBuffer()[0].getNumOfWafers()
        incomingBatch = task.getIncomingBuffer()[0]
        incomingBuffer = task.getIncomingBuffer()
        outgoingBuffer = task.getOutgoingBuffer()

        # En maskin kan bare utføre en task av gangen, må legges til
        if capOutgoingBuffer >= numOfWafersIncomingBatch:
            self.scheduleEvent(Event.BATCH_TO_TASK, self.currentDate, incomingBatch, incomingBuffer, task) # bør heller kalle på 
            self.currentDate += int(1)
            self.scheduleBatchToBuffer(outgoingBuffer)
        else:
            return str("Could not schedule, outgoing_buffer does not have space for this batch.")
    # Finne ut om en TASK kan holde på en batch selvom output_buffer er full? Send mail
    def scheduleBatchToBuffer(self, buffer):
        incomingTask = buffer.getSourceTask()
        incomingBatch = incomingTask.getHoldingBatch()
        if incomingBatch:
            self.scheduleEvent(Event.BATCH_TO_BUFFER, self.currentDate, incomingBatch, buffer, incomingTask)
            self.currentDate += int(1)



        