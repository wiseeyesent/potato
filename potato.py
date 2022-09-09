#!/usr/bin/python
intro = """
POTATO
   A one page RPG by Oliver Darkshire

Source: https://twitter.com/deathbybadger/status/1567425842526945280

You are a halfling, just trying to exist.
Meanwhile, the dark lord rampages across the world.

You do not care about this.
You are trying to farm potatoes
because what could a halfling possibly do about this anyway?

[R]oll the dice to try your luck.
[T]hrow potatoes to distract the orcs.
If any stat reaches 10, the game ends."""

print(intro)
import datetime
import random
import sys

seed = datetime.datetime.now().microsecond
print(f'\nseed: {seed}\n')
random.seed(seed)

choice = ''
roll = 0
potatoes = 0
destiny = 0
orcs = 0
throw = 1

def error_out():
    global potatoes, destiny, orcs, throw, roll
    print(f'What the hell just happened?')
    print(f'choice \'{choice}\', roll {roll}, potatoes {potatoes}, destiny {destiny}, orcs {orcs}, throw {throw}')
    sys.exit(-1)

def prompt_user():
    choice = ''
    while choice != 'r':
        choice = input('What would you like to do? throw/[r]oll: ').lower()[0:1]
        choice = choice if not choice == '' else 'r'
        print(f'\tChoice: {choice}')
        if choice not in ['t', 'r']:
            print('Sorry. You can only throw potatoes or roll the dice.')
        elif choice == 't':
            throw_potatoes()

    roll = random.randint(1, 6)
    print(f'...rolled a {roll}')
    return roll

def throw_potatoes():
    global potatoes
    global throw
    global orcs
    if potatoes >= throw:
        potatoes -= throw
        orcs -= 1
        orcs = orcs if orcs >= 0 else 0
        print(f'You threw {throw} potatoes to the orcs. (potatoes: {potatoes}, throw: {throw}, orcs: {orcs})')
    else:
        print(f'Sorry, but you do not yet have enough potatoes to throw. (potatoes: {potatoes}, throw: {throw}, orcs: {orcs})')

while True:
    roll = 0
    print('Grass And Mud...')
    roll = prompt_user()

    if roll in [1, 2]:
        print('In The Garden...')
        roll = prompt_user()
        
        if roll == 1:
            potatoes += 1
            print('You happily root about all day in your garden. (+1 potatoes)')
        elif roll == 2:
            potatoes += 1
            destiny += 1
            print('You narrowly avoid a visitor by hiding in a potato sack. (+1 potatoes, +1 destiny)')
        elif roll == 3:
            destiny += 1
            orcs += 1
            print('A hooded stranger lingers outside your farm. (+1 destiny, +1 orcs)')
        elif roll == 4:
            potatoes -= 1
            potatoes = potatoes if potatoes >= 0 else 0
            orcs += 1
            print('Your field is ravaged in the night by unseen enemies. (+1 orc, -1 potatoes)')
        elif roll == 5:
            potatoes -= 1
            potatoes = potatoes if potatoes >= 0 else 0
            print('You trade potatoes for other delicious foodstuffs. (-1 potatoes)')
        elif roll == 6:
            potatoes += 2
            print('You burrow into a bumper crop of potatoes. Do you cry with joy? Possibly. (+2 potatoes)')
        else:
            error_out()

    elif roll in [3, 4]:
        print('A Knock At The Door...')
        roll = prompt_user()

        if roll == 1:
            orcs += 1
            print('A distant cousin. They are after your potatoes. They may snitch on you. (+1 orcs)')
        elif roll == 2:
            destiny += 1
            print('A dwarven stranger. You refuse them entry. Ghastly creatures. (+1 destiny)')
        elif roll == 3:
            destiny += 1
            orcs += 1
            print('A wizard strolls by. You pointedly draw the curtains. (+1 destiny, +1 orc)')
        elif roll == 4:
            potatoes -= 1
            potatoes = potatoes if potatoes >= 0 else 0
            orcs += 2
            print('There are rumors of war in the reaches. You eat some potatoes. (-1 potatoes, +2 orcs)')
        elif roll == 5:
            destiny += 1
            print('It\'s an elf. They are not serious people. (+1 destiny)')
        elif roll == 6:
            potatoes += 2
            print('It\'s a sack of potatoes from a generous neighbour. You really must remember to pay them a visit one of these years. (+2 potatoes)')
        else:
            error_out()

    elif roll in [5, 6]:
        throw += 1
        print(f'The world becomes a darker, more dangerous place. Throw costs +1 potato. (throw: {throw})')

    else:
        error_out()

    print(f'\tDestiny {destiny}, Potatoes (throw cost) {potatoes} ({throw}), Orcs {orcs}\n')
    
    if potatoes >= 10:
        print('You have enough potatoes that you can go underground and not return to the surface until the danger is past. You nestly down into your burrow and enjoy your well earned rest.')
        sys.exit(0)
    elif destiny >= 10:
        print('An interfering bard or wizard turns up at your doorstep with a quest, and you are whisked away against your will on an adventure (unless you\'ve already been eaten by orcs).')
        sys.exit(1)
    elif orcs >= 10:
        print('Orcs finally find your farm. Alas, orcs are not so interested in potatoes as they are in eating you, and you end up in a cookpot.')
        sys.exit(2)
