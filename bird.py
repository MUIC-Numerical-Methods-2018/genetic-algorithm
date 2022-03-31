import time
import flappy_bird_gym
env = flappy_bird_gym.make("FlappyBird-v0")

def compute_action(ws, obs) -> int:
    # return 0 if no jump
    # return 1 if jump
    return 0

def play_one_game(ws, render=False) -> int: # ws -> a, b, c
    obs = env.reset()
    i_frame = 0
    while True:
        # Next action:
        # (feed the observation to your agent here)
        action = compute_action(ws, obs)  # for a random action

        # Processing:
        obs, reward, done, info = env.step(action)
        # Rendering the game:
        # (remove this two lines during training)
        if render:
            env.render()
            time.sleep(1 / 30)  # FPS

        # Checking if the player is still alive
        if done:
            break
        i_frame += 1
    return i_frame


def find_super_bird():
    # buy tons of birds from JJ
    # strong_ones = one that survive the squid game
    for gen in range(20):
        pass
        # birds = strong_ones + children of strong_ones + some from JJ
        # strong_ones = squid game on birds
    # super_bird = strongest one from strong_ones
