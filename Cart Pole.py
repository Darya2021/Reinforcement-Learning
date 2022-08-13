# Reinforcement Learning-----------Cart Pole

import gym
env = gym.make("CartPole-v0")
print(env.action_space)
print(env.observation_space)
num_episod = 100
num_timesteps = 50
for i in range(num_episod):
    Return = 0
    state = env.reset()
    for t in range(num_timesteps):
        env.render()
        random_action = env.action_space.sample()
        nexts, reward, done, info = env.step(random_action)
        Return += reward
        if done:
            break
        if i%10 == 0:
            print(f"random action {random_action} Episod {i}, Return {Return}\n")
    
    
