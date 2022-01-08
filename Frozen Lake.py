#Reinforcement Learning------Frozen Lake

import gym
env = gym.make("FrozenLake-v0")
env.reset()
num_episodes = 10
num_timesteps = 20
for i in range(num_episodes):
    state = env.reset()
    print(f"\nEpisode {i} :\n")
    print("Time step 0 :")
    env.render()
    for t in range(num_timesteps):
        random_action = env.action_space.sample()
        next_state, reward, done, info = env.step(random_action)
        print(f"\nTime step {t+1} :\n")
        env.render()
        if done:
            break
