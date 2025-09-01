from sqlmodel import Session, create_engine, select
from src.tasks_manager_api.core.config import settings
from src.tasks_manager_api.models.user import UserTable, Role
from src.tasks_manager_api.schemas.user import AdminRegister
from src.tasks_manager_api.core.security import get_password_hash

                                                         


engine = create_engine(settings.DATABASE_URL, echo=True)



# define function to inilize Data Base with admin
def init_db(session: Session)->None:

    admin_user = session.exec(select(UserTable).where(UserTable.email==settings.FIRST_SUPERUSER)).first()
    
    if not admin_user:
        admin_user = UserTable(
            username="Admin",
            email=settings.FIRST_SUPERUSER,
            hashed_password=get_password_hash(settings.FIRST_SUPERUSER_PASSWORD),
            role=Role.admin
        )
        session.add(admin_user)
        session.commit()
        session.refresh(admin_user)
        print(f'Admin User {admin_user.username} is successfully created')

