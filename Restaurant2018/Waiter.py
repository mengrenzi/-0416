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
        return len(self.__diners)

    def printDinerStatuses(self):
        for value, key in enumerate(self.__diners):
            print("Diner", self.__diners[value].name, " is", self.__diners[value].status)

    def takeOrders(self):
        for value, key in enumerate(self.__diners):
            if key.status == "ordering":
                for valueMenu, keyMenu in enumerate(self.__menu.MENU_ITEM_TYPES):
                    self.__menu.printMenuItemsByType(keyMenu)
                    myOrder = int(input("Please choose your order(use num):"))
                    self.__diners[value].order.append(self.__menu.getMenuItem(keyMenu, myOrder - 1).name)
                self.__diners[value].printOrder()

    def ringUpDiners(self):
        for value, key in enumerate(self.__diners):
            if key.status == "paying":
                totalcost = self.__diners[value].calculateMealCost()
                print("Diner", key.name, "customer's total cost is:", totalcost)

    def removeDoneDiners(self):
        for value, key in enumerate(self.__diners):
            if key.status == "leaving":
                print("thanks for Diner", self.__diners[value].name, "who is leaving")
                self.__diners.pop(value)

    def advanceDiners(self):
        self.printDinerStatuses()
        self.takeOrders()
        self.ringUpDiners()
        self.removeDoneDiners()
        for value, key in enumerate(self.__diners):
            self.__diners[value].updateStatus()
