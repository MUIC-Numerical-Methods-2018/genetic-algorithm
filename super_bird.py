from dataclasses import dataclass
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


def play_game(bird: Bird, render: bool = True) -> int:
    env = flappy_bird_gym.make("FlappyBird-v0")
    reward = 0
    env.seed(555)
    obs = env.reset()
    while True:
        # Next action:
        # (feed the observation to your agent here)

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
    return reward

def random_birds(n) -> list[Bird]:
    return [
        
        Bird(
            a=(np.random.random()-0.5)*2000,
            b=(np.random.rand()*-0.5)*2000,
            c=(np.random.rand()*-0.5)*2000
        )
        for _ in range(n)
    ]

def squid_game(birds: list[Bird]) -> list[tuple[Bird, float]]: # sorted descendingly by score
    bird_scores = [(bird,play_game(bird, False)) for bird in birds]
    return sorted(bird_scores, key=lambda x: x[1], reverse=True)


    
def main():
    bird = Bird(1,2,3)
    reward = play_game(bird)
    print(reward)

#secret_bird = [-3.01968677e+01, -5.84914715e-01, -7.87463216e+02]
#b = Bird(*[-3.01968677e+01, -5.84914715e-01, -7.87463216e+02])
#pprint(squid_game(random_birds(10000))[:50])
#play_game(b)
