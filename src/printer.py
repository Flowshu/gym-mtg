from creature import Creature
from game import Game

def print_creature(self, creature: Creature):
    if creature.power > 99 or creature.toughness > 99:
        print('Can not print creature with power/toughness > 99!')
        return

    if creature.power > 9:
        power = str(creature.power)
    else:
        power = ' ' + str(creature.power)

    if creature.toughness > 9:
        toughness = str(creature.toughness)
    else:
        toughness = str(creature.toughness) + ' '

    print(' |{}/{}| '.format(power,toughness), end='')

def print_battefield(self, game: Game):
    num_creatures1 = len(game.player1.creatures)
    num_creatures2 = len(game.player2.creatures)
    #sys.stdout.flush()
    #os.system('cls||clear')

    print('')
    print('PLAYER2: ' + str(game.player2.life))
    print('  _____  ' * num_creatures2)
    print(' |     | ' * num_creatures2)
    for creature in game.player2.creatures:
        game.print_creature(creature)
    print('')
    print(' |_____| ' * num_creatures2)
    print('_________' * max(num_creatures1,num_creatures2))
    print('  _____  ' * num_creatures1)
    print(' |     | ' * num_creatures1)
    for creature in game.player1.creatures:
        game.print_creature(creature)
    print('')
    print(' |_____| ' * num_creatures1)
    print('')
    print('PLAYER1: ' + str(game.player1.life))
    print('')