import os

class Settings:
    def __init__(self) -> None:
        self.allowed_origins = os.getenv("ALLOWED_ORIGINS", ["http://localhost","https://localhost"])
        self.allow_credentials = bool(os.getenv("ALLOW_CREDENTIALS", True))
        self.allowed_hosts     = ["localhost"]