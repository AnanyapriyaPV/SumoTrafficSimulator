from environment.sumo_env import SumoEnv
from agent.dqn_agent import Agent

env = SumoEnv("config/simulation.sumocfg")

agent = Agent(state_size=2, action_size=3)

env.start()

episodes = 10

for ep in range(episodes):

    env.reset()

    state = env.get_state()

    done = False

    while not done:

        action = agent.act(state)

        next_state, reward, done = env.step(action)

        agent.train(state, action, reward, next_state)

        state = next_state

print("Training finished")