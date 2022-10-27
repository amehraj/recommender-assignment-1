import pandas as pd
df = pd.read_csv('ratings.csv')
#Display the first 10 rows
print('Row count is:', len(df))
result = df.head(10)
print("First 10 rows of the DataFrame:")
print(result)