from urllib.parse import urljoin
import requests


class OwfHttpClient:
    REGISTER_ROUT = "api/auth/register"
    LOGIN_ROUT = "api/auth/login"

    def __init__(self, base_url: str):
        '''Инициализтор класса
        параметр base_url - базовый url тестируемого приложения'''
        self.base_url = base_url

    def register(self, register_data: dict) -> requests.Response:
        '''
        Отправка запроса на регистрацию
        :param register_data: данные запроса регистрации
        :return: объект, содержащий ответ запроса
        '''
        return requests.post(
            url=urljoin(self.base_url, self.REGISTER_ROUT),
            json=register_data)

    def login(self, login_data: dict) -> requests.Response:
        '''
        Отправка запроса на авторизацию пользователя
        :param login_data: данные запроса авторизации
        :return: объект, содержащий ответ запроса
        '''
        return requests.post(
            url=urljoin(self.base_url, self.LOGIN_ROUT),
            json=login_data)
