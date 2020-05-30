class Creature():
    def __init__(self, power: int, toughness: int):
        self.base_power = power
        self.power = power
        self.base_toughness = toughness
        self.toughness = toughness
        self.attacking = 0
        self.blocking = -1
