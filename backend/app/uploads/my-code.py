
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Reading the data from the uploaded file
file_path = '/mnt/data/file-r6MYl4qHzLHXwf8NVIbPHsr0'
data = pd.read_csv(file_path)

# Set up a playful style using seaborn
sns.set_theme(style="whitegrid")

# Create the scatter plot with vibrant colors
plt.figure(figsize=(10, 6))
scatter_plot = sns.scatterplot(data=data, x='SepalLengthCm', y='SepalWidthCm', hue='Species', palette='bright')

# Customizing the plot to be playful and engaging
plt.title('Relationship between Sepal Width and Sepal Length', fontsize=16, fontweight='bold')
plt.xlabel('Sepal Length (cm)', fontsize=14)
plt.ylabel('Sepal Width (cm)', fontsize=14)

# Adding some lively elements like grid and legend
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend(title='Species', title_fontsize='13', loc='upper right', fontsize='11')

# Save the plot as a PNG file
plt.savefig('/mnt/data/sepal_relationship.png')
plt.show()
