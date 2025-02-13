FROM python:3.9-slim

WORKDIR /app

# Install SQLite
RUN apt-get update && apt-get install -y sqlite3

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of the project files (e.g., your SQLite initialization script)
COPY . .

# Run the SQLite script to initialize the database
CMD ["python", "initialize_db.py"]
