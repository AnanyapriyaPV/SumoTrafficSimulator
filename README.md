# Reinforcement Learning Based Autonomous Vehicle Simulation

This project simulates **Reinforcement Learning (RL) based autonomous vehicles** using the **SUMO traffic simulator**.  
The simulation environment is built using **OpenStreetMap data of Anna University – MIT campus**.

---

## Features

- RL-based autonomous vehicle decision making
- Real-world road network generated from OpenStreetMap
- Traffic simulation using SUMO
- Configurable traffic scenarios

---

## Technologies Used

- Python
- SUMO (Simulation of Urban Mobility)
- Reinforcement Learning
- OpenStreetMap (OSM)

---

## Project Structure

```
Traffic-Simulator/
│
├── config/
│   └── simulation.sumocfg
│
├── network/
│
├── routes/
│
├── scripts/
│
└── README.md
```

---

## Running the Simulation

Run the following command from the project directory:

```bash
sumo-gui -c config/simulation.sumocfg
```

---

## Environment

- Python 3.x
- SUMO Traffic Simulator
- OpenStreetMap road network

---

## Author

Developed as part of a **Machine Learning Labaratory**.