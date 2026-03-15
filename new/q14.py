import numpy as np

# Generate 1000 random numbers from normal distribution
data = np.random.normal(loc=50, scale=5, size=1000)

# Mean
mean_value = np.mean(data)

# Median
median_value = np.median(data)

# Standard Deviation
std_dev = np.std(data)

# Variance
variance = np.var(data)

# Percentiles
percentile_25 = np.percentile(data, 25)
percentile_75 = np.percentile(data, 75)

print("Mean:", mean_value)
print("Median:", median_value)
print("Standard Deviation:", std_dev)
print("Variance:", variance)
print("25th Percentile:", percentile_25)
print("75th Percentile:", percentile_75)