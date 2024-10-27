
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load data
data = pd.read_csv('/mnt/data/file-L0SCHiKumJO2eTDsYFbj40ak')

# Set the playful style for the plot
sns.set(style="whitegrid")

# Create a scatter plot
plt.figure(figsize=(10, 6))
scatter_plot = sns.scatterplot(
    data=data, 
    x='SepalLengthCm', 
    y='SepalWidthCm', 
    hue='Species',
    palette='Set1', 
    s=100, 
    edgecolor='w'
)

# Setting title and labels
plt.title('Sepal Width vs Sepal Length by Species', fontsize=14, weight='bold')
plt.xlabel('Sepal Length (cm)', fontsize=12)
plt.ylabel('Sepal Width (cm)', fontsize=12)

# Lively additions, for example using star markers to add a playful element
scatter_plot.set_xticks(range(4, 9))
scatter_plot.set_xticklabels(['🌟4', '🌟5', '🌟6', '🌟7', '🌟8'], fontsize=10)
scatter_plot.set_yticks(range(2, 6))
scatter_plot.set_yticklabels(['✷2', '✷3', '✷4', '✷5'], fontsize=10)

# Save the plot
plt.savefig('/mnt/data/sepal_width_vs_length.png', format='png')
plt.show()
