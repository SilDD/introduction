# 1. Basis-Image auswählen
FROM python:3.9-slim

# 2. Umgebungsvariablen festlegen
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Arbeitsverzeichnis erstellen und festlegen
WORKDIR /app

# 4. Systemabhängigkeiten installieren
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# 5. Abhängigkeiten für Wagtail installieren
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# 6. Projektdateien kopieren
COPY . .

# 7. Ports freigeben
EXPOSE 8000

RUN python manage.py collectstatic --noinput --clear
# 8. Befehle zum Starten des Servers festlegen
#CMD python manage.py runserver 0.0.0.0:8000