from django.db import models

# Create your models here.


class WeaponProficiencyList(models.Model):
    char_list_name = models.CharField(max_length=50)

    def __str__(self):
        return self.char_list_name


class Weapon(models.Model):
    weapon_name = models.CharField(max_length=20)
    SIMPLE_WEAPON = 0
    MARTIAL_WEAPON = 1
    EXOTIC_WEAPON = 2
    weapon_types_list = (
        (SIMPLE_WEAPON, 'Simple'),
        (MARTIAL_WEAPON, 'Martial'),
        (EXOTIC_WEAPON, 'Exotic'),
    )
    MELEE = 0
    RANGED = 1
    WEAPON_MEL_RANGE_LIST = (
        (MELEE, 'melee'),
        (RANGED, 'ranged'),
    )
    weapon_type = models.IntegerField(choices=weapon_types_list)
    weapon_mel_range = models.IntegerField(choices=WEAPON_MEL_RANGE_LIST)
    weapon_damage = models.CharField(max_length=10)
    weapon_crit = models.CharField(max_length = 10)
    weapon_hands = models.PositiveSmallIntegerField()
    weapon_range = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.weapon_name


class ListedWeapon(models.Model):
    proficiency_list = models.ForeignKey(WeaponProficiencyList, on_delete=models.CASCADE)
    weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE)
    damage = Weapon.weapon_damage
    w_list_name = models.CharField(max_length=20)

    def __str__(self):
        return self.w_list_name


class ArmourProficiencyList(models.Model):
    armour_list_name = models.CharField(max_length=20)

    def __str__(self):
        return self.armour_list_name


class Armour(models.Model):
    armour_name = models.CharField(max_length=20)
    LIGHT_ARMOUR = 0
    MEDIUM_ARMOUR = 1
    HEAVY_ARMOUR = 2
    ARMOUR_TYPE_CHOICES = (
        (LIGHT_ARMOUR, 'light'),
        (MEDIUM_ARMOUR, 'medium'),
        (HEAVY_ARMOUR, 'heavy'),
    )
    armour_type = models.IntegerField(choices=ARMOUR_TYPE_CHOICES)
    armour_ac = models.PositiveSmallIntegerField()
    armour_max_dex = models.IntegerField()

    def __str__(self):
        return self.armour_name

class ListedArmour(models.Model):
    proficiency_list = models.ForeignKey(ArmourProficiencyList, on_delete=models.CASCADE)
    armour = models.ForeignKey(Armour, on_delete=models.CASCADE)
    a_list_name = models.CharField(max_length=20)
    def __str__(self):
        return self.a_list_name


class CharClass(models.Model):
    name = models.CharField(max_length=20)
    hit_dice = models.PositiveSmallIntegerField()
    base_attack = models.FloatField()
    fort_save_ratio = models.CharField(max_length=10)
    reflex_save_ratio = models.CharField(max_length=10)
    will_save_ratio = models.CharField(max_length=10)
    weapon_proficiencies = models.ForeignKey(WeaponProficiencyList, on_delete=models.PROTECT)
    armour_proficiencies = models.ForeignKey(ArmourProficiencyList, on_delete=models.PROTECT)

    def __str__(self):
        return self.name