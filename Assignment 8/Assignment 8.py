import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

df = pd.read_csv('weight-height.csv')
df.head()

# #### 1. Verify the Central Limit Theorem using the ”Height” feature of the data.
means = []
for i in range(1000):
    sample = df['Height'].sample(100)
    means.append(sample.mean())

plt.hist(means);


# #### 2. Perform the Bootstrap on ”Height” feature of the data.
samples = 10000
sample_size = 1000
means = []
for i in range(samples):
    means.append(np.mean(np.random.choice(df['Height'], sample_size, replace=True)))

plt.hist(means);
standard_error = np.std(means)/math.sqrt(sample_size)
print('Standard Error: ', standard_error)


# #### 3. Calculate the Confidence Interval of 95 % using sample means derived using Bootstrap
CI = 0.95
sorted_means = np.sort(means)
length = len(sorted_means)
idx = math.floor(length*(1-CI)/2)
print('Upper Bound:', sorted_means[idx])
print('Lower Bound:', sorted_means[length-idx])


