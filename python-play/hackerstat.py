# Hacker Statistics
# In a 100 storey building, move up and down floors on the roll of dice
# Move up +1 on getting a 3 or 4 or 5
# Move down -1 on getting 1 or 2
# On 6, roll die again and move +n steps (n is the number on second roll)

import numpy as np
import matplotlib.pyplot as plt
np.random.seed(123)

# Initialize all walks
all_walks = []

# 5000 random walks
for i in range(5000):
    # Random walk starting point
    random_walk = [0]
    # Roll the dice 100 times
    for x in range(100):
        step = random_walk[-1]
        dice = np.random.randint(1, 7)
        # Move up or down floors
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step += 1
        else:
            step += np.random.randint(1, 7)

        # There's a 0.1% chance of falling down
        if np.random.rand() <= 0.001:
            step = 0

        # Append taken step to Random Walk
        random_walk.append(step)
        # print(random_walk)
        # plt.plot(random_walk)
        # plt.show()
    all_walks.append(random_walk)

np_aw_t = np.transpose(np.array(all_walks))
plt.plot(np_aw_t)
plt.show()
plt.clf()

ends = np_aw_t[-1, :]
plt.hist(ends, bins=10)
plt.show()