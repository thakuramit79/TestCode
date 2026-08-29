from fastapi import APIRouter

router = APIRouter(prefix="/tenants", tags=["tenants"])


@router.get("")
def list_tenants() -> dict:
    return {"tenants": []}


@router.post("")
def create_tenant() -> dict:
    return {"message": "tenant created"}
