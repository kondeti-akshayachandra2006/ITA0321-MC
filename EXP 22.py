
import numpy as np
import matplotlib.pyplot as plt

# Number of users in the network
users = np.arange(1, 101, 10)

# Simulated network latency (ms)
latency = 10 + 0.5 * users + np.random.randint(0, 5, len(users))

# Display latency
for i in range(len(users)):
    print("Users:", users[i],
          "Latency:", latency[i], "ms")

# Plot latency trends
plt.plot(users, latency, 'bo-', linewidth=2)

plt.xlabel("Number of Users")
plt.ylabel("Latency (ms)")
plt.title("Latency Trends in a Simulated Mobile Network")

plt.grid()
plt.show()
