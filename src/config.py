from os import environ
from dotenv import load_dotenv


load_dotenv()


class DatabaseSettings:
    def __init__(self):
        self._DBMS = environ.get('DB_DBMS', 'sqlite')
        self._DRIVER = environ.get('DB_DRIVER')
        self._PASSWORD = environ.get('DB_PASSWORD')
        self._USER = environ.get('DB_USER')
        self._PATH = environ.get('DB_PATH')
        self._HOST = environ.get('DB_HOST')
        self._PORT = environ.get('DB_PORT')
    
    @property
    def DBMS(self):
        """Используемая СУБД"""
        return self._DBMS

    @property
    def DRIVER(self):
        """Используемый драйвер для работы с СУБД"""
        return self._DRIVER

    @property
    def PASSWORD(self):
        """Пароль к базе данных"""
        return self._PASSWORD

    @property
    def USER(self):
        """Пользователь базы данных"""
        return self._USER

    @property
    def PATH(self):
        """Путь к базе данных"""
        return self._PATH

    @property
    def HOST(self):
        """Хост"""
        return self._HOST

    @property
    def PORT(self):
        """Порт хоста"""
        return self._PORT


class AuthSettings:
    def __init__(self):
        self._SECRET_KEY = environ.get("AUTH_SECRET_KEY", "Cactus's secret key =)")
        self._ALGOTITHM = environ.get("AUTH_ALGORITHM", "HS256")
        #self._TVT = environ.get("AUTH_TVT", 20) # Token Validation Time
    
    @property
    def SECRET_KEY(self):
        """Секретный ключ"""
        return self._SECRET_KEY

    @property
    def ALGORITHM(self):
        """Алгоритм подписи"""
        return self._ALGOTITHM
    
    # @property
    # def TVT(self):
    #     return self._TVT


class MailSettings:
    def __init__(self):
        self._LOGIN = environ.get("MAIL_LOGIN")
        self._PASS = environ.get("MAIL_PASSWORD")
        self._SMTP = environ.get("MAIL_SMTP")
        self._PORT = int(environ.get("MAIL_PORT"))
    
    @property
    def LOGIN(self):
        return self._LOGIN
    
    @property
    def PASS(self):
        return self._PASS
    
    @property
    def SMTP(self):
        return self._SMTP
    
    @property
    def PORT(self):
        return self._PORT


db_settings = DatabaseSettings()
auth_settings = AuthSettings()
email_settings = MailSettings()