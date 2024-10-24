from openai import OpenAI

client = OpenAI()

#image_data = client.files.content("file-RjK0VekEX8IfL0yjiShjsMK0")
image_data = client.files.content("file-UnEwHcL4G1nEOmQRjN96gFUB")
image_data_bytes = image_data.read()

with open("./my-image.png", "wb") as file:
    file.write(image_data_bytes)

## do the above but instead save txt file
data = client.files.content("file-943VGWi6ImtxK44UVsgNFAQ9")
data_bytes = data.read()
with open("./my-image.txt", "wb") as file:
    file.write(image_data_bytes)