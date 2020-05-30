from gym.envs.registration import register

register(
    id='mtg-v0',
    entry_point='gym_mtg.envs:MtgEnv'
)
