import numpy as np


data = np.random.randint(1, 100, (8, 5))
print("Original array:\n", data)


sorted_rows_desc = np.sort(data, axis=1)[:, ::-1]
print("\nRows sorted in descending order:\n", sorted_rows_desc)


sorted_by_second = data[data[:, 1].argsort()]
print("\nRows sorted by second column:\n", sorted_by_second)


row_sums = data.sum(axis=1)
max_index = np.argmax(row_sums)

print("\nRow sums:", row_sums)
print("Index of row with highest total sum:", max_index)