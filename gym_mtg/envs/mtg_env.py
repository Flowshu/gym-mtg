import numpy as np
from gym import Env, spaces
from src.creature import Creature
from src.game import Game
from src.player import Player

class MtgEnv(Env):
    def __init__(self):
        self.MAX_CREATURES = 7
        self.action_space = spaces.Box(low=-1, high=5, shape=(self.MAX_CREATURES,), dtype=np.int8)
        self.observation_space = spaces.Dict({
        'turn': spaces.Box(low=1, high=2, shape=(1,), dtype=np.int8),
        'phase': spaces.Box(low=1, high=3, shape=(1,), dtype=np.int8),
        'player2_life': spaces.Box(low=-50, high=5, shape=(1,), dtype=np.int8),
        'player2_creatures': spaces.Box(low=-5, high=5, shape=(self.MAX_CREATURES,4), dtype=np.int8),
        'player1_creatures': spaces.Box(low=-5, high=5, shape=(self.MAX_CREATURES,4), dtype=np.int8),
        'player1_life': spaces.Box(low=-50, high=5, shape=(1,), dtype=np.int8)
    })

    def step(self, action):
        reward = self.game.performAction(action)
        observation = self._get_observation_from_game()
        done = self.game.isOver()
        info = {}
        return observation, reward, done, info

    def reset(self):
        self.game = Game(Player(), Player())
        return self._get_observation_from_game()

    def _get_observation_from_game(self):
        observation = self.observation_space.sample()
        observation['turn'] = self.game.turn
        observation['phase'] = self.game.phase
        observation['player1.life'] = self.game.player1.life
        observation['player2.life'] = self.game.player2.life
        observation['player1.creatures'] = self.game.player1.creatures
        observation['player2.creatures'] = self.game.player2.creatures
        return observation
