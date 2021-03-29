"""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """

from Batch import Batch
from Buffer import Buffer
from Task import Task
from Machine import Machine
import math

class Calculator:

    """def ResetDates(self, plant):
        for task in plant.getAllTasksEvents():
            task.setEarlyStartDate(-1)
            task.setEarlyCompletionDate(-1)
            task.setLateStartDate(-1)
            task.setLateCompletionDate(-1)
    
    def calculateDates(self, plant):
        self.ResetDates(plant)
        self.calculateEarlyDates(plant)
        self.calculateLateDates(plant)
    
    def calculateEarlyDates(self, plant):
        candidates = []
        for task in plant.getAllTasksEvents():
            if not task.getIncomingBuffers():
                candidates.append(task)
        while candidates:
            candidate = self.lookForTaskWithAllPreceedingTasksCalculated(candidates)
            candidates.remove(candidate)
            print("Current task: {0:s}".format(candidate.getName()))
            earlyStartDate = 0
            for buffer in candidate.getIncomingBuffers():
                otherTask = buffer.getSourceTask()
                if otherTask.getEarlyCompletionDate() > earlyStartDate:
                    earlyStartDate = otherTask.getEarlyCompletionDate()
            candidate.setEarlyStartDate(earlyStartDate)
            candidate.setEarlyCompletionDate(earlyStartDate + candidate.getDuration())
            for buffer in candidate.getOutgoingBuffers():
                otherTask = buffer.getTargetTask()
                if not otherTask in candidates:
                    candidates.append(otherTask)

    def lookForTaskWithAllPreceedingTasksCalculated(self, candidates):
        for candidate in candidates:
            allCalculated = True
            for buffer in candidate.getIncomingBuffers():
                otherTask = buffer.getSourceTask()
                if otherTask.getEarlyCompletionDate() == -1:
                    allCalculated = False
                    break
            if allCalculated:
                return candidate
        return None 
            

    def calculateLateDates(self, plant):
        pass"""