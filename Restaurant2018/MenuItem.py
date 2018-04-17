# MenuItem.py
# Goal: This class will represent a single item that a diner can order from the restaurant’s menu

class MenuItem(object):
    def __init__(self, name, type, price, description):
        self.__name = name
        self.__type = type
        self.__price = price
        self.__description = description

    def __str__(self):
        message = self.__name + '(' + self.__type + '):' + '$' + self.__price + "\n" + self.__description
        return message
