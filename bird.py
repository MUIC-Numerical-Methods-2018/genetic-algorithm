import time
import flappy_bird_gym
import numpy
from dataclasses import dataclass
import numpy as np
env = flappy_bird_gym.make("FlappyBird-v0")

@dataclass
class Bird:
    w: np.ndarray

    def should_i_jump(self, obs) -> int:
        z = self.w[0] + self.w[1]*obs[0] + self.w[2]*obs[1]
        return 1 if z > 0 else 0
# karan = Bird([5, 8, 2])

def play_one_game(bird: Bird) -> int:
    obs = env.reset()
    score = 0
    while True:
        score+=1
        # Next action:
        # (feed the observation to your agent here)
        action = bird.should_i_jump(obs)  # for a random action

        # Processing:
        obs, reward, done, info = env.step(action)
        print(obs, action)

        # Rendering the game:
        # (remove this two lines during training)
        #env.render()
        #time.sleep(1 / 60)  # FPS

        # Checking if the player is still alive
        if done:
            break

    env.close()
    return score


def random_bird():
    return Bird((np.random.random(3)-0.5)*2000)

def squid_game():
    birds = [random_bird() for _ in range(2000)]
    scores = [play_one_game(bird) for bird in birds]
    best_bird = np.argmax(scores)
    print(birds[best_bird], scores[best_bird])

squid_game()