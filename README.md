# Machine Learning Project with Flask and Kubernetes

This project demonstrates a machine learning workflow using Flask, Docker, and Kubernetes. It includes database initialization, model training, and an inference API.

## Project Structure

```
.
├── .github
│   └── workflows
│       └── kind-deploy.yml
├── iris
│   ├── initialize_db.py
│   ├── train_model.py
│   └── predict.py
├── Dockerfile
├── pyproject.toml
├── poetry.lock
├── README.md
├── deployment.yaml
├── service.yaml
├── static
│   └── iris.png
└── templates
    ├── index.html
    └── result.html
```

## Features

- **Database Initialization**: Initializes an SQLite database with the Iris dataset.
- **Model Training**: Trains a RandomForestClassifier model using the Iris dataset.
- **Inference API**: Provides a Flask-based API to make predictions using the trained model.
- **CI/CD Pipeline**: Automated testing and deployment to Kubernetes using GitHub Actions.

## Technology Stack

- Python 3.9
- Flask for web API
- Poetry for dependency management
- Docker for containerization
- Kubernetes (Kind) for orchestration
- SQLite for database
- scikit-learn for machine learning

## Setup and Usage

### Local Development

1. Install Poetry:
   ```sh
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. Install dependencies:
   ```sh
   poetry install
   ```

3. Initialize the database and train the model:
   ```sh
   poetry run python iris/initialize_db.py
   poetry run python iris/train_model.py
   ```

4. Run the Flask application:
   ```sh
   poetry run python iris/predict.py
   ```

### Building the Docker Image

1. Build the Docker image:
   ```sh
   docker build -t mlevytskyi089/iris:latest .
   ```

2. Run the container locally:
   ```sh
   docker run -d -p 8080:80 mlevytskyi089/iris:latest
   ```

3. Access the Flask application at http://localhost:8080.

### Deploying to Kubernetes

The project includes a GitHub Actions workflow that automatically:
- Runs tests
- Builds and pushes the Docker image
- Sets up a Kind cluster
- Deploys the application to Kubernetes

To manually deploy to an existing Kubernetes cluster:

1. Apply the Kubernetes manifests:
   ```sh
   kubectl apply -f deployment.yaml
   kubectl apply -f service.yaml
   ```

2. Access the service according to your Kubernetes setup.

## API Documentation

### Prediction Endpoint

- **URL**: `/predict`
- **Method**: `POST`
- **Parameters**:
  - `sepal_length` (float): Length of sepal in cm
  - `sepal_width` (float): Width of sepal in cm
  - `petal_length` (float): Length of petal in cm
  - `petal_width` (float): Width of petal in cm
- **Response**: JSON object with predicted iris species

Example request:
```bash
curl -X POST http://localhost:8080/predict \
  -H "Content-Type: application/json" \
  -d '{"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}'
```

## CI/CD Pipeline

The GitHub Actions workflow (`kind-deploy.yml`) provides:
1. Automated testing using pytest
2. Docker image building and publishing to Docker Hub
3. Deployment to a Kind Kubernetes cluster

## Requirements

- Poetry 1.0.0+
- Python 3.9+
- Docker
- kubectl (for manual Kubernetes deployments)

## Author

Mykhailo Levytskyi
