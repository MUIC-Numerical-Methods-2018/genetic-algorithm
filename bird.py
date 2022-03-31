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
        # 0 no press
        # 1 press the space bar
        action = compute_action(ws, obs)  # for a random action

        # Processing:
        obs, reward, done, info = env.step(action)
        print(obs)
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
