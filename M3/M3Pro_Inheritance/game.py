import random
from characters import Player, Enemy, Skeleton, Dragon
from items import Potion, Weapon, Armor, Shield
from rooms import HealingFountain, Trap, TreasureRoom

class Game:
    def __init__(self):
        self.player = None
        self.rooms = ['Empty', 'Enemy', 'Item', 'Healing Fountain', 'Trap', 'Treasure Room', 'Enemy']
        self.boss_room = 'Dragon'
        self.current_room = 0

    def start_game(self):
        print("Welcome to the land of knights and dragons!")
        name = input("Enter your knight's name: ")
        self.player = Player(name)
        print(f"{self.player.name}, your journey begins now!")

        while self.player.is_alive() and self.current_room < len(self.rooms):
            self.move()

        if self.player.is_alive():
            print("You have reached the final challenge, the Ancient Dragon!")
            dragon = Dragon()
            self.combat(dragon)
        else:
            print("You have fallen in battle.")

    def move(self):
        print("\nYou are in a mysterious land. Choose a direction to move (north, south, east, west):")
        direction = input("Your move: ").lower()
        self.current_room += 1
        room_content = random.choice(self.rooms)

        if room_content == 'Enemy':
            print("An enemy appears!")
            enemy = random.choice([Enemy(), Skeleton()])
            self.combat(enemy)
        elif room_content == 'Item':
            print("You found an item!")
            self.player.add_item(random.choice([Potion(), Weapon(), Armor(), Shield()]))
        elif room_content == 'Healing Fountain':
            print("You have found a Healing Fountain! Your health is restored.")
            healing_fountain = HealingFountain()
            healing_fountain.use(self.player)
        elif room_content == 'Trap':
            print("You triggered a trap!")
            trap = Trap()
            trap.activate(self.player)
        elif room_content == 'Treasure Room':
            print("You found a treasure room with a rare item!")
            treasure_room = TreasureRoom()
            treasure_room.give_treasure(self.player)
        else:
            print("The room is empty.")

    def combat(self, enemy):
        while self.player.is_alive() and enemy.is_alive():
            print(f"\n{self.player.name}'s Health: {self.player.health}")
            print(f"Enemy {enemy.name}'s Health: {enemy.health}")
            action = input("Do you want to 'attack', 'use item', or 'use skill'? ").lower()

            if action == 'attack':
                self.player.attack(enemy)
                if enemy.is_alive():
                    enemy.attack(self.player)
            elif action == 'use item':
                self.player.use_item()
            elif action == 'use skill':
                self.player.use_skill(enemy)

        if not enemy.is_alive():
            print(f"You have defeated {enemy.name}!")
            self.player.gain_experience(enemy.exp_reward)
        if not self.player.is_alive():
            print("You have been defeated.")

if __name__ == "__main__":
    game = Game()
    game.start_game()
