import random

class Character:
    """
    Base Character class for all characters in the game.
    """
    def __init__(self, name, health, attack_power):
        self._name = name
        self._health = health
        self._attack_power = attack_power

    def attack(self, target):
        """
        Method for attacking a target character.
        """
        damage = random.randint(1, self._attack_power)
        print(f"{self._name} attacks {target._name} for {damage} damage!")
        target.take_damage(damage)

    def take_damage(self, damage):
        """
        Method for taking damage from an attack.
        """
        self._health -= damage
        print(f"{self._name} takes {damage} damage!")

    def is_alive(self):
        """
        Checks if the character is still alive.
        """
        return self._health > 0

    def display_stats(self):
        """
        Displays character stats: name, health, and attack power.
        """
        print(f"{self._name} - Health: {self._health}, Attack Power: {self._attack_power}")


class Player(Character):
    """
    Player class inheriting from Character with unique attributes like experience and level.
    """
    def __init__(self, name):
        super().__init__(name, 100, 10)
        self._experience = 0
        self._level = 1
        self._inventory = []
        self._skills = ['Power Strike']

    def gain_experience(self, exp):
        """
        Adds experience points and levels up if threshold is reached.
        """
        self._experience += exp
        print(f"{self._name} gains {exp} experience points!")
        if self._experience >= self._level * 10:
            self.level_up()

    def level_up(self):
        """
        Increases level, health, and attack power upon leveling up.
        """
        self._level += 1
        self._health += 20
        self._attack_power += 5
        print(f"{self._name} has leveled up to level {self._level}!")

    def add_item(self, item):
        """
        Adds an item to the player's inventory.
        """
        self._inventory.append(item)
        print(f"{self._name} picked up a {item.name}.")

    def use_item(self):
        """
        Allows the player to use an item from the inventory.
        """
        if not self._inventory:
            print("You have no items to use!")
            return

        print("Inventory:")
        for idx, item in enumerate(self._inventory):
            print(f"{idx + 1}. {item.name}")
        try:
            choice = int(input("Choose an item to use: ")) - 1
            if 0 <= choice < len(self._inventory):
                item = self._inventory.pop(choice)
                item.use(self)
            else:
                print("Invalid choice.")
        except (IndexError, ValueError):
            print("Invalid input. Please select a valid item number.")

    def use_skill(self, enemy):
        """
        Allows the player to use a skill in combat.
        """
        if not self._skills:
            print("You have no skills!")
            return

        print("Skills:")
        for idx, skill in enumerate(self._skills):
            print(f"{idx + 1}. {skill}")
        try:
            choice = int(input("Choose a skill to use: ")) - 1

            if choice == 0 and self._skills[choice] == 'Power Strike':
                # Power Strike deals double damage
                damage = self._attack_power * 2
                print(f"{self._name} uses Power Strike for {damage} damage!")
                enemy.take_damage(damage)
            else:
                print("Invalid skill or choice.")
        except (IndexError, ValueError):
            print("Invalid input. Please select a valid skill number.")


class Enemy(Character):
    """
    Base class for enemies, inheriting from Character.
    """
    def __init__(self, name, health, attack_power, exp_reward, loot):
        super().__init__(name, health, attack_power)
        self._exp_reward = exp_reward
        self._loot = loot

    def drop_loot(self):
        """
        Drops loot upon defeat.
        """
        print(f"{self._name} dropped {self._loot}!")
        return self._loot


class Goblin(Enemy):
    """
    Goblin enemy subclass inheriting from Enemy.
    """
    def __init__(self):
        super().__init__('Goblin', 30, 5, 5, 'Small Potion')


class Orc(Enemy):
    """
    Orc enemy subclass inheriting from Enemy.
    """
    def __init__(self):
        super().__init__('Orc', 50, 7, 8, 'Battle Axe')


class Dragon(Enemy):
    """
    Dragon enemy subclass, serving as the final boss.
    """
    def __init__(self):
        super().__init__('Dragon', 200, 20, 100, 'Ancient Dragon Scale')
