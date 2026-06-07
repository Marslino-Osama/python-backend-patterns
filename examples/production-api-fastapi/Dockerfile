FROM python:3.12-slim
WORKDIR /app
COPY pyproject.toml README.md ./
COPY modules ./modules
COPY examples/production-api-fastapi ./examples/production-api-fastapi
RUN pip install --no-cache-dir -e .
CMD ["uvicorn", "examples.production-api-fastapi.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
