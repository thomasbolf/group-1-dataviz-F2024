
# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
file_path = '/mnt/data/file-iSdAWtYRnu5icyG4PMWKIrNc'
data = pd.read_csv(file_path)

# Define the style and palette for a playful and vibrant look
sns.set(style="whitegrid")
palette = sns.color_palette("husl", 3)  # Using hues for vibrancy

# Create the scatter plot
plt.figure(figsize=(10, 6))
scatter_plot = sns.scatterplot(
    x='SepalLengthCm', 
    y='SepalWidthCm', 
    hue='Species', 
    style='Species',
    palette=palette,
    data=data,
    s=100, 
    edgecolor='w'
)

# Add titles and labels with a playful font
plt.title('Sepal Length vs Sepal Width', fontsize=16, fontweight='bold', color='navy')
plt.xlabel('Sepal Length (cm)', fontsize=12, color='teal')
plt.ylabel('Sepal Width (cm)', fontsize=12, color='teal')
plt.xticks(color='purple')
plt.yticks(color='purple')
plt.legend(title='Species', fontsize=10, title_fontsize='13', loc='upper right', frameon=True)

# Add more playful elements
plt.text(4.5, 4, "Iris Data!\nExplore the Sepals!", fontsize=14, color='darkorange', weight='bold')
plt.grid(True, linestyle='--', alpha=0.6)

# Save the plot as a .png file
image_file_path = '/mnt/data/sepal_scatter_plot.png'
plt.savefig(image_file_path, bbox_inches='tight', dpi=300)
plt.close()
