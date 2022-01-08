# Reinforcement Learning-----------Cart Pole

import gym
env = gym.make("CartPole-v0")
print(env.action_space)
print(env.observation_space)

num_episodes = 100
num_timesteps = 50


for i in range(num_episodes):

    Return = 0
    state = env.reset()
    
    
    for t in range(num_timesteps):
        random_action = env.action_space.sample()
        next_state, reward, done, info = env.step(random_action)
        Return = Return + reward
        
        if done:
            break
            
    print(f"random action {random_action} Episod {i}, Return {Return}\n")
