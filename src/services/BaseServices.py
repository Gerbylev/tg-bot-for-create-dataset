from src.dao.user_dao import UserData


class BaseService:
    def __init__(self):
        self.buttons = {}

    def add_button(self, button_text, callback):
        if not isinstance(button_text, str) or not callable(callback):
            raise ValueError('Некорректные параметры: button_text должен быть строкой, а callback функцией.')
        self.buttons[button_text] = {"callback": callback}

    def default(self, user_message:str, user: UserData):
        if user_message != '/start':
            return 'Используйте кнопки', user.status
        return 'Привет, я бот', user.status
