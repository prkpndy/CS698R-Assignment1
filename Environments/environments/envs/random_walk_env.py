import gym
from gym import spaces
from gym.utils import seeding
import numpy as np
from os import path
import math


class InValidActionException (Exception):
    pass

class InValidObservationException(Exception):
    pass

class RandomWalkEnv(gym.Env):
    metadata = {
        'render.modes': ['human', 'rgb_array'],
        'video.frames_per_second': 30
    }

    def __init__(self, seed = 0):
        self.state = None

        self.action_space = (0, 1)
        self.observation_space = (0,1,2,3,4,5,6)

        self.action_dict = {"R": 0, "L" : 1 }

        self.max_start_state = 5
        self.min_start_state = 1


        self.intended_action_prob = 0.5



    def step(self, action ):

        if action not in self.action_space:
            raise InValidActionException
        next_state = -1
        reward = -1
        is_Terminal = False
        if action == self.action_dict["R"]:
            intended_next_state = self.state + 1
            not_intended_next_state = self.state - 1

        elif action == self.action_dict["L"]:
            intended_next_state = self.state + 1
            not_intended_next_state = self.state - 1

        if np.random.random() < self.intended_action_prob :
            next_state = intended_next_state
        else:
            next_state = not_intended_next_state

        if next_state == 6:
            reward = 1
        else:
            reward = 0

        if next_state == 6 or next_state == 0:
            is_Terminal = True


        self.last_action = action
        self.last_state = self.state
        self.state = next_state
        return self.state, reward, is_Terminal, {}

    def reset(self):
        self.state = 3 #np.random.randint(self.min_start_state, self.max_start_state, 1)
        self.last_state = None
        self.last_action = None
        return self.state


    def render(self, mode='human'):
       pass

    def close(self):
        pass
