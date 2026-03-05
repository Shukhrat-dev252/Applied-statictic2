import numpy as np


arr = np.random.randint(1, 100, 10)
print("Original array:", arr)

sorted_arr = np.sort(arr)
print("Sorted array:", sorted_arr)



matrix = np.random.randint(1, 100, (5, 3))
print("\nOriginal matrix:")
print(matrix)

sorted_rows = matrix[matrix[:, 1].argsort()]
print("\nRows sorted by second column:")
print(sorted_rows)



arr2 = np.random.randint(1, 100, 15)
print("\nArray:", arr2)

top5 = arr2[np.argsort(arr2)[-5:]]
print("Top 5 largest values:", top5)