import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('/Users/sarge/Downloads/ad_cleaned.csv')

# Create a histogram
plt.hist(df['Age'], bins=20)

# Set the chart title and axis labels
plt.title('Age Distribution of FIFA 19 Players')
plt.xlabel('Age')
plt.ylabel('Number of Players')

# Show the plot
plt.show()
