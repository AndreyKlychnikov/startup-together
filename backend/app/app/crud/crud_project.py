from typing import List, Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models import ProjectMembership
from app.models.project import Project, ProjectCategory
from app.schemas.project import ProjectCreate, ProjectUpdate


class CRUDProject(CRUDBase[Project, ProjectCreate, ProjectUpdate]):
    def create_with_owner(
        self, db: Session, *, obj_in: ProjectCreate, owner_id: int
    ) -> Project:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = Project(**obj_in_data, owner_id=owner_id)
        membership = ProjectMembership(project=db_obj, user_id=owner_id)
        db_obj.members.append(membership)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi(
        self,
        db: Session,
        *,
        skip: int = 0,
        limit: int = 100,
        categories: Optional[List[int]] = None,
    ) -> List[Project]:
        query = db.query(self.model)
        if categories is not None:
            query = query.filter(
                Project.categories.any(ProjectCategory.id.in_(categories))
            )
        return query.offset(skip).limit(limit).all()

    def get_multi_by_owner(
        self,
        db: Session,
        *,
        owner_id: int,
        skip: int = 0,
        limit: int = 100,
        categories: Optional[List[int]] = None,
    ) -> List[Project]:
        query = db.query(self.model)
        if categories is not None:
            query = query.filter(
                Project.categories.any(ProjectCategory.id.in_(categories))
            )
        return (
            query.filter(
                Project.owner_id == owner_id | Project.members.user_id == owner_id
            )
            .offset(skip)
            .limit(limit)
            .all()
        )


project = CRUDProject(Project)
