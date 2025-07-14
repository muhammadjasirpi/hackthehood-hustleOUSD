import random
from ability import Ability
from armor import Armor

class Hero:
    def __init__(self, name, starting_health=1000):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
        self.armors = []
        self.kills = 0
        self.deaths = 0

    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_armor(self, armor):
        self.armors.append(armor)

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def defend(self):
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block

    def take_damage(self, damage):
        defense = self.defend()
        damage_taken = max(0, damage - defense)
        self.current_health -= damage_taken

    def battle(self, opponent):
        if len(self.abilities) == 0 and len(opponent.abilities) == 0:
            print("Draw")
            return
        while self.current_health > 0 and opponent.current_health > 0:
            opponent.take_damage(self.attack())
            if opponent.current_health <= 0:
                print(f"{self.name} won!")
                self.add_kill(1)
                opponent.add_death(1)
                return
            self.take_damage(opponent.attack())
            if self.current_health <= 0:
                print(f"{opponent.name} won!")
                opponent.add_kill(1)
                self.add_death(1)
                return

    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_death(self, num_deaths):
        self.deaths += num_deaths

if __name__ == "__main__":
    my_hero = Hero("Grace Hopper", 200)
    print(my_hero.name)
    print(my_hero.current_health)

    opponent_hero = Hero("Ada Lovelace", 150)
    my_hero.battle(opponent_hero)
    ability = Ability("Lightning Strike", 50)
    my_hero.add_ability(ability)
    print([a.name for a in my_hero.abilities])
    armor = Armor("Shield", 30)
    my_hero.add_armor(armor)
    print([a.name for a in my_hero.armors])
