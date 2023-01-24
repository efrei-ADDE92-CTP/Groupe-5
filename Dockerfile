FROM python:3.8-slim
COPY requirements.txt .
COPY api.py .
COPY iris_knn.pkl .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
ENV FLASK_APP api.py
CMD ["python", "api.py"]