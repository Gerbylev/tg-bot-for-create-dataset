import json

from src.dao.question_answer_dao import QADAO
from src.dao.user_dao import UserData, UserDAO
from src.services.BaseServices import BaseService


class QAService(BaseService):

        def __init__(self):
            super().__init__()
            self.add_button("Отмена", self.back)

        def save_question(self, user_message: str, user: UserData):
            user.context = json.dumps({"question": user_message})
            UserDAO.update(filter_by={"user_id": user.user_id}, **user.to_dict())
            user.status = "qa.save_answer"
            UserDAO.update(filter_by={"user_id": user.user_id}, **user.to_dict())
            return "Напишите ответ на свой вопрос", user.status

        def save_answer(self, user_message: str, user: UserData):
            question = json.loads(user.context)['question']
            answer = user_message
            QADAO.add(**{"user_id": user.user_id, "question": question, "answer": answer})
            user.status = "default.default"
            UserDAO.update(filter_by={"user_id": user.user_id}, **user.to_dict())
            return "Вопрос успешно сохранён", user.status

        def back(self, user: UserData):
            user.status = "default.default"
            UserDAO.update(filter_by={"user_id": user.user_id}, **user.to_dict())
            return "Можешь узнать свой вклад написав команду /rating", user.status