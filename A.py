from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()


class MultiplicationModel(BaseModel):
    a: int
    b: int


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request, exc: RequestValidationError
):
    return JSONResponse(
        status_code=422,
        content={"error": "Type Mismatch: a and b must be integers"}
    )


@app.post("/Dinesh/Bafila/Mul/Pydantic")
def multiply(model: MultiplicationModel):
    return model.a * model.b