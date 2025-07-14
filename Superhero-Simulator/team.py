import random

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = []

    def add_hero(self, hero):
        self.heroes.append(hero)

    def remove_hero(self, name):
        found_hero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                found_hero = True
                break
        if not found_hero:
            return 0

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def stats(self):
        for hero in self.heroes:
            print(f"{hero.name} Kill/Deaths: {hero.kills}/{hero.deaths}")

    def revive_heroes(self):
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def attack(self, other_team):
        living_heroes = [hero for hero in self.heroes if hero.current_health > 0]
        living_opponents = [hero for hero in other_team.heroes if hero.current_health > 0]
        while len(living_heroes) > 0 and len(living_opponents) > 0:
            hero = random.choice(living_heroes)
            opponent = random.choice(living_opponents)
            hero.battle(opponent)
            living_heroes = [h for h in self.heroes if h.current_health > 0]
            living_opponents = [h for h in other_team.heroes if h.current_health > 0]