# Simulation-Based Inference for an Adaptive-Network Epidemic Model
This project studies the spread of infectious diseases on adaptive contact networks, where both the epidemic dynamics and the network structure evolve over time.

We model disease transmission using a stochastic Susceptible–Infected–Recovered (SIR) framework:
β (beta): infection rate
γ (gamma): recovery rate
ρ (rho): rewiring rate where susceptible individuals avoid infected neighbors

Unlike standard SIR models on static graphs, observed individuals adapt their connections, creating a co-evolving system of network dynamics and disease spread.

Problem Setup
Individuals are represented as nodes in a network
Edges represent contacts through which infection can spread
Susceptible nodes may rewire connections away from infected nodes
The system evolves stochastically over time

Dataset:
infected_timeseries.csv	
rewiring_timeseries.csv	
final_degree_histograms.csv

Methods:
- Standard ABC with selected summary statistics
- Regression-adjusted ABC
As the space of possible network configurations is enormous, this likelihood cannot be computed. These approaches allow us to approximate the posterior distribution of θ without evaluating the likelihood.

# GitHub Repository Navigation
Explanation of Directories and Files:
```
ST3247_GROUP5/
├── ABC Script/
│ ├── Experimentation_1.ipynb       # initial experiments on a subset of summary statistics
│ └── Experimentation_2.ipynb       # experiments on a separate subset of summary statistics
├── Regression Adjustment ABC Script/  
│ └── Experimentation_2.ipynb       # code for Regression Adjustment ABC
├── Datasets_n_simulator/
│ ├── final_degree_histograms.csv 	     # observed dataset of final degree histograms
│ ├── infected_timeseries.csv            # observed timeseries dataset of infected
│ ├── rewiring_timeseries.csv	         # observed timeseries dataset of rewiring
│ └── simulator.py              # python code for generating observations
├── .gitignore                  # files excluded from version control
├── README.md                   # project documentation
└── requirements.txt            # Python dependencies ABC and Regression Adjustment ABC
```