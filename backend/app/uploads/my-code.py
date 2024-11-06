
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = '/mnt/data/file-YsbK3gDiyNbVxMHyHcomq9wI'
df = pd.read_csv(file_path)

# Set the style for the plot to be professional
sns.set(style='whitegrid')

# Create a scatter plot of Sepal Width vs Sepal Length
plt.figure(figsize=(10, 6))
ax = sns.scatterplot(data=df, x='SepalLengthCm', y='SepalWidthCm', hue='Species', palette='muted', s=100)

# Set title and labels with a professional feel
plt.title('Relationship between Sepal Length and Sepal Width', fontsize=16)
plt.xlabel('Sepal Length (cm)', fontsize=14)
plt.ylabel('Sepal Width (cm)', fontsize=14)

# Customize the legend
plt.legend(title='Species', title_fontsize='13', fontsize='11')

# Save the plot as a PNG file
plt.savefig('/mnt/data/sepal_scatter_plot.png', bbox_inches='tight')
