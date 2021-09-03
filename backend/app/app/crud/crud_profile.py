import os
import shutil
import uuid
from typing import Any, Dict, Union

from fastapi import UploadFile
from sqlalchemy.orm import Session

from app.core.config import settings
from app.crud.base import CRUDBase
from app.models.user import UserProfile
from app.schemas.profile import ProfileUpdate, ProfileCreate


class CRUDProfile(CRUDBase[UserProfile, ProfileCreate, ProfileUpdate]):
    def create_with_owner(
        self, db: Session, *, obj_in: ProfileCreate, owner_id: int
    ) -> UserProfile:
        db_obj = UserProfile(
            user_id=owner_id,
            bio=obj_in.bio,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self,
        db: Session,
        *,
        db_obj: UserProfile,
        obj_in: Union[ProfileUpdate, Dict[str, Any]],
    ) -> UserProfile:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    @staticmethod
    def save_avatar(image: UploadFile, profile: UserProfile):
        # delete old avatar if exist
        if profile.avatar:
            try:
                os.remove(os.path.join(settings.STATIC_FILES_DIR, profile.avatar))
            except OSError as e:
                # TODO: log error
                pass

        filename = f'{uuid.uuid4()}.{image.filename.split(".")[-1]}'
        with open(os.path.join(settings.STATIC_FILES_DIR, filename), "wb+") as buffer:
            shutil.copyfileobj(image.file, buffer)
        return filename

    def get_by_owner(self, db: Session, owner_id):
        return db.query(UserProfile).filter(UserProfile.user_id == owner_id).first()


profile = CRUDProfile(UserProfile)
