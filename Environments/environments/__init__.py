'''Register all environments with gym.

Needs to be updated whenever a new environment is added.
'''
from gym.envs.registration import register

register(
    id='random_walk_env-v0',
    entry_point='environments.envs:RandomWalkEnv',
)

register(
    id='two_armed_bernoulli_bandit-v0',
    entry_point='environments.envs:BernoulliBandit',
)

register(
    id='ten_armed_gaussian_bandit-v0',
    entry_point='environments.envs:GaussianBandit',
)
