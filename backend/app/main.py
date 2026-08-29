from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import get_settings
from app.routers.appointments import router as appointments_router
from app.routers.queues import router as queues_router
from app.routers.tenants import router as tenants_router

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version="1.0.0",
    description="BookMyQ enterprise queue management SaaS API",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tenants_router, prefix=settings.api_v1_prefix)
app.include_router(queues_router, prefix=settings.api_v1_prefix)
app.include_router(appointments_router, prefix=settings.api_v1_prefix)


@app.get("/health")
def health_check() -> dict:
    return {"status": "ok", "service": settings.app_name}


@app.get("/api/v1/health")
def api_health() -> dict:
    return {"status": "ok", "service": settings.app_name, "environment": settings.environment}
