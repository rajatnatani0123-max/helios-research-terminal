from fastapi import FastAPI

app = FastAPI(
    title="Helios Backend",
    version="0.1.0"
)

@app.get("/")
def root():
    return {
        "status": "online",
        "project": "Helios"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.get("/about")
def about():
    return {
        "name": "Helios Research Terminal",
        "version": "0.1"
    }