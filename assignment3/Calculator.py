"""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """

from Batch import Batch
from Buffer import Buffer
from Task import Task
from Machine import Machine
import math
import statistics
class Calculator:
    
    def minValue(self, values):
        return min(values)

    def maxValue(self, values):
        return max(values)

    def sumValue(self, values):
        return sum(values)

    def meanValue(self, values):
        return statistics.mean(values)