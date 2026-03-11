import traci
import numpy as np

class SumoEnv:

    def __init__(self, config_path):
        self.config = config_path

    def start(self):
        traci.start(["sumo-gui", "-c", self.config])

    def reset(self):
        traci.load(["-c", self.config])

    def get_state(self):

        speed = traci.vehicle.getSpeed("agent_car")

        leader = traci.vehicle.getLeader("agent_car")

        if leader:
            dist = leader[1]
        else:
            dist = 100

        state = np.array([speed, dist])

        return state

    def step(self, action):

        if action == 0:
            traci.vehicle.setSpeed("agent_car", 10)

        elif action == 1:
            traci.vehicle.setSpeed("agent_car", 20)

        elif action == 2:
            traci.vehicle.slowDown("agent_car", 5, 5)

        traci.simulationStep()

        next_state = self.get_state()

        reward = next_state[0] * 0.1

        done = traci.simulation.getMinExpectedNumber() <= 0

        return next_state, reward, done