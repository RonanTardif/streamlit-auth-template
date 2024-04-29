FROM python:3.9

# Exposer le port 8080
EXPOSE 8080

# Mettre à jour pip
RUN python -m pip install --upgrade pip

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires dans le conteneur
COPY requirements.txt .
COPY config.yaml .
COPY streamlit-app.py .

# Installer les dépendances
RUN pip install -r requirements.txt

# Lancer l'application Streamlit
ENTRYPOINT ["streamlit", "run", "streamlit-app.py", "--server.port", "8080"]
