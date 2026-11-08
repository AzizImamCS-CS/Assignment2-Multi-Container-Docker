from fastapi import FastAPI

app = FastAPI()


@app.get("/api/staff")
def get_staff():
    return {"staff": []}


@app.get("/health")
def health_check():
    return {"status": "healthy"}