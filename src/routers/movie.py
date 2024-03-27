from fastapi import APIRouter

router = APIRouter(
    prefix="/items",
    tags=["movies"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def read_movies():
    """_summary_

    :return: _description_
    """
    return "Great Movie"
