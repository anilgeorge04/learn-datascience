# can use conditionals within the list comprehensions
# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship with 7+ characters in their names else empty string
new_fellowship = [member if len(member) > 6 else "" for member in fellowship]

# Print the new list
print(new_fellowship)

# can use the same concept for dict comprehensions too

# Create dict comprehension: new_fellowship
new_fellowship_dict = {member:len(member) for member in fellowship}

# Print the new dictionary
print(new_fellowship_dict)
