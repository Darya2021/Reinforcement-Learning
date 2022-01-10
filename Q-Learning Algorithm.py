# Reinforcement Learning-------Q-Learning

import gym
import numpy as np
import random

env = gym.make("FrozenLake-v0")

Q = {}
for s in range(env.observation_space.n):
    for a in range(env.action_space.n):
        Q[(s, a)] = 0.0
        print(Q[(s, a)])
        
    # or action_size = env.action_space.n
    # state_size = env.observation_space.n
    # Q = np.zeros((state_size, action_size))
    # print(Q)
        
        
def epsilon_greedy(state, epsilon):
    if random.uniform(0,1) < epsilon:
        return env.action_space.sample()
    else:
        return max(list(range(env.action_space.n)), key = lambda x: Q[(state, x)]) 
        # or action = np.argmax(Q[state, :])
        # return action 
    

alpha = 0.85
gamma = 0.90
epsilon = 0.8

num_episodes = 1000
num_timesteps = 100

for i in range(num_episodes):
    s = env.reset()
    
    for t in range(num_timesteps):
        a = epsilon_greedy(s, epsilon)
        
        s_, r, done, _ = env.step(a)
        
        a_ = np.argmax([Q[(s_, a)] for a in range(env.action_space.n)])
        
        Q[(s, a)] += alpha * (r + gamma * Q[(s_, a_)] - Q[(s, a)])
        
        s = s_
        
        if done:
            break

print(Q)
  
