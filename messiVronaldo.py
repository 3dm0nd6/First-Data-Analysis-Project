import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('/Users/sarge/Downloads/messiVronaldo.csv')

# Select two players to compare
player1 = df[df['Name'] == 'Lionel Messi']
player2 = df[df['Name'] == 'Cristiano Ronaldo']

# Select the attributes to compare
attributes = ['Crossing', 'Finishing', 'Dribbling', 'Interceptions', 'Marking']

# Create a radar chart
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111, polar=True)
ax.plot(attributes, player1[attributes].values[0], label=player1['Name'].values[0])
ax.plot(attributes, player2[attributes].values[0], label=player2['Name'].values[0])
ax.fill(attributes, player1[attributes].values[0], alpha=0.1)
ax.fill(attributes, player2[attributes].values[0], alpha=0.1)

# Set the chart title and axis labels
plt.title('Comparison of Messi vs. Ronaldo Attributes in FIFA 19')
ax.set_theta_offset(0)
ax.set_theta_direction(-1)
ax.legend()

# Show the plot
plt.show()
