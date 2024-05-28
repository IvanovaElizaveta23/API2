from fastapi import FastAPI
from service.router import router as bird_router

app = FastAPI()
app.include_router(bird_router, prefix="/api/v1")
