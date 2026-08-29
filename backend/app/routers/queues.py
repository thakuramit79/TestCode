from fastapi import APIRouter

router = APIRouter(prefix="/queues", tags=["queues"])


@router.get("/live")
def live_queue() -> dict:
    return {"queue": [], "status": "ok"}


@router.post("/tokens")
def create_token() -> dict:
    return {"message": "token generated"}
