FROM docker.io/library/python:3.12-slim-bullseye

WORKDIR /app
COPY . /app/

RUN pip install --no-cache-dir --ignore-installed poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-cache --only main

ENTRYPOINT ["hermes"]
