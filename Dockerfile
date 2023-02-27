FROM python:3.8-slim
COPY requirements.txt .
COPY api.py .
COPY iris_knn.pkl .
COPY templates /templates
COPY static /static
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
ENV FLASK_APP api.py
CMD flask run --host 0.0.0.0 --port 5000