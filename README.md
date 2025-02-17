# Machine Learning Project with Flask and Podman

This project demonstrates a simple machine learning workflow using Flask and Docker. It includes database initialization, model training, and an inference API.

## Project Structure

docker-ml-project/
├── Dockerfile
├── initialize_db.py
├── iris.db
├── model.pkl
├── predict.py
├── README.md
├── requirements.txt
├── static
│   └── iris.png
├── templates
│   ├── index.html
│   └── result.html
└── train_model.py


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
