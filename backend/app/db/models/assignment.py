from datetime import datetime
from typing import Optional, TYPE_CHECKING
if TYPE_CHECKING:
    from app.db.models.course import Course
    from app.db.models.submission import Submission
from sqlalchemy import DateTime, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.models import Base

class Assignment(Base):
    __tablename__ = "assignments"

    id: Mapped[str] = mapped_column(String, primary_key=True, nullable=False)
    title: Mapped[str] = mapped_column(String, nullable=False)
    course_id: Mapped[str] = mapped_column(String, ForeignKey("courses.id"), nullable=False)
    due_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)

    course: Mapped["Course"] = relationship(back_populates="assignments")
    submissions: Mapped[list["Submission"]] = relationship("Submission", back_populates="assignment")