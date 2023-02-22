FROM python:3.7.16-slim-bullseye

WORKDIR /app

COPY requirements.txt ./
RUN python3 -m pip install --no-cache-dir -r requirements.txt

COPY . .

COPY api.py /var/server/api.py

CMD ["python3", "/var/server/api.py"]