FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

COPY requirements-prod.txt .
RUN pip install --no-cache-dir -r requirements-prod.txt

COPY . .

RUN chmod +x scripts/entrypoint.sh

ENV DATABASE_URL=sqlite:////app/data/raw_data.db

EXPOSE 8000

ENTRYPOINT ["./scripts/entrypoint.sh"]
