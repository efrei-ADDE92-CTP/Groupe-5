import os
import pandas as pd
import logging
from flask import Flask, render_template
from flask import request, jsonify
import joblib
from prometheus_client import start_http_server, Gauge, Counter, generate_latest

app = Flask(__name__)

with open('iris_knn.pkl', 'rb') as file:
    model = joblib.load(file)

a = Counter('a_requests', 'Number of requests served')  
s = Counter('s_requests', 'Number of sucessful requests')  
f = Counter('f_requests', 'Number of failed requests')
g = Gauge('success_rate_requests', 'Rate of success requests')

@app.route('/')
def index():
    return render_template("index.html") 

@app.route('/predict', methods=['POST'])
def predict():
    result = request.form.to_dict(flat=True)
    a.inc()
    data = result
    df = pd.DataFrame(data, index=[0])

    prediction = model.predict(df)
    return jsonify({'prediction': list(prediction)})


# Define a counter to track the number of requests
REQUEST_COUNT = Counter('myapp_request_count', 'Number of requests received')

@app.after_request
def log_the_status_code(response):
    if response.status_code == 200:
        s.inc()
    else:
        f.inc()
    success_rate = (s._value.get() / (f._value.get() + s._value.get())) * 100           #.get() removed
    g.set(success_rate)
    logging.warning("status as string %s" % response.status)
    logging.warning("status as integer %s" % response.status_code)
    return response


@app.route('/metrics')
def metrics():
    return generate_latest()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)