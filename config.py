from pydantic import ConfigDict
from pydantic_settings import BaseSettings
from typing import Optional
from urllib.parse import quote_plus

class Settings(BaseSettings):
    mongo_user: str
    mongo_password: str
    mongo_host: str
    mongo_db: Optional[str] = None

    @property
    def mongo_uri(self) -> str:
        user = quote_plus(self.mongo_user)
        password = quote_plus(self.mongo_password)

        base = f"mongodb+srv://{user}:{password}@{self.mongo_host}"

        if self.mongo_db:
            return f"{base}/{self.mongo_db}?retryWrites=true&w=majority"

        return base

    model_config = ConfigDict(env_file=".env")

settings = Settings()
    
