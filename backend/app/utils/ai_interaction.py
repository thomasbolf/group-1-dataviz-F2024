
import openai
import os
from openai import OpenAI
import json
import time
import pandas as pd
import random
import json
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
    file = client.files.create(
        file=open(data, "rb"),
        purpose='assistants'
    )
    random_number = random.randint(1, 100000)
    print(f"Generated random number: {random_number}")
    df = pd.read_csv(data)

    csv_data = df.head().to_string()
    print(csv_data)
    assistant = client.beta.assistants.create(
    instructions=initial_instructions,
    model="gpt-4o",
    tools=[{"type": "code_interpreter"}],
    tool_resources={
        "code_interpreter": {
        "file_ids": [file.id]
        }
    }
    )
    thread = client.beta.threads.create(
        messages=[
            {
            "role": "user",
            "content": str(random_number) + prompt
            }
        ]
    )
    message = client.beta.threads.messages.create(
    thread_id=thread.id, role="user", content="Use the file I gave you as the source for data. Could you create a data visualization and save it as a file as requested with this data? Run the code, save the python code in a .py file and save the image as a .png file, and give me both files. Here is a sample of the data  " + csv_data, attachments=[{"file_id": file.id, "tools": [{"type": "code_interpreter"}]}]
    )
    run = client.beta.threads.runs.create(
    thread_id = thread.id,
    assistant_id = assistant.id
    )
    wait_on_run(run, thread)
    messageDone = client.beta.threads.messages.list(
    thread_id=thread.id, order="asc", after=message.id
    )
    print("About to save json object")
    with open('app/uploads/data.json', 'w') as f:
        json.dump(json.loads(messageDone.model_dump_json()), f)
    with open('app/uploads/data.json', 'r') as file:
        data = json.load(file)
    # Extract file_id values
    file_ids = []
    for item in data['data']:
        for attachment in item.get('attachments', []):
            file_ids.append(attachment['file_id'])
        for content in item.get('content', []):
            for annotation in content.get('text', {}).get('annotations', []):
                if 'file_path' in annotation:
                    file_ids.append(annotation['file_path']['file_id'])
    if(len(file_ids) > 1):
        if(client.files.retrieve(file_ids[1]).filename[-3:] == 'png'):
            image_data = client.files.content(file_ids[1])
            image_data_bytes = image_data.read()
            with open("app/uploads/my-image.png", "wb") as file:
                file.write(image_data_bytes)
        elif (client.files.retrieve(file_ids[1]).filename[-2:] == 'py'):
            data = client.files.content(file_ids[1])
            data_bytes = data.read()
            with open("app/uploads/my-code.txt", "wb") as file:
                file.write(data_bytes)
        if(client.files.retrieve(file_ids[0]).filename[-3:] == 'png'):
            image_data = client.files.content(file_ids[0])
            image_data_bytes = image_data.read()
            with open("app/uploads/my-image.png", "wb") as file:
                file.write(image_data_bytes)
        elif (client.files.retrieve(file_ids[0]).filename[-2:] == 'py'):
            data = client.files.content(file_ids[0])
            data_bytes = data.read()
            with open("app/uploads/my-code.txt", "wb") as file:
                file.write(data_bytes)
    elif(len(file_ids) == 1):
        if(client.files.retrieve(file_ids[0]).filename[-3:] == 'png'):
            image_data = client.files.content(file_ids[0])
            image_data_bytes = image_data.read()
            with open("app/uploads/my-image.png", "wb") as file:
                file.write(image_data_bytes)
        elif (client.files.retrieve(file_ids[0]).filename[-2:] == 'py'):
            data = client.files.content(file_ids[0])
            data_bytes = data.read()
            with open("app/uploads/my-code.txt", "wb") as file:
                file.write(data_bytes)

                