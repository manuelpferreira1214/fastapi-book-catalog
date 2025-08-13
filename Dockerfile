# -------- Stage 1: Builder --------
FROM python:3.12-slim AS builder

RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

COPY pyproject.toml poetry.lock* ./

RUN poetry install --only-root --no-interaction --no-ansi

# -------- Stage 2: Development --------
FROM python:3.12-slim AS dev

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

COPY --from=builder /root/.local /root/.local
COPY . .

EXPOSE 8000

CMD ["uvicorn", "project.app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
