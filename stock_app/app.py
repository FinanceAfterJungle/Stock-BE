from fastapi import APIRouter, Response
from fastapi.params import Depends
from sqlalchemy.orm import Session

from stock_app.core.config import get_setting
from pydantic import BaseModel
from stock_app.db.session import get_db
from stock_app.models.stock import Stock as stock_model

router = APIRouter()
setting = get_setting()


@router.get("/", response_model=str)
def test_api():
    return "hello, stock_app~!"


class Stock(BaseModel):
    stock_code: int
    stock_name: str
    market_type: str
    close_price: float
    change: float
    change_rate: float
    open_price: float
    high_price: float
    low_price: float
    volume: int
    trading_value: int
    market_cap: int
    total_shares: int

    class Config:
        orm_mode = True


@router.post("/stock")
def add_stock(stock: Stock, db: Session = Depends(get_db)):
    new_stock = stock_model(**stock.model_dump())
    db.add(new_stock)
    db.commit()

    return Response(status_code=201)
