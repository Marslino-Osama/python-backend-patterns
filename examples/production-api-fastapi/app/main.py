from fastapi import FastAPI

app = FastAPI(title="Python Backend Patterns")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Python Backend Patterns - FastAPI reference app"}
