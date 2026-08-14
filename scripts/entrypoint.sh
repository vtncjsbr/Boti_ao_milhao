#!/bin/sh
set -e

export PYTHONPATH=/app
mkdir -p /app/data

echo "Running database migration..."
python migrate.py

echo "Seeding default user (if missing)..."
python scripts/seed_user.py

echo "Starting API server..."
exec uvicorn main_fastapi:app --host 0.0.0.0 --port 8000
