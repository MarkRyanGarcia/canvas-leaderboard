from datetime import datetime
from typing import Optional, TYPE_CHECKING
if TYPE_CHECKING:
    from app.db.models.user_xp import UserXP 
from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.models import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(String, primary_key=True, nullable=False)
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    email: Mapped[Optional[str]] = mapped_column(String, unique=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, server_default=func.now()
    )
    
    user_xp: Mapped["UserXP"] = relationship("UserXP", back_populates="user", uselist=False)
