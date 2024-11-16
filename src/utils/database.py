import os
from datetime import datetime
from typing import Annotated

from sqlalchemy import create_engine, func
from sqlalchemy.orm import DeclarativeBase, declared_attr, mapped_column, sessionmaker

from src.config.Config import CONFIG

def create_connectdb_url():
    db_config = CONFIG.database
    url = f"{db_config.engine}://{db_config.user}:{db_config.password}@{db_config.host}:{db_config.port}/{db_config.dbname}"
    os.environ['DATABASE_URL'] = url
    return url

engine = create_engine(create_connectdb_url())
Session = sessionmaker(engine, expire_on_commit=False)

int_pk = Annotated[int, mapped_column(primary_key=True)]
str_pk = Annotated[str, mapped_column(primary_key=True)]
created_at = Annotated[datetime, mapped_column(server_default=func.now())]
updated_at = Annotated[datetime, mapped_column(server_default=func.now(), onupdate=datetime.now)]
str_uniq = Annotated[str, mapped_column(unique=True, nullable=False)]
str_null_true = Annotated[str, mapped_column(nullable=True)]

class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    def __repr__(self):
        fields = ', '.join(f"{key}={repr(value)}" for key, value in self.__dict__.items())
        return f"<{self.__class__.__name__}({fields})>"