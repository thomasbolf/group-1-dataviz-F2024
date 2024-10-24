from openai import OpenAI
import json
import time
import pandas as pd
import re
import random

def show_json(obj):
    print(json.loads(obj.model_dump_json()))
client = OpenAI()
def wait_on_run(run, thread):
    while run.status == "queued" or run.status == "in_progress":
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id,
        )
        time.sleep(5)
    return run
    
file = client.files.create(
  file=open("iris.csv", "rb"),
  purpose='assistants'
)
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
    "code_interpreter": {
      "file_ids": [file.id]
    }
  }
)
#generate  a random number
random_number = random.randint(1, 100000)
print(f"Generated random number: {random_number}")
thread = client.beta.threads.create(
  messages=[
    {
      "role": "user",
      "content": str(random_number) + """Do the following: Make sure to adhere to your initial instructions and return python code for me (i.e I want to see the python code in the response). The current selections are as follows:
High-level request: I am interested in the relationship between Sepal Width and Sepal Length.
Visualization Goal: Analyze Data
Target Audience: Experts
Visual Style: Playful
Use the dataset provided, which contains a mix of numerical, categorical, and datetime variables. Your objective is to design a visualization that:
Visualization Goal: Analyze Data - The purpose of this visualization is to analyze the dataset in detail, focusing on uncovering and exploring deep relationships between different variables. The visual should provide insights into how these data points correlate or interact, helping the user identify key patterns or anomalies. It should be designed for individuals who want to dig deeper into the data, providing enough granularity to allow for a comprehensive understanding of the underlying structure. This visualization should support data exploration, enabling the viewer to draw informed conclusions or hypotheses.
Target Audience: Experts - This visualization is designed for a specialized audience with advanced knowledge in the field. The focus should be on delivering detailed, precise, and comprehensive insights that allow for in-depth analysis. The content can assume familiarity with technical terms, complex data structures, and nuanced relationships between variables. The visual should not oversimplify the information but rather offer layers of depth and complexity, providing experts with the tools to derive significant insights, conduct thorough evaluations, and form data-driven conclusions based on their specialized understanding.
Visual Style: Playful - The visualization should adopt a bright, engaging, and fun visual style that is both visually stimulating and approachable, particularly for younger audiences or educational purposes. Colors should be vibrant, and the design should include lively elements that evoke curiosity and excitement. The layout should be simple yet dynamic, focusing on making data more accessible and less intimidating. This style is meant to captivate the viewer’s attention, making learning or data exploration enjoyable while ensuring clarity and understanding without overwhelming the audience with too much detail.

"""
    }
  ]
)
df = pd.read_csv("iris.csv")

csv_data = df.head().to_string()
message = client.beta.threads.messages.create(
    thread_id=thread.id, role="user", content="Use the file I gave you as the source for data. Could you create a data visualization and save it as a file as requested with this data? Run the code, save the python code in a .py file and save the image as a .png file, and give me both files. Here is a sample of the data  " + csv_data, attachments=[{"file_id": file.id, "tools": [{"type": "code_interpreter"}]}]
)

print("message created")
run = client.beta.threads.runs.create(
    thread_id = thread.id,
    assistant_id = assistant.id
)
print("Run created, waiting on run")
wait_on_run(run, thread)
print("Done waiting on run")

messageDone = client.beta.threads.messages.list(
    thread_id=thread.id, order="asc", after=message.id
)
print(messageDone.data)

# Parse messageDone for a substring of the form file-*

file_ids = []
for m in messageDone:
  print(m)

print("Extracted file IDs:", file_ids)
#save the json file
with open('data.json', 'w') as f:
    json.dump(json.loads(messageDone.model_dump_json()), f)

  


