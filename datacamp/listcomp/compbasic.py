# Takes out the for loop and builds lists in single lines from iterables

# Create list comprehension: squares
squares = [i ** 2 for i in range(0,10)]

# Create a 4 x 5 matrix using a list of lists: matrix
matrix = [[col for col in range(1,5)] for row in range(0,5)]

# Print the matrix
for row in matrix:
    print(row)
