from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from stock_app.app import router

from stock_app.db.session import Base, engine

main_app = FastAPI()

origins = [
    "http://localhost:3000",
    "https://v2.foodteacher.xyz",
]
main_app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메서드를 허용하려면 "*"
    allow_headers=["*"],  # 모든 HTTP 헤더를 허용하려면 "*"
)

main_app.include_router(router)


@main_app.get("/")
def test_api():
    return "hello, stock_app~!"


Base.metadata.create_all(bind=engine)
