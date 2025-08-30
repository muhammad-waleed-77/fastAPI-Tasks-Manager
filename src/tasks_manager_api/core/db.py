from sqlmodel import Session, create_engine, select
from src.tasks_manager_api.core.config import settings


engine = create_engine(settings.DATABASE_URL, echo=True)

