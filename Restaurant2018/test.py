from Menu import Menu

menu = Menu("menu.csv")
print(menu.getMenuItem("Dessert", 1))
menu.printMenuItemsByType("Dessert")

