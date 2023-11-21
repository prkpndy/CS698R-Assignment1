# ==================================================
# CS-698R, Assignment 1
# 
# Ques 1: 2-Armed Bernoulli Bandit
# 
# State-space: 
# 1 = hole
# 0 = start
# 2 = goal
#  
# Action-space:
# 1 = move from start to goal state with prob = beta
# 0 = move from start to hole state with prob = alpha
# ===================================================


import gym
from gym.spaces import Discrete

import numpy as np

class BernoulliBandit(gym.Env):

    def __init__(self, mu):
        '''
        Parameters
        ----------
        mu  : .parameter of the bernoulli distribution
        '''
        self.n_bandit     = len(mu)
        self.action_space = Discrete(self.n_bandit)
        self.state_space  = Discrete(3)

        # mu[0] = alpha; mu[1] = beta
        self.mu   = mu

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
        
        p = np.random.uniform()
        if action == 1:
            if p>self.mu[1]:
                self.state = 1
                reward     = 0
            else:
                self.state = 2
                reward     = 1

        elif action == 0:
            if p>self.mu[0]:
                self.state = 2
                reward     = 0
            else:
                self.state = 1
                reward     = 1
        
        return self.state, reward, True, {}

    def reset(self):
        # reset the current state back to start state.
        self.state = 0
