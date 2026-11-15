FROM python:3.12-slim

WORKDIR /app

COPY app/requirements.txt .

RUN pip install \
    --no-cache-dir \
    --retries 10 \
    --timeout 300 \
    -r requirements.txt

COPY app/ .

EXPOSE 5000

CMD ["python", "app.py"]