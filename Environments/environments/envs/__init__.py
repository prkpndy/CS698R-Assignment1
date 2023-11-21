'''Import enviroment classes from files so that they are available under envs directly.
Needs to be updated whenever a new environment is added.
'''
from environments.envs.random_walk_env import RandomWalkEnv
from environments.envs.two_armed_bernoulli_bandit import BernoulliBandit
from environments.envs.ten_armed_gaussian_bandit import GaussianBandit
