from math import floor
import random
from .models import CharClass
from .generator_helper import ability_generator, dice_roller, mod_calculator
from .assign_ability_scores import assign_ability_score

# Defining a character class to hold the attributes we get from the CharClass model
# and the associated weapons lists. The final function will return a string representation
# of the character class
class Character:
    def __init__(self, char_class, level):
        self.level = level
        self.name = char_class.name
        self.hit_dice = char_class.hit_dice
        self.base_attack = char_class.base_attack
        self.fort_save_ratio = char_class.fort_save_ratio
        self.reflex_save_ratio = char_class.reflex_save_ratio
        self.will_save_ratio = char_class.will_save_ratio
        self.armour_proficiencies = char_class.armour_proficiencies.listedarmour_set
        self.weapon_proficiencies = char_class.weapon_proficiencies.listedweapon_set
        self.str = 10
        self.dex = 10
        self.con = 10
        self.int = 10
        self.wis = 10
        self.cha = 10

    def __repr__(self):
        return f'''
        Level {self.level}
        {self.name}  STR:{self.str} DEX:{self.dex} CON:{self.con} INT:{self.int} WIS:{self.wis} CHA:{self.cha}
        '''

# A function which holds the other functions involved in generating the NPC
def character_generator(char_class, level):
    # Defining our character
    character = Character(char_class, level)
    ability_scores = ability_generator()
    assign_ability_score(character, char_class, ability_scores)
    return character

