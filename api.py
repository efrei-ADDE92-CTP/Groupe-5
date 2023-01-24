import os
import pandas as pd
from flask import Flask
from flask import request, jsonify
import joblib

app = Flask(__name__)

with open('iris_knn.pkl', 'rb') as file:
    model = joblib.load(file)


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    df = pd.DataFrame(data, index=[0])

    prediction = model.predict(df)
    return jsonify({'prediction': list(prediction)})


if __name__ == '__main__':
    app.run(port=5000, debug=True)
