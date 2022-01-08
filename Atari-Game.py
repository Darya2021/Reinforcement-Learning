#Reinforcement Learning--------------Atari-Game

import gym
env = gym.make("ReversedAddition-v0")
print(env.action_space)
print(env.observation_space)

env.render()

env.reset()

episods = 20
timesteps = 10

for i in range(episods):
    Return = 0
    state = env.reset()
    
    for t in range(timesteps):
        env.render()
        random_action = env.action_space.sample()
        nest_satae, reward, done, info = env.step(random_action)
        Return = Return + reward
        
        if done:
            break
