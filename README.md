# Machine Learning Project with Flask and Docker

This project demonstrates a simple machine learning workflow using Flask and Docker. It includes database initialization, model training, and an inference API.

## Project Structure

docker-ml-project/
├── Dockerfile
├── requirements.txt
├── initialize_db.py
├── train_model.py
└── predict.py


## Features

- **Database Initialization**: Initializes an SQLite database with the Iris dataset.
- **Model Training**: Trains a RandomForestClassifier model using the Iris dataset.
- **Inference API**: Provides a Flask-based API to make predictions using the trained model.

## Setup and Usage

### Prerequisites

- Docker
- Podman (optional, for running containers)

### Building the Docker Image

1. Navigate to the project directory:
   ```sh
   cd docker-ml-project
   ```
2. Build the Docker image: 
    ```sh
    podman build -t ml_project\:latest .
    ```

### Running the Container

1. Run the container with port mapping:
    ```sh
    podman run -d -p 8080:80 ml_project\:latest
    ```
2. Access the Flask application at http://localhost:8080.

### Making Predictions
Use curl or any API client to send a POST request to the /predict endpoint:
    ```
    curl -X POST http://localhost:8080/predict -H "Content-Type: application/json" -d '{"features": [5.1, 3.5, 1.4, 0.2]}'
    ```
