class HealingFountain:
    def use(self, player):
        player.health = 100
        print(f"{player.name} has fully restored their health!")

class Trap:
    def activate(self, player):
        trap_damage = 10
        player.health -= trap_damage
        print(f"{player.name} is caught in a trap and takes {trap_damage} damage!")

class TreasureRoom:
    def give_treasure(self, player):
        player.add_item(Weapon())
        print("You have found a rare weapon!")
