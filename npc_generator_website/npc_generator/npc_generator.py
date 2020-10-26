from math import floor
from .generator_helper import ability_generator, dice_roller, mod_calculator, save_ratio
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
        self.fort_save = 0
        self.reflex_save = 0
        self.will_save = 0
        self.extra_attacks = ''
        self.extra_melee_attacks = ''
        self.extra_ranged_attacks = ''

    def __repr__(self):
        return f'''
        Level {self.level}
        {self.name}  STR:{self.str} DEX:{self.dex} CON:{self.con} INT:{self.int} WIS:{self.wis} CHA:{self.cha}
        F/R/W: +{self.fort_save}/+{self.reflex_save}/+{self.will_save}
        Base attack: +{self.base_attack}{self.extra_attacks} Melee attack: +{self.melee_attack}{self.extra_melee_attacks}
        Ranged attack: +{self.ranged_attack}{self.extra_ranged_attacks}
        '''

    # A method which uses the character class's base attack and the characters level, str and dex to calculate
    # base attack, melee attack and ranged attack
    def update_attacks(self):
        base = self.base_attack
        level = self.level
        str_mod = mod_calculator(self.str)
        dex_mod = mod_calculator(self.dex)
        self.base_attack = floor(base * level)
        self.melee_attack = self.base_attack + str_mod
        self.ranged_attack = self.base_attack + dex_mod

    def update_extra_attacks(self):
        base = self.base_attack
        melee = self.melee_attack
        ranged = self.ranged_attack
        num_bonus_attacks = floor((base-1)/5) # First bonus attack at +6, second at +11 etc.
        self.extra_attacks = ''
        self.extra_melee_attacks = ''
        self.extra_ranged_attacks = ''
        for i in range(num_bonus_attacks):  # Each extra attack has an attack stat 5 lower than the previous attack
            self.extra_attacks += f'/+{base-(i+1)*5}'
            self.extra_melee_attacks += f'/+{melee-(i+1)*5}' # Using "melee" and "ranged" rather than simply adding str or dex modifier
            self.extra_ranged_attacks += f'/+{ranged-(i+1)*5}' # because melee and ranged might be updated based on magic weapons


    # A method which uses the character's save ratios, abilities and level to determine their saves.
    # This uses the "save_ratio" function defined in generator_helper
    def update_saves(self):
        level = self.level
        con_mod = mod_calculator(self.con)
        dex_mod = mod_calculator(self.dex)
        wis_mod = mod_calculator(self.wis)
        self.fort_save = save_ratio(self.fort_save_ratio, level) + con_mod
        self.reflex_save = save_ratio(self.reflex_save_ratio, level) + dex_mod
        self.will_save = save_ratio(self.will_save_ratio, level) + wis_mod



# A function which holds the other functions involved in generating the NPC
def character_generator(char_class, level):
    # Defining our character
    character = Character(char_class, level)
    ability_scores = ability_generator()
    assign_ability_score(character, char_class, ability_scores, level)
    character.update_attacks()
    character.update_saves()
    character.update_extra_attacks()
    return character


