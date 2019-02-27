from classess.game import Person, bcolors
from classess.magic import Spell

# Black Magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("thunder", 8, 60, "black")
blizzard = Spell("blizzard", 15, 90, "black")
meteor = Spell("meteor", 20, 110, "black")
quake = Spell("quake", 12, 70, "black")

# White Magic
cure = Spell("Cure", 15, 200, "white")
cura = Spell("Cura", 10, 100, "white")

player = Person(460, 65, 60, 34, [fire, thunder, meteor, cura, cure])
enemy = Person(1200, 65, 45, 25, [])

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD +"Enemy Attacks" + bcolors.ENDC)

while running:
    print("============")
    player.choose_action()
    choice = input("Choose Actions: ")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg, "points of damage. Enemy HP: ", enemy.get_hp())
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose magic")) - 1

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()
        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(bcolors.FAIL + "you Dont have enough MP" + bcolors.ENDC)
            continue

        player.reduce_mp(spell.cost)

        if spell.type == "white":
            player.heal(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + " heals for", str(magic_dmg), "HP" +bcolors.ENDC)
        elif spell.type == "black":
            enemy.take_damage(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + "deals", str(magic_dmg), " points of damgae" + bcolors.ENDC)

    enemy_choice = 1

    enemy_damage = enemy.generate_damage()
    player.take_damage(enemy_damage)
    print("Enemy attacked for", enemy_damage)
    print("________________")
    print("Enemy HP: ", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC)
    print("Player HP: ", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC)
    print("Player MP: ", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC)

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You Win" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "Defeated" + bcolors.ENDC)
        running = False

