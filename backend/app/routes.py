
from flask import Blueprint, render_template, request
from .utils import data_processing, plot_generation, ai_interaction, prompt_creation
import pandas as pd
import os
# Define the blueprint
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/visualize', methods=['POST'])
def visualize():
    user_data = request.files['data']
    task_type = request.form.get('task')

    # Process the data
    processed_data = data_processing.process(user_data)

    # Create and send a prompt to the AI model
    prompt = prompt_creation.create_prompt(processed_data, task_type)
    ai_response = ai_interaction.get_insights(prompt)

    # Generate the plot
    plot_image = plot_generation.generate_plot(processed_data)

    return render_template('result.html', plot_image=plot_image, ai_response=ai_response)

@main.route("/upload", methods["POST"])
def upload_file():
    visualization_goal = request.form['visualization_goal']
    target_audience = request.form['target_audience']
    visual_style = request.form['visual_style']

    file = request.files['file']
    file_path = os.path.join("/tmp", file.filename)

    prompt = prompt_creation.create_viz_prompt(visualization_goal, target_audience, visual_style)
    ai_interaction.generate_code_and_graph(pd.read_csv(file_path), prompt)

    
    
