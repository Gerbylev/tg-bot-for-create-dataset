from sqlalchemy import Column, Integer, String, create_engine, MetaData, ForeignKey, Text
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.testing.schema import mapped_column

from src.utils.database import Base, int_pk, str_pk


class User(Base):
    user_id: Mapped[int] = mapped_column(primary_key=True)
    status: Mapped[str]
    contribution: Mapped[int] = mapped_column(default=0)
    context: Mapped[str]



class QaA(Base):
    __tablename__ = "question_answer"

    id: Mapped[int_pk]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"), nullable=False)
    question: Mapped[str] = mapped_column(Text, nullable=False)
    answer: Mapped[str] = mapped_column(Text, nullable=False)

class Fact(Base):
    id: Mapped[int_pk]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"), nullable=False)
    fact: Mapped[str] = mapped_column(Text, nullable=False)