# Generated by Django 3.1.2 on 2020-10-23 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('npc_generator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArmourProficiencyList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('armour_list_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Armours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('armour_name', models.CharField(max_length=20)),
                ('armour_type', models.IntegerField(choices=[(0, 'light'), (1, 'medium'), (2, 'heavy')])),
                ('armour_ac', models.PositiveSmallIntegerField()),
                ('armour_max_dex', models.IntegerField()),
                ('armour_list_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='npc_generator.armourproficiencylist')),
            ],
        ),
        migrations.CreateModel(
            name='CharClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('hit_dice', models.PositiveSmallIntegerField()),
                ('base_attack', models.FloatField()),
                ('fort_save_ratio', models.FloatField()),
                ('reflex_save_ratio', models.FloatField()),
                ('will_save_ratio', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='WeaponProficiencyList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('char_list_name', models.CharField(max_length=50)),
                ('char_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='npc_generator.charclass')),
            ],
        ),
        migrations.CreateModel(
            name='Weapons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weapon_name', models.CharField(max_length=20)),
                ('weapon_type', models.IntegerField(choices=[(0, 'Simple'), (1, 'Martial'), (2, 'Exotic')])),
                ('weapon_mel_range', models.IntegerField(choices=[(0, 'melee'), (1, 'ranged')])),
                ('weapon_damage', models.CharField(max_length=5)),
                ('weapon_crit', models.CharField(max_length=10)),
                ('weapon_hands', models.PositiveSmallIntegerField()),
                ('weapon_range', models.PositiveSmallIntegerField()),
                ('weapon_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='npc_generator.weaponproficiencylist')),
            ],
        ),
        migrations.RemoveField(
            model_name='response',
            name='question',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='Response',
        ),
        migrations.AddField(
            model_name='armourproficiencylist',
            name='char_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='npc_generator.charclass'),
        ),
    ]
