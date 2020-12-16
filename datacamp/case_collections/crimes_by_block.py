from collections import Counter
from collections import defaultdict
from datetime import datetime

# crimes_by_block dictionary uses block name as key and contains list of crimes

# Create a unique list of crimes for the first block: n_state_st_crimes
n_state_st_crimes = set(crimes_by_block['001XX N STATE ST'])

# Print the list
print(n_state_st_crimes)

# Create a unique list of crimes for the second block: w_terminal_st_crimes
w_terminal_st_crimes = set(crimes_by_block['0000X W TERMINAL ST'])

# Print the list
print(w_terminal_st_crimes)

# Find the differences between the two blocks: crime_differences
# crimes in first block but not in second
crime_differences = n_state_st_crimes - w_terminal_st_crimes

# Print the differences
print(crime_differences)
