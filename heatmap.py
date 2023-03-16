import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('/Users/sarge/Downloads/heatmap_cleaned.csv')

# Create a heatmap of player attributes by position
position_groups = df.groupby('Position')[df.columns[61:88]].mean().reset_index()
heatmap_data = position_groups.set_index('Position').T
sns.heatmap(heatmap_data, cmap='RdYlGn', linewidths=0.5, 
            annot=True, fmt='.2f', cbar=False)
plt.title('Player Attributes by Position in FIFA 19')
plt.xlabel('Position')
plt.ylabel('Attribute')

# Show the plot
plt.show()


