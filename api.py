import os
import pandas as pd
from flask import Flask
from flask import request, jsonify
import joblib
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

with open('iris_knn.pkl', 'rb') as file:
    model = joblib.load(file)


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    df = pd.DataFrame(data, index=[0])

    prediction = model.predict(df)
    return jsonify({'prediction': list(prediction)})


# Define a counter to track the number of requests
REQUEST_COUNT = Counter('myapp_request_count', 'Number of requests received')

@app.route('/metrics')
def metrics():
    # Increment the request count
    REQUEST_COUNT.inc()

    # Return the latest metrics as a string in Prometheus text format
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
