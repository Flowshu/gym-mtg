from creature import Creature
from random import choice

class Player():
    def __init__(self):
        self.life = 5
        self.creatures = []
        #self.agent = 0
        #self.battlefield = 0
        #self.deck = 0
        #self.hand = []
        #self.lands = []
        #self.graveyard = []
        #self.exile = []

    def play_creature(self, creature: Creature):
        self.creatures.append(creature)

    def declare_attacks(self):
        attack_vector = []
        for _ in range(len(self.creatures)):
            attack_vector.append(choice(range(2)))
        return attack_vector

    def declare_blocks(self, attack_vector):
        blockables = [-1]
        for attacker in range(len(attack_vector)):
            if attack_vector[attacker] == 1:
                blockables.append(attacker)
        block_vector = []
        for _ in range(len(self.creatures)):
            block_vector.append(choice(blockables))
        return block_vector
