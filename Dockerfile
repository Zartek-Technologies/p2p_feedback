FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /opt/app-root/src

COPY install-packages.sh ./
RUN ./install-packages.sh && rm install-packages.sh

COPY . ./
RUN pip install --upgrade pip setuptools wheel \
    && pip install -e .[postgres]

EXPOSE 8080
ENTRYPOINT ["./gunicorn_starter.sh"]
