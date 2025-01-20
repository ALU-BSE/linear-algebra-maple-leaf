import pandas as pd
import numpy as np

# Load data
data = pd.read_csv('path/to/data')

# Example arrays
Prices = [[300, 500],
          [1000, 120.85]]

Array2 = [200, 100]

# Calculate the result
Ans = []
# (300*200 + 500*100) as an example calculation

# Iterate through each row in the Prices matrix
for i in range(len(Prices)):
    row_sum = 0  # Initialize the sum for the current row
    for j in range(len(Prices[0])):
        # Multiply each element in the row by the corresponding element in Array2
        row_sum += Prices[i][j] * Array2[j]
        # # Append the row sum to the result list
        Ans.append(row_sum)  # Append the row sum to the result list

# Print the final result
print("Total costs for each row:", Ans)
