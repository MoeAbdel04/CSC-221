import random

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, target):
        damage = random.randint(1, self.attack_power)
        print(f"{self.name} attacks {target.name} for {damage} damage!")
        target.take_damage(damage)

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage!")

    def is_alive(self):
        return self.health > 0

class Player(Character):
    def __init__(self, name):
        super().__init__(name, 100, 10)
        self.experience = 0
        self.level = 1
        self.inventory = []
        self.skills = ['Power Strike']  # Added Power Strike as a skill

    def gain_experience(self, exp):
        self.experience += exp
        print(f"{self.name} gains {exp} experience points!")
        if self.experience >= self.level * 10:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.health += 20
        self.attack_power += 5
        print(f"{self.name} has leveled up to level {self.level}!")

    def add_item(self, item):
        self.inventory.append(item)
        print(f"{self.name} picked up a {item.name}.")

    def use_item(self):
        if not self.inventory:
            print("You have no items to use!")
            return

        print("Inventory:")
        for idx, item in enumerate(self.inventory):
            print(f"{idx + 1}. {item.name}")
        try:
            choice = int(input("Choose an item to use: ")) - 1

            if 0 <= choice < len(self.inventory):
                item = self.inventory.pop(choice)
                item.use(self)
            else:
                print("Invalid choice.")
        except (IndexError, ValueError):
            print("Invalid input. Please select a valid item number.")

    def use_skill(self, enemy):
        if not self.skills:
            print("You have no skills!")
            return

        print("Skills:")
        for idx, skill in enumerate(self.skills):
            print(f"{idx + 1}. {skill}")
        try:
            choice = int(input("Choose a skill to use (enter the number): ")) - 1

            if choice == 0 and self.skills[choice] == 'Power Strike':
                # Power Strike deals double damage
                damage = self.attack_power * 2
                print(f"{self.name} uses Power Strike for {damage} damage!")
                enemy.take_damage(damage)
            else:
                print("Invalid skill or choice.")
        except (IndexError, ValueError):
            print("Invalid input. Please select a valid skill number.")

class Enemy(Character):
    def __init__(self):
        super().__init__('Goblin', 30, 5)
        self.exp_reward = 5

class Skeleton(Character):
    def __init__(self):
        super().__init__('Skeleton', 40, 7)
        self.exp_reward = 7

class Dragon(Character):
    def __init__(self):
        super().__init__('Ancient Dragon', 200, 20)
        self.exp_reward = 100
