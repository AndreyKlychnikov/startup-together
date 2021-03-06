from typing import Optional, List

from pydantic import BaseModel

from .membership import ZippedMembership

# Project category
class ProjectCategory(BaseModel):
    value: str

    class Config:
        orm_mode = True


# Shared properties
class ProjectBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


# Properties to receive on item creation
class ProjectCreate(ProjectBase):
    title: str


# Properties to receive on item update
class ProjectUpdate(ProjectBase):
    pass


# Properties shared by models stored in DB
class ProjectInDBBase(ProjectBase):
    id: int
    title: str
    owner_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Project(ProjectInDBBase):
    members: List[ZippedMembership]
    categories: List[ProjectCategory]


# Properties properties stored in DB
class ProjectInDB(ProjectInDBBase):
    pass
