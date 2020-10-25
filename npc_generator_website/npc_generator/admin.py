from django.contrib import admin

# Register your models here.
from .models import CharClass, WeaponProficiencyList, Weapon, ArmourProficiencyList, Armour, ListedWeapon, ListedArmour

class ListedWeaponInline(admin.TabularInline):
    model = ListedWeapon
    extra = 3


class WeaponProfsAdmin(admin.ModelAdmin):
    inlines = [ListedWeaponInline]


class ListedArmourInline(admin.TabularInline):
    model = ListedArmour
    extra = 3


class ArmourProfsAdmin(admin.ModelAdmin):
    inlines = [ListedArmourInline]


admin.site.register(CharClass)
admin.site.register(WeaponProficiencyList, WeaponProfsAdmin)
admin.site.register(Weapon)
admin.site.register(ArmourProficiencyList, ArmourProfsAdmin)
admin.site.register(Armour)