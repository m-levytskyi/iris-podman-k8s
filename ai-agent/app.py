from flask import Flask, request, jsonify
import joblib
import requests

app = Flask(__name__)

# Load the model
model = joblib.load('model/model.pkl')

# Configuration for external APIs
LLM_API_URL = "http://your-llm-api-endpoint"  # Replace with your LLM API endpoint
IMAGE_GENERATION_API_URL = "http://your-image-generation-api-endpoint"  # Replace with your image generation API endpoint

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse input data
        data = request.json
        features = [data['sepal_length'], data['sepal_width'], data['petal_length'], data['petal_width']]

        # Make prediction
        prediction = model.predict([features])
        species = prediction[0]

        # Call LLM API to get species description
        description_response = requests.post(LLM_API_URL, json={"species": species})
        description = description_response.json().get("description", "No description available.")

        # Call Image Generation API to get flower image
        image_response = requests.post(IMAGE_GENERATION_API_URL, json={"species": species})
        image_url = image_response.json().get("image_url", "")

        # Return prediction result along with description and image URL
        return jsonify({
            "species": species,
            "description": description,
            "image_url": image_url
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
