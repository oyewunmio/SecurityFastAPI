from fastapi import FastAPI, Request, status
from routes import router
from sqlmodel import SQLModel
from db import engine
from fastapi.exceptions import RequestValidationError
from config import settings
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

app = FastAPI()
app.include_router(router, prefix=settings.API_V1_STR)


@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)


@app.exception_handler(RequestValidationError)
async def standard_validation_exception_handler(
    request: Request, exc: RequestValidationError
):
    error_list = []
    for errors in exc.errors():
        err = f"{errors['loc'][1]} {errors['msg']}"
        error_list.append(err)
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": error_list}),
    )
