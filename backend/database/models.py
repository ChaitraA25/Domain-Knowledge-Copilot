from sqlalchemy.orm import declarative_base,mapped_column,Mapped

# Every model inherits from Base
Base = declarative_base()

#Represents DB structure
class User(Base):
    __tablename__= "users"

    id:Mapped[int]= mapped_column(primary_key=True)

    username:Mapped[str] = mapped_column(unique=True,nullable=False)

    email:Mapped[str] = mapped_column(unique=True,nullable=False)

    hashed_password:Mapped[str] = mapped_column(nullable=False)


