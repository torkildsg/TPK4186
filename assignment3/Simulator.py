"""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """

from Schedule import Schedule
from Plant import Plant
from Event import Event

class Simulator:
    def __init__(self, plant):
        self.plant = plant
        self.executionTime = dict() # Key: batchCode, value: total time for all tasks
        self.execution = []
        self.eventNumber = 0
    
    def getExecution(self):
        return self.execution
    
    def getExecutionTime(self):
        return self.executionTime
    
    def simulationLoop(self, schedule):
        while schedule.getSchedule():
            event = schedule.popFirstEvent()
            self.execution.append(event)
            self.executeEvent(event, schedule)
    
    def executeEvent(self, thisEvent, schedule):
        self.currentDate = thisEvent.getDate()
        thisBatch = thisEvent.getBatch()
        thisTask = thisEvent.getTask()
        outgoingBuffer = thisTask.getOutgoingBuffer()
        incomingBuffer = thisTask.getIncomingBuffer()
        thisBuffer = thisEvent.getBuffer()
        if thisEvent.getType() == Event.BATCH_TO_TASK:
            schedule.scheduleBatchToTask(thisTask)
            duration = self.plant.taskServesBatch(thisBatch, thisTask)
            self.executionTime[thisBatch.getBatchCode()] += duration
            #schedule.scheduleBatchToBuffer(thisBuffer)
        elif thisEvent.getType() == Event.BATCH_TO_BUFFER:
            schedule.scheduleBatchToBuffer(thisBuffer)
            self.plant.enqueueBatchIntoBuffer(thisBatch, thisBuffer)
        print(self.executionTime)
        

            
            


