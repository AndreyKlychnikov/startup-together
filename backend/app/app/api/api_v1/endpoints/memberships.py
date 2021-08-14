from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


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
        raise HTTPException(status_code=404, detail="membership not found")
    if not crud.user.is_superuser(current_user) and (membership.project.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    membership = crud.membership.remove(db=db, id=id)
    return membership
