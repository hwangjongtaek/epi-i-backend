from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def generate_report():
    return {"message": "Generated report"}
