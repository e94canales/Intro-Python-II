class Item():
    def __init__(self, name, description, rarity):
        self.name = name
        self.description = description
        self.rarity = rarity

    def __str__(self):
        return f"{self.name} - {self.description}, Rarity: {self.rarity}"

    def ontake(self):
        return f"You have picked up: {self.name}"

    def printName(self):
        return self.name

