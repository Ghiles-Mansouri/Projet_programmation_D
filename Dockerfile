#  ÉTAPE 1 : BUILDER 
FROM python:3.11-slim AS builder
WORKDIR /app

# Copie le fichier des dépendances
COPY requirements.txt .
# Installe les dépendances dans un dossier spécifique (user) pour pouvoir les isoler
RUN pip install --user --no-cache-dir -r requirements.txt

#  ÉTAPE 2 : RUNTIME 
FROM python:3.11-slim
WORKDIR /app

# Récupère uniquement les librairies proprement installées lors de l'étape 1
COPY --from=builder /root/.local /root/.local

# Copie ton code source (le main.py)
COPY . .

# Indique à Python le chemin pour trouver les librairies récupérées
ENV PATH=/root/.local/bin:$PATH

# Expose le port 8000
EXPOSE 8000

# La commande lancée au démarrage du conteneur
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]