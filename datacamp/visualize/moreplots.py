from matplotlib import pyplot as plt

# Scatter plot
plt.scatter(x, y, color='red', marker='s', alpha=0.1)
plt.ylabel("Y label")
plt.xlabel('X axis')

# Bar chart, error bars
plt.bar(x, y, yerr=col_err)

# Horizontal bar plot
plt.barh(x, y)

# Stacked bar chart
plt.bar(df.precinct, df.dog, label='dog')
plt.bar(df.precinct, df.cat, bottom='df.dog', label='Cat')


# Plot the number of hours spent on desk work
plt.bar(hours.officer, hours.desk_work, label='Desk Work')

# Plot the hours spent on field work on top of desk work
plt.bar(hours.officer, hours.field_work, bottom=hours.desk_work, label="Field Work")

# Add a legend
plt.legend()

# Display the plot
plt.show()

# Histograms
plt.hist(gravel.mass) # default 10 bins
plt.hist(data, bins=40)
plt.hist(data, range=(xmin, xmax))

# Unnormalized
plt.hist(male_weight) # large sample
plt.hist(female_weight) # small sample

# Normalize, i.e. sum of bar area =1 
plt.hist(male_weight, density=True)
plt.hist(female_weight, density=True)
# this allows to understand the proprotion of each population in a comparable way


# Change the range to start at 5 and end at 35
plt.hist(puppies.weight, range=(5, 40), bins=50)

# Add labels
plt.xlabel('Puppy Weight (lbs)')
plt.ylabel('Number of Puppies')

# Display
plt.show()

# Create a histogram
plt.hist(gravel.radius,
         bins=40,
         range=(2, 8),
         density=True)

# Label plot
plt.xlabel('Gravel Radius (mm)')
plt.ylabel('Frequency')
plt.title('Sample from Shoeprint')

# Display histogram
plt.show()