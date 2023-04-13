import numpy as np
from scipy.stats import bernoulli

# Number of trials
n_trials = int(1e6)

# Bernoulli random variables for three coin tosses
X1 = bernoulli.rvs(0.5, size=n_trials)
X2 = bernoulli.rvs(0.5, size=n_trials)
X3 = bernoulli.rvs(0.5, size=n_trials)

# (A) E: head on third toss, F: heads on first two tosses
F_a = (X1 + X2 == 2)
EF_a = np.sum(X3[F_a] == 1)
Pr_E_given_F_a = EF_a / np.sum(F_a)
print("Pr(E|F) for a) is:", Pr_E_given_F_a)

# (B) E: at least two heads, F: at most two heads
F_b = (X1 + X2 + X3 <= 2)
EF_b = np.sum((X1 + X2 + X3 >= 2) & F_b)
Pr_E_given_F_b = EF_b / np.sum(F_b)
print("Pr(E|F) for b) is:", Pr_E_given_F_b)

# (C) E: at most two tails, F: at least one tail
F_c = (X1 + X2 + X3 >= 1)
EF_c = np.sum((X1 + X2 + X3 <= 2) & F_c)
Pr_E_given_F_c = EF_c / np.sum(F_c)
print("Pr(E|F) for c) is:", Pr_E_given_F_c)