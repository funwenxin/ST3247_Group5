
import numpy as np
def simulate(beta, gamma, rho, N=200, p_edge=0.05,
             n_infected0=5, T=200, rng=None):

    if rng is None:
        rng = np.random.default_rng()

    # -------------------------
    # Build graph
    # -------------------------
    neighbors = [set() for _ in range(N)]
    for i in range(N):
        for j in range(i + 1, N):
            if rng.random() < p_edge:
                neighbors[i].add(j)
                neighbors[j].add(i)

    # -------------------------
    # Initial state
    # -------------------------
    state = np.zeros(N, dtype=np.int8)
    initial_infected = rng.choice(N, size=n_infected0, replace=False)
    state[initial_infected] = 1

    infected_nodes = set(initial_infected)

    infected_fraction = np.zeros(T + 1)
    rewire_counts = np.zeros(T + 1, dtype=np.int64)

    infected_fraction[0] = len(infected_nodes) / N

    # -------------------------
    # Simulation loop
    # -------------------------
    for t in range(1, T + 1):

        # =========================
        # PHASE 1: Infection
        # =========================
        new_infections = set()

        for i in infected_nodes:
            for j in neighbors[i]:
                if state[j] == 0 and rng.random() < beta:
                    new_infections.add(j)

        for j in new_infections:
            state[j] = 1

        # IMPORTANT: include newly infected BEFORE recovery
        infected_nodes |= new_infections

        # =========================
        # PHASE 2: Recovery
        # =========================
        # ✔ Matches professor: includes newly infected nodes
        recovered = set()

        for i in infected_nodes:
            if rng.random() < gamma:
                state[i] = 2
                recovered.add(i)

        infected_nodes -= recovered

        # =========================
        # PHASE 3: Rewiring
        # =========================
        rewire_count = 0

        for s_node in range(N):
            if state[s_node] != 0:
                continue

            nbrs = list(neighbors[s_node])  # snapshot

            for i_node in nbrs:
                if state[i_node] != 1:
                    continue

                if rng.random() < rho:

                    # Edge might already be removed
                    if i_node not in neighbors[s_node]:
                        continue

                    # Remove edge
                    neighbors[s_node].discard(i_node)
                    neighbors[i_node].discard(s_node)

                    # Rejection sampling for new partner
                    while True:
                        k = rng.integers(N)
                        if k != s_node and k not in neighbors[s_node]:
                            break

                    neighbors[s_node].add(k)
                    neighbors[k].add(s_node)

                    rewire_count += 1

        # =========================
        # Record stats
        # =========================
        infected_fraction[t] = len(infected_nodes) / N
        rewire_counts[t] = rewire_count

    # -------------------------
    # Degree histogram
    # -------------------------
    degree_histogram = np.zeros(31, dtype=np.int64)
    for i in range(N):
        deg = min(len(neighbors[i]), 30)
        degree_histogram[deg] += 1

    return infected_fraction, rewire_counts, degree_histogram
