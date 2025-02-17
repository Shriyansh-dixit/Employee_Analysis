import pandas as pd
import numpy as np

df = pd.read_csv("Employeee.csv")
# Remove rows with missing values
df = df.dropna()
# Fill missing numerical values with the median
df['Salary'] = df['Salary'].fillna(df['Salary'].median())

# Fill missing categorical values with the mode
df['Department'] = df['Department'].fillna(df['Department'].mode()[0])
# Remove duplicate rows
df = df.drop_duplicates()
# Standardize text columns to lowercase
df['Department'] = df['Department'].str.lower()
# Convert 'Age' to integer
df['Age'] = df['Age'].astype(int)

# Ensure 'Employee ID' is treated as a string (to avoid any numerical interpretation)
df['Employee ID'] = df['Employee ID'].astype(str)
# Check the cleaned data
print(df.info())
print(df.head())

# Save the cleaned data to a new file
df.to_csv("cleaned_employee_data.csv", index=False)

