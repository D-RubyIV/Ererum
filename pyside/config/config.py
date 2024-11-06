from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)
    DBPATH: str
    SLEEP_TIME: list[int] = [2700, 4200]
    START_DELAY: list[int] = [5, 100]
    AUTO_TASK: bool = True
    RECHARGE_SPEED_MAX_LEVEL: int = 11
    POINTS_3X: bool = False

settings = Settings()

