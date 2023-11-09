FROM nikolaik/python-nodejs:python3.11-nodejs20

WORKDIR /work

COPY package*.json .
COPY tailwind.config.js .
RUN npm install

WORKDIR /work/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
