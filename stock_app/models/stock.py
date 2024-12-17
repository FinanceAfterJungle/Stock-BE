from sqlalchemy import Column, String, Float, BigInteger, Date
from stock_app.db.session import Base


class Stock(Base):
    __tablename__ = "stock"

    trade_date = Column(
        Date, nullable=False, comment="거래일자"
    )  # 날짜 필드 추가
    stock_code = Column(
        String, primary_key=True, index=True, comment="종목코드"
    )
    stock_name = Column(String, nullable=False, comment="종목명")
    close_price = Column(Float, nullable=False, comment="종가")
    change = Column(Float, nullable=True, comment="대비")
    change_rate = Column(Float, nullable=True, comment="등락률")
    open_price = Column(Float, nullable=True, comment="시가")
    high_price = Column(Float, nullable=True, comment="고가")
    low_price = Column(Float, nullable=True, comment="저가")
    volume = Column(BigInteger, nullable=True, comment="거래량")
    trading_value = Column(BigInteger, nullable=True, comment="거래대금")
    market_cap = Column(BigInteger, nullable=True, comment="시가총액")
    total_shares = Column(BigInteger, nullable=True, comment="상장주식수")
