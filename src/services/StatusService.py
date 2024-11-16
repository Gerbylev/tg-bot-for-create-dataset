from alembic.util import status
from telegram import Update
from telegram.ext import ContextTypes

from src.dao.user_dao import UserDAO, UserData
from src.models.models import User
from src.services.BaseServices import BaseService
from src.services.default_service import DefaultService
from src.services.fact_service import FactService
from src.services.qa_service import QAService
from src.services.registry import REGISTRY


class StatusService:
    def __init__(self):
        REGISTRY.put(FactService(), 'fact')
        REGISTRY.put(QAService(), 'qa')
        REGISTRY.put(DefaultService(), 'default')

    def magic(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_text = update.message.text
        cls, func, user = self.get_full_info(update.effective_user.id)
        if user_text in cls.buttons:
            message_text, status = cls.buttons[user_text]['callback'](user)
        else:
            message_text, status = getattr(cls, func)(user_text, user)
        buttons = self.get_button(status)
        return message_text, buttons

    def get_button(self, status):
        cls, func = self.parse_status(status)
        cls: BaseService = REGISTRY.get(cls)
        buttons = list(cls.buttons.keys())
        return [buttons]

    def get_full_info(self, user_id: int):
        user: User | None = UserDAO.find_one_or_none_by_id(user_id)
        if user is None:
            user = UserData(user_id=user_id, status="default.default", contribution=0, context="")
            UserDAO.add(**user.to_dict())
        else:
            user = UserData.from_db(user)
        cls, func = self.parse_status(user.status)
        cls: BaseService = REGISTRY.get(cls)
        return cls, func, user

    def parse_status(self, status_str: str):
        part = status_str.split('.')
        func = part[-1]
        cls = '.'.join(part[:-1])
        return cls, func