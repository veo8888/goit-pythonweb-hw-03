# goit-pythonweb-hw-03

Tutorial Project: Building a Simple Web Application

## Running in VS Code

Open the project folder in VS Code.

To run the project, follow these steps:

1. Create a virtual environment:

```bash
python -m venv .venv
```

2. Activate the virtual environment:

```bash
.\.venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Start the project (Make sure the virtual environment is sourced/activated!):

```bash
python app.py
```

The web application will be available at: http://localhost:3000

5. Deactivate the virtual environment:

```bash
deactivate
```

6. Remove the virtual environment:

```bash
rm -r .venv
```

## Running with Docker

1. Build the image and start the container:

```bash
docker-compose up --build
```

The web application will be available at: http://localhost:3000

2. Restart the container:

```bash
docker-compose up
```

Message files are stored on the host machine at: ./storage/data.json.
