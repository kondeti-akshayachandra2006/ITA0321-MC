
import numpy as np
import matplotlib.pyplot as plt

# Number of users and time slots
users = 4
slots = 100

# Available data rates for each user (Mbps)
np.random.seed(1)
rates = np.random.randint(1, 20, (slots, users))

# Round Robin Scheduling
rr = np.zeros(users)

for t in range(slots):
    user = t % users
    rr[user] += rates[t, user]

# Proportional Fair Scheduling
pf = np.zeros(users)
avg = np.ones(users)

for t in range(slots):
    metric = rates[t] / avg
    user = np.argmax(metric)

    pf[user] += rates[t, user]
    avg = 0.9 * avg
    avg[user] += 0.1 * rates[t, user]

# Jain's Fairness Index
def fairness(x):
    return (np.sum(x) ** 2) / (len(x) * np.sum(x ** 2))

print("Round Robin Throughput:", rr)
print("Round Robin Fairness:", fairness(rr))

print("Proportional Fair Throughput:", pf)
print("Proportional Fair Fairness:", fairness(pf))

# Plot throughput
plt.bar(np.arange(users) - 0.2, rr, width=0.4, label="Round Robin")
plt.bar(np.arange(users) + 0.2, pf, width=0.4, label="Proportional Fair")

plt.xlabel("Users")
plt.ylabel("Throughput")
plt.title("OFDMA Scheduling and Fairness")
plt.legend()
plt.grid()
plt.show()
