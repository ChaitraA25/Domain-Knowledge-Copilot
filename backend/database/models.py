from sqlalchemy.orm import mapped_column,Mapped
from backend.database.db import Base


#Represents DB structure
class User(Base):
    __tablename__= "users"

    id:Mapped[int]= mapped_column(primary_key=True)

    username:Mapped[str] = mapped_column(unique=True,nullable=False)

    email:Mapped[str] = mapped_column(unique=True,nullable=False)

    hashed_password:Mapped[str] = mapped_column(nullable=False)


