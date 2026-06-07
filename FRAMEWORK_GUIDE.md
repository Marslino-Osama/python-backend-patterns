# Framework Guide: FastAPI vs Flask

## Strategy

1. Learn with FastAPI first because it supports type hints, Pydantic validation, dependency injection, OpenAPI docs, and async routes.
2. Reimplement selected projects with Flask to understand framework portability.
3. Focus on layered architecture: API/controller layer, service layer, repository layer, domain models, schemas, middleware.

## Quick Comparison

| Feature | FastAPI | Flask | Note |
|---|---|---|---|
| Typing | First-class | Optional | FastAPI rewards strong type hints |
| Validation | Pydantic built-in | Extension/manual | Flask needs Marshmallow/Pydantic/manual validation |
| OpenAPI docs | Built-in | Extension needed | FastAPI wins for API products |
| Async support | Native | Possible but less central | Use async only when the stack is async end-to-end |
| Ecosystem age | Newer | Mature | Flask is widely known |
| Learning value | Modern API architecture | Minimal framework fundamentals | Learn both patterns |

## Basic Server

### FastAPI

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Hello from FastAPI"}
```

### Flask

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def root():
    return jsonify({"message": "Hello from Flask"})
```

## Architecture Rule

Keep handlers/controllers small. They should parse input, call services, and return responses. Business logic belongs in services; persistence belongs in repositories.
