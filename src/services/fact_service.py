from src.dao.fact_dao import FactDAO
from src.dao.user_dao import UserData, UserDAO
from src.services.BaseServices import BaseService


class FactService(BaseService):

    def __init__(self):
        super().__init__()
        self.add_button("Отмена", self.back)

    def save_fact(self, user_message: str, user: UserData):
        FactDAO.add(**{"user_id": user.user_id, "fact": user_message})
        user.status = "default.default"
        UserDAO.update(filter_by={"user_id": user.user_id}, **user.to_dict())
        return "Факт успешно сохранён", user.status

    def back(self, user: UserData):
        user.status = "default.default"
        UserDAO.update(filter_by={"user_id": user.user_id}, **user.to_dict())
        return "Можешь узнать свой вклад написав команду /rating", user.status