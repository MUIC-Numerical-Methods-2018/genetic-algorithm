import time

import flappy_bird_gym
import numpy as np

env = flappy_bird_gym.make("FlappyBird-v0")


def compute_action(ws, obs) -> int:
    # return 0 if no jump
    # return 1 if jump
    return 1 if ws[1:] @ obs + ws[0] > 0 else 0


def play_one_game(ws, render=False, max_frame=1000) -> int:  # ws -> a, b, c
    env = flappy_bird_gym.make("FlappyBird-v0")
    env.seed(100)
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

        if i_frame > max_frame:
            break
        i_frame += 1
    env.close()
    return i_frame


def random_bird():
    return np.random.rand(3) * 2000 - 1000  # 3 numbers between -100, 100


def squid_games(birds):
    tmp = []
    for bird in birds:
        score = play_one_game(bird, max_frame=2000)
        tmp.append((score, bird))
    tmp = sorted(tmp, key=lambda x: -x[0])
    for x in tmp[:10]:
        print(x[0], x[1])
    return [x[1] for x in tmp[:20]]


def breed(mom, dad):
    t = np.random.rand()
    return t * mom + (1 - t) * dad


def random_breed(birds):
    mom_idx = np.random.randint(len(birds))
    dad_idx = np.random.randint(len(birds))
    return breed(birds[mom_idx], birds[dad_idx])


def find_super_bird():
    birds = [random_bird() for _ in range(200)]
    strong_ones = squid_games(birds)
    for gen in range(20):
        print('-' * 30, gen)
        children = [random_breed(strong_ones) for i in range(150)]
        jj = [random_bird() for _ in range(30)]
        birds = strong_ones + children + jj
        strong_ones = squid_games(birds)
    return strong_ones[0]

super_bird = find_super_bird()
print(super_bird)

score = play_one_game(super_bird,
                      render=True, max_frame=999999)
print(score)
