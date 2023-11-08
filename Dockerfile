# pythonのバージョンは任意
FROM python:3.11.5

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
