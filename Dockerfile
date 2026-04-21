# FROM python:3.10-slim

# WORKDIR /app

# COPY requirements.txt .

# RUN pip install -r requirements.txt

# COPY app.py .

# CMD ["python", "app.py"]

FROM python:3.9-slim

WORKDIR /app

# On copie le fichier des dépendances d'abord (optimisation du cache)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# On copie tout le reste du projet (templates, static, app.py)
COPY . .

EXPOSE 5000

CMD ["python", "app.py"]