import time
import sys
from game_room import Room
from game_item import Item
from game_character import Character
from game_character import Enemy

inventory = ['Bare Hand']
k = Room('Kitchen')
d = Room('Dining Hall')
b = Room('Ballroom')
l = Room('Living Room')
g = Room('Gym')
t = Room('Toilet')

d.set_des('A luxury room with expensive utensils')
k.set_des('A big room in the side of the house')
b.set_des('A big room with wine and beer')
l.set_des('A large recreational place')
g.set_des('A large room with weights and treadmills')
t.set_des('BOSS ROOM - FINAL DESTINATION')

k.link_room(g, 'north')
k.link_room(d, 'south')
k.link_room(b, 'west')
k.link_room(l, 'east')
k.link_room(t, 'up stair')

d.link_room(g, 'south')
d.link_room(k, 'north')
d.link_room(b, 'west')
d.link_room(l, 'east')
d.link_room(t, 'up stair')

b.link_room(g, 'east')
b.link_room(d, 'south')
b.link_room(k, 'north')
b.link_room(l, 'west')
b.link_room(t, 'up stair')

l.link_room(g, 'east')
l.link_room(k, 'north')
l.link_room(b, 'west')
l.link_room(d, 'south')
l.link_room(t, 'up stair')

g.link_room(k, 'south')
g.link_room(d, 'north')
g.link_room(b, 'west')
g.link_room(l, 'east')
g.link_room(t, 'up stair')

# Kitchen
k.set_char('Tom')
k.set_char_des('A tall athletic zombie [Common Zombie]')

# Dining Hall
d.set_char('Barry')
d.set_char_des('Barry used to be in the military before he became a zombie [Epic Zombie]')
knife = Item('Butterfly Knife', 'A legendary combat knife [Legendary Item]')
toilet = Item('Toilet Paper', 'Cleaning usage [Common Item]')

# Ballroom
b.set_char('Bao')
b.set_char_des("Bao is a cooking master zombie but he couldn't handle sharp objects [Rare Zombie]")
gun = Item('Gun', 'A pistol with 12 bullets [Epic Item]')
coin = Item('Golden coin', 'A historical fragment')

# Living Room
l.set_char('Harold')
l.set_char_des('Harold is a muscular zombie but sometimes he is vulnurable to his own strength [Common Zombie]')
sword = Item('Sword', 'A long sharp sword [Rare Item]')
key = Item('Ballroom key', 'Key to Ballroom')

# Gym
dumbell = Item('Dumbell', 'A big heavy dumbell [Common Item]')

# Toilet
t.set_char('Andrew')
t.set_char_des('Lord of the zombie! The strongest of the kind [Legendary Zombie]')


def Kitchen():
    print('\n')
    global current_room
    print(current_room.get_name().upper())
    print('-------------------------')
    print(current_room.get_des())
    print('------------------------')
    print(current_room.get_char(), 'is here')
    print(current_room.get_char_des())
    tom = Character(current_room.get_char())
    tom.set_conv("What's up human!")
    print('[Tom]', tom.talk())
    tom.set_conv("Don't kill me. I'm a friendly zombie")
    print('[Tom]', tom.talk())
    print('Do you want to fight Tom or you decide to trust him (fight or trust)')
    fight = input('<')
    if fight == 'fight':
        print("Tom doesn't want to fight with you")
        print("He's a friendly zombie and you killed him")
    if fight == 'trust':
        tom.set_conv("Look like you need a weapon")
        print('[Tom]', tom.talk())
        tom.set_conv("Want me to show you where to get it? (yes or no)")
        print('[Tom]', tom.talk())
        ans = input('<')
        if ans == 'yes':
            print('--------------------')
            tom.set_conv("Go to the Gym")
            print('[Tom]', tom.talk())
            tom.set_conv("Beware of the Toilet...")
            print('[Tom]', tom.talk())
        else:
            tom.set_conv("Okay man you're on your own")
            print('[Tom]', tom.talk())
    print('------------------------')
    current_room.get_det()
    command = input('<')
    current_room = current_room.move(command)


def Dining():
    print('\n')
    global current_room
    print(current_room.get_name().upper())
    print('-------------------------')
    print(current_room.get_des())
    print('------------------------')
    print(current_room.get_char(), 'is here')
    print(current_room.get_char_des())
    barry = Enemy(current_room.get_char())
    barry.set_conv("I'm surprised you made it here!")
    print('[Barry]', barry.talk())
    barry.set_weak(gun.get_item())
    print('Do you want to fight with Barry or you decide to trust him or retreat (fight or trust or retreat)')
    fight = input('<')
    if fight == 'fight':
        while True:
            print('What do you want to fight with')
            print('Here is your inventory', inventory)
            pick = input('<')
            if pick not in inventory:
                print("You don't have this item")
            else:
                break
        if pick == gun.get_item():
            print('Barry has PTSD after the war and he is extremely vulnurable to guns and you found his weakness!')
            print('Barry has been defeated')
            print('-------------------------')

            print('You found a', toilet.get_item(), 'in here')
            print(toilet.get_des())

            print('Do you want to pick this item (yes or no)')
            pick = input('<')
            if pick == 'yes':
                inventory.append(toilet.get_item())
                print('You picked up a knife')
                print('------------------------')
                current_room.get_det()
                command = input('<')
                current_room = current_room.move(command)
        else:
            print('Barry shoot you and run over you with a tank')
            print('WASTED')
            print('YOU HAVE BEEN DEFEATED')
            sys.exit()
    if fight == 'retreat':
        print('------------------------')
        current_room.get_det()
        command = input('<')
        current_room = current_room.move(command)

    if fight == 'trust':
        print('Trusting Barry is the right choice')
        barry.set_conv('I can sell you the best weapon in the realm')
        print('[Barry]', barry.talk())
        barry.set_conv("Here is the legendary weapon for you but I'll need a Golden Coin in exchange ")
        print('[Barry]', barry.talk())
        print('Inventory', inventory)
        if coin.get_item() not in inventory:
            barry.set_conv("You don't have a Golden Coin yet")
            print('[Barry]', barry.talk())
            barry.set_conv("You need to find the Golden Coin in order to buy this weapon")
            print('[Barry]', barry.talk())
            print('------------------------')
            current_room.get_det()
            command = input('<')
            current_room = current_room.move(command)
        else:
            print('Do you want to buy the legendary', knife.get_item(), 'by the Golden Coin (yes or no)')
            choice = input('<')
            if choice == 'yes':
                inventory.append(knife.get_item())
                print('You got a', knife.get_item())
                print('-------------------------')
                current_room.get_det()
                command = input('<')
                current_room = current_room.move(command)
            if choice == 'no':
                print('-------------------------')
                current_room.get_det()
                command = input('<')
                current_room = current_room.move(command)


def Ball():
    global current_room
    print('\n')
    print(current_room.get_name().upper())
    print('-------------------------')
    print(current_room.get_des())
    print('------------------------')
    print('Do you want to enter this room (unlock or retreat)')
    print('Here is your inventory', inventory)
    lock = input('<')
    if lock == 'retreat':
        print('-------------------------')
        current_room.get_det()
        command = input('<')
        current_room = current_room.move(command)
    if lock == 'unlock':
        if key.get_item() not in inventory:
            print('You need to find a key to unlock this room')
            print('-------------------------')
            current_room.get_det()
            command = input('<')
            current_room = current_room.move(command)
        else:
            print('------------------------')
            print('Access Granted')
            print(current_room.get_char(), 'is here')
            print(current_room.get_char_des())
            bao = Enemy(current_room.get_char())
            bao.set_conv("I don't want to fight you, I want to be your partner")
            print('[Bao]', bao.talk())
            bao.set_weak(sword.get_item())
            print('Do you want to fight with Bao or you decide to trust him or retreat (fight or trust or retreat)')
            fight = input('<')
            if fight == 'fight':
                bao.set_conv("I'll cook you alive")
                print('[Bao]', bao.talk())
                while True:
                    print('What do you want to fight with')
                    print('Here is your inventory', inventory)
                    pick = input('<')
                    if pick not in inventory:
                        print("You don't have this item")
                    else:
                        break
                if pick == sword.get_item():
                    print("Bao's weakness is the sword and you found it!")
                    print('Bao has been defeated')
                    print('-------------------------------------')
                    print('You found a', gun.get_item(), 'in here')
                    print(gun.get_des())
                    print('Do you want to pick this item (yes or no)')
                    pick = input('<')
                    if pick == 'yes':
                        inventory.append(gun.get_item())
                        print('You picked up a gun')
                    print('------------------------')
                    print('There is a', coin.get_item(), 'on the table')
                    print(coin.get_des())
                    print('Do you want to pick this item (yes or no)')
                    pick = input('<')
                    if pick == 'yes':
                        inventory.append(coin.get_item())
                        print('You picked up the Golden Coin')
                        print('------------------------')
                        current_room.get_det()
                        command = input('<')
                        current_room = current_room.move(command)

            if fight == 'retreat':
                print('------------------------')
                current_room.get_det()
                command = input('<')
                current_room = current_room.move(command)

            if fight == 'trust':
                print('Bao betrayed you')
                print('You have been cooked')
                sys.exit()


def Living():
    print('\n')
    global current_room
    print(current_room.get_name().upper())
    print('-------------------------')
    print(current_room.get_des())
    print('------------------------')
    print(current_room.get_char(), 'is here')
    print(current_room.get_char_des())
    harold = Enemy(current_room.get_char())
    harold.set_conv("You are too small")
    print('[Harold]', harold.talk())
    harold.set_weak(dumbell.get_item())
    print('Do you want to fight with Harold (yes or no)')
    fight = input('<')
    if fight == 'yes':
        while True:
            print('What do you want to fight with')
            print('Here is your inventory', inventory)
            pick = input('<')
            if pick not in inventory:
                print("You don't have this item")
            else:
                break
        if pick == dumbell.get_item():
            print('Harold weakness is the dumbell and you found it!')
            print('Harold has been defeated')
            print('------------------------------')
            print('You found a', sword.get_item(), 'in here')
            print(sword.get_des())
            print('Do you want to pick this item (yes or no)')
            pick = input('<')
            if pick == 'yes':
                inventory.append(sword.get_item())
                print('You picked up a sword')
            else:
                print('------------------------')
                current_room.get_det()
                command = input('<')
                current_room = current_room.move(command)
            print('-------------------------')
            print('You found a key in here')
            print('Do you want to pick it up (pick or ignore)')
            choice = input('<')
            if choice == 'pick':
                inventory.append(key.get_item())
                print('*This is the key to the Ballroom*')
                print('------------------------')
                current_room.get_det()
                command = input('<')
                current_room = current_room.move(command)
            else:
                print('------------------------')
                current_room.get_det()
                command = input('<')
                current_room = current_room.move(command)

        else:
            print('Harold knock you out and throw you out of the window')
            print('WASTED')
            print('YOU HAVE BEEN DEFEATED')
            sys.exit()
    if fight == 'no':
        print('------------------------')
        current_room.get_det()
        command = input('<')
        current_room = current_room.move(command)


def Gym():
    print('\n')
    global current_room
    print(current_room.get_name().upper())
    print('-------------------------')
    print(current_room.get_des())
    print('You found a', dumbell.get_item(), 'in here')
    print(dumbell.get_des())
    print('Do you want to pick this item (yes or no)')
    pick = input('<')
    if pick == 'yes':
        inventory.append(dumbell.get_item())
        print('You picked up a dumbell')
        print('------------------------')
    print('You found a note in here')
    print('A small piece of note')
    print('Do you want to open this note (open or ignore)')
    open = input('<')
    if open == 'open':
        print('[Note] Your journey start from the Living room')
        print('------------------------')
        current_room.get_det()
        command = input('<')
        current_room = current_room.move(command)
    else:
        print('------------------------')
        current_room.get_det()
        command = input('<')
        current_room = current_room.move(command)


def Toilet():
    print('\n')
    global current_room
    print(current_room.get_name().upper())
    print('-------------------------')
    print(current_room.get_des())
    print('------------------------')
    print(current_room.get_char(), 'is here')
    print(current_room.get_char_des())
    bob = Enemy(current_room.get_char())
    bob.set_conv("You made it here!")
    print('[Andrew]', bob.talk())
    bob.set_conv("Bring it on human")
    print('[Andrew]', bob.talk())
    bob.set_conv("You are no match to my power")
    print('[Andrew]', bob.talk())
    print('Do you want to fight Andrew (yes or no)')
    fight = input('<')
    if fight == 'yes':
        while True:
            print('What do you want to fight with')
            print('Here is your inventory', inventory)
            pick = input('<')
            if pick not in inventory:
                print("You don't have this item")
            else:
                break
        if pick == knife.get_item():
            bob.set_conv("It can't be happening")
            print('[Andrew]', bob.talk())
            print('YOU DEFEATED ANDREW AND ESCAPE FROM THE ROOMS')
            print("YOU WIN!")
            sys.exit()
        else:
            print('Andrew crushed you')
            print('YOU HAVE BEEN DEFEATED')
            sys.exit()
    if fight == 'no':
        bob.set_conv("That's what I think")
        print('[Andrew]', bob.talk())
        bob.set_conv("You are not ready for me")
        print('[Andrew]', bob.talk())
        bob.set_conv("Human kinds are full of cowards")
        print('[Andrew]', bob.talk())
        print('------------------------')
        print('Andrew caught you and crushed you')
        print('You have been defeated')
        sys.exit()


def typewriter(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    sys.stdout.write('\n')


def start_game():
    start = input('Press Enter to start:')
    if start == ' ':
        return True
    else:
        return True


typewriter('WELCOME TO THE ROOMS')
typewriter('THE ROOMS SURROUNDING YOU HAS BEEN DESIGNED TO TEST YOUR WILL TO SURVIVE')
typewriter('YOU WILL HAVE TO DEFEATED THE LORD OF THE ZOMBIE IN ORDER TO SURVIVE')
typewriter('IF YOU SURVIVE, YOU EARN YOUR FREEDOM')
typewriter('LIVE OR DIE')
typewriter('MAKE YOUR CHOICE')
print('---------------------------')

if start_game():
    typewriter('GOOD LUCK SOLDIER!')
    print('----------------------')

current_room = k
while True:
    if current_room == k:
        Kitchen()
    if current_room == d:
        Dining()
    if current_room == b:
        Ball()
    if current_room == l:
        Living()
    if current_room == g:
        Gym()
    if current_room == t:
        Toilet()