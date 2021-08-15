from typing import Any

import sqlalchemy
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.post("/", response_model=schemas.membership.ZippedMembership)
def create_membership(
    *,
    db: Session = Depends(deps.get_db),
    membership_in: schemas.membership.MembershipCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new membership (join request).
    """
    if membership_in.user_id != current_user.id:
        raise HTTPException(status_code=400, detail="Not enough permissions")
    try:
        membership = crud.membership.create(db=db, obj_in=membership_in)
    except sqlalchemy.exc.IntegrityError:
        raise HTTPException(status_code=404, detail="Not found")
    return membership


@router.put("/{id}", response_model=schemas.membership.Membership)
def update_membership(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    membership_in: schemas.membership.MembershipUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update an membership.
    """
    membership = crud.membership.get(db=db, id=id)
    if not membership:
        raise HTTPException(status_code=404, detail="Membership not found")
    if not crud.user.is_superuser(current_user) and (membership.project.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    membership = crud.membership.update(db=db, db_obj=membership, obj_in=membership_in)
    return membership


@router.delete("/{id}", response_model=schemas.membership.ZippedMembership)
def delete_membership(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete an membership.
    """
    membership = crud.membership.get(db=db, id=id)
    if not membership:
        raise HTTPException(status_code=404, detail="Membership not found")
    if (
        not crud.user.is_superuser(current_user)
        and membership.user_id != current_user.id
        and membership.project.owner_id != current_user.id
    ):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    membership = crud.membership.remove(db=db, id=id)
    return membership
