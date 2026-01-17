import pandas as pd

file_path = "student_exam_scores.csv"
df = pd.read_csv(file_path)

print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])
print("\nFirst five rows:\n", df.head())
print("\nDataset size (rows * columns):", df.size)
print("\nMissing values:\n", df.isnull().sum())

num_cols = df.select_dtypes(include='number')

print("\nSum of numerical columns:\n", num_cols.sum())
print("\nAverage of numerical columns:\n", num_cols.mean())
print("\nMinimum values of numerical columns:\n", num_cols.min())
print("\nMaximum values of numerical columns:\n", num_cols.max())

summary_stats = pd.DataFrame({
    "Sum": num_cols.sum(),
    "Average": num_cols.mean(),
    "Min": num_cols.min(),
    "Max": num_cols.max()
})

summary_stats.to_csv("dataset_summary.csv")

print("\nSummary statistics exported to 'dataset_summary.csv'")
