# default dictionary
# this skips the step of having to define an empty list when key is missing
from collections import defaultdict
ridership = defaultdict(list)

for date, stop, riders in entries:
    ridership[stop].append(riders)

# Print first 10 elements in a dictionary
# Convert dictonary items to list to be able to slice
print(list(ridership.items())[:10])

# Order in python dictionaries
from collections import OrderedDict
ridership_date = OrderedDict()

# add key date and value riders

# Print the first key in ridership_date
print(list(ridership_date.keys())[0])

# Pop the first item from ridership_date and print it
print(ridership_date.popitem(last=False))

# Print the last key in ridership_date
print(list(ridership_date.keys())[-1])

# Pop the last item from ridership_date and print it
print(ridership_date.popitem())
