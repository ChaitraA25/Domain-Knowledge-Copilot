# This file creates a Session for SQLAlchemy ORM.
# Configures the database connection. It creates a SQLAlchemy engine to connect to SQLite
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL= "sqlite:///./knowledge_copilot.db"

#orm_engine create the db connection, orm-session - starts the conversation with db
#check_same_thread=False - allows only the thread that created the connection to use it.
orm_engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
orm_session=sessionmaker(autocommit=False, autoflush=False,bind=orm_engine)

