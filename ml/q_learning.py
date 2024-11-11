import numpy as np
import random


class Enviornment:
    def __init__(self, size):
        self.size = size
        self.state = (0, 0)
        self.goal = (size - 1, size - 1)

    def reset(self):
        self.state = (0, 0)
        return self.state

    def step(self, action):
        if action == 0:
            self.state = (max(0, self.state[0] - 1), self.state[1])
        if action == 1:
            self.state = (min(self.size - 1, self.state[0] + 1), self.state[1])
        if action == 2:
            self.state = (self.state[0], max(0, self.state[1] - 1))
        if action == 3:
            self.state = (self.state[0], min(self.size - 1, self.state[1] + 1))
        reward = 1 if self.state == self.goal else -0.1
        return self.state, reward


class Agent:
    def __init__(self, enviornment, learning_rate=0.1, discount_factor=0.9, exploration_rate=1.0, exploration_decay=0.99):
        self.q_table = np.zeros((enviornment.size, enviornment.size, 4))
        self.enviornment = enviornment
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.exploration_decay = exploration_decay

    def choose_action(self, state):
        if random.uniform(0, 1) < self.exploration_rate:
            return random.choice([0, 1, 2, 3])
        return np.argmax(self.q_table[state[0], state[1]])

    def learn(self, state, action, reward, next_state):
        self.q_table[state[0], state[1], action] = self.learning_rate * (
            reward + self.discount_factor * np.max(
                self.q_table[next_state[0], next_state[1]] - self.q_table[state[0], state[1], action]
            )
        )

    def train(self, episodes=100):
        for _ in range(episodes):
            state = self.enviornment.reset()
            done = False
            while not done:
                action = self.choose_action(state)
                next_state, reward = self.enviornment.step(action)
                self.learn(state, action, reward, next_state)
                if reward > 0: done = True
                state = next_state
                self.exploration_rate *= self.exploration_decay


env = Enviornment(4)
agent = Agent(env)
agent.train()

state = env.reset()
done = False
while not done:
    action = agent.choose_action(state)
    print("Action:", action)
    next_state, reward = env.step(action)
    if reward > 0: done = True
    state = next_state

print("Reached Goal:", state)
