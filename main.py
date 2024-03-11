from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.database.database import create_db
from src.database.schemas.schemas import update_forward_refs
from src.routers import router_address

update_forward_refs()
create_db()

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


# app.include_router(router_users.router)
app.include_router(router_address.router)
# app.include_router(router_vehicles.router)
