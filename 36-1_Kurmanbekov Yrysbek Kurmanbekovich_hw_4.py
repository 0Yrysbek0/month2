from enum import Enum
from random import choice, randint


class SuperAbility(Enum):
    CRITICAL_DAMAGE = 1
    BOOST = 2
    BLOCK_DAMAGE_AND_REVERT = 3
    HEAL = 4
class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

        @property
        def name(self):
            return self.__name

        @property
        def health(self):
            return self.__health

        @health.setter
        def health(self, value):
            self.__health = value

        @damage.setter
        def damage(self, value):
            self.__damage = value

        def __str__(self):
           return f'{self.__name} health: {self.__health} damage: {self.__damage}'

class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None

        def choose_defence(self, heroes):
            random_hero = choice(heroes)
            self.__defence = random_hero.ability

        def attack(self, heroes):
            for hero in heroes:
                hero.health -= self.damage

         def __str__(self):
            return 'BOSS '  + super().__str__() + f' defence: {self.__defence}'


class Hero(GameEntity):
    def  __init__(self, name, health, damage, ability):
        super().__init__(name, health, damage)
        if type(ability) == SuperAbility:
            self.__ability = ability

    @property
    def ability(self):
        return self.__ability

    def attack(self, boss):
        boss.health -= self.damage

    def start_game():
        boss = Boss(name:'Balmond', health:1000, damage:50)

