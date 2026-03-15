import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create date range for January 2025
dates = pd.date_range(start="2025-01-01", end="2025-01-31")

# Generate sinusoidal temperature pattern
days = np.arange(len(dates))
temperature = 15 + 10 * np.sin(2 * np.pi * days / len(dates))

# Create DataFrame
df = pd.DataFrame({
    "Date": dates,
    "Temperature": temperature
})

df.set_index("Date", inplace=True)

# Compute 7-day rolling average
df["Rolling_Avg"] = df["Temperature"].rolling(window=7).mean()

# Plot temperature and rolling average
plt.figure()
plt.plot(df.index, df["Temperature"], label="Daily Temperature")
plt.plot(df.index, df["Rolling_Avg"], label="7-Day Rolling Average")

plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title("Daily Temperature - January 2025")
plt.legend()

plt.show()

# Identify days where temperature > 20°C
hot_days = df[df["Temperature"] > 20]

print("Days when temperature was above 20°C:")
print(hot_days)