function sendPredictionRequest() {
    const data = {
        sepal_length: document.getElementById('sepal_length').value,
        sepal_width: document.getElementById('sepal_width').value,
        petal_length: document.getElementById('petal_length').value,
        petal_width: document.getElementById('petal_width').value
    };

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        // Update the image and description based on the result
        document.getElementById('flowerImage').src = data.image_url;
        alert(`Species: ${data.species}\nDescription: ${data.description}`);
    })
    .catch(error => console.error('Error:', error));
}

function randomizeInputs() {
    document.getElementById('sepal_length').value = (Math.random() * (7.9 - 4.3) + 4.3).toFixed(2);
    document.getElementById('sepal_width').value = (Math.random() * (4.4 - 2.0) + 2.0).toFixed(2);
    document.getElementById('petal_length').value = (Math.random() * (6.9 - 1.0) + 1.0).toFixed(2);
    document.getElementById('petal_width').value = (Math.random() * (2.5 - 0.1) + 0.1).toFixed(2);
}
