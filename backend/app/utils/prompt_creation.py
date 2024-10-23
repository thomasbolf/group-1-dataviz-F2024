
def create_prompt(data, task_type):
    if task_type == 'storytelling':
        prompt = f"Create a narrative for the following dataset: {data.to_string()}"
    elif task_type == 'analysis':
        prompt = f"Analyze the following dataset: {data.to_string()}"
    elif task_type == 'comparison':
        prompt = f"Compare and contrast key features in this dataset: {data.to_string()}"
    else:
        prompt = f"Provide insights for this dataset: {data.to_string()}"

    return prompt
                