from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from src.core.config import settings
from src.api.v1.endpoints import items
from src.schemas.models import HealthResponse

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Initialize connections, cache pools, background resources
    print("🚀 FastAPI application bootstrapping...")
    yield
    # Shutdown: Clean up connections, flush metrics
    print("🛑 FastAPI application graceful shutdown.")

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    lifespan=lifespan,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url=f"{settings.API_V1_STR}/docs",
    redoc_url=f"{settings.API_V1_STR}/redoc",
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Healthcheck
@app.get("/health", response_model=HealthResponse, tags=["health"])
async def health_check():
    return HealthResponse(version=settings.VERSION)

# Include v1 Routers
app.include_router(items.router, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)
