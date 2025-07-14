from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def read_seizures():
    return [{"message": "List of seizures"}]
