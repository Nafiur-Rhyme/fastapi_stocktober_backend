from fastapi import FastAPI

from api.routes import router as api_router
from core.config import settings

# Initialize FastAPI application
app = FastAPI(
    title=settings.app_name,
    description="API for the Stock Market Simulation App: Stocktober",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Include API routes
app.include_router(api_router, prefix="/api/v1")
