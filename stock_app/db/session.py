from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import inspect
from sqlalchemy.orm import DeclarativeBase

from typing import Generator, Optional

from stock_app.core.config import get_setting


settings = get_setting()

# SQLALCHEMY_DATABASE_URL = "sqlite+sqlite3://{}:{}@{}:{}/{}".format(
#     settings.MYSQL_USER,
#     settings.MYSQL_PASSWORD,
#     settings.MYSQL_HOST,
#     settings.MYSQL_PORT,
#     settings.MYSQL_DATABASE,
# )

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, pool_pre_ping=True, max_overflow=150, echo=True
# )

SQLALCHEMY_DATABASE_URL = f"sqlite:///{settings.DATABASE_FILE}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    pool_size=5,  # 기본 연결 수
    max_overflow=10,  # 추가 연결 수
    echo=True,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
insp = inspect(engine)


# Base = declarative_base()
class Base(DeclarativeBase):
    pass


def get_db() -> Generator[Session, None, None]:
    db: Optional[Session] = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


# # Initialize Database
# if not os.path.exists(settings.DATABASE_FILE):
#     print(f"Database file {settings.DATABASE_FILE} does not exist. Initializing...")
#     Base.metadata.create_all(bind=engine)
