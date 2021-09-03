from typing import Any, List

from app import models, schemas, crud
from app.api import deps
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session

router = APIRouter()


@router.put("/", response_model=schemas.Profile)
def update_my_profile(
    *,
    db: Session = Depends(deps.get_db),
    profile_in: schemas.ProfileUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update own profile.
    """
    profile = crud.profile.update(db, db_obj=current_user.profile, obj_in=profile_in)
    return profile


@router.post("/upload_avatar", response_model=schemas.Profile)
def upload_avatar(
    *,
    img: UploadFile = File(...),
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
):
    """
    Upload avatar for own profile
    """
    filename = crud.profile.save_avatar(img, current_user.profile)
    profile = crud.profile.update(
        db, db_obj=current_user.profile, obj_in={"avatar": filename}
    )
    return profile


@router.get("/me", response_model=schemas.Profile)
def read_profile_me(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get current profile.
    """
    return current_user.profile


@router.get("/{user_id}", response_model=schemas.Profile)
def read_profile_by_owner(
    user_id: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get profile by owner.
    """
    return crud.profile.get_by_owner(db, owner_id=user_id)
