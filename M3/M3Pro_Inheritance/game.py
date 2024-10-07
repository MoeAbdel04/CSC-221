import random
from characters import Player, Enemy, Orc, Dragon
from items import Potion, Weapon, Armor, Shield
from rooms import HealingFountain, Trap, TreasureRoom

class Game:
    def __init__(self):
        self._player = None
        self._rooms = ['Empty', 'Enemy', 'Item', 'Healing Fountain', 'Trap', 'Treasure Room', 'Enemy']
        self._boss_room = 'Dragon'
        self._current_room = 0
        self._enemies_defeated = 0  # Track the number of enemies defeated

    def start_game(self):
        self.display_banner("Welcome to the land of knights and dragons!")
        name = input("Enter your knight's name: ").strip()
        self._player = Player(name)  # Use protected attribute _player
        print(f"\n{'*' * 50}")
        print(f"{self._player._name}, YOUR JOURNEY BEGINS NOW!")
        print(f"{'*' * 50}\n")

        while self._player.is_alive() and self._current_room < len(self._rooms):
            self.move()

        if self._player.is_alive() and self._enemies_defeated >= 2:
            print(f"\n{'=' * 50}")
            print(f"YOU HAVE REACHED THE FINAL CHALLENGE, THE ANCIENT DRAGON!")
            print(f"{'=' * 50}\n")
            dragon = Dragon()
            self.combat(dragon)

            if self._player.is_alive():
                self.end_game()
        elif self._player.is_alive():
            print("\nYou sense that you are not yet prepared to face the Ancient Dragon.")
            print("Defeat at least 2 enemies before you may proceed.")
        else:
            self.display_banner("You have fallen in battle.")
            print("GAME OVER")

    def move(self):
        print("\nYou are in a mysterious land. Choose a direction to move (north, south, east, west):")
        direction = input("Your move: ").lower()
        self._current_room += 1
        room_content = random.choice(self._rooms)

        print(f"\n{'-' * 50}")
        if room_content == 'Enemy':
            print("An enemy appears!")
            enemy = random.choice([Enemy('Goblin', 30, 5, 5, 'Small Potion'), Orc()])
            self.combat(enemy)
        elif room_content == 'Item':
            print("You found an item!")
            self._player.add_item(random.choice([Potion(), Weapon(), Armor(), Shield()]))
        elif room_content == 'Healing Fountain':
            print("You have found a Healing Fountain! Your health is restored.")
            healing_fountain = HealingFountain()
            healing_fountain.use(self._player)
        elif room_content == 'Trap':
            print("You triggered a trap!")
            trap = Trap()
            trap.activate(self._player)
        elif room_content == 'Treasure Room':
            print("You found a treasure room with a rare item!")
            treasure_room = TreasureRoom()
            treasure_room.give_treasure(self._player)
        else:
            print("The room is empty.")
        print(f"{'-' * 50}\n")

    def combat(self, enemy):
        self.display_banner(f"Combat against {enemy._name}!")
        while self._player.is_alive() and enemy.is_alive():
            print(f"\n{self._player._name}'s Health: {self._player._health}")
            print(f"Enemy {enemy._name}'s Health: {enemy._health}")
            action = input("Do you want to 'attack', 'use item', or 'use skill'? ").lower()

            if action == 'attack':
                self._player.attack(enemy)
                if enemy.is_alive():
                    enemy.attack(self._player)
            elif action == 'use item':
                self._player.use_item()
            elif action == 'use skill':
                self._player.use_skill(enemy)

        if not enemy.is_alive():
            print(f"\n{'*' * 50}")
            print(f"YOU HAVE DEFEATED {enemy._name.upper()}!")
            print(f"{'*' * 50}\n")
            self._player.gain_experience(enemy._exp_reward)
            self._enemies_defeated += 1  # Increment enemy defeat count
        if not self._player.is_alive():
            self.display_banner("You have been defeated.")

    def end_game(self):
        """Display the ending message when the game is won."""
        print(f"\n{'=' * 50}")
        print(f"CONGRATULATIONS, {self._player._name.upper()}!")
        print(f"{'=' * 50}\n")
        print("YOU HAVE DEFEATED THE ANCIENT DRAGON AND RESTORED PEACE TO THE KINGDOM.")
        print("THE PEOPLE WILL SING SONGS OF YOUR HEROIC DEEDS FOR GENERATIONS TO COME!")
        print("THANK YOU FOR PLAYING!")
        print(f"\n{'=' * 50}")

    def display_banner(self, message):
        """Utility function to display a banner message."""
        print(f"\n{'=' * 50}")
        print(f"{message.center(50)}")
        print(f"{'=' * 50}\n")

if __name__ == "__main__":
    game = Game()
    game.start_game()
