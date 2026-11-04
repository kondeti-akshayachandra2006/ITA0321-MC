
import numpy as np

# Walsh codes
codes = np.array([
    [1, 1, 1, 1],
    [1, -1, 1, -1],
    [1, 1, -1, -1],
    [1, -1, -1, 1]
])

# User data bits
data = np.array([1, -1, 1, -1])

# Spread data using Walsh codes
signals = data[:, None] * codes

# Combined transmitted signal
transmitted = np.sum(signals, axis=0)

print("Walsh Codes:")
print(codes)

print("\nUser Data:")
print(data)

print("\nTransmitted Signal:")
print(transmitted)

# Receiver: Decode each user's data
print("\nReceived Data:")
for i in range(len(codes)):
    received = np.dot(transmitted, codes[i]) / len(codes[i])
    print("User", i + 1, ":", received)
