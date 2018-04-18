# Diner.py
# Goal: This class represents one of the diners at the restaurant and keeps tracks of their status and meal.

class Diner(object):
    STATUS = ["seated", "ordering", "eating", "playing", "leaving"]

    def __init__(self, name):
        self.__name = name
        self.__order = []
        self.__status = self.STATUS[0]

    def __str__(self):
        return 'Diner {p.name} is currently {p.status}\n'.format(p=self)

    __repr__ = __str__

    def updateStatus(self):
        count = 0
        for x in self.STATUS:
            if x == self.__status:
                print(self.STATUS[count + 1])
            count += 1

    def printOrder(self):
        print(self.__order)

    def calculateMealCost(self):
        totalcost = 0
        for item in self.__order:
            totalcost += item[1]
        return totalcost

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self, value):
        self.__order = value

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
