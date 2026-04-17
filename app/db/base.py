

from sqlalchemy.orm import declarative_base

Base = declarative_base()

# IMPORTANT: import models here
from app.models import user