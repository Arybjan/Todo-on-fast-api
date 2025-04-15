from fastapi import FastAPI
from api.routers.todo import todo_router


app = FastAPI()
app.include_router(todo_router)


@app.get("/")
def index():
    return {"status": "Hello world! Todo api is raunning.."}
