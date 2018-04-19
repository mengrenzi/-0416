# Waiter.py
# Goal: This class will represent the restaurant's waiter. The waiter maintains a list of the dines it is currently taking care of, and progresses them through the different stages of the restaurant. The waiter in the simulation will repeat multiple cycles of attending to the diners. In each cycle, the waiter will seat a new diner, if one arrives, take any diners' orders if needed, and give diners their bill, according to each diner's status.

from Menu import Menu
from Diner import Diner

class Waiter(object):
    def __init__(self, Menu):
        self.__diners = []
        self.__menu = Menu

    def addDiner(self, Diner):
        self.__diners.append(Diner)

    def getNumDiners(self):
        return len(self.__diner)

    def printDinerStatuses(self):
        pass

    def takeOrders(self):
        pass

    def ringUpDiners(self):
        pass

    def removeDoneDiners(self):
        pass

    def advanceDiners(self):
        pass
