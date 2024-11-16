from dataclasses import dataclass
from typing import Optional

from pydantic import BaseModel
from sqlalchemy import select, desc
from sqlalchemy.orm.sync import update

from src.dao.base import BaseDAO
from src.models.models import User
from src.utils.database import Session


class UserData(BaseModel):
    user_id: int
    status: str
    contribution: int
    context: Optional[str]

    def to_dict(self):
        return {"user_id": self.user_id, "status": self.status, "contribution": self.contribution, "context": self.context}

    @classmethod
    def from_db(cls, user: User):
        return UserData(user_id=user.user_id, status=user.status, contribution=user.contribution, context=user.context)


class UserDAO(BaseDAO):
    model = User

    @classmethod
    def find_one_or_none_by_id(cls, data_id: int):
        with Session() as session:
            query = select(cls.model).filter_by(user_id=data_id)
            return session.execute(query).scalar_one_or_none()

    @classmethod
    def get_user_rank_by_contribution(cls, user_id: int):
        with Session() as session:
            user = cls.find_one_or_none_by_id(user_id)
            if not user:
                return None

            query = select(cls.model).order_by(desc(cls.model.contribution))
            users = session.execute(query).scalars().all()

            rank = next((index + 1 for index, u in enumerate(users) if u.user_id == user.user_id), None)
            return rank, user