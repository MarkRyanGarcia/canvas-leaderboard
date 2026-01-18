from typing import TYPE_CHECKING
if TYPE_CHECKING:
     from app.db.models.course import Course
     from app.db.models.user import User
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.models import Base

class UserXP(Base):
    __tablename__ = "user_xp"

    id: Mapped[str] = mapped_column(String, primary_key=True, nullable=False)
    user_id: Mapped[str] = mapped_column(String, ForeignKey("users.id"), nullable=False)
    course_id: Mapped[str] = mapped_column(String, ForeignKey("courses.id"), nullable=False)
    total_xp: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    user: Mapped["User"] = relationship("User", back_populates="user_xp")
    course: Mapped["Course"] = relationship("Course", back_populates="user_xp")
    
