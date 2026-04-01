from fastapi import FastAPI
from .api import router

app = FastAPI(title="Ride-Share API (Uber/Rapido)")
app.include_router(router)