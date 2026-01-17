import pandas as pd

# Load dataset
df = pd.read_csv("student_exam_scores.csv")

# Define a function to categorize exam scores
def performance_category(score):
    if score < 30:
        return "Low"
    elif score <= 40:
        return "Medium"
    else:
        return "High"

# Create new categorical column
df['performance_level'] = df['exam_score'].apply(performance_category)

# Save the modified dataframe if needed
df.to_csv("student_exam_scores_with_perf.csv", index=False)

# Display first rows to check new column
print(df[['student_id', 'exam_score', 'performance_level']].head())
