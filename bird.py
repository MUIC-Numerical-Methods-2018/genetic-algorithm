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
    env.seed(555)
    obs = env.reset()
    score = 0
    while True:
        score+=1
        # Next action:
        # (feed the observation to your agent here)
        action = bird.should_i_jump(obs)  # for a random action

        # Processing:
        obs, reward, done, info = env.step(action)

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

def squid_game() -> List[Bird]:
    birds = [random_bird() for _ in range(10000)]
    scores = [play_one_game(bird) for bird in birds]
    best_bird = np.argmax(scores)
    print(birds[best_bird], scores[best_bird])
    return get_winning_birds(birds, scores)

def breed(male_bird: Bird, female_bird: Bird) -> Bird:
    return Bird((male_bird.w + female_bird.w)/2)

def gamma_ray_radition(bird: Bird) -> Bird:
    return Bird(bird.w + np.random.randn(3)*5)

from typing import List

def new_bird_generation(winning_birds: List[Bird]) -> List[Bird]:
    # 10000
    # winning_bird --> 1000
    # winning_bird + radiation --> 1000
    # breed some more + radiation --> 7000
    # totally new ---> 1000
    winning_bird_radiation = [gamma_ray_radition(bird) for bird in winning_birds]

    def random_children():
        b1, b2 = np.random.choice(winning_birds, 2)
        return breed(b1, b2)
    
    child_birds = [gamma_ray_radition(random_children()) for _ in range(7000)]
    new_birds = [random_bird() for _ in range(1000)]

    return winning_birds + winning_bird_radiation + child_birds + new_birds

def get_winning_birds(birds: List[Bird], scores: np.ndarray) -> List[Bird]: 
    bs = [(b, s) for b, s in zip(birds, scores)]
    bs.sort(key=lambda x: x[1], reverse=True) # sort score descendingly
    return bs[: 1000]


squid_game()