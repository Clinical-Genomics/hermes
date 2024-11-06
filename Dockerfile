FROM docker.io/library/python:3.12-slim-bullseye

WORKDIR /app
COPY . /app/

RUN pip install --ignore-installed poetry \
    && poetry config virtualenvs.create false \
    && poetry install --only main

ENTRYPOINT ["hermes"]
