from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.db.models.user import User
    from app.db.models.assignment import Assignment
    from app.db.models.user_xp import UserXP
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.models import Base

class Course(Base):
    __tablename__ = "courses"

    id: Mapped[str] = mapped_column(String, primary_key=True, nullable=False)
    title: Mapped[str] = mapped_column(String, unique=True, nullable=False)

    users: Mapped[list["User"]] = relationship(
        secondary="user_courses", back_populates="courses"
    )
    assignments: Mapped[list["Assignment"]] = relationship(back_populates="course")
    user_xp: Mapped[list["UserXP"]] = relationship("UserXP", back_populates="course")