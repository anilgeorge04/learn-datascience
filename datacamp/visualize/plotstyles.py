from matplotlib import pyplot as plt

# check available styles
# this is similar to choosing bootstrap for css
print(plt.style.available)
plt.style.use('seaborn')

# dataframes: ransom, suspect1 and suspect2 with letter and frequency

# Plot each line
plt.plot(ransom.letter, ransom.frequency,
         label='Ransom', linestyle=':', color='gray')
plt.plot(suspect1.letter, suspect1.frequency, label='Fred Frequentist')
plt.plot(suspect2.letter, suspect2.frequency, label='Gertrude Cox')

# Add x- and y-labels
plt.xlabel("Letter")
plt.ylabel("Frequency")

# Add a legend
plt.legend()

# Display plot
plt.show()