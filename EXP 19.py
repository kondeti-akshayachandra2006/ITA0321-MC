
import numpy as np
import matplotlib.pyplot as plt

# Distance between nodes (meters)
distance = np.arange(1, 101, 1)

# Transmitted power (dBm)
Pt = 20

# Path loss model
path_loss = 20 * np.log10(distance) + 40

# Received signal strength
Pr = Pt - path_loss

# Display signal strength
for i in range(0, 100, 20):
    print("Distance:", distance[i], "m",
          "Signal Strength:", round(Pr[i], 2), "dBm")

# Plot signal strength
plt.plot(distance, Pr, 'b-', linewidth=2)

plt.xlabel("Distance between Nodes (m)")
plt.ylabel("Received Signal Strength (dBm)")
plt.title("Signal Strength Analysis Between Nodes")

plt.grid()
plt.show()
