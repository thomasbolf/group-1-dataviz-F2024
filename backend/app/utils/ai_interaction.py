
import openai
import os
from openai import OpenAI
import json
import time
import pandas as pd
def show_json(obj):
    print(json.loads(obj.model_dump_json()))
client = OpenAI()
def wait_on_run(run, thread):
    while run.status == "queued" or run.status == "in_progress":
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id,
        )
        time.sleep(10)
    return run
def get_insights(prompt):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.ChatCompletion.create(
        model="gpt-4",  # Using GPT-4
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150
    )
    return response['choices'][0]['message']['content'].strip()
def generate_code_and_graph(data, prompt):
    initial_instructions = """
        You are working on an automated visualization system that generates customizable visualizations using Python’s Matplotlib library. 
        The system takes user inputs through a dropdown menu with three types of selections: "Visualization Goal," "Target Audience," and "Visual Style." 
        Based on these inputs, you are tasked with producing the appropriate Matplotlib code to create the requested visual.
        """
    assistant = client.beta.assistants.create(
        instructions=initial_instructions,
        model="gpt-4o",
        tools=[{"type": "code_interpreter"}],
        tool_resources={
            "code_interpreter": {}
        }
    )
    thread = client.beta.threads.create(
        messages=[
            {
            "role": "user",
            "content": "Make sure to adhere to your initial instructions and return python code for me (i.e I want to see the python code in the response)." + prompt,

            # "attachments": [
            #   {
            #     "file_id": file.id,
            #     "tools": [{"type": "code_interpreter"}]
            #   }
            # ]
            }
        ]
    )
    message = client.beta.threads.messages.create(
    thread_id=thread.id, role="user", content="Could you create a data visualization and save it as a file as requested with this data? Run the code, save the python code in a .py file and save the image as a .png file, and give me both files. Here is a sample of the data  " + csv_data, attachments=[{"file_id": file.id, "tools": [{"type": "code_interpreter"}]}]
    )
    run = client.beta.threads.runs.create(
    thread_id = thread.id,
    assistant_id = assistant.id
    )
    wait_on_run(run, thread)
    messageDone = client.beta.threads.messages.list(
        thread_id=thread.id, order="asc", after=message.id
    )
    show_json(messageDone)

    ## TODO: parse json for filenames
    
    




                