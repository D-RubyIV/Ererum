from sqlalchemy import String, Integer, DateTime, func, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class BaseModel(DeclarativeBase):
    __abstract__ = True
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    created_time: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    updated_time: Mapped[DateTime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())

class ProxyRecord(BaseModel):
    __tablename__ = "proxy"

    ip: Mapped[str] = mapped_column(String(30), nullable=False)
    port: Mapped[str] = mapped_column(String(10), nullable=False)
    username: Mapped[str] = mapped_column(String(50))
    password: Mapped[str] = mapped_column(String(50))

    tg_records: Mapped[list["TgRecord"]] = relationship("TgRecord", back_populates="proxy")

    @property
    def to_proxy_content(self) -> str:
        return f"{self.ip}:{self.port}:{self.username}:{self.password}"

class TgRecord(BaseModel):
    __tablename__ = "tg"

    name: Mapped[str] = mapped_column(String(30), nullable=False)
    phone: Mapped[str] = mapped_column(String(10), nullable=False)
    username: Mapped[str] = mapped_column(String(50))
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    authKey: Mapped[str] = mapped_column(String(500))

    proxy_id: Mapped[int] = mapped_column(ForeignKey("proxy.id"), nullable=False)
    proxy: Mapped["ProxyRecord"] = relationship("ProxyRecord", back_populates="tg_records")

    @property
    def to_proxy_content(self) -> str:
        return f"{self.ip}:{self.port}:{self.username}:{self.password}"
