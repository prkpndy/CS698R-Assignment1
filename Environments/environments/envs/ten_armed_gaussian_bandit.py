# =====================================================
# CS-698R, Assignment 1
# 
# Ques 1: 10-Armed Gaussian Bandit
# 
# State-space: 
# 0 = start
# i = for action i
#   
# Action-space:
# i = move from start to i_th state with reward ~ N(mu,1)
# ======================================================


import gym
from gym.spaces import Discrete

import numpy as np

class GaussianBandit(gym.Env):

    def __init__(self, mean):
        '''
        Parameters
        ----------
        mu  : .parameter of the gaussian distribution
        '''
        self.n_bandit     = len(mean)
        self.action_space = Discrete(self.n_bandit)
        self.state_space  = Discrete(11)

        # mu[i] = mean of Gaussian distribution for i_th action
        self.mu   = mean

    def step(self, action):
        '''
        Parameters
        ----------
        action : Action to take.

        Returns
        -------
        tuple[int, float, bool, None]
            A tuple containing the next state, reward obtained, whether terminal state has been reached, and None.
        '''
        # action is valid or not
        assert (action < self.n_bandit)
        
        self.state = action+1
        reward     = np.random.normal(loc=self.mu[action])
        
        return self.state, reward, True, {}

    def reset(self):
        # reset the current state back to start state.
        self.state = 0
