
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv(file_path)

# Set the style for a futuristic and digital look
plt.style.use('dark_background')
sns.set_palette("husl")

# Create a scatter plot to analyze the relationship between Sepal Width and Sepal Length
plt.figure(figsize=(14, 8))
sns.scatterplot(data=data, x='SepalLengthCm', y='SepalWidthCm', hue='Species', s=100, alpha=0.7, edgecolor='w')

# Adding titles and labels
plt.title('Analysis of Sepal Dimensions in Different Iris Species', fontsize=20, fontweight='bold', color='#0ff')
plt.xlabel('Sepal Length (cm)', fontsize=15, color='#0ff')
plt.ylabel('Sepal Width (cm)', fontsize=15, color='#0ff')

# Save the visual to a .png file
plt.savefig('sepal_analysis.png', bbox_inches='tight', dpi=300)

# Show the plot
plt.show()
