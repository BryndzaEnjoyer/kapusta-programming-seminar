import pandas as pd

data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}

df = pd.DataFrame(data)

# Sum along columns (default: axis=0)
col_sum = df.sum()

# Sum along rows (axis=1)
row_sum = df.sum(axis=1)
print("data", df)
print("Column-wise sum:\n", col_sum)
print("\nRow-wise sum:\n", row_sum)