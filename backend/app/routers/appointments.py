from fastapi import APIRouter

router = APIRouter(prefix="/appointments", tags=["appointments"])


@router.get("")
def list_appointments() -> dict:
    return {"appointments": []}


@router.post("")
def create_appointment() -> dict:
    return {"message": "appointment booked"}
