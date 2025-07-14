from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def read_lifestyles():
    return [{"message": "List of lifestyle logs"}]
