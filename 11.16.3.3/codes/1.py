import numpy as np
import matplotlib.pyplot as plt

# Define the sample space of the die roll
sample_space = [0,1, 2, 3, 4, 5, 6,7]

# Define the probability distribution of the die roll
prob_dist = [0,0,1/6, 1/6, 1/6, 1/6, 1/6, 1/6]

# Calculate the cumulative probabilities for the die roll
cumulative_prob = np.cumsum(prob_dist)

# Plot the CDF
plt.step(sample_space, cumulative_prob)
plt.title("Cumulative Distribution Function")
plt.xlabel("Number on the Die")
plt.grid('on')
plt.ylabel("Cumulative Probability")
plt.savefig("../figs/fig.png")