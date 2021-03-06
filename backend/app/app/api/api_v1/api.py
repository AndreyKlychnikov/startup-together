from fastapi import APIRouter

from app.api.api_v1.endpoints import items, login, users, utils, projects, memberships, profiles

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(profiles.router, prefix="/profile", tags=["profiles"])
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(projects.router, prefix="/projects", tags=["projects"])
api_router.include_router(memberships.router, prefix="/memberships", tags=["memberships"])
