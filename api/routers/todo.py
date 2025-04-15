from fastapi import APIRouter


todo_router = APIRouter(prefix="/api", tags=["Todo"])


@todo_router.get("/")
def all_todos():
    return "Not Implemeted"


@todo_router.post("/")
def post_todo():
    return "Not Implemeted"


@todo_router.put("/{key}")
def update_todo(key: int):
    return "Not Implemeted"


@todo_router.delete("/{key}")
def delete_todo(key: int):
    return "Not Implemeted"