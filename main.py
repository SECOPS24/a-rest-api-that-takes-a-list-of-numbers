from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator
from typing import List
import uvicorn

app = FastAPI(
    title="Number Statistics API",
    description="A REST API that computes sum, average, and max value from a list of numbers.",
    version="1.0.0"
)


class NumbersInput(BaseModel):
    numbers: List[float]

    @field_validator("numbers")
    @classmethod
    def numbers_must_not_be_empty(cls, v):
        if len(v) == 0:
            raise ValueError("The list of numbers must not be empty.")
        return v


class StatisticsResponse(BaseModel):
    count: int
    numbers: List[float]
    sum: float
    average: float
    max: float
    min: float


@app.get("/health", summary="Health Check")
def health_check():
    return {"status": "ok"}


@app.post("/statistics", response_model=StatisticsResponse, summary="Compute Statistics")
def compute_statistics(payload: NumbersInput):
    """
    Accepts a JSON body with a list of numbers and returns:
    - **sum**: total sum of all numbers
    - **average**: arithmetic mean
    - **max**: maximum value
    - **min**: minimum value
    - **count**: how many numbers were provided

    **Example request body:**
    ```json
    { "numbers": [1, 2, 3, 4, 5] }
    ```
    """
    nums = payload.numbers
    total = sum(nums)
    average = total / len(nums)
    maximum = max(nums)
    minimum = min(nums)

    return StatisticsResponse(
        count=len(nums),
        numbers=nums,
        sum=total,
        average=average,
        max=maximum,
        min=minimum
    )


@app.get("/", summary="Root")
def root():
    return {
        "message": "Welcome to the Number Statistics API!",
        "docs": "/docs",
        "health": "/health",
        "usage": "POST /statistics with body: {\"numbers\": [1, 2, 3, ...]}"
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)
