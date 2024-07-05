import os

class Settings:
    def __init__(self) -> None:
        self.allowed_origins    = os.getenv("ALLOWED_ORIGINS", ["http://localhost","https://localhost"])
        self.allow_credentials  = bool(os.getenv("ALLOW_CREDENTIALS", True))
        self.allowed_hosts      = ["localhost"]
        self.db_user            = os.getenv("DB_USER")
        self.db_password        = os.getenv("DB_PASSWORD")
        self.db_host            = os.getenv("DB_HOST")
        self.db_port            = int(os.getenv("DB_PORT"))
        self.db                 = os.getenv('DB_NAME')
        

    def get_full_database_url(self):
        return f"postgresql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db}"


