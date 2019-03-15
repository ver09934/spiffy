import numpy as np

vals = np.array([1, 1, 1, 1, 1, 1, 1, 0])

x = 0
for i in range(0, vals.size):
	x = x | vals[i]
	if i < vals.size - 1:
		x = x << 1

print(x)

for i in range(0, 8):
	print(x & 1)
	x = x >> 1

