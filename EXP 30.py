import numpy as np
import matplotlib.pyplot as plt

# Network load (number of packets)
load = np.array([20, 40, 60, 80, 100])

# Simulated network performance values
sent = load
received = np.array([19, 37, 54, 68, 80])

# Calculate Packet Delivery Ratio (PDR)
pdr = (received / sent) * 100

# Calculate Throughput (Mbps)
throughput = np.array([1.8, 3.5, 4.8, 5.6, 6.0])

# Average delay (milliseconds)
delay = np.array([10, 15, 22, 30, 42])

# Display results
print("Network Load | PDR (%) | Throughput (Mbps) | Delay (ms)")
for i in range(len(load)):
    print(load[i], "         ", round(pdr[i], 2),
          "       ", throughput[i], "            ", delay[i])

# Plot performance graphs
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.plot(load, pdr, marker='o')
plt.title("MANET Performance Analysis")
plt.ylabel("PDR (%)")
plt.grid()

plt.subplot(3, 1, 2)
plt.plot(load, throughput, marker='o', color='green')
plt.ylabel("Throughput (Mbps)")
plt.grid()

plt.subplot(3, 1, 3)
plt.plot(load, delay, marker='o', color='red')
plt.xlabel("Network Load (Packets)")
plt.ylabel("Delay (ms)")
plt.grid()

plt.tight_layout()
plt.show()
