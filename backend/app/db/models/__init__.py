from sqlalchemy.orm import declarative_base


Base = declarative_base()


from .user import User
from .enrollment import Enrollment
from .submission import Submission
from .course import Course
from .assignment import Assignment
