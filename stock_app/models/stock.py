from sqlalchemy import Column, String, Float, BigInteger
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Stock(Base):
    __tablename__ = "stock"

    # 종목코드 (Primary Key)
    stock_code = Column(
        String, primary_key=True, index=True, comment="종목코드"
    )

    # 종목명
    stock_name = Column(String, nullable=False, comment="종목명")

    # 시장구분
    market_type = Column(String, nullable=False, comment="시장구분")

    # 종가
    close_price = Column(Float, nullable=False, comment="종가")

    # 대비
    change = Column(Float, nullable=True, comment="대비")

    # 등락률
    change_rate = Column(Float, nullable=True, comment="등락률")

    # 시가
    open_price = Column(Float, nullable=True, comment="시가")

    # 고가
    high_price = Column(Float, nullable=True, comment="고가")

    # 저가
    low_price = Column(Float, nullable=True, comment="저가")

    # 거래량
    volume = Column(BigInteger, nullable=True, comment="거래량")

    # 거래대금
    trading_value = Column(BigInteger, nullable=True, comment="거래대금")

    # 시가총액
    market_cap = Column(BigInteger, nullable=True, comment="시가총액")

    # 상장주식수
    total_shares = Column(BigInteger, nullable=True, comment="상장주식수")
