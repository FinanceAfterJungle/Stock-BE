from fastapi import APIRouter
from stock_app.core.config import get_setting

router = APIRouter()
setting = get_setting()


@router.get("/")
def test_api():
    return "hello, stock_app~!"
