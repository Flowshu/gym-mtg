from creature import Creature
from player import Player
from random import choice
from rewards import Rewards

class Game():
    def __init__(self, player1 : Player, player2 : Player):
        self.player1 = player1
        self.player2 = player2
        self.attacking_player = player1
        self.blocking_player = player2
        self.turn = 1
        self.phase = 1
        num_creatures_player1 = range(choice(range(1,7)))
        for _ in num_creatures_player1:
            self.player1.play_creature(randomCreature())
        num_creatures_player2 = range(choice(range(1,7)))
        for _ in num_creatures_player2:
            self.player2.play_creature(randomCreature())

    def isOver(self):
        cond1 = self.player1.life < 1
        cond2 = self.player2.life < 1
        cond3 = self.player1.creatures == []
        cond4 = self.player2.creatures == []
        return (cond1 or cond2 or cond3 or cond4)

    def performAttack(self, attacks):
        for creature in range(len(self.attacking_player.creatures)):
            if attacks[creature] == 1:
                self.attacking_player.creatures[creature].attacking = 1

    def performBlocks(self, blocks):
        for creature in range(len(self.blocking_player.creatures)):
            if blocks[creature] > -1:
                self.blocking_player.creatures[creature].blocking = blocks[creature]


    def performDamage(self, attacks, blocks):
        attacker_board = self.attacking_player.creatures
        blocker_board = self.blocking_player.creatures

        #creature damage
        for creature in range(len(blocker_board)):
            if blocks[creature] > -1:
                attacker_board[blocks[creature]].toughness -= blocker_board[creature].power
                blocker_board[creature].toughness -= attacker_board[blocks[creature]].power
                attacker_board[blocks[creature]].power -= blocker_board[creature].toughness

        #player damage
        for creature in range(len(attacker_board)):
            if not (creature in blocks) and (attacks[creature] == 1):
                self.blocking_player.life -= attacker_board[creature].power

    def performCleanup(self):
        player1_board = self.player1.creatures
        player2_board = self.player2.creatures

        player1_board[:] = [creature for creature in player1_board if creature.toughness > 0]
        player2_board[:] = [creature for creature in player2_board if creature.toughness > 0]
        for creature in (player1_board +player2_board):
            creature.toughness = creature.base_toughness
            creature.power = creature.base_power

    def passTurn(self):
        temp = self.attacking_player
        self.attacking_player = self.blocking_player
        self.blocking_player = temp

    def performAction(self, action):
        if self.phase == 1: #attacks
            attack_vector = action
            self.performAttack(attack_vector)
            
            block_vector = self.blocking_player.declare_blocks(attack_vector)
            self.performBlocks(block_vector)

            self.performDamage(attack_vector, block_vector)
            self.performCleanup()
            self.passTurn()

            attack_vector = self.attacking_player.declare_attacks()
            self.performAttack(attack_vector)
            self.phase = 2

        elif self.phase == 2: #blocks
            block_vector = action
            self.performBlocks(block_vector)

            self.performDamage(attack_vector, block_vector)
            self.performCleanup()
            self.passTurn()
            self.phase = 1

        return Rewards.DEFAULT

def randomCreature():
    return Creature(choice(range(6)), choice(range(1,6)))
