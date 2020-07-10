from Item import Item

class Weapon(Item):
    def __init__(self, name, description, rarity, damage):
        super().__init__(name, description, rarity)
        self.damage = damage
    
    def __str__(self):
        return f"{super().__str__()}, DPS: {self.damage}"