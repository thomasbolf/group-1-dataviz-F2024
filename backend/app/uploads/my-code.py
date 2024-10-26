
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = '/mnt/data/file-ctfOc2xVq7gHZlREbDL7mfmW'
data = pd.read_csv(file_path)

# Set a playful theme for the plot
sns.set_theme(style="whitegrid", palette="pastel")

# Create a scatter plot using Seaborn with vibrant colors for different species
plt.figure(figsize=(10, 6))
scatter_plot = sns.scatterplot(data=data, x='SepalLengthCm', y='SepalWidthCm', hue='Species', 
                               palette='Set2', s=100, edgecolor='w', alpha=0.8)

# Add title and labels with a playful font size
plt.title('Playful Visualization of Sepal Width vs Sepal Length', fontsize=14, fontweight='bold')
plt.xlabel('Sepal Length (cm)', fontsize=12)
plt.ylabel('Sepal Width (cm)', fontsize=12)

# Enhance the legend
plt.legend(title='Iris Species', title_fontsize='13', loc='best', fontsize='11')

# Save the plot
plt.savefig('/mnt/data/playful_scatter_plot.png', dpi=300)
plt.show()
