import random

num_trials = 100000  # number of trials to run
count_E_F = 0  # count of trials where both E and F occurred
count_F = 0  # count of trials where F occurred

# Part A
for i in range(num_trials):
    coin_tosses = [random.choice(['H', 'T']) for _ in range(3)]
    if coin_tosses[:2] == ['H', 'H']:
        count_F += 1
        if coin_tosses[2] == 'H':
            count_E_F += 1

print("(A) Simulated probability of E given F:", count_E_F / count_F)


# Part B
count_E_F = 0 
count_F = 0

for i in range(num_trials):
    coin_tosses = [random.choice(['H', 'T']) for _ in range(3)]
    if coin_tosses.count('H') <= 2:
        count_F += 1
        if coin_tosses.count('H') >= 2:
            count_E_F += 1

print("(B) Simulated probability of E given F:", count_E_F / count_F)


# Part C
count_E_F = 0 
count_F = 0

for i in range(num_trials):
    coin_tosses = [random.choice(['H', 'T']) for _ in range(3)]
    if 'T' in coin_tosses:
        count_F += 1
        if coin_tosses.count('T') <= 2:
            count_E_F += 1

print("(C) Simulated probability of E given F:", count_E_F / count_F)