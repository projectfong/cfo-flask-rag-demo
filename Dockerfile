# Demo-only Dockerfile for cfo-flask-rag
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ ./src/
EXPOSE 8002
CMD ["gunicorn", "-w", "2", "-t", "120", "-b", "0.0.0.0:8002", "src.main:app"]
