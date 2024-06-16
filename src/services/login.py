from src.repositories.auth import IAuthRepository, AuthRepository
from src.schemas.user import User

from src.utils.mail import mail
from src.utils.codegen import codegen

class LoginService:
    def __init__(self, auth_repo: IAuthRepository):
        self.repo = auth_repo

    def send_code(self, user: User) -> int:
        code = codegen(6)
        cid = self.repo.add(user, code)
        mail.send(
            reciever=user.email,
            subject="Код подтверждения",
            text="Если вы не запрашивали код - проигнорируйте это письмо.\n" + code
        )
        return cid

    def check_code(self, user: User, code: str) -> bool:
        return self.repo.check(user, code)


def get_login_service():
    yield LoginService(AuthRepository())