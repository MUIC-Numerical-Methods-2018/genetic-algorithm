from dataclasses import dataclass
import random
import time
import flappy_bird_gym
import numpy as np
from pprint import pprint
@dataclass
class Bird:
    a: float
    b: float
    c: float

    def action(self, obs):
        z = self.a + self.b*obs[0] + self.c*obs[1]
        return 1 if z > 0 else 0

    def breed(self, bird) -> 'Bird':
        return Bird(
            a = (self.a+bird.a)/2,
            b = (self.b+bird.b)/2,
            c = (self.c+bird.c)/2,
        )
    
    def mutated(self) -> 'Bird':
        return Bird(
            a = self.a + np.random.random()*10,
            b = self.b + np.random.random()*10,
            c = self.c + np.random.random()*10
        )

def play_game(bird: Bird, render: bool = True) -> int:
    env = flappy_bird_gym.make("FlappyBird-v0")
    score = 0
    env.seed(555)
    obs = env.reset()
    while True:
        # Next action:
        # (feed the observation to your agent here)
        score += 1
        action = bird.action(obs)

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

    env.close()
    return score

def random_birds(n) -> list[Bird]:
    return [
        
        Bird(
            a=(np.random.random()-0.5)*2000,
            b=(np.random.rand()-0.5)*2000,
            c=(np.random.rand()-0.5)*2000
        )
        for _ in range(n)
    ]

def squid_game(birds: list[Bird]) -> list[tuple[Bird, float]]: # sorted descendingly by score
    bird_scores = [(bird,play_game(bird, False)) for bird in birds]
    return sorted(bird_scores, key=lambda x: x[1], reverse=True)

def breed(birds: list[Bird], n=1) -> list[Bird]:
    return [np.random.choice(birds).breed(np.random.choice(birds)) for _ in range(n)]

def radiation(birds: list[Bird], n=1) -> list[Bird]:
    return [np.random.choice(birds).mutated() for _ in range(n)]

def genetic_algo(n, n_per_gen=1000):
    n_birds = n_per_gen
    next_gen_bird = random_birds(n_birds)
    n_keep = round(0.1*n_birds)
    n_breed = round(0.3*n_birds)
    n_mutated = round(0.4*n_birds)
    n_random = round(0.2*n_birds)
    for i in range(n):
        # race
        bird_scores = squid_game(next_gen_bird)
        # keep good ones
        good_birds = [b for b, score in bird_scores[:n_keep]]
        # breed them
        kid_birds = breed(good_birds, n_breed)
        radiated_birds = radiation(good_birds, n_mutated)
        # breed some good ones
        new_birds = random_birds(n_random)
        next_gen_bird = good_birds + kid_birds + radiated_birds + new_birds
        print(i, bird_scores[0])
    
def main():
    genetic_algo(100, 10000)

main()
#secret_bird = [-3.01968677e+01, -5.84914715e-01, -7.87463216e+02]
#b = Bird(*[-3.01968677e+01, -5.84914715e-01, -7.87463216e+02])
#pprint(squid_game(random_birds(10000))[:50])
#play_game(b)
