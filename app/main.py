from fastapi import FastAPI
from .database import Base, engine
from .controllers import customer_controller, payment_controller, crypto_controller

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(customer_controller.router)
app.include_router(payment_controller.router)
app.include_router(crypto_controller.router)