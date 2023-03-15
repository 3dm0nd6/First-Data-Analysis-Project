import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv('/Path/to/file.csv')

# Calculate the potential increase for each player
data['Potential Increase'] = data['Potential'] - data['Overall']

# Group the data by club and calculate the total potential increase for each club
club_totals = data.groupby('Club')['Potential Increase'].sum()

# Sort the clubs in descending order based on their total potential increase
club_totals = club_totals.sort_values(ascending=False)

# Select the top 50 clubs with the highest total potential increase
top_clubs = club_totals.iloc[0:50]

# Create a bar chart showing the total potential increase for each of the top 50 clubs
plt.bar(top_clubs.index, top_clubs.values)

# Add labels and title to the chart
plt.xlabel('Club')
plt.ylabel('Total Potential Increase')
plt.title('Top 50 Clubs by Total Potential Increase')

# Rotate the x-axis labels to avoid overlap
plt.xticks(rotation=90)

# Show the chart
plt.show()
