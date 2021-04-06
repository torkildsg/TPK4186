"""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """

class Simulator:
    def __init__(self, plant):
        self.plant = plant
        self.schedule = []
    
    def getSchedule(self):
        return self.schedule
    
    def isScheduleEmpty(self):
        return len(self.schedule)==0
    
    def popFirstEvent(self):
        return self.schedule.pop(0)
    
    def insertEvent(self, event):
        if event not in self.schedule:
            position = 0
            while position < lene(self.schedule):
                otherEvent = self.schedule[position]
                if otherEvent.getDate() > event.getDate():
                    break
                position += 1
            self.schedule.insert(event)
    
    # Et event hvor man flytter en batch fra buffer til task til buffer
    def newEvent(self, type, batch, buffer):
        event = Event(type, date)
        event.set
    