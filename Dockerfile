FROM python:3.9-slim

WORKDIR /app

# Install necessary dependencies
RUN apt-get update && apt-get install -y sqlite3
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy all scripts into the container
# COPY initialize_db.py train_model.py predict.py  /app/
# COPY templates /app/templates
COPY . . 
# Initialize the database and train the model
RUN python initialize_db.py && python train_model.py

# Expose the port for the inference server
EXPOSE 80

# Run the inference server
CMD ["python", "predict.py"]
