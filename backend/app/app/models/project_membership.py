from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.schema import UniqueConstraint

from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401
    from .project import Project  # noqa: F401


class ProjectMembership(Base):
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="projects")
    project_id = Column(Integer, ForeignKey("project.id"))
    project = relationship("Project", back_populates="members")
    accepted = Column(Boolean, default=False)

    __table_args__ = (
        UniqueConstraint("user_id", "project_id", name="membership_uniq"),
    )
