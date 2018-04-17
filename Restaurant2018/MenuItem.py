# MenuItem.py
# Goal: This class will represent a single item that a diner can order from the restaurant’s menu

class MenuItem(object):
    def __init__(self, name, type, price, description):
        self.__name = name
        self.__type = type
        self.__price = price
        self.__description = description

    # more format tricks: https://pyformat.info/
    def __str__(self):
        return '{p.name} ({p.type}): ${p.price}\n{p.description}'.format(p=self)

    __repr__ = __str__

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value
