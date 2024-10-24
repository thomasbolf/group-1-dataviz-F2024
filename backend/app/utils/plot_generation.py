
import matplotlib.pyplot as plt
import base64
from io import BytesIO

def generate_plot(data):
    plt.figure(figsize=(10, 6))
    # Example plot (a line chart):
    plt.plot(data[data.columns[0]], data[data.columns[1]])
    plt.title('Generated Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')

    # Save the plot to a BytesIO object
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    return f"data:image/png;base64,{plot_url}"
                