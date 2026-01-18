from app.db.models import Base
from app.deps.db import engine

# This will create all tables in the database
Base.metadata.create_all(bind=engine)

print("Tables created successfully")