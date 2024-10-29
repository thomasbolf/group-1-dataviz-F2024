
from flask import Blueprint, render_template, request, send_file
from .utils import data_processing, plot_generation, ai_interaction, prompt_creation
import pandas as pd
import os
import json 
from flask import jsonify
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

@main.route("/upload", methods=["POST"])
def upload_file():
    visualization_goal = request.form['visualization_goal']
    target_audience = request.form['target_audience']
    visual_style = request.form['visual_style']
    file = request.files['file']
    print(f"Visualization Goal: {visualization_goal}")
    print(f"Target Audience: {target_audience}")
    print(f"Visual Style: {visual_style}")
    print(f"File Name: {file.filename}")
    file_path = os.path.join('app/uploads', "data.csv")
    file.save(file_path) 
    prompt = prompt_creation.create_viz_prompt(visualization_goal, target_audience, visual_style)
    print(prompt)
    ai_interaction.generate_code_and_graph(file_path, prompt)
    return jsonify({
            }), 200
        


@main.route("/get-image", methods=["GET"])
def get_image():
    image_path = os.path.join(os.path.abspath('app/uploads'), 'my-image.png')
    print(image_path)
    if os.path.exists(image_path):
        return send_file(image_path, mimetype='image/png')
    else:
        return jsonify({
            'error': 'Image file not found'
        }), 404
    
@main.route("/get-code", methods=["GET"])
def get_code():
    code_path = os.path.join('uploads', 'my-code.py')
    if os.path.exists(code_path):
        with open(code_path, 'r') as code_file:
            code_content = code_file.read()
            return code_content
    else:
        return jsonify({
            'error': 'Code file not found'
        }), 404
    
    
