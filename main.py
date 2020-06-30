from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

print('\n\n')
print('Name:               HP                                      MP')
print('                    _________________________               __________' )
print(bcolors.BOLD + 'Valos:    ' +
      '460/460  |' + bcolors.OKGREEN + '██████████████           ' + bcolors.ENDC + bcolors.BOLD + '|      ' +
      '65/65  |' + bcolors.OKBLUE + '██████████' + bcolors.ENDC + '|')

print('                           _________________________        __________' )
print('Valos:      460/460       |                         |      |          |')

print('                           _________________________        __________' )
print('Valos:      460/460       |                         |      |          |')


# Create Black Magic
fire = Spell('Fire', 10, 100, 'black')
thunder = Spell('Thunder', 10, 100, 'black')
blizzard = Spell('Blizzard', 10, 100, 'black')
meteor = Spell('Meteor', 20, 200, 'black')
quake = Spell('Quake', 14, 140, 'black')

# Create White Magic
cure = Spell('Cure', 12, 120, 'white')
curea = Spell('Cura', 18, 200, 'white')


# Create some Items
potion = Item('Potion', 'potion', 'Heals 50 HP', 50)
hipotion = Item('Hi-Potion', 'potion', 'Heals 100 HP', 100)
superpotion = Item('Super Potion', 'potion', 'Heals 500 HP', 500)
elixir = Item('Elixir', 'elixir', 'Fully restores HP/MP of one party member', 9999)
hielixir = Item('MegaElixir', 'elixir', 'Fully restores parties HP/MP', 9999)

grenade = Item('Grenade', 'attack', 'Deals 500 damage', 500)

player_spells = [fire, thunder, blizzard, meteor, cure, curea]
player_items = [{'item': potion, 'quantity': 15}, {'item': hipotion, 'quantity': 5},
                {'item': superpotion, 'quantity': 5}, {'item': elixir, 'quantity': 5},
                {'item': hielixir, 'quantity': 2}, {'item': grenade, 'quantity': 5}]

# Instantiate People
player = Person(460, 65, 60, 34, player_spells, player_items)
enemy = Person(1200, 65, 45, 25, [],[])

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print('======================')
    player.choose_action()
    choice = input('Choose Action:')
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print('You attacked for', dmg, 'points of damage')
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input('Choose Magic: ')) - 1

        if magic_choice == -1:
            continue

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(bcolors.FAIL + '\nNOT ENOUGH MP!\n' + bcolors.ENDC)
            continue

        player.reduce_mp(spell.cost)

        if spell.type == 'white':
            player.heal(magic_dmg)
            print(bcolors.OKGREEN + '\n' + spell.name + 'heals for', str(magic_dmg), 'HP' + bcolors.ENDC)
        elif spell.type == 'black':
            enemy.take_damage(magic_dmg)
            print(bcolors.OKBLUE + '\n' + spell.name + ' deals', str(magic_dmg), 'points of damage' + bcolors.ENDC)

    elif index == 2:
        player.choose_item()
        item_choice = int(input('Choose Item: ')) - 1

        if item_choice == -1:
            continue

        item = player.items[item_choice]['item']
        if player.items[item_choice]['quantity'] == 0:
            print(bcolors.FAIL + '\n' + 'None left...' + bcolors.ENDC)
            continue

        player.items[item_choice]['quantity'] -= 1

        if item.type == 'potion':
            player.heal(item.prop)
            print(bcolors.OKGREEN + '\n'+ item.name + ' heals for', str(item.prop), 'HP' + bcolors.ENDC)
        elif item.type == 'elixir':
            player.hp = player.max_hp
            player.mp = player.max_mp
            print(bcolors.OKGREEN + '\n' + item.name + ' fully restores HP/MP' + bcolors.ENDC)
        elif item.type == 'attack':
            enemy.take_damage(item.prop)
            print(bcolors.FAIL + '\n' + item.name + ' deals',str(item.prop), 'points of Damage' + bcolors.ENDC)


    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print('Enemy attacks for', enemy_dmg)

    print('----------------------')
    print('Enemy HP:', bcolors.FAIL + str(enemy.get_hp()) + '/' + str(enemy.get_max_hp()) + bcolors.ENDC + '\n')

    print('Your HP:', bcolors.OKGREEN + str(player.get_hp()) + '/' + str(player.get_max_hp()) + bcolors.ENDC)
    print('Your MP:', bcolors.OKBLUE + str(player.get_mp()) + '/' + str(player.get_max_mp()) + bcolors.ENDC + '\n')

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + 'YOU WIN!' + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + 'YOUR ENEMY HAS DEFEATED YOU!' + bcolors.ENDC)
        running = False




