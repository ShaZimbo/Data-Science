""" Numpy array with numbers from 1 to 48 and data manipulation."""
import numpy as np

arr = np.arange(1, 49).reshape(3, 4, 4)
print(arr)

# Select the second sub-matrix, first row, last entry
print(f"\n1:\n{arr[1, 0, 3]}")

# Select the first sub-matrix, third row
print(f"\n2:\n{arr[0, 2]}")

# Select the entire third sub-matrix
print(f"\n3:\n{arr[2]}")

# Select the first two entries of the second row from each sub-matrix
print(f"\n4 as array(no comma):\n{arr[0:3, 1, 0:2]}")

# Print the first two entries of the second row
# From each sub-matrix as a string
print(f"\n4 as string (with comma):\n["
      f"{arr[0, 1, 0:2]}, "
      f"{arr[1, 1, 0:2]} "
      f"{arr[2, 1, 0:2]}]"
      )

# Select the last two entries of each row
# In the third sub-matrix in reverse order
print(f"\n5:\n{arr[2, 0:4, :-3:-1]}")

# Select the first entry of each row in each sub-matrix,
# Then reverse the order of entries
first_num = arr[:, :, 0]
print(f"\n6:\n{first_num[0:4, ::-1]}")

# Select the first and last entry from the first row of the first sub-matrix
# Select the first and last entry from the last row of the third sub-matrix
# Stack the results vertically
top = arr[0, 0, ::3]
bottom = arr[2, 3, ::3]
top_bottom = np.vstack([top, bottom])
print(f"\n7 as an array:\n{top_bottom}")

# Provide the results without np.vstack as a string
print(f"\n7 as a string:\n[{arr[0, 0, ::3]}{arr[2, 3, ::3]}]")

# Select the last two rows of the second sub-matrix
# Select the first two rows of the third sub-matrix
# Stack the results vertically
print("\n8 as array (no commas):")
top = arr[1, 2:4, 0:5]
bottom = arr[2, 0:2, 0:5]
top_bottom = np.vstack([top, bottom])
print(f"{top_bottom}")

# Provide the results without np.vstack as a string
print(f"\n8 as string (with commas):\n[{arr[1, 2, 0:5]}, "
      f"{arr[1, 3, 0:5]}, {arr[2, 0, 0:5]}, {arr[2, 1, 0:5]}]"
      )
