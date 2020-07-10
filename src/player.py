# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    def __init__(self, name, location = "outside", inventory = []):
        self.name = name
        self.location = location
        self.inventory = inventory
    def __str__(self):
        return f"Name: {self.name}, Current Location: {self.location}"

    def showinventory(self):
        if len(self.inventory) == 0:
            return "You have nothing in your inventory"
        elif len(self.inventory) >= 1:
            return f"Inventory: {[e.printName() for e in self.inventory]}"