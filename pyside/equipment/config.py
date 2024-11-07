from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DBPATH: str  # Trường bắt buộc

    class Config:
        env_file = ".env"  # Đọc từ file .env ở thư mục gốc

settings = Settings()
