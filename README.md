# Number Statistics API

A lightweight REST API built with **FastAPI** that accepts a list of numbers and returns useful statistics: **sum**, **average**, **max**, and **min** value.

---

## Features

- `POST /statistics` — compute statistics for a list of numbers
- `GET /health` — health check endpoint
- `GET /docs` — interactive Swagger UI (auto-generated)
- `GET /redoc` — ReDoc documentation

---

## Quick Start

### Run with Docker

```bash
# Build the image
docker build -t number-stats-api .

# Run the container
docker run -p 3000:3000 number-stats-api
```

The API will be available at `http://localhost:3000`.

### Run locally

```bash
# Install dependencies
pip install -r requirements.txt

# Start the server
python main.py
```

---

## API Reference

### `POST /statistics`

Compute statistics from a list of numbers.

**Request Body:**
```json
{
  "numbers": [10, 20, 30, 40, 50]
}
```

**Response:**
```json
{
  "count": 5,
  "numbers": [10.0, 20.0, 30.0, 40.0, 50.0],
  "sum": 150.0,
  "average": 30.0,
  "max": 50.0,
  "min": 10.0
}
```

**Validation Rules:**
- `numbers` must be a non-empty list.
- All values must be valid numbers (integers or floats).

**Error Response (empty list):**
```json
{
  "detail": [
    {
      "loc": ["body", "numbers"],
      "msg": "The list of numbers must not be empty.",
      "type": "value_error"
    }
  ]
}
```

---

### `GET /health`

Returns `200 OK` with `{"status": "ok"}`. Used for load balancer / uptime checks.

---

## Example cURL Commands

```bash
# Health check
curl http://localhost:3000/health

# Compute statistics
curl -X POST http://localhost:3000/statistics \
  -H "Content-Type: application/json" \
  -d '{"numbers": [5, 10, 15, 20, 25]}'

# With negative and decimal numbers
curl -X POST http://localhost:3000/statistics \
  -H "Content-Type: application/json" \
  -d '{"numbers": [-3.5, 0, 7.2, 100, -50]}'
```

---

## Interactive Docs

Once the server is running, visit:
- **Swagger UI**: [http://localhost:3000/docs](http://localhost:3000/docs)
- **ReDoc**: [http://localhost:3000/redoc](http://localhost:3000/redoc)

---

## Tech Stack

| Component | Technology |
|-----------|------------|
| Framework | FastAPI 0.111 |
| Server    | Uvicorn 0.30 |
| Validation| Pydantic v2 |
| Runtime   | Python 3.12 |
| Container | Docker (python:3.12-slim) |
