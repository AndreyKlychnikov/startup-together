from typing import Optional, List

from pydantic import BaseModel

from .user import User


# Shared properties
class MembershipBase(BaseModel):
    pass


# Properties to receive on item creation
class MembershipCreate(MembershipBase):
    project_id: int
    user_id: int


# Properties shared by models stored in DB
class MembershipInDBBase(MembershipBase):
    id: int
    project_id: int
    user_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Membership(MembershipInDBBase):
    user: User


# Properties properties stored in DB
class ProjectInDB(MembershipInDBBase):
    pass


# Zipped properties (for example, to get project request)
class ZippedMembership(MembershipBase):
    user: User

    class Config:
        orm_mode = True
