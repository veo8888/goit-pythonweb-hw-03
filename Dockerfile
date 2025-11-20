FROM python:3.13-slim

# Set the working directory
WORKDIR /app

# First, copy only the requirements (if any)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy everything else
COPY . .

# Create a storage folder if it doesn't exist
RUN mkdir -p /app/storage

# The container is listening on port 3000
EXPOSE 3000

# Volume for storing data.json outside the container
VOLUME ["/app/storage"]

# Launch the application
CMD ["python", "app.py"]