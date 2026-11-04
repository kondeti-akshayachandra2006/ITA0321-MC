
import numpy as np
import matplotlib.pyplot as plt

# Frequency reuse factors
N = np.array([1, 3, 4, 7, 9, 12])

# Total available channels
total_channels = 120

# Channels per cell
capacity = total_channels / N

# Calculate co-channel interference
interference = 1 / N

# Plot capacity
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.plot(N, capacity, 'bo-', linewidth=2)
plt.xlabel("Frequency Reuse Factor")
plt.ylabel("Channels per Cell")
plt.title("Frequency Reuse vs Capacity")
plt.grid()

# Plot interference
plt.subplot(1, 2, 2)
plt.plot(N, interference, 'ro-', linewidth=2)
plt.xlabel("Frequency Reuse Factor")
plt.ylabel("Relative Interference")
plt.title("Frequency Reuse vs Interference")
plt.grid()

plt.tight_layout()
plt.show()
