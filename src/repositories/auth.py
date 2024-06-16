from abc import ABC, abstractmethod

from src.database.db import session_factory as _session_factory
from src.database.user import UserLoginDataTable
from src.schemas.user import User


class IAuthRepository(ABC):
    def add(self, user: User, code: str) -> int:
        pass

    def check(self, user: User, code: str) -> bool:
        pass


class AuthRepository(IAuthRepository):
    def __init__(self, session_factory=_session_factory):
        self.session_factory = session_factory

    def add(self, user: User, code: str) -> int:
        with self.session_factory() as session:
            rec = (
                session
                .query(UserLoginDataTable)
                .filter(UserLoginDataTable.email == user.email)
                .one_or_none()
            )
            if rec:
                rec.code = code
            else:
                rec = UserLoginDataTable(email=user.email, code=code)
                session.add(rec)

            session.commit()
            return rec.id

    def check(self, user: User, code: str) -> bool:
        with self.session_factory() as session:
            rec = (
                session
                .query(UserLoginDataTable)
                .filter(UserLoginDataTable.email == user.email)
                .one_or_none()
            )
            if not rec:
                return False
            
            return rec.code == code