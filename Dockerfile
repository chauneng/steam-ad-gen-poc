FROM python:3.13-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
  build-essential curl git bash ca-certificates \
  && rm -rf /var/lib/apt/lists/*

ENV POETRY_HOME=/opt/poetry \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="$POETRY_HOME/bin:$PATH"

WORKDIR /app
COPY pyproject.toml poetry.lock* /app/
RUN poetry install --no-root

COPY . /app
