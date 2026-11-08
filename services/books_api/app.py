
import logging
from pathlib import Path

from fastapi import FastAPI, Request

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)

app = FastAPI()

BOOKS_FILE = Path(__file__).parent / "books.txt"


@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(
        "Request: %s %s",
        request.method,
        request.url.path,
    )

    response = await call_next(request)

    logger.info(
        "Response: %s",
        response.status_code,
    )

    return response


@app.get("/api/books")
@app.get("/items")
@app.get("/GET")
def get_items():
    with open(BOOKS_FILE, "r", encoding="utf-8") as file:
        books = [line.strip() for line in file if line.strip()]
    return books


@app.get("/health")
def health_check():
    return {"status": "healthy"}
