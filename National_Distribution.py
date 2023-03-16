import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('/Users/sarge/Downloads/kl_cleaned.csv')

# Count the number of players from each nationality
nationality_counts = df['Nationality'].value_counts()

# Create a bar chart
plt.bar(nationality_counts.index, nationality_counts.values)

# Set the chart title and axis labels
plt.title('Nationality Distribution of FIFA 19 Players')
plt.xlabel('Nationality')
plt.ylabel('Number of Players')

# Rotate the x-axis labels to avoid overlapping
plt.xticks(rotation=90)

# Show the plot
plt.show()
