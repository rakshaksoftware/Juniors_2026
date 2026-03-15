import pandas as pd

# Create the DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Ethan"],
    "Age": [28, 34, 25, 42, 30],
    "Salary": [70000, 80000, 50000, 110000, 75000]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Add a new column Tax (20% of Salary)
df["Tax"] = df["Salary"] * 0.20

print("\nDataFrame after adding Tax column:")
print(df)

# Filter employees aged 30 and above
filtered_df = df[df["Age"] >= 30]

print("\nEmployees aged 30 and above:")
print(filtered_df)

# Average salary of employees aged below 30
avg_salary = df[df["Age"] < 30]["Salary"].mean()

print("\nAverage salary of employees below 30:")
print(avg_salary)

# Sort DataFrame by Salary in descending order
sorted_df = df.sort_values(by="Salary", ascending=False)

print("\nDataFrame sorted by Salary (descending):")
print(sorted_df)