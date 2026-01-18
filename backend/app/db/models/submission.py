from datetime import datetime
from app.db.models.assignment import Assignment
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.db.models.course import Course
    from app.db.models.user import User
from sqlalchemy import DateTime, String, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.models import Base

class Submission(Base):
    __tablename__ = "submissions"

    id: Mapped[str] = mapped_column(String, primary_key=True, nullable=False)
    submitted_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=func.now())
    user_id: Mapped[str] = mapped_column(String, ForeignKey("users.id"), nullable=False)
    assignment_id: Mapped[str] = mapped_column(String, ForeignKey("assignments.id"), nullable=False)
    course_id: Mapped[str] = mapped_column(String, ForeignKey("courses.id"), nullable=False)

    user: Mapped["User"] = relationship("User", back_populates="submissions")
    assignment: Mapped["Assignment"] = relationship("Assignment", back_populates="submissions")
    course: Mapped["Course"] = relationship("Course", back_populates="submissions")