from math import floor
import random
from .models import CharClass
from .generator_helper import ability_generator, dice_roller, mod_calculator

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
        self.armour_proficiencies = char_class.armourproficiencylist.listedarmour_set
        self.weapon_proficiencies = char_class.weaponproficiencylist.listedweapon_set
        self.str = 10
        self.dex = 10
        self.con = 10
        self.int = 10
        self.wis = 10
        self.cha = 10

    def _repr__(self):
        return self.name


