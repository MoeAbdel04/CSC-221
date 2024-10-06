class Item:
    def __init__(self, name):
        self.name = name

    def use(self, player):
        raise NotImplementedError("Use method must be implemented by subclass")

class Potion(Item):
    def __init__(self):
        super().__init__('Potion')

    def use(self, player):
        heal_amount = 20
        player.health += heal_amount
        print(f"{player.name} uses a Potion and heals for {heal_amount} health!")

class Weapon(Item):
    def __init__(self):
        super().__init__('Sword')

    def use(self, player):
        bonus_attack = 5
        player.attack_power += bonus_attack
        print(f"{player.name} uses a Sword and gains {bonus_attack} attack power!")

class Armor(Item):
    def __init__(self):
        super().__init__('Armor')

    def use(self, player):
        damage_reduction = 5
        player.attack_power += damage_reduction
        print(f"{player.name} uses Armor and takes {damage_reduction} less damage from attacks!")

class Shield(Item):
    def __init__(self):
        super().__init__('Shield')

    def use(self, player):
        block_chance = 50
        player.block_chance = block_chance
        print(f"{player.name} uses a Shield with a {block_chance}% chance to block enemy attacks!")
