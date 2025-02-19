from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load('/app/model.pkl')

# Map class indices to class names
class_names = {0: "setosa", 1: "versicolor", 2: "virginica"}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [
        float(request.form['sepal_length']),
        float(request.form['sepal_width']),
        float(request.form['petal_length']),
        float(request.form['petal_width'])
    ]
    prediction = model.predict([features])
    predicted_class_name = class_names[prediction[0]]
    return render_template('result.html', prediction=predicted_class_name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
