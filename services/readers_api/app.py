from fastapi import FastAPI

app = FastAPI()


@app.get("/api/readers")
def get_readers():
    return {"readers": []}


@app.get("/health")
def health_check():
    return {"status": "healthy"}