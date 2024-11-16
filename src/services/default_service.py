from src.dao.user_dao import UserData, UserDAO
from src.services.BaseServices import BaseService


class DefaultService(BaseService):

    def __init__(self):
        super().__init__()
        self.add_button("Добавить факт", self.add_fact)
        self.add_button("Добавить вопрос ответ", self.add_qa)

    def add_fact(self, user: UserData):
        user.status = "fact.save_fact"
        UserDAO.update(filter_by={"user_id": user.user_id}, **user.to_dict())
        return "Добавь факт", user.status

    def add_qa(self, user: UserData):
        user.status = "qa.save_question"
        UserDAO.update(filter_by={"user_id": user.user_id}, **user.to_dict())
        return "Сначала введите вопрос", user.status