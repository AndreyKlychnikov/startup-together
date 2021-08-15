from app.crud.base import CRUDBase
from app.models import ProjectMembership
from app.schemas.membership import MembershipCreate


class CRUDMembership(CRUDBase[ProjectMembership, MembershipCreate, MembershipCreate]):
    pass


membership = CRUDMembership(ProjectMembership)
