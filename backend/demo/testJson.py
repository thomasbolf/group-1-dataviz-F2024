import json

# Load the JSON data from the file
with open('data.json', 'r') as file:
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

# Print the extracted file_ids
for file_id in file_ids:
    print(f"file_id: {file_id}")



from openai import OpenAI

client = OpenAI()

#image_data = client.files.content("file-RjK0VekEX8IfL0yjiShjsMK0")
image_data = client.files.content(file_ids[0])
image_data_bytes = image_data.read()

with open("./my-image.png", "wb") as file:
    file.write(image_data_bytes)

## do the above but instead save txt file
data = client.files.content(file_ids[1])
data_bytes = data.read()
with open("./my-code.txt", "wb") as file:
    file.write(data_bytes)
