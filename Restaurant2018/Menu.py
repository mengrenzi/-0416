# Menu.py
# Goal: This class represents the restaurant’s menu which contains four different categories of menu items diners can order from.

import csv

from MenuItem import MenuItem

class Menu(object):
    MENU_ITEM_TYPES = ["Drink", "Appetizer", "Entree", "Dessert"]

    def get_keys(d, value):
        return [k for k,v in d.items() if v == value]

    def __init__(self, filename):
        count = 0
        with open(filename) as f:
            reader = list(csv.reader(f))
            for row in reader:
                menuItem = MenuItem(row[0],row[1],row[2],row[3])
                self.__menuItemDictionary = {menuItem:count}
                count += 1
            f.close()

    def getMenuItem(self, type, index):
        myMenuItem = Menu.get_keys(self.__menuItemDictionary,index)
        return myMenuItem

    def printMenuItemsByType(self, type):


    #def getNumMenuItemsByType(self):
        #a = 1
        # 返回类型：MenuItems
