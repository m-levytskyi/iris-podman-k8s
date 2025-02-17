from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load('/app/model.pkl')

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
    return render_template('result.html', prediction=prediction[0])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
