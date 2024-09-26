from fastapi import APIRouter

users_router = APIRouter()

@users_router.get("/users")
def get_users():
    return {"message": "Get all users"}

@users_router.get("/users/{user_id}")
def get_user(user_id: int):
    return {"message": f"Get user with id {user_id}"}

@users_router.post("/users")
def create_user(user: dict):
    return {"message": f"Create user with data {user}"}
