import pandas as pd

# Load any DataFrame (example using CSV)
df = pd.read_csv("output.csv")

# Display data types of each column
print("Column Data Types:")
print(df.dtypes)

import pandas as pd

# Example DataFrame with missing values
data = {
    "Name": ["kenl", "mihir", "milan"],
    "Age": [30, None, 35]     # Missing value in Age column
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Fill missing values in 'Age' column with mean
df['Age'] = df['Age'].fillna(df['Age'].mean())

print("\nDataFrame After Filling Missing Values:")
print(df)