import pandas as pd


df = pd.read_csv('input.csv')  


print("\n--- Dataset Information ---")
print(f"Number of rows: {df.shape[0]}")
print(f"Number of columns: {df.shape[1]}")
print(f"Shape: {df.shape}")
print(f"Dataset size (total elements): {df.size}")

print("\n--- First 5 Rows ---")
print(df.head())

print("\n--- Missing Values per Column ---")
print(df.isnull().sum())


print("\n--- Numerical Column Statistics ---")
print("Sum:\n", df.sum(numeric_only=True))
print("Average:\n", df.mean(numeric_only=True))
print("Minimum:\n", df.min(numeric_only=True))
print("Maximum:\n", df.max(numeric_only=True))

print("\n--- Full Description of Numerical Data ---")
print(df.describe())


df.to_csv('output.csv', index=False)
print("\nData exported to 'output.csv' successfully!")
