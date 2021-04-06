""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """

class Event:
    
    def __init__(self, type, date):
        self.type = type
        self.date = date
    
    def getType(self):
        return self.type
    
    def setType(self, type):
        self.type = type
    
    def getDate(self):
        return self.date
    
    
