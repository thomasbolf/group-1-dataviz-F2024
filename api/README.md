## Requirements

- Python 3.x
- Flask
- Requests
- Flask-CORS

## Installation

To set up the project, follow these steps:



1. Install the required dependencies:
   ```bash
   pip install --no-cache-dir -r requirements.txt
   ```

## Running the Application

To start the Flask API, run the following command:

```bash
flask --app api run
```

By default, the API will be served at `http://localhost:5000`.

## Example Usage

You can send a POST request to the `/api/exec` endpoint to execute Python code. Here's an example using `curl` to run a simple "Hello World" program:

```bash
curl -X POST http://localhost:5000/api/exec \
-H "Content-Type: application/json" \
-d '{"code": "print(\"Hello world\")"}'
```

