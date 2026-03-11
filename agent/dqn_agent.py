import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

class DQN(nn.Module):

    def __init__(self, state_size, action_size):
        super(DQN, self).__init__()

        self.fc1 = nn.Linear(state_size, 64)
        self.fc2 = nn.Linear(64, 64)
        self.fc3 = nn.Linear(64, action_size)

    def forward(self, x):

        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        return self.fc3(x)


class Agent:

    def __init__(self, state_size, action_size):

        self.model = DQN(state_size, action_size)
        self.optimizer = optim.Adam(self.model.parameters(), lr=0.001)

        self.gamma = 0.95
        self.epsilon = 1.0
        self.epsilon_decay = 0.995
        self.epsilon_min = 0.01

        self.action_size = action_size

    def act(self, state):

        if np.random.rand() < self.epsilon:
            return np.random.randint(self.action_size)

        state = torch.FloatTensor(state)

        q_values = self.model(state)

        return torch.argmax(q_values).item()

    def train(self, state, action, reward, next_state):

        state = torch.FloatTensor(state)
        next_state = torch.FloatTensor(next_state)

        q_values = self.model(state)

        next_q_values = self.model(next_state)

        target = reward + self.gamma * torch.max(next_q_values)

        loss = (q_values[action] - target.detach()) ** 2

        self.optimizer.zero_grad()

        loss.backward()

        self.optimizer.step()

        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay