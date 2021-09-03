from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401
    from .project_membership import ProjectMembership  # noqa: F401


class Project(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="own_projects")
    members = relationship("ProjectMembership", back_populates="project", lazy="selectin")
    categories = relationship("ProjectCategory", back_populates="projects", lazy="selectin", secondary="project_category_association")


class ProjectCategory(Base):
    id = Column(Integer, primary_key=True, index=True)
    value = Column(String)
    projects = relationship("Project", back_populates="categories", secondary="project_category_association")

    __tablename__ = 'project_category'


class ProjectCategoryAssociation(Base):
    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("project.id"))
    category_id = Column(Integer, ForeignKey("project_category.id"))

    __table_args__ = (
        UniqueConstraint("category_id", "project_id", name="project_category_uniq"),
    )
    __tablename__ = 'project_category_association'
