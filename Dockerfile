FROM python:3.9-slim

WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy poetry configuration files
COPY pyproject.toml poetry.lock* ./

# Configure poetry to not use a virtual environment
RUN poetry config virtualenvs.create false

# Copy application code
COPY . .

# Install dependencies
RUN poetry install --no-interaction

# Install SQLite
RUN apt-get update && apt-get install -y sqlite3



# Initialize the database and train the model
RUN python iris/initialize_db.py && python iris/train_model.py

# Expose the port for the inference server
EXPOSE 80

# Run the inference server
CMD ["python", "iris/predict.py"]
