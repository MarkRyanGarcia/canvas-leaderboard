from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.models import Base

class Course(Base):
    __tablename__ = "courses"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    course_name: Mapped[str] = mapped_column(String, nullable=False)

    assignments = relationship("Assignment", back_populates="course")
    enrollments = relationship("Enrollment", back_populates="course")
    submissions = relationship("Submission", back_populates="course")