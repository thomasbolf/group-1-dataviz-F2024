import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
file_path = 'file-YEy6KcReHex8c2BxHYq38F7F'
data = pd.read_csv(file_path)

# Set up the visual style
sns.set(style="whitegrid", palette="pastel")

# Create a playful and informative scatter plot with SepalWidthCm and SepalLengthCm
plt.figure(figsize=(10, 6))
scatter_plot = sns.scatterplot(data=data, x='SepalLengthCm', y='SepalWidthCm', hue='Species', s=100, palette='bright', alpha=0.7)

# Add titles and labels
scatter_plot.set_title('Relationship between Sepal Width and Sepal Length', fontsize=16, fontweight='bold')
scatter_plot.set_xlabel('Sepal Length (cm)', fontsize=12)
scatter_plot.set_ylabel('Sepal Width (cm)', fontsize=12)

# Additional playful elements
plt.gca().set_facecolor('#f9f9f9')

# Save the plot
plt.savefig('sepal_relationship.png')
