FROM python:3.12.5-alpine3.20

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "run.py"]

EXPOSE 5000
