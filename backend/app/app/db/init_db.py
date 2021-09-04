from sqlalchemy.orm import Session

from app import crud, schemas
from app.core.config import settings
from app.db import base  # noqa: F401
from app.models.project import ProjectCategory

# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    # Base.metadata.create_all(bind=engine)

    user = crud.user.get_by_email(db, email=settings.FIRST_SUPERUSER)
    if not user:
        user_in = schemas.UserCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
        )
        user = crud.user.create(db, obj_in=user_in)  # noqa: F841

    categories_count = db.query(ProjectCategory).count()
    if categories_count == 0:
        init_categories(db)


def init_categories(db: Session) -> None:
    db.add_all(
        [
            ProjectCategory(value="Backend"),
            ProjectCategory(value="Frontend"),
            ProjectCategory(value="Study"),
            ProjectCategory(value="Beginner"),
            ProjectCategory(value="Desktop"),
        ]
    )
    db.commit()
