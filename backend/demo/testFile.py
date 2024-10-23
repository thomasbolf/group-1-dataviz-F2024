from openai import OpenAI

client = OpenAI()

image_data = client.files.content("file-G8QXqZvRtiFuNiKGafmNdGT8")
image_data_bytes = image_data.read()

with open("./my-image.png", "wb") as file:
    file.write(image_data_bytes)

data = client.files.content("file-x4MbGuiK0nFcD2ZWpUUcOpJV")
#save as txt
with open("./my-text.txt", "wb") as file:
    file.write(data.read())