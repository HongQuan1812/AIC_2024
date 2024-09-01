FROM python:latest

WORKDIR /app

# Copy requirements.txt to the working directory (already in /app)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the entire project into the working directory
COPY . .

# Start the FastAPI application
CMD ["fastapi", "run", "main.py", "--port", "80"]